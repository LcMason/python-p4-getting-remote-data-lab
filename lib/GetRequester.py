import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        pass
        # URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        response = requests.get(self.url)
        return response.content

#         # load_json method that should use get_response_body to send a request, then return a Python list or dictionary made up of data converted from the response of that request.

    def load_json(self):
        pass
        # program_list = []
        # programs = json.loads(self.get_response_body())
        # for program in programs:
        #     program_list.append(program.get("occuptation", "N/A)"))

        # return program_list
        data = json.loads(self.get_response_body())
        return data


# # In GetRequester.py
if __name__ == "__main__":
        requester = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
        
        data = json.loads(requester.get_response_body())
        print("Raw JSON data:", data)

        processed_list = requester.load_json()
        print("Processed list from load_json():", processed_list)
