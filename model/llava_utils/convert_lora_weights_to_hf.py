import glob, os
import torch
import shutil
import argparse
from safetensors import safe_open
from safetensors.torch import save_file

KEYS_TO_MODIFY_MAPPING = {
    "base_model.model.": "",
    "model.vision_tower.": "",
    "model.mm_projector": "multi_modal_projector",
    "model": "model.model",
    "vision_model.model": "vision_model",
    "lm_head": "language_model.lm_head",
    "model.model": "language_model.model",
    "multi_modal_projector.0": "multi_modal_projector.linear_1",
    "multi_modal_projector.2": "multi_modal_projector.linear_2",
    "language_model.model.image_newline": "image_newline",
}

def load_original_state_dict(model_dir):
    directory_path = model_dir

    original_state_dict = {}
    for path in glob.glob(f"{directory_path}/*"):
        if path.endswith(".safetensors"):
            with safe_open(path, framework="pt", device="cpu") as f:
                for key in f.keys():
                    original_state_dict[key] = f.get_tensor(key)

    return original_state_dict

def convert_state_dict_to_hf(state_dict):
    new_state_dict = {}
    for key, value in state_dict.items():
        if key.endswith(".inv_freq"):
            continue
        for key_to_modify, new_key in KEYS_TO_MODIFY_MAPPING.items():
            if key_to_modify in key:
                key = key.replace(key_to_modify, new_key)
        key = "base_model.model." + key
        new_state_dict[key] = value.to(torch.float16)
    return new_state_dict

def convert_lora_to_hf(model_dir, dump_path):
    # Load original state dict
    print("Load original state dict ...")
    state_dict = load_original_state_dict(model_dir)
    
    # Convert keys to HF format
    print("Convert keys to HF format ...")
    state_dict = convert_state_dict_to_hf(state_dict)
    
    # Save converted state dict
    print("Save converted state dict ...")
    os.makedirs(dump_path,exist_ok=True)
    save_file(state_dict, f"{dump_path}/adapter_model.safetensors")

    shutil.copy2(f"{model_dir}/adapter_config.json", f"{dump_path}/adapter_config.json")
    
    print(f"Converted LORA weights saved to {dump_path}/adapter_model.safetensors")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model_dir", type=str, required=True, help="Path to the input PyTorch model directory."
    )
    parser.add_argument(
        "--dump_path", type=str, required=True, help="Path to the output PyTorch model directory."
    )
    args = parser.parse_args()

    convert_lora_to_hf(args.model_dir, args.dump_path)
