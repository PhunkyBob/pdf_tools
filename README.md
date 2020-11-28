# PDF Tools
Petits outils développés en Python pour effectuer des manipulations simples sur des fichiers PDF (fonctions souvent disponibles uniquement dans les versions payantes des outils PDF). 

## Utilisation

### pdf_merge.py
Outil qui permet de fusionner une liste de fichiers PDF vers un fichier unique. 
  
**Utilisation en mode interactif**  
```
pdf_merge.py
```
L'outil demande une liste de fichiers à fusionner (séparés par un espace).  
Si tous les fichiers existent, l'outil demande le nom du fichier de destination.  
  
**Utilisation en ligne de commande**  
```
pdf_merge.py <file_out> <file_in_1> [file_in_2 ...]
```
file_out : le chemin vers le fichier PDF de destination.  
file_in_1 : le chemin vers le 1er fichier PDF à fusionner.  
file_in_2 (optionnel) : le chemin vers le 2em fichier PDF à fusionner.  
...  
file_in_n (optionnel) : le chemin vers le Nem fichier PDF à fusionner.  
  
  
Exemples :  
- Pour fusionner les fichiers `in_1.pdf` et `in_2.pdf` dans `out.pdf` : 
```
pdf_merge out.pdf in_1.pdf in_2.pdf
```
Le programme créera le fichier `out.pdf`.  
  
  
### pdf_extract.py 
Outil qui permet d'extraire une liste de pages d'un PDF vers des fichiers séparés.  
  
**Utilisation en mode interactif**  
```
pdf_extract.py
```
L'outil demande le chemin vers le fichier dont on veut des pages.  
Si le fichier existe, l'outil demande la liste des pages à extraire (séparées par un espace).  
Si on saisit uniquement `*`, toutes les pages seront extraites individuellement.  
Si on saisit `X-Y`, les pages X à Y seront extraites dans le même document PDF.  
  
  
**Utilisation en ligne de commande**  
```
pdf_extract.py <file_in> <page_1> [page_2 ...]
pdf_extract.py <file_in> *
```
file_in : le chemin vers le fichier PDF dont on veut des pages.  
page_1 : le numéro de la 1er page à extraire. Possibilité de définir une plage avec `X-Y`.  
page_2 (optionnel) : le numéro de la 2em page à extraire.  
...  
page_n (optionnel) : le numéro de la Nem page à extraire.  
`*` : extrait toutes les pages.  
  
  
Exemples :  
- Pour extraire la page 3 de `in.pdf` : 
```
pdf_extract in.pdf 3
```
Le programme créera le fichier `in_3.pdf` qui contiendra une seule page.  

- Pour extraire les pages 3, 5 et 7 de `in.pdf` : 
```
pdf_extract in.pdf 3 5 7
```
Le programme créera les fichiers `in_3.pdf`, `in_5.pdf` et `in_7.pdf` qui contiendront une seule page chacun.  
  
- Pour extraire les pages 3 à 7 de `in.pdf` : 
```
pdf_extract in.pdf 3-7
```
Le programme créera le fichier `in_3-7.pdf` qui contiendra 5 pages.  
  
- Pour extraire toutes les pages `in.pdf` : 
```
pdf_extract in.pdf *
```
Le programme créera les fichiers `in_1.pdf`, `in_1.pdf`, ... `in_n.pdf` qui contiendront une seule page chacun.  
  
  
## Installation
### Prérequis
- Python 3.7+ (non testé avec les versions précédentes)  
- pip  
  
  
#### Sous Windows
##### Python
Allez sur ce site :  
https://www.python.org/downloads/windows/  
et suivez les instructions d'installation de Python 3.  
  
##### Pip
- Téléchargez [get-pip.py](https://bootstrap.pypa.io/get-pip.py) dans un répertoire.  
- Ouvrez une ligne de commande et mettez vous dans ce répertoire.  
- Entrez la commande suivante :  
```
python get-pip.py
```
- Voilà ! Pip est installé !  
- Vous pouvez vérifier en tapant la commande :  
```
pip -v
```

#### Sous Linux
Si vous êtes sous Linux, vous n'avez pas besoin de moi pour installer Python ou Pip...  
  
### Téléchargement
- Vous pouvez cloner le repo git :  
```
git clone https://github.com/PhunkyBob/pdf_tools
```
ou  
- Vous pouvez télécharger uniquement [le binaire Windows](https://github.com/PhunkyBob/pdf_tools/releases/latest) (expérimental).   
  
  
### Configuration
```
pip install -r requirements.txt
```
