# -*- coding: utf-8 -*-
__version__ = "0.2.0"
"""
pdf_merge.py

Outil qui permet de fusionner une liste de fichiers PDF vers un fichier unique.

Source : https://github.com/PhunkyBob/pdf_tools
"""

from PyPDF2 import PdfFileMerger
import sys
import shlex
import os.path

if __name__ == "__main__":
    console_mode = False
    files_in_txt = ""
    file_out = ""
    if len(sys.argv) > 1:
        # Il y a au moins 1 argument.
        file_out = sys.argv[1]

    if len(sys.argv) > 2:
        files_in_txt = " ".join(sys.argv[2:])
        console_mode = True

    pdfs = []

    if len(files_in_txt) == 0:
        files_in_txt = input("Liste des fichiers à fusionner (séparés par un espace) : ")
    files_in = shlex.split(files_in_txt)
    tout_est_ok = True
    for f in files_in:
        if not os.path.isfile(f):
            print(f'Le fichier "{f}" n\'existe pas.')
            tout_est_ok = False
        else:
            pdfs.append(f)

    if not tout_est_ok:
        print("Essaye encore...")
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
        ).upper()

    if answer.upper() in ["N", "Q"]:
        sys.exit()

    if len(file_out) == 0:
        print("OK, relance moi quand tu te seras décidé...")
        sys.exit()

    print(f'Création de "{file_out}" ', end="")
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(file_out)
    merger.close()
    print("OK")

    if console_mode == False:
        print("Terminé !")
        os.system("pause")