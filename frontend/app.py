import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from backend.agents.router_agent import route_question_llm
from backend.graph.workflow import workflow
from backend.agents.dynamic_visualization_agent import generate_chart
import streamlit as st

from backend.services.analysis_service import analyze_file

st.set_page_config(
    page_title="DecisionPilot AI",
    page_icon="📊",
    layout="wide"
)

st.sidebar.title("DecisionPilot AI")

st.sidebar.markdown(
    """
    ### AI Business Analytics Agent

    Upload a CSV dataset and ask
    business questions in natural language.
    """
)



if "messages" not in st.session_state:
    st.session_state.messages = []


uploaded_file = st.sidebar.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if not uploaded_file:

    st.title("📊 DecisionPilot AI")

    st.markdown(
        """
        ## Welcome

        Upload a CSV dataset using the sidebar.

        You can:

        - Analyze business data
        - Generate insights
        - Create visualizations
        - Ask questions in natural language
        - Generate executive reports
        """
    )

    st.stop()

if uploaded_file:

    result = analyze_file(uploaded_file)

    df = result["df"]

    profile = result["profile"]

    analysis = result["analysis"]

    charts = result["charts"]

    insights = result["insights"]
    

    st.success(
        f"""
        Dataset Loaded Successfully

        Rows: {profile['rows']}
        Columns: {profile['columns']}
        """
    )
    from backend.agents.report_agent import generate_report

    generate_report_btn = st.button(
        "Generate Executive Report"
    )

    if generate_report_btn:

        report = generate_report(analysis)

        st.subheader("Executive Report")

        st.write(report)

    st.divider()
    st.success(
        f"""
        Dataset Loaded Successfully

        Rows: {profile['rows']}
        Columns: {profile['columns']}
        """
    )

    st.divider()

    st.subheader("💬 Chat With DecisionPilot AI")

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input(
        "Ask a business question..."
    )
    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.write(question)

        result = workflow.invoke(
            {
                "question": question,
                "analysis": analysis,
                "charts": charts,
                "route": "",
                "result": ""
            }
        )

        route = result["route"]

        if route == "analytics":

            response = str(result["result"])

            with st.chat_message("assistant"):
                st.write(response)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": response
                }
            )

        elif route == "visualization":

            fig = generate_chart(
                df,
                question
            )

            with st.chat_message("assistant"):

                st.write(
                    f"Generated {question}"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

        else:

            response = str(result["result"])

            with st.chat_message("assistant"):
                st.write(response)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": response
                }
            )

      
with st.expander("🔍 Dataset Technical Details"):

    st.write(insights)

    st.subheader("Column Names")
    st.write(profile["column_names"])

    st.subheader("Data Types")
    st.json(profile["data_types"])

    st.subheader("Missing Values")
    st.json(profile["missing_values"])

    st.subheader("Duplicate Rows")
    st.write(profile["duplicate_rows"])

    st.subheader("Numerical Columns")
    st.write(profile["numerical_columns"])

    st.subheader("Categorical Columns")
    st.write(profile["categorical_columns"])

    st.subheader("Numeric Analysis")

    st.json(
        analysis["numeric_summary"]
    )

    st.subheader("Top Categories")

    st.json(
        analysis["categorical_summary"]
    )

    st.subheader("Distribution")

    st.plotly_chart(
        charts["histogram"],
        use_container_width=True,
        key="agent_histogram"
    )

    st.subheader("Top Categories")

    st.plotly_chart(
        charts["bar"],
        use_container_width=True,
        key="agent_bar"
    )

