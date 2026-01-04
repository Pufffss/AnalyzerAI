# AnalyzerAI 🤖📊

**An Agentic AI System for Autonomous Data Analysis**

AnalyzerAI is an **agentic AI framework** built using **AutoGen** that enables users to perform end-to-end data analysis using **natural language prompts**. 
Given a CSV dataset and a user request, AnalyzerAI autonomously generates, executes, debugs, and refines Python code until the desired result is achieved.

---

## 🚀 Key Features

* **Multi-Agent Architecture** using AutoGen
* **Natural Language → Executable Python Code**
* **Self-Correcting Feedback Loop** between agents
* **Secure Docker-based Code Execution**
* Supports:

  * Data cleaning & preprocessing
  * Feature engineering
  * Machine learning model training & evaluation
  * Data visualizations & saved outputs
  * Interactive **Streamlit UI**

---

## 🧠 System Architecture

AnalyzerAI consists of **two collaborating agents**:

### 1️⃣ Data Analyzer Agent

* Takes:

  * User prompt (natural language)
  * Uploaded CSV dataset
* Responsibilities:

  * Understands the task
  * Generates task-specific Python code (EDA, ML, plots, etc.)
  * Improves the code when execution errors occur

### 2️⃣ Code Executor Agent

* Receives Python code from the Analyzer Agent
* Executes it **inside a Docker container at runtime**
* Returns:

  * Outputs (metrics, plots, files)
  * Or error logs if execution fails

🔁 If an error occurs, the executor sends it back to the analyzer agent, which refines the code and retries execution.
This loop continues **until the user’s request is fully satisfied**, after which the agents terminate.

---

## 📊 Example Use Cases

* *“Clean the dataset and remove missing values”*
* *“Normalize and scale numeric features”*
* *“Train a Decision Tree classifier and print accuracy”*
* *“Generate and save bar plots or visualizations”*
* *“Perform EDA and summarize dataset statistics”*

---

## 🖥️ Demo

A full demo showcasing:

* Agent interactions
* Error handling & recovery
* Model training & evaluation
* Visualization generation

is available in the attached **PDF** inside the repository.

---

## 🛠️ Tech Stack

* **Python**
* **AutoGen**
* **Docker**
* **Streamlit**
* **Pandas, NumPy**
* **Scikit-learn**
* **Matplotlib**
* **Seaborn**

---

## 🤝 Contributions

Contributions, ideas, and feedback are welcome!
Feel free to open an issue or submit a pull request.
