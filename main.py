import openai
import os
import re

# Set up OpenAI API credentials
openai.api_key = "Your-OpenAI-Key"

# Define a function to generateg a response to the user's input
def generate_response(prompt):
    # Generate a response using the OpenAI GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the text of the response from the API output
    text = response.choices[0].text.strip()

    # Remove any newlines or extraneous whitespace from the text
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\s+", " ", text)

    # Return the response text
    return text

# Define a function to start the chatbot
def start_chat():
    # Greet the user and ask for their name
    print("Hi, I'm your personal Recipe assistant. What's your name?")
    user_name = input("You: ")
    print(f"Nice to meet you, {user_name}! How can I help you today?")

    # Keep the chatbot running until the user says "bye"
    while True:
        # Get the user's input
        user_input = input("You: ")

        # If the user says "bye", exit the chatbot
        if user_input.lower() == "bye":
            print("Recipe assistant: Goodbye! Happy shopping!")
            break

        # Generate a response to the user's input
        response = generate_response(user_input)

        # If the user asks for a recipe recommendation
        if "recipe" in user_input.lower():
            # Ask the user what type of recipe they're looking for
            print("Recipe assistant: Sure, what type of recipe are you looking for?")
            product_type = input("You: ")
            print("Recipe assistant: Sure, what is your dietry preference?")
            diet_type = input("You: ")
            cart_list = ["flour","tomatoes","garlic","cheese"]           # Generate a response with a product recommendation based on the user's input
            prompt = f"I'm looking for a {diet_type} {product_type} recipe with {cart_list} to recommend to {user_name}."
            response = generate_response(prompt)
            # Print the chatbot's response
            print("Recipe assistant:", response)

        # Otherwise, print the chatbot's response to the user's input
        else:
            print("Recipe assistant:", response)

# Start the chatbot
start_chat()
