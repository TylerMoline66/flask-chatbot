from flask import Flask, request, jsonify
from transformers import ConversationalPipeline, GPT2TokenizerFast, GPT2LMHeadModel, Conversation, AutoModelForCausalLM, AutoTokenizer
import torch
# import psycopg2
import Routes

model_name = "microsoft/DialoGPT-medium"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

chatbot = ConversationalPipeline(model=model, tokenizer=tokenizer, return_conversations=True)

conversation_history = []

def chat():
    global conversation_history

    user_message = request.json['message']
    conversation_history.append({'role': 'user', 'content': user_message})

    input_ids = tokenizer.encode(user_message, return_tensors='pt')
    response = model.generate(input_ids, max_length=100, pad_token_id=tokenizer.eos_token_id)
    response_text = tokenizer.decode(response[0], skip_special_tokens=True)

    conversation_history.append({'role': 'assistant', 'content': response_text})

    return jsonify({'message': response_text})