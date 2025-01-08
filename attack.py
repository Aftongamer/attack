import requests, time, os


text = "Hi my name is Afton V 1.0"
texts = ""
for i in text:
    os.system("clear")
    texts += i
    print(f"{texts}|")
    time.sleep(0.1)
os.system("clear")
print(texts)
print("loding ...")
time.sleep(10)
text = "my channel is : @Aftonplus , my id telegram = @Aftonplus1 exit = Ctrl + C"
texts = ""
for i in text:
    os.system("clear")
    texts += i
    print(f"{texts}|")
    time.sleep(0.1)
os.system("clear")
print(texts)
print("loding ...")
time.sleep(10)
print("your url (http:// or https://)")
url = input("URL : ")

while True:
    response = requests.get(url=url)
    print(f"send code : {response.status_code}")


