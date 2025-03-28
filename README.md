<div align="center">
<img src="./assets/logo.jpg" width="400"/>
</div>

# **RoboBrain**: A Unified Brain Model for Robotic Manipulation from Abstract to Concrete.



<p align="center">
        </a>&nbsp&nbsp⭐️ <a href="https://superrobobrain.github.io/">Project</a></a>&nbsp&nbsp | &nbsp&nbsp🤗 <a href="https://huggingface.co/BAAI/RoboBrain/">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://superrobobrain.github.io/">ModelScope</a>&nbsp&nbsp | &nbsp&nbsp🌎 <a href="https://github.com/FlagOpen/ShareRobot">Dataset</a>&nbsp&nbsp | &nbsp&nbsp📑 <a href="http://arxiv.org/abs/2502.21257">Paper</a>&nbsp&nbsp | &nbsp&nbsp💬 <a href="https://superrobobrain.github.io/">WeChat</a>
</p>
<p align="center">
        </a>&nbsp&nbsp🎯 <a href="">RoboOS (Coming Soon)</a>: An Efficient Open-Source Multi-Robot Coordination System for RoboBrain.
</p>
<p align="center">
</a>&nbsp&nbsp🎯 <a href="https://tanhuajie.github.io/ReasonRFT/">ReasonRFT</a>: Exploring a New RFT Paradigm to Enhance RoboBrain's Visual Reasoning Capabilities.
</p>

## 🔥 Overview
Recent advancements in Multimodal Large Language Models (MLLMs) have shown remarkable capabilities across various multimodal contexts. However, their application in robotic scenarios, particularly for long-horizon manipulation tasks, reveals significant limitations. These limitations arise from the current MLLMs lacking three essential robotic brain capabilities: **(1) Planning Capability**, which involves decomposing complex manipulation instructions into manageable sub-tasks; **(2) Affordance Perception**, the ability to recognize and interpret the affordances of interactive objects; and **(3) Trajectory Prediction**, the foresight to anticipate the complete manipulation trajectory necessary for successful execution. To enhance the robotic brain's core capabilities from abstract to concrete, we introduce ShareRobot, a high-quality heterogeneous dataset that labels multi-dimensional information such as task planning, object affordance, and end-effector trajectory. ShareRobot's diversity and accuracy have been meticulously refined by three human annotators. Building on this dataset, we developed RoboBrain, an MLLM-based model that combines robotic and general multi-modal data, utilizes a multi-stage training strategy, and incorporates long videos and high-resolution images to improve its robotic manipulation capabilities. Extensive experiments demonstrate that RoboBrain achieves state-of-the-art performance across various robotic tasks, highlighting its potential to advance robotic brain capabilities.

<div align="center">
<img src="./assets/overview.png" />
</div>

