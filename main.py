import os
import discord
import os
import json
import random
from replit import db

my_secret = os.environ['TOKEN']

client = discord.Client()

def add_citation_type(citation_type):
  if "citation" in db.keys():
    return

def add_citation(citation_message):
  if "citations" in db.keys():
    citations = db["citations"]
    citations.append(citation_message)
    db["citations"] = citations
  else:
    db["citations"] = [citation_message]

def delete_citation(index):
  citations = db["citations"]
  if len(citations) > index:
    del citations[index]
    db["citations"] = citations

@client.event
async def on_ready():
  print('up and running as user {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  #options = start_citations
  #if "citations" in db.Keys():
    #options = options + db["citations"]

  if message.content.startswith('>c'):
    await message.channel.send('Ready to make citations')

  if msg.startswith(">c"):
    citation_message = msg.split(">c ", 1)[1]
    add_citation(citation_message)
    
    await message.channel.send('Citation Added.)


  if msg.startswith(">list"):
    for key in db.keys():
      print(key)
      print(db[key])

  if msg.startswith(">appeal"):
    citations = []
    if "citations" in db.keys():
      index = int(msg.split(">appeal",1)[1])
      delete_citation(index)
      citations = db["citations"]
    await message.channel.send(citations)

client.run(my_secret)