from backend.services.llm_service import generate_response


def generate_report(report_data, insights):

    prompt = f"""
    You are preparing an Executive Business Report.

    Dataset Information:
    {report_data}

    Business Insights Already Generated:
    {insights}

    Create a professional report.

    Structure:

    EXECUTIVE SUMMARY

    DATASET OVERVIEW

    KEY FINDINGS

    DATA QUALITY ASSESSMENT

    BUSINESS RISKS

    RECOMMENDATIONS

    CONCLUSION

    Rules:

    - Use business language
    - Use bullet points
    - Do not repeat statistics unnecessarily
    - Base recommendations on findings
    - Keep report concise and actionable
    - Use bullet points using "-" symbol
    - Every finding, risk and recommendation must be a separate bullet
    - Do not write findings in paragraph form
    """

    return generate_response(prompt)