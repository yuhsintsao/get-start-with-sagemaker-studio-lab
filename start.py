import yaml
import gradio as gr
from utils import chat

with open('config.yml', 'r') as file:
	config = yaml.safe_load(file)
	
with gr.Blocks() as demo:

    with gr.Row():
        chatbot = gr.Chatbot(label=config['MODEL_ID_A'], show_copy_button=True, likeable=True, layout='bubble')
    with gr.Row():
        msg = gr.Textbox()
    
    btn = gr.Button("Send")
    btn.click(chat.chat, inputs=[msg, chatbot], outputs=[msg, chatbot])
    clear = gr.ClearButton([msg, chatbot])
    