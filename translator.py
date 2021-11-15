# Text Translator Program

import argparse, os
from requests import ConnectionError

# Save Program Language Settings
def savedata(arg):
    file = open("data.py","w")
    file.write(f"lang = '{arg}'")
    file.close()

# Reset Program Language Settings And Selected Language History
def reset():
    if args.reset == True:
        if os.name == 'nt':
            os.system("del data.py")
            os.system("del langdatainp.py")
        else:
            os.system("rm data.py")
            os.system("rm langdatainp.py")
        exit()

# Add Argument
parser = argparse.ArgumentParser(description='A simple program to translate a text into another language.', prog="Text Translator CLI",
                                 epilog="For more information, visit https://github.com/Arkan237/text-translator-cli")
parser.add_argument("--hide", help="hide translation result and save to clipboard", action='store_true')
parser.add_argument("-s","--setlang", help="set program language", metavar="(en,id)")
parser.add_argument("--reset", help="reset program language settings and selected language history and exit", action='store_true')
parser.add_argument("-r","--recent", help="use the pre-selected language (not program language)", action="store_true")
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
        langs_list = GoogleTranslator.get_supported_languages()
        # Detect If User Enter Argument "--recent"
        if args.recent == True:
            import langdatainp
            text = input("Enter the text : ")
            translate = GoogleTranslator(langs_list[langdatainp.src-1], langs_list[langdatainp.tgt-1]).translate(text)
            r = translate
            return r
        else:
            # List Supported Language
            print("List Supported Language")
            print("0. auto detect")
            for i in range(len(langs_list)):
                print(f"{i+1}. {langs_list[i]}")
            # Language Input (Source)
            print("Enter the language of the text you want to translate")
            while True:
                try:
                    userinput = int(input("Enter the number : "))
                    hist = open("langdatainp.py","w")
                    hist.write(f"src = {userinput}")
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
                            hist.write(f"\ntgt = {target}")
                            hist.close()
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
                            hist.write(f"\ntgt = {target}")
                            hist.close()
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
        langs_list = GoogleTranslator.get_supported_languages()
        # Deteksi Jika Pengguna Memasukkan Argumen "--recent"
        if args.recent == True:
            import langdatainp
            text = input("Masukan teks : ")
            translate = GoogleTranslator(langs_list[langdatainp.src-1], langs_list[langdatainp.tgt-1]).translate(text)
            r = translate
            return r
        else:
            # Daftar Bahasa Yang Didukung
            print("Daftar Bahasa Yang Didukung")
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

    reset()

    def detect_args_recent(lang):
        if args.recent == True:
            if lang == "en":
                try:
                    import langdatainp
                except ImportError:
                    print("No Data")
                    exit()
            else:
                try:
                    import langdatainp
                except ImportError:
                    print("Tidak Ada Data")
                    exit()

    if args.setlang == "en":
        savedata(1)
        detect_args_recent("en")
        if args.hide == True:
            cp.copy(en())
        else:
            print(en())
    elif args.setlang == "id":
        savedata(2)
        detect_args_recent("id")
        if args.hide == True:
            cp.copy(id())
        else:
            print(id())
    else:
        try:
            import data
            if data.lang == '1':
                detect_args_recent("en")
                if args.hide == True:
                    cp.copy(en())
                else:
                    print(en())
            else:
                detect_args_recent("id")
                if args.hide == True:
                    cp.copy(id())
                else:
                    print(id())  
        except ImportError:
            print('Choose Language/Pilih Bahasa')
            print('1. English\n2. Indonesia')
            setlang = input('')
            if setlang == '1':
                savedata(setlang)
                detect_args_recent("en")
                if args.hide == True:
                    cp.copy(en())
                else:
                    print(en())
            elif setlang == '2':
                savedata(setlang)
                detect_args_recent("id")
                if args.hide == True:
                    cp.copy(id())
                else:
                    print(id())  
            else:
                exit()

except ConnectionError:
    reset()
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
                    
except KeyboardInterrupt:
    print(); exit()
