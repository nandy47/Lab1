import json
from pathlib import Path

conversations_dir = Path("conversations")
conversations_file = conversations_dir / "chat1.json"

def load_history(path):
    #load the file, read the json object
    
    if not path.exists():
        messages = [{"role":"system","content":"You are a helpful assistant."}]
        return messages
    
    #solving for corrupted JSON file on load.
    try:
        with open(path,'r',encoding='utf-8') as f:
            return json.load(f)
    
    except json.decoder.JSONDecodeError:
        print("Warning: Conversation history is invalid. Starting a new conversation.")
        return [{"role": "system", "content": "You are a helpful assistant."}]


def save_history(path,messages):
    #open the file in write mode, save messages as json object
    with open(path, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2)
