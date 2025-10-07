from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def generate_text(prompt, sentiment):
    """
    Generate text aligned with a given sentiment.
    """
    model_name = "gpt2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    sentiment_prefix = {
        "positive": "Write a cheerful and optimistic paragraph about:",
        "negative": "Write a sad and pessimistic paragraph about:",
        "neutral": "Write an informative and balanced paragraph about:"
    }

    full_prompt = f"{sentiment_prefix[sentiment]} {prompt}\n\n"

    inputs = tokenizer(full_prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_length=150,
        temperature=0.8,
        top_p=0.95,
        do_sample=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
