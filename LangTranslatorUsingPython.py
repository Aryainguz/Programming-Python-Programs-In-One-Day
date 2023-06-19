import requests
import json
#aryainguz™

print("Welcome to shell translator by Aryainguz")

source = input("Enter language code your text is in, eg => for English add EN, ES for spanish, hi for Hindi ").lower()
target = input("Enter language code you want to translate to, eg => for italian add IT, ES for spanish, hi for Hindi ").lower()
your_lang = input("Enter you text here ")

key = "9ef548e8160cd3da6264"
url = f"https://api.mymemory.translated.net/get?q={your_lang}&langpair={source}|{target}"

answer = requests.get(url)
data = answer.json()
try:
    print(data['responseData']['translatedText'])
except:
    print("You got an error, try to run again or contact Aryan")
