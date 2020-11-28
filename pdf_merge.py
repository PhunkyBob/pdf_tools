# -*- coding: utf-8 -*-
__version__ = "0.2.1"
"""
pdf_merge.py

Outil qui permet de fusionner une liste de fichiers PDF vers un fichier unique.

Source : https://github.com/PhunkyBob/pdf_tools
"""

from PyPDF2 import PdfFileMerger
import sys
import shlex
import os.path
import glob

if __name__ == "__main__":
    console_mode = False
    files_in_txt = ""
    file_out = ""
    if len(sys.argv) > 1:
        # Il y a au moins 1 argument.
        file_out = sys.argv[1]

    if file_out.strip().lower() in ("--version", "-v"):
        print(f"{__version__}")
        sys.exit()

    if len(sys.argv) > 2:
        files_in_txt = " ".join(sys.argv[2:])
        console_mode = True

    pdfs = []

    if len(files_in_txt) == 0:
        files_in_txt = input(
            "Liste des fichiers à fusionner (séparés par un espace) : "
        )
    files_in = shlex.split(files_in_txt.replace('\\', '/'))
    tout_est_ok = True
    for f in files_in:
        for file_sub in glob.iglob(f):
            if not os.path.isfile(file_sub):
                print(f'Le fichier "{file_sub}" n\'existe pas.')
                tout_est_ok = False
            else:
                print(f'Ajout de "{file_sub}" ', end="")
                pdfs.append(file_sub)
                print("OK")

    if not tout_est_ok:
        print("On s'arrête là...")
        sys.exit()

    if len(pdfs) == 0:
        sys.exit()

    if len(file_out) == 0:
        file_out = input("Fichier de destination : ")
    if file_out[0] == '"' and file_out[-1] == '"':
        file_out = file_out[1:-1]
    answer = ""
    while os.path.isfile(file_out) and answer not in ["O", "Y", "N", "Q"]:
        answer = input(
            f'Le fichier de destination "{file_out}" existe déjà. Voulez-vous l\'écraser ? [O]ui / [N]on : '
        ).upper().strip()

    if answer.upper() in ["N", "Q"]:
        print("Alors on ne fait rien.")
        if console_mode == False:
            os.system("pause")
        sys.exit()

    if len(file_out) == 0:
        print("OK, relance moi quand tu te seras décidé...")
        if console_mode == False:
            os.system("pause")
        sys.exit()

    print(f'Création de "{file_out}" ', end="")
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
        
    merger.write(file_out)
    merger.close()
    print("OK")

    if console_mode == False:
        os.system("pause")