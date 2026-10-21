# 🚀 Gemini Django Single-File Core

[![System Status](https://shields.io)](#)
[![Python Engine](https://shields.io)](#)
[![Framework](https://shields.io)](#)

A production-ready hybrid web application that merges a complete **Django server environment** and a **Gemini Dual-Pass AI orchestration workflow** straight into a single, self-contained execution script (`main.py`). This project is designed for rapid prototype scaling and secure GitHub deployments without the typical framework file bloat.

---

## 📸 Architecture & System Preview

### Core Infrastructure Blueprint
![Server Core Infrastructure](https://pexels.com)

### AI Synthesis Workspace
![Developer Workspace Context](https://pexels.com)

---

## 🧠 Architectural Deep-Dive

Click the expandable panels below to explore the functional mechanics running inside `main.py`:

<details>
<summary><b>⚡ Pass 1: Intent Flash Preprocessor</b></summary>
<br>
When a raw message hits the backend controller, it is routed straight into <code>gemini-2.5-flash</code>. This pass programmatically expands minimal or vague human inputs, extracting explicit structural demands, developer restrictions, and hidden intent profiles before formatting a highly comprehensive metaprompt payload.
</details>

<details>
<summary><b>🧠 Pass 2: High-Reasoning Execution Engine</b></summary>
<br>
The augmented payload from Pass 1 is securely dispatched directly into <code>gemini-2.5-pro</code>. Operating under strict system rules (defined inside the <code>GenerateContentConfig</code>), this engine processes the complex programmatic directives to generate top-tier, accurate, and deeply structured technical answers.
</details>

<details>
<summary><b>🛠️ Single-File Hybrid Routing Model</b></summary>
<br>
Instead of splitting configurations across multiple directories, all database setup, base configurations, URL patterns, UI templates, and API methods execute entirely out of <code>main.py</code> using an in-memory configuration engine initialized via <code>settings.configure()</code>.
</details>

---

## 🛠️ Getting Started & Installation

### 1. Install System Dependencies
Install the required packages in your local environment container:
```bash
pip install django google-genai
```

### 2. Run the Web Server
Launch the server directly using your main script:
```bash
python main.py
```

> 🔑 **Security Alert:** If the engine does not detect a `GEMINI_API_KEY` preset inside your local environment variable map, the console will safely mask your input and prompt you to paste your key securely right in the terminal window before allowing initialization.

### 3. Open the Dashboard Interface
Once the local development web server initiates successfully, point your browser viewport to:
```text
http://127.0.0
```

---

## 🔮 Scalability Map

* **Ecosystem Conversion:** When you are ready to expand past a single-file template framework, execute `python manage.py startapp chatbot` to automatically partition your code logic into classic modular files (`models.py`, `views.py`, `urls.py`).
* **Asynchronous Streams:** The frontend is built on highly accessible asynchronous JavaScript `fetch()` calls, ready to be stepped up with Django Channels or server-sent events for live, character-by-character token response streaming.

---

<p align="center">
  <sub>© 2026 Gemini Django Platform Core Architecture.</sub><br>
  <b>Authorized by <a href="https://github.com/rayaantasnim">RAYAAN TASNIM</a></b>
</p>
