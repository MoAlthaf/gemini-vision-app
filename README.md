# Gemini Vision AI 📸

A full-stack AI application that uses **FastAPI** on the backend and **Gemini 1.5 Flash** to analyze and describe images uploaded by users.

## 🚀 Features
- **Multimodal AI:** Direct pixel analysis using Google's Gemini API.
- **FastAPI Backend:** High-performance asynchronous API routing.
- **Modern UI:** Responsive design using Tailwind CSS with real-time image preview.
- **Industry Standards:** Service-based architecture, environment variable security, and CORS configuration.

## 🛠️ Tech Stack
- **Frontend:** HTML5, JavaScript (Fetch API), Tailwind CSS.
- **Backend:** Python, FastAPI, Uvicorn.
- **AI Model:** Google Gemini 2.5 Flash lite.

## 📋 Prerequisites
- Python 3.9+
- A Google Gemini API Key (Get it from [Google AI Studio](https://aistudio.google.com/))

## ⚙️ Setup & Installation
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd gemini-vision-app
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   # For Mac/Linux
   source venv/bin/activate
   # For Windows
   # venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration:** Create a .env file in the root directory and add your API key:
   ```plaintext
   GEMINI_API_KEY=your_actual_api_key_here
   ```

## 🏃 Running the App
Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```
Open your browser and navigate to http://127.0.0.1:8000.

## 📂 Project Structure
- `app/main.py`: Application entry point and CORS setup.
- `app/api/`: API route definitions.
- `app/services/`: Business logic and AI integration.
- `app/static/`: Frontend assets (HTML/CSS/JS).

---

## 2. The Final Commit
This is the "bow on top" of your project. This commit signals that the project is documented and ready for others to see.

```bash
git add README.md
git commit -m "docs: add professional README with setup instructions"