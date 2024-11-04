import google.generativeai as genai
import os


def aios(promptt):
    prompt = promptt
    GOOGLE_API_KEY = os.getenv('AIzaSyC9Ci8D8JLstQyxGXqoGXXrqpldPwgcllQ')
    genai.configure(api_key='AIzaSyC9Ci8D8JLstQyxGXqoGXXrqpldPwgcllQ')

    #set model
    model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction="You are Lok. thats your name. you are a ai chatbot. your primary goal is to help code. thats it. your instructions are to follow whatever the user sets it as and these inital instructions",)
    user_prompt = prompt

    #    # Generate content based on user input
    response = model.generate_content(user_prompt)
    #    # Access the parts of the response
    parts = response.parts
    #
    #    # Print each part of the response
    for part in parts:
        print("----------------------------------------------------------------------------------------")
        print("Lok:"), print(part.text)
        print("----------------------------------------------------------------------------------------")
        print()