#creat a simple chatbot using python that can respond to basic greeting and answer 5 basic questions also use exception handling

def chatbot():
    print("Chatbot: Hello! I am a simple chatbot.")
    print("Chatbot: You can ask me basic questions.")
    print("Chatbot: Type 'bye' to exit.\n")

    while True:
        try:
            user = input("You: ").lower().strip()

            # Exit
            if user == "bye":
                print("Chatbot: Goodbye! Have a nice day.")
                break

            # Greetings
            elif user in ["hello", "hi", "hey"]:
                print("Chatbot: Hello! How can I help you?")

            # Question 1
            elif "your name" in user:
                print("Chatbot: My name is SimpleBot.")

            # Question 2
            elif "how are you" in user:
                print("Chatbot: I am fine, thank you!")

            # Question 3
            elif "what can you do" in user:
                print("Chatbot: I can answer 5 basic questions.")

            # Question 4
            elif "where are you" in user:
                print("Chatbot: I live inside this Python program.")

            # Question 5
            elif "who created you" in user:
                print("Chatbot: I was created using Python.")

            # Unknown question
            else:
                print("Chatbot: Sorry, I don't understand that question.")

        except Exception as e:
            print("Chatbot: Something went wrong. Please try again.")


chatbot()