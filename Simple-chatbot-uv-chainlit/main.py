import chainlit as cl

@cl.on_message                 #buildin decorator
async def main(message:cl.Message):
    
    response = f"You said : {message.content} " 
    
    await cl.Message(content=response).send()

