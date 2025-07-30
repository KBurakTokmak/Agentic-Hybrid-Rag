import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM
from trl import DPOConfig, DPOTrainer

from huggingface_hub import login


dpo_data_pth = "./dpo_data.csv"

def create_data_from_csv(csv_path):
  df = pd.read_csv(csv_path, encoding='latin-1')
  data = []
  for idx, row in df.iterrows():
    prompt = f"Question: {row['question']} \nAnswer:"
    chosen = row['correct_response']
    rejected = row['wrong_response']
    data.append({
        "prompt": prompt,
        "chosen": chosen,
        "rejected": rejected,
    })
    dataset = Dataset.from_list(data)
  return dataset

def create_model(model_name):
  tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
  tokenizer.pad_token = tokenizer.eos_token

  model = AutoModelForCausalLM.from_pretrained(
      model_name,
      trust_remote_code=True,
      torch_dtype="auto",
      device_map="auto",
  )
  return tokenizer, model

dataset = create_data_from_csv(dpo_data_pth)

tokenizer, model = create_model("mistralai/Mistral-7B-Instruct-v0.2")

training_args = DPOConfig(output_dir="./", logging_steps=10)

trainer = DPOTrainer(
    model=model,
    train_dataset=dataset,
    args=training_args,
    beta=0.1,
    tokenizer=tokenizer
)

trainer.train()
