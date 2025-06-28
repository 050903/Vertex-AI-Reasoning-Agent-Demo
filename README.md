![Project Icon](https://img.icons8.com/color/96/000000/artificial-intelligence.png)

# Vertex AI Reasoning Agent Demo

This project demonstrates a simple AI agent using Google Vertex AI Reasoning Engines, with a PyQt6-based GUI for user interaction. The agent performs basic addition of two numbers and showcases how to deploy and interact with a custom reasoning engine on Vertex AI.

## Features
- **Simple Addition Agent**: Adds two integers and returns the result.
- **PyQt6 GUI**: User-friendly interface to input numbers and view results.
- **Google Vertex AI Integration**: Uses Vertex AI Reasoning Engines for agent deployment and querying.

## File Overview
- `addition_agent.py`: Defines and deploys a simple addition agent to Vertex AI Reasoning Engines.
- `reasoning_ui.py`: PyQt6 GUI to interact with the deployed reasoning agent.
- `cli.txt`: Example command to run the GUI application.
- `requirements.txt`: Python dependencies for the project.

## Setup
1. **Clone the repository** and navigate to the project directory.
2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### 1. Deploy the Addition Agent
- Run `addition_agent.py` to deploy the agent to Vertex AI (ensure you have configured your Google Cloud credentials and have the necessary permissions):
  ```bash
  python addition_agent.py
  ```

### 2. Launch the GUI
- Run the GUI to interact with the agent:
  ```bash
  python reasoning_ui.py
  ```
- Or use the command in `cli.txt` if you want to use a specific Python interpreter.

### 3. Using the App
- Enter two integers separated by a space (e.g., `3 4`) and click "Ask Reasoning Agent". The result will be displayed below.

## Requirements
- Python 3.8+
- Google Cloud account with Vertex AI enabled
- See `requirements.txt` for all Python dependencies

## Notes
- You must have valid Google Cloud credentials set up (e.g., via `gcloud auth application-default login`).
- The project IDs, region, and engine IDs are hardcoded for demo purposes. Update them as needed for your own deployment.

## License
MIT License © 2025 Tran The Hao 