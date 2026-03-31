from dotenv import load_dotenv

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

        if language == "Hindi":
            joke_prompt = PromptTemplate.from_template(
                "Write a 10 line funny joke in Hindi about {topic}"
            )
            summary_prompt = PromptTemplate.from_template(
                "Read the following joke and summarize it in Hindi in one line:\n{text}"
            )
        else:
            joke_prompt = PromptTemplate.from_template(
                "Write a 10 line funny joke in English about {topic}"
            )
            summary_prompt = PromptTemplate.from_template(
                "Read the following joke and summarize it in English in one line:\n{text}"
            )


        joke_chain = joke_prompt | model | parser
        summary_chain = summary_prompt | model | parser


        joke = joke_chain.invoke({"topic": topic})
        summary = summary_chain.invoke({"text": joke})


        results.append({
            "joke": joke,
            "summary": summary,
        })

    return results