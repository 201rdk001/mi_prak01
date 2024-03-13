# Makslīga intelekta pamati: pirmais praktiskais darbs

Minimālā Python versija: 3.11  
Minimālā Kivy versija: jaunākā (2.3.0)

### Izstrādes vides uzstādīšana

1. Python uzinstalēšana

Python instalācija uz Windows: [DigitalOcean pamācība Python instalācijai](https://www.digitalocean.com/community/tutorials/install-python-windows-10)  
Python instalācija uz MacOS/Linux/Citi: Nav dots (noteikti paši zināsiet labāk, kā uzinstalēt)

2. Trešās puses pakotņu pieinstalēšana

Uz Windows - no CMD vai Powershell komandrindas palaist: ```py -m pip install -r requirements.txt```  
Uz MacOS/Linux/Citi - no Jūsu noklusētās komandrindas čaulas: ```python -m pip install -r requirements.txt```

### Noderīgas saites

Kivy dokumentācija:  
https://kivy.org/doc/stable/  
https://kivy.org/doc/stable/api-kivy.html

### Citi izstrādes ieteikumi

Lai pārbaudītu, vai pastāv iespējamas koda stila nepilnības, ir ieteikts pielietot [pylint](https://pypi.org/project/pylint/) rīku, kā arī [autopep8](https://pypi.org/project/autopep8/), kas daļēji noformātēs koda failu automātiski.

Ja Jūs bieži lietojat Python valodu citiem projektiem, kam nepieciešamas citas pakotnes, kas varētu konfliktēt ar ši projekta izstrādes vidi, tiek ieteikts izpētīt [Python virtuālās vides](https://docs.python.org/3/tutorial/venv.html) (Python virtual enviroments), lai novērstu šāda tipa problēmas.
