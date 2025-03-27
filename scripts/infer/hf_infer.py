import torch
from transformers import AutoProcessor, AutoModelForPreTraining

model_id = "BAAI/RoboBrain"

print("Loading Checkpoint ...")
model = AutoModelForPreTraining.from_pretrained(
    model_id, 
    torch_dtype=torch.float16, 
    low_cpu_mem_usage=True, 
).to("cuda:0")

processor = AutoProcessor.from_pretrained(model_id)

# Define a chat history and use `apply_chat_template` to get correctly formatted prompt
# Each value in "content" has to be a list of dicts with types ("text", "image") 
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What is shown in this image?"},
            {"type": "image", "url": "http://images.cocodataset.org/val2017/000000039769.jpg"},
        ],
    },
]

print("Processing input...")
inputs = processor.apply_chat_template(
    messages, 
    add_generation_prompt=True, 
    tokenize=True, 
    return_dict=True, 
    return_tensors="pt"
)

inputs = {k: v.to("cuda:0") for k, v in inputs.items()}

print("Generating output...")
output = model.generate(**inputs, max_new_tokens=250)
print(processor.decode(output[0][2:], skip_special_tokens=True))