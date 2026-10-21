import sys
import os
import getpass
from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import path
from google import genai
from google.genai import types

# 1. ⚙️ IMMERSIVE CONFIGURATION (Single-File Settings)
if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY='vibe-coder-secret-key-change-in-production',
        ROOT_URLCONF=__name__,
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
        }],
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
        ]
    )

# 2. 🔑 SECURE GEMINI INITIALIZATION
def get_gemini_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        # Prompt securely in terminal if environment variable is missing
        api_key = getpass.getpass("🔑 Paste your Gemini API Key: ").strip()
        os.environ["GEMINI_API_KEY"] = api_key
    return genai.Client(api_key=api_key)

# 3. 🧠 GEMINI DUAL-PASS ENGINE
def process_ai_message(raw_message):
    client = get_gemini_client()
    
    # Pass 1: Enhancement
    enhancer_prompt = f"Optimize and enrich this user intent for a chatbot: '{raw_message}'"
    enhanced_payload = client.models.generate_content(
        model='gemini-2.5-flash', contents=enhancer_prompt
    ).text
    
    # Pass 2: Final Response
    response = client.models.generate_content(
        model='gemini-2.5-pro',
        contents=enhanced_payload,
        config=types.GenerateContentConfig(
            system_instruction="You are an elite web application chatbot.",
            temperature=0.7
        )
    )
    return response.text

# 4. 🚀 VIEWS & ENDPOINTS
def home(request):
    # Renders the HTML interface directly from an inline template string
    from django.template import Template, Context
    html_template = """
    <!DOCTYPE html>
    <html>
    <head><title>Gemini Django Co-Pilot</title></head>
    <body style="font-family: sans-serif; margin: 40px; background: #f4f6f9;">
        <h2>🤖 Gemini Django Hybrid Bot</h2>
        <input type="text" id="msg" placeholder="Type a message..." style="width:300px; padding:8px;">
        <button onclick="send()">Send</button>
        <p><strong>Response:</strong> <span id="reply">...</span></p>

        <script>
            async function send() {
                let msg = document.getElementById('msg').value;
                let res = await fetch('/chat/?message=' + encodeURIComponent(msg));
                let data = await res.json();
                document.getElementById('reply').innerText = data.reply;
            }
        </script>
    </body>
    </html>
    """
    return render(request, Template(html_template).compile(), Context({}))

def chat_endpoint(request):
    # Handles dynamic asynchronous background requests from the front-end
    user_message = request.GET.get('message', '')
    if not user_message:
        return JsonResponse({'reply': 'Empty message received.'})
    
    try:
        bot_reply = process_ai_message(user_message)
        return JsonResponse({'reply': bot_reply})
    except Exception as e:
        return JsonResponse({'reply': f"Error: {str(e)}"})

# 5. 🗺️ URL ROUTING MAP
urlpatterns = [
    path('', home),
    path('chat/', chat_endpoint),
]

# 6. 🏁 RUNTIME EXECUTION ENTRY
if __name__ == '__main__':
    # Start the local development web server automatically
    execute_from_command_line([sys.argv[0], 'runserver', '8000'])
