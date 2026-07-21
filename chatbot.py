print("🤖 Welcome to CodeAlpha Chatbot!")
print("I'm your friendly chatbot.")
print("Type 'bye' anytime to exit.\n")

name = input("What is your name? ")
print(f"\nHello, {name}! Nice to meet you.\n")

while True:
    message = input("You: ").lower()

    if message == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif message == "hello":
        print("Bot: Hi! How can I help you?")

    elif message == "how are you":
        print("Bot: I'm doing great! How about you?")

    elif message == "what is your name":
        print("Bot: My name is CodeAlpha Bot.")

    elif message == "who created you":
        print("Bot: I was created by Gaddamidi Rishika Goud.")

    elif message == "what are you doing":
        print("Bot: I'm chatting with you! ")

    elif message == "what can you do":
        print("Bot: I can answer simple questions and have a basic conversation with you.")

    elif message == "who are you":
        print("Bot: I am a simple Python chatbot.")

    elif message == "where do you live":
        print("Bot: I live inside your computer.")

    elif message == "good morning":
        print("Bot: Good morning! Have a wonderful day!")

    elif message == "good afternoon":
        print("Bot: Good afternoon! Hope you're having a great day!")

    elif message == "good evening":
        print("Bot: Good evening! How was your day?")

    elif message == "good night":
        print("Bot: Good night! Sweet dreams.")

    elif message == "thank you":
        print("Bot: You're welcome! ")

    elif message == "help":
        print("Bot: You can ask me things like 'hi', 'how are you', 'what is your name', or type 'bye' to exit.")

    elif message == "tell me a joke":
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs! ")

    elif message == "i am sad":
        print("Bot: I'm sorry to hear that. Remember, every day is a new beginning. Keep smiling! ")

    elif message == "bye":
        print(f"Bot: Goodbye, {name}! Have a wonderful day. ")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")
    
