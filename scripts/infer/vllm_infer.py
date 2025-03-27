from openai import OpenAI
import base64

openai_api_key = "robobrain-123123" 
openai_api_base = "http://127.0.0.1:8000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

response = client.chat.completions.create(
    model="robobrain",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "http://images.cocodataset.org/val2017/000000039769.jpg"
                    },
                },
                {"type": "text", "text": "What is shown in this image?"},
            ],
        },
    ]
)

content = response.choices[0].message.content
print(content)