## Introduction

This is a simple program i created to translate text to any language from command line. You can use this program for any purpose.

## Getting Started
**ATTENTION!**
<br>
>You must install [`python 3.x`](https://www.python.org) or this program will not work.

Follow this step to run this program

1. Clone this repository
```sh
git clone https://github.com/Arkan237/text-translator-cli
```

2. Copy command on below then paste it on terminal or CMD to run it
<details>
<summary>Mac OS & Linux</summary>

   ```sh
   cd text-translator-cli &&
   python3 translator.py
   ```
</details>
<details>
  <summary>Windows</summary>
   
  ```sh
   cd text-translator-cli &&
   python translator.py
  ```
</details>

3. When first run. the program will install the required library and ask you what language you want to use. Choose the language you want to use.
> For now, there are only 2 languages are available (English and Indonesian). You can add other languages by editing the `translator.py` file


## How To Use
There are 2 ways to use this program. [`With Argument`](#wa) and [`Without Argument`](#woa)

<h2 id="woa">Without Argument</h2>

1. To run it, just like the first time running it.
2. Select the language of the text you want to translate. If you don't know, choose `Auto Detect`
3. Select target languange
4. Enter the text you want to translate
5. The result will be displayed in the console. if you want the result is not displayed. Use argument [`--hide`](#hide)

<h2 id="wa">With Argument</h2>
There are 5 arguments that can be used to use this program. The following is a list of arguments that can be used and their explanations.

```sh
   usage (Mac OS/Linux) : python3 translator.py <args>
   usage (Windows)      : python translator.py <args>
 ```

1. `--help` `-h` Show a list of arguments that can be used.
2. `--hide` Hide translation result and save to clipboard.
3. `--setlang` `-s` Set program language (en,id)
> For now, there are only 2 languages are available (English (en) and Indonesian (id)). You can add other languages by editing the `translator.py` file
4. `--reset` Reset program language settings and selected language history.
5. `--recent` `-r` Use the pre-selected language (not program language)
> if this argument is used when a this program is run for the first time or after running the `--reset` argument. The message "No Data" will appear