## 🚀 Features
This repository supports:
- **`Data Preparation`**: Please refer to [Dataset Preparation](https://github.com/FlagOpen/ShareRobot) for how to prepare the dataset.
- **`Training for RoboBrain`**: Please refer to [Training Section](#Training) for the usage of training scripts.
- **`Support HF/VLLM Inference`**: Please see [Inference  Section](#Inference), now we support inference with [VLLM](https://github.com/vllm-project/vllm).
- **`Evaluation for RoboBrain`**: Please refer to [Evaluation Section](#Evaluation) for how to prepare the benchmarks.
- **`ShareRobot Generation`**: Please refer to [ShareRobot](https://github.com/FlagOpen/ShareRobot) for details.


## 🗞️ News

- **`2025-03-27`**: 🤗 We have released [Planning Checkpoint](https://huggingface.co/BAAI/RoboBrain/) in Huggingface.
- **`2025-03-26`**: 🔥 We have released the [RoboBrain](https://superrobobrain.github.io/) repository.
- **`2025-02-27`**: 🌍 Our [RoboBrain](https://superrobobrain.github.io/) was accepted to CVPR2025.


## 📆 Todo
- [x] Release scripts for model training and inference.
- [x] Release Planning checkpoint.
- [ ] Release Affordance and Trajectory checkpoints.
- [ ] Release ShareRobot dataset.
- [ ] Release evaluation scripts for Benchmarks.
- [ ] Training more powerful Robobrain (v2).


## 🤗 Models

- **[`Base Planning Model`](https://huggingface.co/BAAI/RoboBrain/)**: The model was trained on general datasets in Stages 1–2 and on the Robotic Planning dataset in Stage 3, which is designed for Planning prediction.
- **[`A-LoRA for Affordance`](https://github.com/FlagOpen/RoboBrain/)**: Based on the Base Planning Model, Stage 4 involves LoRA-based training with our Affordance dataset to predict affordance. *(Coming Soon)*
- **[`T-LoRA for Trajectory`](https://github.com/FlagOpen/RoboBrain/)**: Based on the Base Planning Model, Stage 4 involves LoRA-based training with our Trajectory dataset to predict trajectory. *(Coming Soon)*

<div align="center">
<img src="./assets/training.png" />
</div>

| Models               | Checkpoint                                                     | Description                                                | 
|----------------------|----------------------------------------------------------------|------------------------------------------------------------|
| Planning Model       | [🤗 Planning CKPTs](https://huggingface.co/BAAI/RoboBrain/)   | Used for Planning prediction in our paper                   | 
| Affordance (A-LoRA)  | [🤗 Affordance CKPTs](https://superrobobrain.github.io/)      | Used for Affordance prediction in our paper *(Coming Soon)* | 
| Trajectory (T-LoRA)  | [🤗 Trajectory CKPTs](https://superrobobrain.github.io/)      | Used for Trajectory prediction in our paper *(Coming Soon)* | 


## 🛠️ Setup

```bash
# clone repo.
git clone https://github.com/FlagOpen/RoboBrain.git
cd RoboBrain

# build conda env.
conda create -n robobrain python=3.10
conda activate robobrain
pip install -r requirements.txt
```

## <a id="Training"> 🤖 Training</a>

### 1. Data Preparation

```bash
# Modify datasets for Stage 1, please refer to:
- yaml_path: scripts/train/yaml/stage_1_0.yaml

# Modify datasets for Stage 1.5, please refer to:
- yaml_path: scripts/train/yaml/stage_1_5.yaml

# Modify datasets for Stage 2_si, please refer to:
- yaml_path: scripts/train/yaml/stage_2_si.yaml

# Modify datasets for Stage 2_ov, please refer to:
- yaml_path: scripts/train/yaml/stage_2_ov.yaml

# Modify datasets for Stage 3_plan, please refer to:
- yaml_path: scripts/train/yaml/stage_3_planning.yaml

# Modify datasets for Stage 4_aff, please refer to:
- yaml_path: scripts/train/yaml/stage_4_affordance.yaml

# Modify datasets for Stage 4_traj, please refer to:
- yaml_path: scripts/train/yaml/stage_4_trajectory.yaml
```
**Note:** The sample format in each json file should be like:
```json
{
    "id": "xxxx",
    "image": [
        "image1.png",
        "image2.png",
    ],
    "conversations": [
        {
            "from": "human",
            "value": "<image>\n<image>\nAre there numerous dials near the bottom left of the tv?"
        },
        {
            "from": "gpt",
            "value": "Yes. The sun casts shadows ... a serene, clear sky."
        }
    ]
},
```

### 2. Training 
```bash
# Training on Stage 1:
bash scripts/train/stage_1_0_pretrain.sh

# Training on Stage 1.5:
bash scripts/train/stage_1_5_direct_finetune.sh

# Training on Stage 2_si:
bash scripts/train/stage_2_0_resume_finetune_si.sh

# Training on Stage 2_ov:
bash scripts/train/stage_2_0_resume_finetune_ov.sh

# Training on Stage 3_plan:
bash scripts/train/stage_3_0_resume_finetune_robo.sh

# Training on Stage 4_aff:
bash scripts/train/stage_4_0_resume_finetune_lora_a.sh

# Training on Stage 4_traj:
bash scripts/train/stage_4_0_resume_finetune_lora_t.sh
```
**Note:** Please change the environment variables (e.g. *DATA_PATH*, *IMAGE_FOLDER*, *PREV_STAGE_CHECKPOINT*) in the script to your own.

### 3. Convert original weights to HF weights
```bash
python scripts/infer/convert_robobrain_to_hf.py --model_dir /path/to/original/checkpoint/ --dump_path /path/to/output/
```


## <a id="Inference">🤖 Inference</a>

### Option 1: HF inference

#### Run python script as example:
```python
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

```

### Option 2: VLLM inference
#### Install and launch VLLM
```bash
# Install vllm package
pip install vllm==0.6.6.post1

# Launch Robobrain with vllm
python -m vllm.entrypoints.openai.api_server --model BAAI/RoboBrain --served-model-name robobrain  --max_model_len 16384 --limit_mm_per_prompt image=8
```

#### Run python script as example:
```python
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
```
## <a id="Evaluation">🤖 Evaluation</a>
*Coming Soon ...*

<div align="center">
<img src="./assets/result.png" />
</div>

## 😊 Acknowledgement  

We would like to express our sincere gratitude to the developers and contributors of the following projects:  
1. [LLaVA-NeXT](https://github.com/LLaVA-VL/LLaVA-NeXT): The comprehensive codebase for training Vision-Language Models (VLMs).  
2. [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval): A powerful evaluation tool for Vision-Language Models (VLMs).
3. [vllm](https://github.com/vllm-project/vllm): A high-throughput and memory-efficient LLMs/VLMs inference engine.
4. [OpenEQA](https://github.com/facebookresearch/open-eqa): A wonderful benchmark for Embodied Question Answering.
5. [RoboVQA](https://github.com/google-deepmind/robovqa): Provide high-level reasoning models and datasets for robotics applications.

Their outstanding contributions have played a pivotal role in advancing our research and development initiatives.

## 📑 Citation
If you find this project useful, welcome to cite us.
```bib
@article{ji2025robobrain,
  title={RoboBrain: A Unified Brain Model for Robotic Manipulation from Abstract to Concrete},
  author={Ji, Yuheng and Tan, Huajie and Shi, Jiayu and Hao, Xiaoshuai and Zhang, Yuan and Zhang, Hengyuan and Wang, Pengwei and Zhao, Mengdi and Mu, Yao and An, Pengju and others},
  journal={arXiv preprint arXiv:2502.21257},
  year={2025}
}
```
