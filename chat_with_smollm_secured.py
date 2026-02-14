import requests
import json
import sys
import os

def chat_with_smollm(prompt):
    url = "http://localhost:12434/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "ai/smollm2",
        "messages": [
            {"role": "system", "content": "You are a helpful cybersecurity assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "stream": False  # Set to True if you want to see words as they generate
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        
        result = response.json()
        return result['choices'][0]['message']['content']
    
    except requests.exceptions.RequestException as e:
        return f"Error connecting to Docker Model Runner: {e}"

def lakera(prompt):
    session = requests.Session()  # Allows persistent connection
    project_id = os.getenv("LAKERA_PROJECT_ID")
    api_key = os.getenv("LAKERA_API_KEY")
    response = session.post(
        "https://api.lakera.ai/v2/guard",
        json={"messages": [{"content": prompt, "role": "user"}],"project_id": project_id},
        headers={"Authorization": f'Bearer {api_key}'},
    )

    response_json = response.json()

    # If Lakera Guard detects any threats, do not call the LLM!
    if response_json["flagged"]:
        print("Lakera Guard identified a threat. No user was harmed by this LLM.")
        print(response_json)
    else:
        print(chat_with_smollm(prompt))
        
if __name__ == "__main__":
    # Check if a prompt was provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python ask_smollm.py \"Your prompt here\"")
    else:
        # Join all arguments after the script name into a single string
        user_prompt = " ".join(sys.argv[1:])
        print(f"\n--- SmolLM2 Response ---\n")
        print(lakera(user_prompt))
        print(f"\n------------------------")