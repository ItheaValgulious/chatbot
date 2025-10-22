from basic import *

class PeopleGenerator:
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