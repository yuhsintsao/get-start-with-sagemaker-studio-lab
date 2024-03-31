import yaml
import gradio as gr
from utils import chat

with open('config.yml', 'r') as file:
	config = yaml.safe_load(file)
    
with gr.Blocks() as demo:

    with gr.Row():
        chatbot = gr.Chatbot(label=config['MODEL_ID'], show_copy_button=True, likeable=True, layout='bubble')
    with gr.Row():
        msg = gr.Textbox()
    
    btn = gr.Button("Send")
    btn.click(chat.chat, inputs=[msg, chatbot], outputs=[msg, chatbot])
    clear = gr.ClearButton([msg, chatbot])
    
if __name__ == "__main__":
    port = config['SAGEMAKER_STUDIO_PORT']
    root_path = f"/studiolab/default/jupyter/proxy/{port}"
    print(f"[URL] https://{config['SAGEMAKER_STUDIO_IDENTIFIER']}.studio.{config['SAGEMAKER_STUDIO_REGION']}.sagemaker.aws/studiolab/default/jupyter/proxy/{port}/")

    demo.launch(server_port=port, root_path=root_path, inline=False)
    