import requests
import json

if __name__ == "__main__":
    number_of_question = 3
    question_number = 0

    while question_number < number_of_question:
        question = str(input("Question : "))
        data = {
            "model" : "llama3:latest",
            "messages" : [{"role":"user","content": question}],
            "stream" : False
        }
        url ="http://localhost:11434/api/chat"
        response = requests.post(url,json=data)
        response.raise_for_status()
        response_json = json.loads(response.text)
        ai_reply = response_json["message"]["content"]
        print(ai_reply)
        question_number+=1
