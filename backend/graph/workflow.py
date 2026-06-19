from typing import TypedDict
from backend.agents.router_agent import route_question
from backend.agents.question_agent import answer_question
from backend.agents.report_agent import generate_report
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    question: str
    analysis: dict
    chat_history: str
    charts: dict
    route: str
    result: object
    analytics_output: dict
    report: str

def report_node(state):

    report = generate_report(
        state["analytics_output"]
    )

    state["report"] = report

    return state

def supervisor_node(state):

    route = route_question(
        state["question"]
    )

    state["route"] = route

    return state

def analytics_node(state):

    state["analytics_output"] = {
        "numeric_summary":
            state["analysis"]["numeric_summary"],

        "categorical_summary":
            state["analysis"]["categorical_summary"]
    }

    return state

def visualization_node(state):

    state["result"] = (
        state["charts"]
    )

    return state

def insight_node(state):
    answer = answer_question(
    state["question"],
    state["analytics_output"],
    state["chat_history"]
)      
    state["result"] = answer

    return state

graph = StateGraph(AgentState)

graph.add_node(
    "supervisor",
    supervisor_node
)

graph.add_node(
    "analytics",
    analytics_node
)

graph.add_node(
    "visualization",
    visualization_node
)

graph.add_node(
    "insights",
    insight_node
)

graph.add_edge(
    "analytics",
    "insights"
)

def route_decision(state):

    return state["route"]

graph.set_entry_point(
    "supervisor"
)

graph.add_conditional_edges(
    "supervisor",
    route_decision,
    {
        "analytics": "analytics",
        "visualization": "visualization",
        "insights": "analytics"
    }
)

workflow = graph.compile()

