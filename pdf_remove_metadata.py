# -*- coding: utf-8 -*-
__version__ = "0.1.0"
"""
pdf_remove_metadata.py

Outil qui permet de supprimer les metadata d'un fichier PDF.

Source : https://github.com/PhunkyBob/pdf_tools
"""

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import sys
import shlex
import os.path
import re

if __name__ == "__main__":
    console_mode = False
    file_in = ""
    file_out = ""
    if len(sys.argv) > 1:
        # Il y a au moins 1 argument.
        file_in = sys.argv[1]

    if len(sys.argv) > 2:
        # Il y a au moins 2 arguments.
        file_out = sys.argv[2]

    if file_in.strip().lower() in ("--version", "-v"):
        print(f"{__version__}")
        sys.exit()

    if len(file_in) == 0:
        file_in = input("Fichier d'entrée : ")
        console_mode = True
    if file_in[0] == '"' and file_in[-1] == '"':
        file_in = file_in[1:-1]

    if not os.path.isfile(file_in):
        print(f"Le fichier d'entrée n'existe pas...")
        sys.exit()

    pdf_file_in = open(file_in, 'rb')
    pdf_reader = PdfFileReader(pdf_file_in)
    metadata = pdf_reader.getDocumentInfo()
    if not metadata or len(metadata) == 0:
        print("Pas de metadata")
        sys.exit()
        
    print("METADATA")
    for m in metadata:
        print(f"{m} : {metadata[m]}")

    if len(file_out) == 0:
        file_out = input("Fichier de sortie : ")
    if file_out[0] == '"' and file_out[-1] == '"':
        file_out = file_out[1:-1]

    if os.path.isfile(file_out):
        answer = ""
        while answer.lower() not in ("y", "yes", "o", "oui", "n", "no", "non", "q", "quit"):
            answer = input(f"Le fichier existe déjà. Ecraser [O/N] ? ")
            if answer.lower() in ("n", "no", "non", "q", "quit"):
                sys.exit()

    pdf_merger = PdfFileMerger()
    pdf_merger.append(pdf_file_in)
    pdf_file_in.close()
    pdf_merger.addMetadata({
        '/Producer': ''
    })
    file_out = open(file_out, 'wb')
    pdf_merger.write(file_out)

    pdf_file_in.close()
    file_out.close()

    if console_mode == False:
        print("Terminé !")
        os.system("pause")