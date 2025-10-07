# AI-Text-Generator-Based-on-Sentiment

🧠 AI Text Generator Based on Sentiment
📋 Project Overview

- The AI Text Generator Based on Sentiment is an intelligent NLP system that automatically analyzes the emotional tone (positive, negative, or neutral) of a user’s input prompt and generates a coherent paragraph aligned with that sentiment.
- It combines sentiment analysis and text generation using state-of-the-art transformer models to produce contextually relevant and emotionally consistent writing.

🎯 Objective

To develop an AI model that can:

- Detect the sentiment of an input prompt using machine learning.

- Generate a paragraph or essay that reflects the detected sentiment.

- Provide an interactive interface for users to input prompts and view generated text in real time.

⚙️ Technical Workflow

- Sentiment Detection:
  The user’s prompt is analyzed using a pretrained transformer-based sentiment analysis model to classify it as positive, negative, or neutral.

- Text Generation:
  A generative language model (such as GPT-2) produces a paragraph matching the detected sentiment. The model is guided with sentiment-specific prompts to maintain emotional alignment.

- Frontend Integration:
  The system uses Streamlit to create an intuitive web interface where users can easily enter prompts, visualize sentiment results, and read generated text.

🧩 Key Features

✅ Automatic Sentiment Classification – Detects emotional tone from input text.

📝 Sentiment-Aligned Text Generation – Generates coherent, human-like responses.

🌐 Interactive Frontend – Built with Streamlit for an easy user experience.

⚙️ Modular Architecture – Separate modules for sentiment analysis and text generation.

🚀 Extendable Design – Can be expanded for manual sentiment selection, essay length adjustment, or custom datasets.

🧰 Tech Stack
 - Component Technology Used
- Language : 	Python
- Frameworks :	Streamlit, Transformers, PyTorch
- Models :	Pretrained Hugging Face Models (e.g., distilbert-base-uncased-finetuned-sst-2-english, gpt2)
- Deployment :	Streamlit Cloud
🧠 Use Cases

 - Content creation with emotion-aware tone.

- Chatbots that generate empathetic or mood-based responses.

- Marketing tools to craft emotionally resonant messages.

Educational AI assistants for creative writing or mood-based essay prompts.
