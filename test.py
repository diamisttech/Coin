from tkinter.ttk import Combobox
import requests
import json
import pprint
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
response.raise_for_status()
data = response.json()
print(data)