from llm import call_model
from history import load_history,save_history,conversations_file

def run_chat(messages):

    while True:
        #take an input from user
        user_input = input("Enter prompt: ").strip()

        #solving for empty prompt - not calling the API
        if not user_input:
            print("Please enter a prompt")
            continue
        
        if user_input.strip().lower() == "end":
            break

        #add that input to the messages list as a dictionary
        messages.append({"role":"user","content":user_input})

        #call the model with messages
        response = call_model(messages)

        #add the response to the messages list as a dictionary
        messages.append({"role":"assistant","content":response})

        print(f"Assistant: {response}")

    return messages

if __name__ == "__main__":
    messages = load_history(conversations_file)
    messages = run_chat(messages)
    save_history(conversations_file,messages)
    print(f"Saved to {conversations_file}")