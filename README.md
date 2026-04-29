# ElectIQ

ElectIQ is a modern, interactive, non-partisan election process assistant powered by Google's Gemini AI. It is designed to help citizens understand the democratic process, including voter registration, primaries, general elections, how votes are counted, and the electoral college.

## Features

* **Interactive AI Chat:** Ask questions about the election process and get clear, objective, and easy-to-understand explanations powered by the Gemini 2.5 Flash model.
* **Election Journey Guide:** A built-in stepper that guides users through the key stages of an election:
  1. Voter Registration
  2. Primaries & Caucuses
  3. General Election
  4. Results & Certification
  5. Inauguration
* **Quick Actions:** One-click buttons for frequently asked questions (e.g., "What is the Electoral College?", "When is Election Day?").
* **Modern UI:** Built with a sleek, responsive dark-navy theme using Tailwind CSS.
* **Rich Text Formatting:** AI responses are parsed from Markdown into readable HTML using Marked.js.

## Tech Stack

* **Backend:** Python, Flask
* **AI Integration:** Google GenAI SDK (`google-genai`), using the `models/gemini-2.5-flash` model.
* **Frontend:** HTML5, Vanilla JavaScript, Tailwind CSS (CDN), Marked.js
* **Deployment:** Docker, Gunicorn (Cloud Run ready)

## Prerequisites

* Python 3.11+
* A valid Gemini API Key (obtainable from Google AI Studio).

## Installation & Setup

1. **Navigate to the project directory:**
   ```bash
   cd ElectIQ
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   
   # On Windows:
   .venv\Scripts\activate
   
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables:**
   Create a `.env` file in the root directory and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   PORT=8080
   ```

## Running the Application

### Local Development
Run the Flask application directly:
```bash
python app/main.py
```
The app will be available at `http://127.0.0.1:8080/`.

### Production / Docker
You can also run the application using the included Dockerfile:
```bash
docker build -t electiq .
docker run -p 8080:8080 --env-file .env electiq
```

## Project Structure

* `app/main.py`: The Flask backend routing and Gemini API integration.
* `app/templates/index.html`: The single-page frontend application layout, styling, and logic.
* `requirements.txt`: Python package dependencies.
* `Dockerfile`: Container configuration for production deployment.
