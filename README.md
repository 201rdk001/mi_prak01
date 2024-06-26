# Makslīga intelekta pamati: pirmais praktiskais darbs

Minimālā Python versija: 3.11  
Minimālā wxPython versija: jaunākā (4.2.1)

### Izstrādes vides uzstādīšana

1. Python uzinstalēšana

Python instalācija uz Windows: [DigitalOcean pamācība Python instalācijai](https://www.digitalocean.com/community/tutorials/install-python-windows-10)  
Python instalācija uz MacOS/Linux/Citi: Nav dots (noteikti paši zināsiet labāk, kā uzinstalēt)

Piezīme: Uz Windows sistēmām, ```python``` no komandrindas var būt nepieejama, tādējādi tā vietā ver mēģināt lietot ```py```. Ja arī ```py``` nav pieejams, lūdzu pārbaudiet, vai esat pareizi uninstalējuši Python vidi.

2. Trešās puses pakotņu pieinstalēšana

No komandrindas (CMD/Powershell/Bash/citi) palaist:
    ```pip install -r requirements.txt```  
    vai  
    ```python -m pip install -r requirements.txt```  

3. Programmas palaišana

Lai palaistu programmu, no komandrindas projekta mapē palaist: ```python src/main.py```

### Noderīgas resursi

[https://wiki.wxpython.org/](https://wiki.wxpython.org/) - Visparīgs info par wxPython pielietošanu
[https://docs.wxpython.org/](https://docs.wxpython.org/) - Info par atseviškiem wxPython bibliotēkas moduļiem
[https://github.com/wxFormBuilder/wxFormBuilder/releases](https://github.com/wxFormBuilder/wxFormBuilder/releases) - Lietotāja saskarnes veidošanas rīks

Lai varētu vizualizēt spēles koku, var palaist failu ```tree_debug.py``` no python interpretatora, kas uzģenerēs koku un izvadīs kodu, kuru pēctam iekopējot kādā no šiem grafu vizalizācias rīkiem:

[https://dreampuf.github.io/GraphvizOnline/](https://dreampuf.github.io/GraphvizOnline/)
[http://magjac.com/graphviz-visual-editor/](http://magjac.com/graphviz-visual-editor/)

izviedos uzģēnerētā koka vizualizāciju, kas var būt noderīgs koda izstrādē un/vai atkļūdošanā.
 
### Citi izstrādes ieteikumi

Lai pārbaudītu, vai pastāv iespējamas koda stila nepilnības, ir ieteikts pielietot [pylint](https://pypi.org/project/pylint/) rīku, kā arī [autopep8](https://pypi.org/project/autopep8/), kas daļēji noformātēs koda failu automātiski.

Ja Jūs bieži lietojat Python valodu citiem projektiem, kam nepieciešamas citas pakotnes, kas varētu konfliktēt ar ši projekta izstrādes vidi, tiek ieteikts izpētīt [Python virtuālās vides](https://docs.python.org/3/tutorial/venv.html) (Python virtual enviroments), lai novērstu šāda tipa problēmas.

## Praktiskā darba saites

[Darba Apraksts](https://rtucloud1-my.sharepoint.com/:w:/g/personal/kristaps-arnolds_kaidalovs_edu_rtu_lv/EV4opThjx7tNrvAiIB6KMgMB3KaWZBorr9cjN6yHeCr3WQ)  
[Atskaites melnraksts](https://rtucloud1-my.sharepoint.com/:w:/g/personal/kristaps-arnolds_kaidalovs_edu_rtu_lv/Ecz4K5vDS9REk-cEYLN1vygBL0_AB51tkJkkhI4punW_RA?e=KhIhYk)  
[Izmaiņu reģistrs](https://rtucloud1-my.sharepoint.com/:w:/g/personal/kristaps-arnolds_kaidalovs_edu_rtu_lv/Ee3QjAfrwD9CkkP6DCNtZtEBoNTS4nny9UP4APn9T-aRew?e=2lhEkU)  
[Uzdevumu reģistrs](https://rtucloud1-my.sharepoint.com/:w:/g/personal/kristaps-arnolds_kaidalovs_edu_rtu_lv/EQ0JB2iJSUlDlVmaPKTD8AgBXjnGY_7y214hm_fkKjbJWQ?e=bV0vJv)  