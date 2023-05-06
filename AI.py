import requests
from bs4 import BeautifulSoup

def search_web(query):
    # Function to search the web for the query using Google search API
    search_url = "https://www.google.com/search?q=" + query
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    page = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
    if len(results) > 0:
        answer = results[0].get_text()
    else:
        answer = "Sorry, I couldn't find any relevant information."
    return answer

def chatbot():
    # Function to take input from user and generate response using search_web function
    print("Hello, I'm an AI chatbot. How can I help you today?")
    while True:
        query = input("You: ")
        if query.lower() == 'exit':
            break
        else:
            answer = search_web(query)
            print("AI: " + answer)

chatbot()
