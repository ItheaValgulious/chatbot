# Chatbot

## Data

Memory:
- date
- full_content
- abstract
- vector
- importantance
  - initial
  - reduce
- role

Memorys:
- memories:Memory

people:
- name
- memorys:Memorys

## Memory Generating

### PeriodGenerator

- generate the memory about some certain period
parameter: 
- context
- role

### Initial_memory_generator:

- generate the memory that the before the bot meet you.
- role: self,friends

BasicInfoGenerator
- name
- birth
- location
- background

Generate people you know:
- name
- know_age

Fill the others with period generator

### Daylife_memory_generator

generate an experience about day life.

parameter:
- period
- time(in a day)



## Chat

state:
- chatting
- waiting

chatting -> waiting:10min
waiting->chatting:2min or randomly(begin)

chatting:

for each paragraph inputs:
- loading memorys
- generating response
- saving memorys

paragraph_checker: check if a paragraph is finished(by modle or time)

loading memorys:
- randomly recall
- vector database

generator

memory_saver: save memory to memorys