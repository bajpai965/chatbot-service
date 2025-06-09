import re

class CustomerServiceChatbot:
    def __init__(self):
        self.responses = [
            (r"(hi|hello|hey)", "Hello! How can I assist you today?"),
            (r"(.*)(hours|open|close)", "Our business hours are 9 AM to 5 PM, Monday through Friday."),
            (r"(.*)(price|cost|charges)", "Our services start at $19.99. Do you want a detailed quote?"),
            (r"(.*)(support|help|issue|problem)", "I'm here to help. Can you describe the issue?"),
            (r"(bye|exit|quit)", "Thank you for visiting! Have a great day."),
        ]

    def get_response(self, user_input):
        user_input = user_input.lower()
        for pattern, response in self.responses:
            if re.search(pattern, user_input):
                return response
        return "I'm sorry, I didn't understand that. Could you please rephrase?"

def main():
    bot = CustomerServiceChatbot()
    print("Customer Service Chatbot (type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        response = bot.get_response(user_input)
        print("Bot:", response)
        if "thank you" in user_input.lower() or "bye" in user_input.lower():
            break

if __name__ == "__main__":
    main()
