import time

# Predefined responses grouped by categories
RESPONSES = {
    "greetings": ["hello", "hi", "hey", "good morning", "good evening"],
    "status": ["how are you", "how's it going", "how are you doing"],
    "identity": ["who are you", "what is your name", "your name"],
    "help": ["help", "what can you do", "commands"]
}

def get_bot_response(user_input):
    """Determines the appropriate bot response based on user input keywords."""
    # Convert input to lowercase and remove trailing spaces
    clean_input = user_input.lower().strip()
    
    if any(word in clean_input for word in RESPONSES["greetings"]):
        return "Hello there! I'm glad you stopped by to chat. How can I assist you today?"
        
    elif any(word in clean_input for word in RESPONSES["status"]):
        return "I'm functioning at peak efficiency, thank you for asking! How are you doing?"
        
    elif any(word in clean_input for word in RESPONSES["identity"]):
        return "I am the CodeAlpha Assistant, a smart rule-based chatbot built entirely in Python!"
        
    elif any(word in clean_input for word in RESPONSES["help"]):
        return ("I can chat with you, tell you my identity, or answer basic questions. "
                "Try asking 'who are you?' or 'how are you?'.")
                
    elif "bye" in clean_input or "exit" in clean_input:
        return "Goodbye! It was a pleasure chatting with you. Have a fantastic day! 👋"
        
    else:
        return "Hmm, I didn't quite catch that. Could you try rephrasing, or type 'help' to see what I can do?"

def run_chatbot():
    print("\n" + "="*40)
    print("      🤖 CODEALPHA INTELLIGENT CHATBOT 🤖      ")
    print("="*40)
    print("Status: Online | Type 'bye' or 'exit' to quit.\n")
    
    time.sleep(0.5)
    print("Chatbot: Hello! I am your automated assistant. How can I help you today?")
    print("-" * 40)

    while True:
        user_input = input("You: ").strip()
        
        # Check for empty input
        if not user_input:
            print("Chatbot: (Silence... Please type something so I can respond!)\n" + "-" * 40)
            continue
            
        # Dramatic pause to simulate "thinking" like a real bot
        print("Chatbot: Thinking...", end="\r")
        time.sleep(0.6) 
        
        # Get and display the response
        response = get_bot_response(user_input)
        print(f"Chatbot: {response}")
        print("-" * 40)
        
        # Break the loop if the user wants to exit
        if any(exit_word in user_input.lower() for exit_word in ["bye", "exit"]):
            break

# Main execution loop mimicking your Hangman structure
while True:
    run_chatbot()
    print("\n" + "="*40)
    play_again = input("Would you like to start a new chat session? (y/n): ").strip().lower()
    if play_again != "y":
        print("\nThank you for using CodeAlpha Chatbot. System Shutdown. 🛑")
        break
