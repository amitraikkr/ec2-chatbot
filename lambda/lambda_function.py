import json
import openai
import boto3
import os

# Function to generate the chatbot response using OpenAI's GPT-3
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response.choices[0].text.strip()

# Function to generate a chatbot response to the user's input
def chatbot_response(text):
    prompt = f"Using AWS SDK boto3 and ChatGPT, I received the following question: {text}."
    response = generate_response(prompt)
    return response

# Function to manage EC2 instances based on user input
def manage_ec2_instances(text):
    # Convert the input to lowercase and split into words
    words = text.lower().split()
    
    if 'list' in words and ('ec2' in words or 'instances' in words):
        # List EC2 instances
        instances = list_ec2_instances()
        return instances

    elif 'start' in words and ('instance' in words or 'ec2' in words):
        # Start an EC2 instance
        instance_id = extract_instance_id(text)
        if instance_id:
            return start_instance(instance_id)

    elif 'stop' in words and ('instance' in words or 'ec2' in words):
        # Stop an EC2 instance
        instance_id = extract_instance_id(text)
        if instance_id:
            return stop_instance(instance_id)

    else:
        # Generate a response using OpenAI's GPT-3
        return chatbot_response(text)
    
# Function to list EC2 instances
def list_ec2_instances():
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running', 'stopped']}])
    result = "Instance ID | State | Type"
    for instance in instances:
        result += f"\n\n{instance.id} | {instance.state['Name']} | {instance.instance_type}\n\n"
    return result

# Function to start an EC2 instance
def start_instance(instance_id):
    instance = ec2.Instance(instance_id)
    if instance.state['Name'] == 'stopped':
        instance.start()
        return f"Starting instance {instance_id}."
    else:
        return f"Instance {instance_id} is already running."

# Function to stop an EC2 instance
def stop_instance(instance_id):
    instance = ec2.Instance(instance_id)
    if instance.state['Name'] == 'running':
        instance.stop()
        return f"Stopping instance {instance_id}."
    else:
        return f"Instance {instance_id} is already stopped."

# Function to extract the instance ID from the user's input
def extract_instance_id(response):
    words = response.split(' ')
    for word in words:
        if word.startswith('i-'):
            return word
    return None

# Create an EC2 resource using the boto3 library
ec2 = boto3.resource('ec2')

# Load the OpenAI API key from a JSON file
config=json.load(open("parameters.json"))
openai.api_key = config['API_KEY']

# Test the manage_ec2_instances function
user_input = 'list Instances'
response = manage_ec2_instances(user_input)
print(response)

# AWS Lambda function handler
def lambda_handler(event, context):
    user_input = event.get('user_input', '')
    if user_input:
        # Generate a chatbot response based on the user's input
        response = manage_ec2_instances(user_input)
