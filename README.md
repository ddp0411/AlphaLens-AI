
# 🚀 AgentFinance AI – Smart Investment Research Assistant

> A GenAI-powered financial analyst that fetches real-time stock data, analyzes SEC filings, generates risk summaries, and delivers actionable investment recommendations using an autonomous multi-agent system.

---

## 📌 Features

- 🔍 **Data Collector Agent** – fetches real-time data from Yahoo Finance & Alpha Vantage
- 📉 **Risk Analysis Agent** – evaluates financial risks from stock and earnings reports
- 📊 **Recommendation Generator Agent** – generates Buy/Hold/Sell advice
- 💬 **Q&A Analyst Agent** – answers user queries using vectorized SEC filings
- 🧠 **LangChain + LangGraph** powered multi-agent architecture
- 🧪 **LangSmith** evaluation for hallucination tracking and LLM quality

## 🗂️ Project Structure

```bash
agentfinance_ai/
├── app/
│   ├── agents/                    # All GenAI-powered agents
│   │   ├── data_collector.py
│   │   ├── risk_analyzer.py
│   │   ├── recommendation_generator.py
│   │   └── qa_analyst.py
│   ├── chains/
│   │   └── langgraph_pipeline.py  # Multi-agent pipeline graph
│   ├── llm/
│   │   ├── embeddings.py
│   │   ├── vectorstore.py
│   │   └── summarizer.py          # For ingesting SEC filings
│   ├── routes/
│   │   ├── dashboard.py
│   │   ├── insights.py
│   │   └── recommendation.py
│   ├── utils/
│   │   ├── api_utils.py
│   │   ├── filings_parser.py
│   │   └── evaluation.py
│   ├── main.py                    # FastAPI app entrypoint
│   └── config.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── requirements.txt
├── Dockerfile                    # (Optional - for containerized use)
├── render.yaml                   # Render deployment config (optional)
└── README.md                     # Project documentation



⚙️ Setup Instructions (Local)

1. 🔧 Clone the Repository

git clone https://github.com/yourusername/agentfinance-ai.git
cd agentfinance-ai

2. 📦 Create .env File

ALPHA_VANTAGE_API_KEY=your_alpha_key
OPENAI_API_KEY=your_openai_key

3. 📥 Install Dependencies

pip install -r requirements.txt

4. 📚 Ingest SEC Filings

Place PDFs into data/sec_filings/, then run:

python -c "from app.llm.summarizer import ingest_filings; ingest_filings()"

5. 🚀 Run Locally

uvicorn app.main:app --reload

Visit: http://localhost:8000


🚀 Deployment on Render (No Docker)

📝 Steps:

1. Push your code to GitHub


2. Go to https://render.com → New → Web Service


3. Connect your repo


4. Fill in:

Build Command: pip install -r requirements.txt

Start Command: uvicorn app.main:app --host=0.0.0.0 --port=10000



5. Add Environment Variables:

ALPHA_VANTAGE_API_KEY

OPENAI_API_KEY



6. Click "Deploy"



After deployment, your app will be available at:

https://<your-app-name>.onrender.com


🌐 Frontend Usage

Open frontend/index.html in your browser to:

Enter a stock symbol

Fetch recommendations

Display real-time JSON result from FastAPI backend


📈 Example Usage

GET /recommendation/run?symbol=AAPL

Response:
{
  "recommendation": {
    "symbol": "AAPL",
    "alpha_vantage": {...},
    "yfinance": {...},
    "risk_summary": "Low short-term risk...",
    "final_verdict": "✅ Buy - Strong fundamentals and stable cash flow"
  }
}

🧪 Powered by GenAI Stack

LangChain Agents

LangGraph Node Flow

LangSmith Evaluation

OpenAI GPT APIs

FAISS Vector Retrieval from SEC PDFs


🧠 Future Enhancements

📅 Scheduled portfolio analysis

🗣️ Voice-based Q&A

📊 Visual dashboards using Plotly

💼 CRM-style portfolio history


💡 Credits

Built by Devanshu Vijay Patil
Part of a GenAI ecosystem learning series.



📬 Feedback / Contact

Want to contribute, ask questions, or partner?
→ Email: devanshupatil1712@gmail.com
→ LinkedIn: https://www.linkedin.com/in/devanshu-patil-8618b3222





