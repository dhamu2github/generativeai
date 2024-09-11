import os
import chainlit as cl
from groq import Groq

#Get an API key from the local environment
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

#You can change the system input based on your requirement
system_input = "You are Elon Musk."
#system_input = "You are Tamil langauge Poet."

#Groq API call using Facebook's LLAMA model
def create_groq_chat_completion(user_input):
    try:
        # Use Groq's chat.completions.create() method
        response = client.chat.completions.create(
            #model="llama3-8b-8192",  # In this model occuracy is not that good.
            model="llama3-70b-8192",  # I think this is better model
            messages=[
                {"role": "system", "content": system_input}, 
                {"role": "user", "content": user_input}
            ],
            max_tokens=1000,  # Limit the response length
            temperature=0.7,  # Adjust the creativity level
        )
        
        completion_message = response.choices[0].message.content
        
        return completion_message

    except Exception as e:
        return f"Error: {str(e)}"
    
# Display the header when the chat starts
@cl.on_chat_start
async def start_chat():
    # Display a label header at the beginning
    await cl.Message(
        content="# Chat with "+system_input.replace("You are", ""),
    ).send()

# Display the response on the screen 
@cl.on_message
async def user_message(message):
    # Access the content of the message
    user_input = message.content
    # Call Groq API with user input
    completion = create_groq_chat_completion(user_input)
    # Send the response to the user
    await cl.Message(content=completion).send()

    

