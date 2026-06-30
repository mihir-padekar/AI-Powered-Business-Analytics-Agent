import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
llm_call_count = 0

def generate_response(prompt,agent_name="Unknown Agent"):

    global llm_call_count

    llm_call_count += 1

    print("\n========================")
    print(f"LLM CALL #{llm_call_count}")
    print(f"Prompt Length: {len(prompt)} chars")
    print("========================")
    
    response = client.chat.completions.create(
        model="qwen/qwen3-27b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
