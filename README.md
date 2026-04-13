# Social-to-Lead-Agentic-Workflow
## Tech Stack
- Python
- LangChain (conceptual use)
- JSON-based knowledge base

## Architecture
The system uses a modular architecture:
- Intent module classifies user input
- RAG module retrieves relevant information
- Agent manages conversation state
- Tool executes lead capture

State is maintained using a custom AgentState class.

## How to Run
```bash
pip install -r requirements.txt
python app.py
