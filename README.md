# SnapStudy

SnapStudy is an AI-powered application designed to help
users study more effectively.

## Features

- AI-powered responses using a custom system prompt
- Interactive Streamlit interface
- Structured AI-generated summaries
- Messaging or email integration, if configured

## Tech Stack

- Python
- Streamlit
- Large Language Model API

## Project Structure

    snapstudy/
    ├── app.py
    ├── prompts.py
    ├── requirements.txt
    └── .streamlit/
        └── secrets.toml.example

## Run Locally

### 1. Clone the repository

    git clone <YOUR_GITHUB_REPOSITORY_URL>
    cd snapstudy

### 2. Create a virtual environment

    python -m venv venv

### 3. Activate the environment

Windows PowerShell:

    .\venv\Scripts\Activate.ps1

### 4. Install dependencies

    pip install -r requirements.txt

### 5. Configure secrets

Create `.streamlit/secrets.toml` and add the
API keys required by the application.

Refer to `.streamlit/secrets.toml.example`
for the expected configuration format.

Never commit your actual secrets.

### 6. Run the application

    streamlit run app.py