# AI Email Response Assistant ✉️✨

![Workflow Diagram](https://img.shields.io/badge/flow-mermaid-blue) 
![Python](https://img.shields.io/badge/python-3.8+-blue)
![API](https://img.shields.io/badge/API-OpenRouter-green)

## 🌟 Elegant • Intelligent • Professional

An AI-powered email assistant that generates context-aware, tone-perfect email responses tailored to your needs. Built with Python and leveraging the OpenRouter API (with Google's Gemini 2.0 Flash model), it crafts polished professional or casual email drafts in seconds.

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🎭 **Tone Customization** | Generate responses in specified tones (professional, friendly, concise) |
| 🧠 **Smart Prompt Engineering** | Structured prompts ensure relevant and clear responses |
| 🛡️ **Error-Resilient** | Robust handling for API failures and malformed responses |
| ⚙️ **Configurable** | Easy model/API changes via `.env` and `config.py` |

## 🔄 Workflow

```mermaid
flowchart TD
    A[User Input: Email + Desired Tone] --> B[Build Prompt]
    B --> C[API Request to OpenRouter]
    C --> D{Success?}
    D -->|Yes| E[Parse Response]
    D -->|No| F[Handle Error]
    E --> G[Extract AI-Generated Email]
    F --> H[Return Error Message]
