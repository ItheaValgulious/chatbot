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

People
- gender
- name
- know_time
- description:str
- current_state:int


## Memory Generating

### PeriodGenerator

- generate the memory about some certain period
parameter: 
- context
- role

### PeopleGenerator

1. generate basic people info

2. generate the related memorys(period generator):
   - beginning
   - process

### InitialMemoryGenerator:

generate the memory that the before the bot meet you.

BasicInfoGenerator
- gender
- name
- birth
- location
- background

generate people you know

generate the memorys

### Daylife_memory_generator

generate an experience about day life.

parameter:
- period
- time(in a day)
- role



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