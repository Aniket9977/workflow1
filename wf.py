import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langsmith import Client  
load_dotenv()

OPENAI_API_KEY= os.getenv("OPENAI_API")
os.environ["OPENAI_API_KEY"] =OPENAI_API_KEY
os.environ["LANGCHAIN_TRACING_V2"] = "true" 
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
LANGCHAIN_API_KEY= os.getenv("LANGSMIT_API")
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
os.environ["LANGCHAIN_PROJECT"] = "WorkOrderGenerator"  


langsmith_client = Client()


def get_user_input(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value
        else:
            print("Input cannot be empty. Please try again.")
prompt_template = """
You are an expert in construction management. Your task is to generate a standard construction work order in Markdown format for the following company and contractor:
Company Name: {company_name}
Contractor Name: {contractor_name}
The work order should include the following sections:
1. **Header** with the company name and a work order number (use 'WO-001' as the number).
2. **Contractor Information** section with the contractor's name and a generic contact placeholder.
3. **Scope of Work** section. Since no specific task is provided, assume a generic construction project (e.g., building foundations).
4. **Materials and Labor** section. Provide generic information about materials and labor.
5. **Terms and Conditions** section with standard clauses (e.g., payment terms, signatures required).
Please generate the work order in Markdown format, suitable for printing or sharing.
"""

# Initialize the LLM
llm = OpenAI(temperature=0.2) 

prompt = PromptTemplate(
    input_variables=["company_name", "contractor_name"],
    template=prompt_template
)


chain = LLMChain(llm=llm, prompt=prompt)

company_name = get_user_input("Enter the company name: ")
contractor_name = get_user_input("Enter the contractor name: ")

print("\nGenerating work order...")
work_order = chain.run({
    "company_name": company_name,
    "contractor_name": contractor_name
})

print("\nGenerated Work Order:\n")
print(work_order)

with open("work_order.md", "w") as file:
    file.write(work_order)
print("\nWork order saved to 'work_order.md'.")