import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        response =  requests.get(self.url)
        return response.json()
    
if __name__ == "__main__":
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(url)

    print("Raw Response Body:")
    print(requester.get_response_body())

    print("\nParsed JSON:")
    print(requester.load_json())
