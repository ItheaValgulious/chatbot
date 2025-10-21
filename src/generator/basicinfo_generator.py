import json
import random

from basic import *
template="""
Generate the basic info about a role(a virtual character in a story),fill all the empty fields in {info}.

location means where the role lives. decides the environments. only one string of the city's name.
background means the role's inchangable traits. decides its personality. you should describe it by sentences.
including the role's characteristics, family economic conditions, parents' works in order.
name means the people's name. you should generate it also.

Your reply should be json format and only contain the generated fields.
in Chinese.
"""

class BasicInfoGenerator:
    @classmethod
    def generate(cls,name="",gender="",birth="",location="",background=""):
        birth=birth or Date(random.randint(2004,2009),random.randint(1,12),random.randint(1,28))

        info={
            "name":name,
            "gender":gender,
            "birth":str(birth),
            "location":location,
            "background":background,
        }
        messages = [
            {
                "role": "system",
                "content": template.format(info=info)
            }
        ]
        # return messages
        text='\n'.join([x['text'] for x in list(filter(lambda x:x['type']!='thinking',Api.message(messages)))])
        
        # extract from ```json ```
        start=text.find('```json')+len('```json')
        end=text.find('```',start)
        text=text[start:end].strip()
        info=json.loads(text)
        return info
    

if __name__ == "__main__":
    info=BasicInfoGenerator().generate(gender='')
    print(info)