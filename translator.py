# Text Translator Program

import argparse, os
from requests import ConnectionError

# Save Program Language Settings
def savedata(arg):
    file = open("data.py","w")
    file.write(f"lang = '{arg}'")
    file.close()

# Reset Program Language Settings
def resetlang():
    if args.reset == True:
        if os.name == 'nt':
            os.system("del data.py")
        else:
            os.system("rm data.py")
        exit()

# Add Argument
parser = argparse.ArgumentParser(description='A simple program to translate a text into another language.', prog="Text Translator CLI",
                                 epilog="For more information, visit https://github.com/Arkan237")
parser.add_argument("--hide", help="hide translation result and save to clipboard", action='store_true')
parser.add_argument("--setlang", "-s", help="set program language", metavar="(en,id)")
parser.add_argument("--reset", help="reset program language settings and exit", action='store_true')
args = parser.parse_args()

try:
    try:
        from deep_translator import GoogleTranslator
        import pyperclip as cp
    except ImportError:
        if os.name == 'nt':
            os.system('pip install deep-translator')
            os.system('pip install pyperclip')
            os.system('cls')
        else:
            os.system('pip3 install deep-translator')
            os.system('pip3 install pyperclip')
            os.system('clear')
        from deep_translator import GoogleTranslator
        import pyperclip as cp

    def en(): # English
        # Watermark
        print('-'*20)
        print('Text Translator Program')
        print('This Program Was Created Using Python3')
        print('Created By Arkan')
        print('Github : Arkan237')
        print('-'*20)
        # List Supported Language
        print("List Supported Language")
        langs_list = GoogleTranslator.get_supported_languages()
        print("0. auto detect")
        for i in range(len(langs_list)):
            print(f"{i+1}. {langs_list[i]}")
        # Language Input (Source)
        print("Enter the language of the text you want to translate")
        while True:
            try:
                userinput = int(input("Enter the number : "))
                break
            except ValueError:
                print("Sorry, try again")
        # Language Input (Target)
        # Auto Detect
        if userinput == 0:
            while True:
                try:
                    target = int(input("Translate to : "))
                    if target == 0:
                        print("Sorry, try again")
                    else:
                        break
                except ValueError:
                    print("Sorry, try again")
            # Input text
            text = input("Enter the text : ")
            translate = GoogleTranslator(source='auto', target=langs_list[target-1]).translate(text)
            r = translate
            return r
        # ...
        else:
            while True:
                try:
                    target = int(input("Translate to : "))
                    if target == 0:
                        print("Sorry, try again")
                    else:
                        break
                except ValueError:
                    print("Sorry, try again")
            text = input("Enter the text : ")
            translate = GoogleTranslator(source=langs_list[userinput-1], target=langs_list[target-1]).translate(text)
            r = translate
            return r

    def id(): # Indonesian
            # Watermark
        print('-'*20)
        print('Text Translator Program')
        print('Program Ini Dibuat Menggunakan Python3')
        print('Dibuat Oleh Arkan')
        print('Github : Arkan237')
        print('-'*20)
        # Daftar Bahasa Yang Didukung
        print("Daftar Bahasa Yang Didukung")
        langs_list = GoogleTranslator.get_supported_languages()
        print("0. deteksi otomatis")
        for i in range(len(langs_list)):
            print(f"{i+1}. {langs_list[i]}")
        # Input Bahasa (Sumber)
        print("Masukan bahasa yang dari teks yang ingin anda terjemahkan")
        while True:
            try:
                userinput = int(input("Masukan angka : "))
                break
            except ValueError:
                print("Maaf, coba lagi")
        # Input Bahasa (Target)
        # Deteksi Otomatis
        if userinput == 0:
            while True:
                try:
                    target = int(input("Terjemahkan ke : "))
                    if target == 0:
                        print("Maaf, coba lagi")
                    else:
                        break
                except ValueError:
                    print("Maaf, coba lagi")
            # Input teks
            text = input("Masukan teks : ")
            translate = GoogleTranslator(source='auto', target=langs_list[target-1]).translate(text)
            r = translate
            return r
        # ...
        else:
            while True:
                try:
                    target = int(input("Terjemahkan ke : "))
                    if target == 0:
                        print("Maaf, coba lagi")
                    else:
                        break
                except ValueError:
                    print("Maaf, coba lagi")
            text = input("Masukan teks : ")
            translate = GoogleTranslator(source=langs_list[userinput-1], target=langs_list[target-1]).translate(text)
            r = translate
            return r

    resetlang()

    if args.setlang == "en":
        if args.hide == True:
            cp.copy(en())
        else:
            print(en())
        savedata(1)
    elif args.setlang == "id":
        if args.hide == True:
            cp.copy(id())
        else:
            print(id())
        savedata(2)
    else:
        try:
            import data
            if data.lang == '1':
                if args.hide == True:
                    cp.copy(en())
                else:
                    print(en())
            else:
                if args.hide == True:
                    cp.copy(id())
                else:
                    print(id())  
        except ImportError:
            print('Choose Language/Pilih Bahasa')
            print('1. English\n2. Indonesia')
            setlang = input('')
            if setlang == '1':
                if args.hide == True:
                    cp.copy(en())
                else:
                    print(en())
                savedata(setlang)
            elif setlang == '2':
                if args.hide == True:
                    cp.copy(id())
                else:
                    print(id())  
                savedata(setlang)
            else:
                exit()

except ConnectionError:
    resetlang()
    if args.setlang == "en":
        print("Connection Error. Please check your internet connection!")
        savedata(1)
        exit()
    elif args.setlang == "id":
        print("Koneksi bermasalah. Silahkan periksa koneksi internet anda!")  
        savedata(2)
        exit()
    else:
        try:
            import data
            if data.lang == '1':
                print("Connection Error. Please check your internet connection!")
            else:
                print("Koneksi bermasalah. Silahkan periksa koneksi internet anda!")  
        except ImportError:
            if args.setlang == "en":
                print("Connection Error. Please check your internet connection!")
                savedata(1)
            elif args.setlang == "id":
                print("Koneksi bermasalah. Silahkan periksa koneksi internet anda!")  
                savedata(2)
            else:
                print('Choose Language/Pilih Bahasa')
                print('1. English\n2. Indonesia')
                setlang = input('')
                if setlang == '1':
                    print("Connection Error. Please check your internet connection!")
                    savedata(setlang)
                elif setlang == '2':
                    print("Koneksi bermasalah. Silahkan periksa koneksi internet anda!")  
                    savedata(setlang)
                else:
                    exit()      