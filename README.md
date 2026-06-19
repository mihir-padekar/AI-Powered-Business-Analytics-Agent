<img width="1914" height="867" alt="image" src="https://github.com/user-attachments/assets/734fedf9-fc4c-4ef0-a2d0-6ff671a40afc" /># 📊 DecisionPilot AI

An AI-powered Business Analytics Assistant that transforms raw CSV datasets into actionable business insights, visualizations, and executive reports using LLMs, LangGraph, and Streamlit.

## 🚀 Live Demo

🔗 **Try the application:**
[https://ai-powered-business-analytics-agent.streamlit.app/]

---

## 🎯 Overview

DecisionPilot AI helps users analyze business datasets without writing code.

Simply upload a CSV file and interact with the data through a conversational chat interface.

The application automatically performs:

* Dataset profiling
* Statistical analysis
* Business insight generation
* Dynamic visualizations
* Executive report generation
* PDF export

---

## ✨ Features

### 📁 CSV Upload & Profiling

* Upload any CSV dataset
* Automatic schema detection
* Missing value analysis
* Duplicate detection
* Data type inspection

### 📊 Business Analytics

* Summary statistics
* Categorical analysis
* Data quality assessment
* Key business findings

### 💬 AI Chat Assistant

Ask questions in natural language such as:

* What is this dataset about?
* What are the key insights?
* What business risks do you see?
* Expand on the second finding.

### 📈 Dynamic Visualizations

Generate charts directly from chat:

* Bar Charts
* Pie Charts
* Line Charts
* Scatter Plots
* Histograms
* Box Plots

### 📄 Executive Reports

Generate professional business reports containing:

* Executive Summary
* Dataset Overview
* Key Findings
* Data Quality Assessment
* Business Risks
* Recommendations
* Conclusion

### 📥 PDF Export

Download executive reports as PDF files.

---

## 🏗️ Architecture

User Upload CSV
↓
Dataset Profiling
↓
Analytics Engine
↓
AI Assistant (LangGraph Workflow)
↓
Insights / Visualizations / Reports
↓
PDF Export

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### AI & Workflow

* LangGraph
* Groq LLM
* Prompt Engineering

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly

### Reporting

* FPDF

---

## 📦 Installation

Clone the repository:

```bash
https://github.com/mihir-padekar/AI-Powered-Business-Analytics-Agent.git

cd AI-Powered-Business-Analytics-Agent
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Run the application:

```bash
streamlit run frontend/app.py
```

---

## 📸 Screenshots

Add screenshots here:

* Home Screen
<img width="1919" height="857" alt="image" src="https://github.com/user-attachments/assets/d45832a0-1f86-41ed-a520-df0cf2beb873" />

* Chat Interface
  <img width="1914" height="867" alt="image" src="https://github.com/user-attachments/assets/420b63c9-3b18-444f-84b0-d6abee70c62b" />

* Dynamic Visualization
  <img width="1900" height="864" alt="image" src="https://github.com/user-attachments/assets/2db88c92-e9a8-48a4-86d1-c24b3d891edc" />

* Executive Report
<img width="1919" height="870" alt="image" src="https://github.com/user-attachments/assets/2e47ea6d-837a-48f4-8e47-0b7bbee3b61b" />

---

## 🔮 Future Improvements

* Enhanced conversation memory
* Advanced chart recommendations
* Multi-file analysis
* Additional report templates
* FastAPI deployment backend

---

## 👨‍💻 Author

Mihir Padekar

MCA (Data Science)

AI | Machine Learning | Generative AI | Data Analytics
