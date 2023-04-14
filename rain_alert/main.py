import requests

API_KEY = "af829f94eae434efba38efc3f64685c2"


def get_quote():
    try:
        response = requests.get(url="https://api.kanye.rest/")
        response.raise_for_status()
        quote = response.json()["quote"]
        canvas.itemconfig(quote_text, text=quote)
    except:
        pass




get_quote()