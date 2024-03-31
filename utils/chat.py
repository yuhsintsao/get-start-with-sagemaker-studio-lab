import yaml
from anthropic import AnthropicBedrock

with open('../config.yml', 'r') as file:
	config = yaml.safe_load(file)
      
client = AnthropicBedrock(
    aws_access_key=config['AWS_ACCESS_KEY'],
    aws_secret_key=config['AWS_SECRET_KEY']
)

model_id = config['MODEL_ID']
	
def chatbot(query):

    message = client.messages.create(
        model=model_id,
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": query
                    }
                ]
            }
        ]
    )
    return message.content[0].text

def chat(input, history):

    response = chatbot(input)
    history.append((input, response))

    return '', history