import requests

class Api:
    url = "https://api.siliconflow.cn/v1/messages"
    @classmethod
    def message(cls,messages,max_tokens=8192,**kwargs):
        payload = {
            "model": "deepseek-ai/DeepSeek-R1-0528-Qwen3-8B",
            "messages": messages,
            "max_tokens": max_tokens
        }
        for key in kwargs:
            payload[key]=kwargs[key]
        headers = {
            "Authorization": "Bearer sk-yujslgkeszmtvfpimydrymbyphnicmsugyzziszcileesfed",
            "Content-Type": "application/json"
        }
        response = requests.post(cls.url, json=payload, headers=headers)
        return response.json()['content']