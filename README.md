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
* **Accessibility:** Designed with WCAG 2.1 AA accessibility standards in mind, featuring full keyboard navigation, screen reader support, ARIA labels, and appropriate focus management.
* **Modern UI:** Built with a sleek, responsive dark-navy theme using Tailwind CSS and custom vanilla CSS for animations and enhanced UX.
* **Rich Text Formatting:** AI responses are parsed from Markdown into readable HTML using Marked.js.
* **Robust Testing:** Includes a comprehensive pytest test suite for the Flask backend, covering API endpoints, error handling, rate limiting, and CORS compliance.

## Tech Stack

* **Backend:** Python 3.11+, Flask
* **AI Integration:** Google GenAI SDK (`google-genai`), using the `models/gemini-2.5-flash` model.
* **Frontend:** HTML5, Vanilla JavaScript, Tailwind CSS (CDN), Marked.js
* **Testing:** Pytest, pytest-mock
* **Deployment:** Docker, Gunicorn (Cloud Run ready)

## Prerequisites

* Python 3.11+
* A valid Gemini API Key (obtainable from Google AI Studio).
* Docker (Optional, for containerized deployment)

## Installation & Setup

1. **Clone and navigate to the project directory:**
   ```bash
   git clone https://github.com/Captain-Piyush/ElectIQ.git
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

### Running Tests
To run the test suite to ensure the backend is functioning properly:
```bash
pytest app/
```

### Production / Docker
You can also run the application using the included Dockerfile:
```bash
docker build -t electiq .
docker run -p 8080:8080 --env-file .env electiq
```

## Project Structure

```text
ElectIQ/
├── app/                        # Main application package
│   ├── main.py                 # Flask application backend and Gemini API integration
│   ├── test_app.py             # Pytest test suite for the Flask backend
│   ├── conftest.py             # Pytest configuration and test fixtures
│   ├── pytest.ini              # Pytest settings and options
│   ├── static/                 # Static assets directory
│   └── templates/              # HTML templates directory
│       └── index.html          # Single-page frontend application layout, styling, and logic
├── .venv/                      # Python virtual environment (ignored by git)
├── .env                        # Environment variables (ignored by git)
├── .gitignore                  # Git ignore rules
├── Dockerfile                  # Container configuration for production deployment
├── requirements.txt            # Python package dependencies
├── LICENSE                     # Project license
└── README.md                   # Project documentation (this file)
```

## Contributing
Feel free to open issues or submit pull requests for any enhancements or bug fixes.
