from ollama import chat

response = chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": """
            Extract the following resume information into JSON:
            name, email, skills, and education.

            Resume:
            John Smith
            Email: john.smith@example.com
            Skills: Python, C++, OpenCV
            B.Sc. in Computer Engineering, Example University, 2020-2024

            Return only a JSON object. Do not invent missing information.
            """
                }
            ],
            format="json",
)

print(response.message.content)