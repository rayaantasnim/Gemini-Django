<div align="center">

# ⚡ Gemini-Django

**A self-contained, single-file Django web application driving a dynamic Dual-Pass Gemini AI workspace.**

![System Status](https://img.shields.io/badge/System_Status-Online-brightgreen?style=flat-square)
![Engine](https://img.shields.io/badge/Engine-Dual--Pass_SDK-blue?style=flat-square)
![Framework](https://img.shields.io/badge/Framework-Django_Hybrid-0C4B33?style=flat-square&logo=django)

---

</div>

## 📌 Overview

**Gemini-Django** bridges a complete, production-ready Django backend configuration and a high-reasoning dual-pass AI architecture directly inside a single execution file: `main.py`. By leveraging inline programmatic runtime settings via `settings.configure()`, this architecture eliminates traditional multi-directory boilerplate clutter while serving a responsive, Tailwind CSS-powered dashboard interface. User interactions trigger a sequential two-stage synthesis process, routing raw prompts through swift contextual pre-processing before delivering polished, high-fidelity AI output.

---

## 🖼️ Media Reference Gallery

<div align="center">

| Core Infrastructure Blueprint | AI Synthesis Workspace |
| :---: | :---: |
| [![Core Infrastructure Blueprint](https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=800)](https://pexels.com) | [![AI Synthesis Workspace](https://images.pexels.com/photos/1181675/pexels-photo-1181675.jpeg?auto=compress&cs=tinysrgb&w=800)](https://pexels.com) |
| *Single-file Django setup & SDK routing* | *Dual-Pass Gemini synthesis engine* |

</div>

---

## 🏗️ Architectural Deep-Dive

<details>
<summary><b>🔍 Pass 1: Intent Flash Preprocessor</b></summary>

<br>

The initial pipeline phase utilizes `gemini-2.5-flash` to execute fast, low-latency analysis on incoming user requests. It sanitizes user input, classifies core intent, extracts critical entities, and generates structured contextual directives. This pre-processing pass minimizes latency while ensuring the secondary model receives optimized, well-bounded system instructions.

</details>

<details>
<summary><b>🧠 Pass 2: High-Reasoning Execution Engine</b></summary>

<br>

The secondary pipeline phase routes the enriched output from Pass 1 into `gemini-2.5-pro`. Serving as the primary cognitive layer, `gemini-2.5-pro` performs deep logical inference, multi-step problem solving, and complex code synthesis. It delivers the final, refined technical payload back to the interface with high accuracy and domain depth.

</details>

<details>
<summary><b>⚡ Single-File Hybrid Routing Model</b></summary>

<br>

`main.py` encapsulates the entire Django ecosystem without requiring external management scripts (`manage.py`) or separate application directories. Inside `main.py`:
* **Settings:** Configured programmatically using `django.conf.settings.configure()`.
* **Routing:** URL patterns defined dynamically via `django.urls.path`.
* **Views:** Functional request handlers manage API interaction and UI rendering inline.
* **Execution:** WSGI application server startup and command-line entry loops execute seamlessly in place.

</details>

---

## 🚀 Getting Started & Installation

Follow these steps to deploy the local single-file environment.

### 1. Clone Repository & Prepare Virtual Environment

```bash
git clone https://github.com/rayaantasnim/Gemini-Django.git
cd Gemini-Django

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Core Dependencies

```bash
pip install django google-genai
```

### 3. Launch the Server

Execute the entry point directly using `main.py`:

```bash
python main.py
```

> 🔒 **Security Notice:** During execution startup, `main.py` utilizes secure terminal prompting (`getpass`) to capture your Google GenAI API key safely without persisting credentials or environment exposure in code logs.

### 4. Access Interactive Dashboard

Open your web browser and navigate to:
```text
http://127.0.0.1:8000
```

---

## 📈 Scalability Path

While `main.py` serves as a powerful, zero-boilerplate runtime proof-of-concept, you can scale the application using standard growth vectors:

* **Modular Refactoring (`startapp`):** Transition from inline configuration to standard Django project structure using `python -m django startapp` when scaling data models and database migrations.
* **Asynchronous Token Streaming:** Upgrade view functions to handle asynchronous generation streams using Django Channels or ASGI websockets for real-time token rendering from the `google-genai` SDK.
* **Persistent Storage:** Integrate Django ORM models to log dual-pass prompt history and track system token usage over time.

---

<br>

<div align="center">

Authorized by [RAYAAN TASNIM](https://github.com/rayaantasnim)

</div>
