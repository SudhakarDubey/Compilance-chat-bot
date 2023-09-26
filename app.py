import openai
import gradio as gr

# Set your OpenAI API key
openai.api_key = "API KEY"


messages = [{"role": "system", "content": """Hello and welcome to ComplianceBot! I'm here to assist you with any regulatory compliance questions you may have. Feel free to ask, and I'll provide you with the information you need."""}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

# Define your Gradio interface here
gr.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="ComplianceBot").launch()
