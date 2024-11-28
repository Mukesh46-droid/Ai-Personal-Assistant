
import openai

# Initialize OpenAI with your API key
openai.api_key = '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' 


def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or another model like gpt-4
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def main():
    print("Welcome to your AI assistant! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = get_response(user_input)
        print("AI Assistant:", response)

if __name__ == "__main__":
    main()


def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or another model like gpt-4
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
  
def main():
    print("Welcome to your AI assistant! Type 'exit' to end the conversation.")exit
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = get_response(user_input)
        print("AI Assistant:", response)

if __name__ == "__main__":
    main()

