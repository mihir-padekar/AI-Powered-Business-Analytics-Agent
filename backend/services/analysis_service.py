from backend.tools.data_loader import load_data
from backend.agents.profiling_agent import profile_data
from backend.agents.analytics_agent import analyze_data
from backend.agents.visualization_agent import generate_charts
from backend.agents.insight_agent import generate_insights
from backend.agents.question_agent import answer_question

def analyze_file(file):

    df = load_data(file)

    profile = profile_data(df)

    analysis = analyze_data(df)

    charts = generate_charts(df)

    insights = generate_insights(analysis)

    return {
        "df": df,
        "profile": profile,
        "analysis": analysis,
        "charts": charts,
        "insights": insights
    }