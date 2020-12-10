import request

url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

headers = {
    'accept': "application/json",
    'x-rapidapi-key': "a68db12002msh3adc7eccf7e64fep17b596jsnfb8739f37240",
    'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)
html = response.text
print(html)

result = dict(json.loads(html))
print(result['value']) 
