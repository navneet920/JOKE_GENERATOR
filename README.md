# JOKE_GENERATOR
# 😂 Smart Joke Generator App (LangChain + Streamlit)

An AI-powered interactive web application that generates jokes based on a given topic and provides explanation, summary, and sentiment analysis using **LangChain Runnables** and **Hugging Face models**.

---

## 🚀 Features

- 🎯 Generate jokes based on any topic  
- 🌐 Language support (Hindi / English)  
- 🔁 Generate multiple jokes at once  
- 🧠 Explanation of each joke  
- ✍️ One-line summary of jokes  
- 📊 Sentiment analysis (Positive / Neutral / Negative)  
- 📥 Download results as a text file  
- 🖥️ Interactive UI using Streamlit  

---

## 🧠 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** LangChain (RunnableSequence, PromptTemplate)  
- **LLM:** Hugging Face (`google/flan-t5-base`)  
- **Language:** Python  
- **Environment:** dotenv  

---

## 📁 Project Structure
# 😂 Smart Joke Generator App (LangChain + Streamlit)

An AI-powered interactive web application that generates jokes based on a given topic and provides explanation, summary, and sentiment analysis using **LangChain Runnables** and **Hugging Face models**.

---

## 🚀 Features

- 🎯 Generate jokes based on any topic  
- 🌐 Language support (Hindi / English)  
- 🔁 Generate multiple jokes at once  
- 🧠 Explanation of each joke  
- ✍️ One-line summary of jokes  
- 📊 Sentiment analysis (Positive / Neutral / Negative)  
- 📥 Download results as a text file  
- 🖥️ Interactive UI using Streamlit  

---

## 🧠 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** LangChain (RunnableSequence, PromptTemplate)  
- **LLM:** Hugging Face (`google/flan-t5-base`)  
- **Language:** Python  
- **Environment:** dotenv  

---

## 📁 Project Structure
```
project/
│
├── app.py # Streamlit UI
├── llm_logic.py # LangChain backend logic
├── requirements.txt
├── .env

```


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/joke-generator-app.git
cd joke-generator-app
```

## Create Virtual Environment
```
python -m venv .venv
.venv\Scripts\activate
source .venv/bin/activate
```

## Install Dependencies
```aiignore
pip install -r requirements.txt
```

## Add Hugging Face API Key
```
HUGGINGFACEHUB_API_TOKEN=your_api_key_here
```

## Run the Application

```aiignore
streamlit run app.py
```

## 🎯 How It Works

- User enters a topic
- App generates jokes using LLM
- Each joke is processed through:
- Explanation generation
- Summary generation
- Results are displayed in UI
- User can download results

## Core Concepts Used
- RunnableSequence (LangChain pipeline)
- Prompt Engineering
- Sequential LLM chaining (Joke → Explanation → Summary → Sentiment)
- Modular architecture (UI + backend separation)

## 💡 Example

```aiignore
Input

Topic: Dost
Language: English
```

## Output:
```aiignore
Joke 😂
Summary ✍️
```
## 🚀 Future Improvements
- Add chat memory (conversation history)
- Integrate advanced LLMs (GPT / Mistral)
- Deploy on AWS / Streamlit Cloud
- Add voice input/output
- Store results in database
- Build REST API using FastAPI

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and improve it.

## 📜 License

This project is open-source and free to use.

# 👨‍💻 Author

Navneet Kumar

Data Scientist | AI/ML Engineer

