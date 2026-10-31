from ollama import chat
from resume_schema import Resume

response = chat(
    model="gemma3:4b",
    messages=[
        {
            "role": "user",
            "content": """
            Extract this information:

            Name: Mohammad
            Email: test@example.com
            Skills: Python, C++, MATLAB

            Return the extracted information.
            """
        }
    ],
    format=Resume.model_json_schema(),
    options={"temperature": 0},
)

print(response.message.content)