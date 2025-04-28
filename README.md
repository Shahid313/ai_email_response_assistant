**Project Description: AI Email Response Assistant**

**Elegant • Intelligent • Professional**

This project is an AI-powered email assistant that generates context-aware, tone-perfect email responses tailored to the user's needs. Built with Python and leveraging the OpenRouter API (with Google's Gemini 2.0 Flash model), it crafts polished, professional, or casual email drafts in seconds.

**Key Features:**
✨ **Tone Customization:** 
      Generates responses in user-specified tones (e.g., professional, friendly, concise).
✨ **Prompt Engineering:**
      Structured prompts ensure relevance and clarity.
✨ **Error-Resilient:** 
      Robust error handling for API failures or malformed responses.
✨ **Configurable:** 
      Easy model/API changes via .env and config.py.

 A[User Input: Email + Desired Tone] --> B[Build Prompt]
    B --> C[API Request to OpenRouter]
    C --> D{Success?}
    D -->|Yes| E[Parse Response]
    D -->|No| F[Handle Error]
    E --> G[Extract AI-Generated Email]
    F --> H[Return Error Message]
    G --> I[Output: Polished Email]
    H --> I
