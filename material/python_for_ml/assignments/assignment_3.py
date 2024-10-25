import random, os

class ChatBot():
    # Chatbot function
    def __init__(self):
        print("Chatbot: Hi! How can I assist you today?")
        
        while True:
            user_input = input("User: ").lower()
            response = self.get_response(user_input)
            print("Chatbot:", response)
            if user_input == "goodbye":
                break
    
    # Function to get a response based on user input
    def get_response(self, user_input):
        # Predefined responses file
        input_file = open(r'C:\Users\Lenovo\Desktop\amit\advanced_machine_learning_course_amit\material\python_for_ml\assignments\chatbot responses.txt','r')
        text = input_file.read()
        input_file.close()
        sen = text.split('\n')
        responses = dict()

        for i in sen:
            words = i.split(':')
            key_word = words[0]
            value_list =words[1].split(',')
            responses[key_word]=value_list
        for key in responses:
            if key in user_input:
                return random.choice(responses[key])
        return random.choice(responses["default"])

    
    

# Run the chatbot
if '__main__'==__name__: 
    ChatBot()
