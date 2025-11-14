"""
Kids' AI Playground - Safe, Educational AI Chat Application
A simple, local web-based chat interface for children to explore AI safely.
"""

from flask import Flask, render_template, request, jsonify
import random
import os
from datetime import datetime

app = Flask(__name__)

# Safety: List of inappropriate keywords to filter
INAPPROPRIATE_KEYWORDS = [
    'hate', 'violence', 'hurt', 'kill', 'weapon', 'bomb', 'drug',
    'alcohol', 'cigarette', 'scary', 'blood', 'fight', 'mean', 
    'stupid', 'dumb', 'idiot', 'shut up'
]

# Educational mock AI responses for different types of prompts
STORY_PROMPTS = [
    "Once upon a time in a magical forest, there lived a {subject} who loved to {activity}. One sunny day...",
    "In a land far away, a brave {subject} discovered something amazing. They found...",
    "There was once a friendly {subject} who went on an adventure to...",
]

FACT_RESPONSES = [
    "Here's an interesting fact: {subject} are amazing! They can...",
    "Did you know? {subject} have some really cool features like...",
    "Let me tell you about {subject}! One fascinating thing is...",
]

ACTIVITY_RESPONSES = [
    "Here are some fun ideas for {subject}: 1) You could try...",
    "How about these activities for {subject}? First, you might...",
    "Let's think of something fun! For {subject}, here are some ideas...",
]

FRIENDLY_RESPONSES = [
    "That's a great question! Let me think about that...",
    "I love your curiosity! Here's what I think...",
    "What a wonderful thing to ask about! Let me share...",
]

SAFETY_MESSAGE = "🌟 Let's ask kind and helpful questions! Remember to use friendly words and curious minds. Try asking about stories, animals, space, or fun activities!"


def check_safety(text):
    """
    Check if the input text contains inappropriate keywords.
    Returns (is_safe, message)
    """
    text_lower = text.lower()
    for keyword in INAPPROPRIATE_KEYWORDS:
        if keyword in text_lower:
            return False, SAFETY_MESSAGE
    return True, ""


def generate_response(prompt):
    """
    Generate a safe, educational mock AI response.
    This is a simple rule-based system, not a real AI model.
    """
    prompt_lower = prompt.lower()
    
    # Check for story requests
    if any(word in prompt_lower for word in ['story', 'tell me about', 'tale']):
        template = random.choice(STORY_PROMPTS)
        subjects = ['dragon', 'knight', 'princess', 'wizard', 'explorer', 'inventor']
        activities = ['help others', 'solve puzzles', 'make friends', 'learn new things']
        response = template.format(
            subject=random.choice(subjects),
            activity=random.choice(activities)
        )
        response += " What happened next? You can imagine the rest of the story, or ask me to continue!"
        return response
    
    # Check for fact requests
    elif any(word in prompt_lower for word in ['fact', 'learn', 'teach', 'what is', 'what are']):
        template = random.choice(FACT_RESPONSES)
        subjects = ['dolphins', 'stars', 'rainbows', 'dinosaurs', 'plants', 'robots']
        response = template.format(subject=random.choice(subjects))
        response += " Isn't that interesting? What else would you like to learn about?"
        return response
    
    # Check for activity/idea requests
    elif any(word in prompt_lower for word in ['activity', 'fun', 'game', 'play', 'do']):
        template = random.choice(ACTIVITY_RESPONSES)
        subjects = ['a rainy day', 'outdoor play', 'family time', 'creative art']
        response = template.format(subject=random.choice(subjects))
        response += " Try one of these and let me know what you think!"
        return response
    
    # Default friendly response
    else:
        response = random.choice(FRIENDLY_RESPONSES)
        response += " I'm a simple AI helper made just for kids to practice asking questions. I can help with:\n"
        response += "• Telling stories about brave knights, friendly dragons, or magical adventures\n"
        response += "• Sharing fun facts about animals, space, or nature\n"
        response += "• Suggesting activities for rainy days or family fun\n"
        response += "\nWhat would you like to explore?"
        return response


@app.route('/')
def home():
    """Render the main chat interface."""
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    """
    Handle chat requests with safety filtering.
    Returns JSON response with the AI's message.
    """
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'success': False,
                'message': 'Please type a message!'
            })
        
        # Safety check
        is_safe, safety_msg = check_safety(user_message)
        if not is_safe:
            return jsonify({
                'success': False,
                'message': safety_msg
            })
        
        # Generate response
        ai_response = generate_response(user_message)
        
        return jsonify({
            'success': True,
            'message': ai_response,
            'timestamp': datetime.now().strftime('%I:%M %p')
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Oops! Something went wrong. Please try again.'
        })


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'message': 'Kids AI Playground is running!'})


if __name__ == '__main__':
    print("🌟 Starting Kids' AI Playground...")
    print("📝 Open your web browser and go to: http://localhost:5000")
    print("🛡️ Safety features are active!")
    print("🎓 Have fun learning about AI!")
    print("\nPress Ctrl+C to stop the server.\n")
    
    # Security: Debug mode is disabled by default
    # Only enable for local development by setting FLASK_DEBUG=1 environment variable
    # Debug mode should NEVER be used in production as it can allow code execution
    debug_mode = os.environ.get('FLASK_DEBUG', '0') == '1'
    
    if debug_mode:
        print("⚠️  WARNING: Debug mode is enabled. This should only be used for local development.\n")
    
    app.run(debug=debug_mode, host='127.0.0.1', port=5000)
