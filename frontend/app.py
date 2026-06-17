import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from backend.agents.router_agent import route_question
from backend.graph.workflow import workflow
from backend.agents.dynamic_visualization_agent import generate_chart
from backend.agents.report_agent import generate_report
from backend.agents.memory_agent import (
    get_chat_history
)   
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


st.sidebar.divider()

st.sidebar.subheader(
    "💡 Suggested Questions"
)

q1 = st.sidebar.button(
    "📊 Key Findings"
)

q2 = st.sidebar.button(
    "📈 Age Distribution"
)

q3 = st.sidebar.button(
    "📄 Executive Report"
)

q4 = st.sidebar.button(
    "⚠️ Data Quality"
)

q5 = st.sidebar.button(
    "💡 Generate Insights"
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

    current_file = uploaded_file.name

    if (
        "uploaded_filename" not in st.session_state
        or
        st.session_state["uploaded_filename"]
            != current_file
    ):

        print(">>> NEW FILE DETECTED")

        st.session_state.analysis_result = (
            analyze_file(uploaded_file)
        )

        st.session_state["uploaded_filename"] = (
            current_file
        )
        st.session_state.messages = []

        st.session_state.pop(
            "insights",
            None
        )

        st.session_state.pop(
            "report",
            None
        )

        st.session_state.pop(
            "pdf_file",
            None
        )
    result = st.session_state.analysis_result

    df = result["df"]

    profile = result["profile"]

    analysis = result["analysis"]

    charts = result["charts"]


    st.sidebar.subheader(
        "📥 Export"
    )

    generate_report_btn = st.sidebar.button(
        "Generate Executive Report"
    )

    if generate_report_btn:

        report_data = {
            "rows": profile["rows"],
            "columns": profile["columns"],
            "missing_values": profile["missing_values"],
            "duplicate_rows": profile["duplicate_rows"]
        }

        report = generate_report(
            report_data,
            st.session_state.get(
                "insights",
                "No insights generated yet."
            )
        )

        from backend.utils.pdf_generator import (
            create_pdf
        )

        pdf_file = create_pdf(
            report
        )

        st.session_state["report"] = report
        st.session_state["pdf_file"] = pdf_file
    st.success(
        f"""
        Dataset Loaded Successfully

        Rows: {profile['rows']}
        Columns: {profile['columns']}
        """
    )
    

    
    report_data = {
        "rows": profile["rows"],
        "columns": profile["columns"],
        "missing_values": profile["missing_values"],
        "duplicate_rows": profile["duplicate_rows"]
    }


    st.subheader("💬 Chat With DecisionPilot AI")

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    question = None
    if q1:
        question = "What are the key findings?"

    elif q2:
        question = "Visualize age distribution"

    elif q3:
        question = "Generate executive report"

    elif q4:
        question = "Show data quality issues"

    if q5:

        from backend.agents.insight_agent import (
            generate_insights
        )

        insights = generate_insights(
            analysis
        )
        print("INSIGHTS GENERATED:")
        st.session_state["insights"] = insights
        st.success("Insights stored successfully")

        st.write(st.session_state["insights"])

    st.sidebar.divider()

    
    if "report" in st.session_state:

        st.subheader("📄 Executive Report")

        st.write(
            st.session_state["report"]
        )
    
        with open(
            st.session_state["pdf_file"],
            "rb"
        ) as file:

            st.download_button(
                label="Download PDF Report",
                data=file,
                file_name="Executive_Report.pdf",
                mime="application/pdf"
            )
    chat_question = st.chat_input(
        "Ask a business question..."
    )
    if chat_question:
        question = chat_question
    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.write(question)
        chat_history = get_chat_history(
            st.session_state.messages
        )
        result = workflow.invoke(
            {
                "question": question,
                "chat_history": chat_history,
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

            try:

                fig = generate_chart(
                    df,
                    question
                )

                with st.chat_message("assistant"):

                    if fig is None:

                        response = """
        Sorry, I cannot generate that chart yet.

        Currently supported charts:

        • Bar Chart
        • Pie Chart
        • Line Chart
        • Scatter Plot
        • Histogram
        • Box Plot
        """

                        st.write(response)

                        st.session_state.messages.append(
                            {
                                "role": "assistant",
                                "content": response
                            }
                        )

                    else:

                        st.plotly_chart(
                            fig,
                            use_container_width=True
                        )

            except Exception as e:

                with st.chat_message("assistant"):

                    st.error(
                        f"Visualization Error: {e}"
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
        if "insights" in st.session_state:

            st.subheader("💡 Business Insights")

            st.write(
                st.session_state["insights"]
            )
      
    with st.expander("🔍 Dataset Technical Details"):

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

