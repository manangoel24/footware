 # 👟 AI Shoe Advisor

This app helps users find the perfect pair of shoes based on comfort, purpose, durability, and personal style — powered by OpenAI.

## 🚀 Features
- 🎯 Personalized recommendations from GPT
- 🧠 Context-aware logic using uploaded files (e.g. shoe reviews, receipts)
- 🎨 AI-generated shoe design using DALL·E (or OpenAI Image API)
- 📂 File uploader with PDF/image support (RAG-style)
- 🖼️ Clean Streamlit interface with sidebar + output preview

## 🛠️ Setup
```bash
# Clone the repo
pip install -r requirements.txt

# Add your OpenAI key
export OPENAI_API_KEY="sk-..."  # Or create .env with it

# Run the app
streamlit run app.py
```

## 📁 Project Structure
```
├── app.py                # Main Streamlit UI
├── utils/
│   ├── agents.py         # GPT-powered agent logic
│   ├── image_gen.py      # DALL·E image generation
│   └── rag.py            # Upload processing & RAG context
├── requirements.txt
└── README.md
```

## 📌 Example Use Case
> "I'm looking for stylish shoes for casual wear that are very comfortable and last 2+ years."

The AI will respond with a custom recommendation, explain why, and show a shoe concept image.

---

