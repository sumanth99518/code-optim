from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
template = (
"    You are an expert software engineer and code optimizer. Your task is to analyze and improve the given code while preserving its functionality. Provide optimized code with explanations."
"### **Instructions:**"
"    - Improve code readability, maintainability, and efficiency."
"    - Optimize performance (e.g., reduce loops, use built-in functions)."
"    - Follow best coding practices and language-specific guidelines."
"    - Ensure security by identifying vulnerabilities (e.g., SQL injection, XSS)."
"    - Provide a **clear explanation** of the changes."
"### **Input Code:**"
"{code}"
"### **Optimized Code:**"
)
model = OllamaLLM(model="deepseek-r1")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
def optimize_code(code):
    response = chain.invoke({"code": code})
    return response
