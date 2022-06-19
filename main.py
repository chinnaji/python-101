import requests
import webbrowser

# open pages on browser
def open_page():
    urls = ["https://chinnaji.vercel.app/","https://www.google.com/"]
    for url in urls:
        webbrowser.open(url)

open_page()