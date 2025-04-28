import requests, json
from config import API_KEY, API_URL, MODEL

def build_prompt(user_email: str, tone:str) -> str:
    return f"""
    You are an intelligent, polite, and professional email assistant.
    Write a smart, clear, and {tone.lower()} email response to the following message:

    \"\"\"{user_email}\"\"\"

    Make sure the response matches the tone and remains relevant to the query.
    """

def generate_email_response(user_email: str, tone: str) -> str:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model":MODEL,
        "messages":[
            {"role":"user", "content":build_prompt(user_email, tone)}
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        result = response.json()

        choices = result.get("choices")
        if choices and isinstance(choices, list):
            return choices[0]["message"]["content"]

        raise ValueError("Unexpected API response format.")

    except requests.exceptions.RequestException as req_err:
        raise Exception(f"API connection error: {req_err}")
    except ValueError as val_err:
        raise Exception(f"API response error: {val_err}")

