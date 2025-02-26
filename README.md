# Construction Work Order Generator

This project is a Python script that generates construction work orders in Markdown format using **LangChain** and **LangSmith**. It takes user inputs for a company name and contractor name, then creates a standardized work order document with predefined sections. The process is traced using LangSmith for visibility into the workflow.

## Features
- Generates a work order with sections: Header, Contractor Information, Scope of Work, Materials and Labor, and Terms and Conditions.
- Uses OpenAI's LLM via LangChain to create the document.
- Integrates LangSmith for tracing and monitoring the generation process.
- Saves the output as a Markdown file (`work_order.md`).

## Prerequisites
- **Python 3.8+**: Ensure Python is installed on your system.
- **API Keys**:
  - OpenAI API key (get it from [OpenAI](https://platform.openai.com/)).
  - LangSmith API key (get it from [LangSmith](https://smith.langchain.com/)).
- **Dependencies**:
  - `langchain`
  - `openai`
  - `python-dotenv`
  - `langsmith`

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Aniket9977/workflow1.git
   cd construction-work-order-generator
   ```


2.**Install Dependencies**:
  ```bash
    pip install langchain openai python-dotenv langsmith
  ```


3. **Set Up Environment Variables**:
  Create a .env file in the project root directory:
  ```bash
    OPENAI_API=your-openai-api-key
    LANGCHAIN_API=your-langsmith-api-key
  ```
  
Replace your-openai-api-key and your-langsmith-api-key with your actual keys.


Usage
Run the Script:
```bash
    python wf.py
  ```
## Follow Prompts:
  Enter the company name when prompted.
  Enter the contractor name when prompted.


## Output:

The generated work order is printed to the console.
It’s also saved as work_order.md in the project directory.
View Tracing:
Go to LangSmith, log in, and navigate to the "WorkOrderGenerator" project to see the execution flow.