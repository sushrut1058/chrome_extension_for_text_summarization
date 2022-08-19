#!pip install transformers
#!pip install torch



import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config
import asyncio
import websockets
model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')
device = torch.device('cpu')

async def server(socket):
	async for message in socket:
		preprocessed_text = message.strip().replace('\n','')
		t5_input_text = 'summarize: ' + preprocessed_text

		tokenized_text = tokenizer.encode(t5_input_text, return_tensors='pt', max_length=512).to(device)
		summary_ids = model.generate(tokenized_text, min_length=30, max_length=120)
		summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
		await socket.send(summary)

start_server = websockets.serve(server,"localhost",3000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()