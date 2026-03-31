# llm_logic.py

from dotenv import load_dotenv
import os

from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# LLM
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
)

model=ChatHuggingFace(llm=llm)
parser = StrOutputParser()

# 🔹 Main function
def generate_jokes(topic, language="English", num_jokes=1):

    results = []

    for _ in range(num_jokes):

        # Language condition
        if language == "Hindi":
            joke_prompt = PromptTemplate.from_template(
                "Write a 10 line funny joke in Hindi about {topic}"
            )
        else:
            joke_prompt = PromptTemplate.from_template(
                "Write a 10 line funny joke in English about {topic}"
            )

        explain_prompt = PromptTemplate.from_template(
            "Summaries this joke in simple words:\n{text}"
        )



        # Chains
        joke_chain = joke_prompt | model | parser
        explain_chain = explain_prompt | model | parser

        joke = joke_chain.invoke({"topic": topic})
        explanation = explain_chain.invoke({"text": joke})

        results.append({
            "joke": joke,
            "explanation": explanation,
        })

    return results