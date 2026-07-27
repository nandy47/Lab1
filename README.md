# Submitted for Lab 1

## Chatbot

A command-line chatbot built in Python using the NVIDIA Inference API. The program allows users to have multi-turn conversations with an AI assistant and saves conversation history locally.

## How to Run

1. Install the required dependencies:

```bash
pip3 install -r requirements.txt
```

2. Create a `.env` file in the project folder and add your NVIDIA API key:

```text
NVIDIA_API_KEY=your_api_key_here
```

3. Run the chatbot:

```bash
python3 chatbot.py
```

Enter your prompts in the terminal to chat with the assistant.

To end the conversation, type:

```text
end
```

## Files

- `chatbot.py` - Main program and chat loop
- `llm.py` - Handles API calls to the NVIDIA language model
- `history.py` - Handles loading and saving conversation history
- `requirements.txt` - Lists required Python dependencies
- `.gitignore` - Ensures the `.env` file containing the API key is not committed