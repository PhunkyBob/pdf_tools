# -*- coding: utf-8 -*-
__version__ = "0.2.0"
"""
pdf_extract.py

Outil qui permet d'extraire une liste de pages d'un PDF vers des fichiers séparés.

Source : https://github.com/PhunkyBob/pdf_tools
"""

from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
import shlex
import os.path
import re

if __name__ == "__main__":
    console_mode = False
    file_in = ""
    pages_txt = ""
    if len(sys.argv) > 1:
        # Il y a au moins 1 argument.
        file_in = sys.argv[1]

    if len(sys.argv) > 2:
        pages_txt = " ".join(sys.argv[2:])
        console_mode = True

    if len(file_in) == 0:
        file_in = input("Fichier d'entrée : ")
    if file_in[0] == '"' and file_in[-1] == '"':
        file_in = file_in[1:-1]

    if not os.path.isfile(file_in):
        print(f"Le fichier d'entrée n'existe pas...")
        sys.exit()

    pdf = PdfFileReader(file_in)

    nb_pages = pdf.numPages
    print(f"Nombre de pages trouvées : {nb_pages}")

    if len(pages_txt) == 0:
        pages_txt = input("Pages à extraire : ")
    pages = shlex.split(pages_txt)
    if pages_txt.strip() == "*":
        # On souhaite extraire toutes les pages.
        pages = [str(x) for x in range(1, nb_pages + 1)]

    for p in pages:
        subpdf = re.match(r"(\d+)-(\d)", p)
        tout_est_ok = True
        if subpdf:
            # On souhaite extraire des pages continues.
            subpdf_from = subpdf[1]
            subpdf_to = subpdf[2]

            if (
                not subpdf_from.isnumeric()
                or int(subpdf_from) > nb_pages
                or not subpdf_to.isnumeric()
                or int(subpdf_to) > nb_pages
            ):
                print(f'"{p}" n\'est pas une plage de pages valide.')
                tout_est_ok = False
        else:
            # On souhaite extraire une page seule.
            if not p.isnumeric() or int(p) > nb_pages:
                print(f'"{p}" n\'est pas une page valide.')
                tout_est_ok = False

        if tout_est_ok == True:
            pdfWriter = PdfFileWriter()
            if subpdf:
                for sub_page in range(int(subpdf_from), int(subpdf_to) + 1):
                    pdfWriter.addPage(pdf.getPage(sub_page - 1))
            else:
                pdfWriter.addPage(pdf.getPage(int(p) - 1))

            file_out = re.sub(".pdf$", f"_{p}.pdf", file_in, flags=re.IGNORECASE)

            answer = ""
            while os.path.isfile(file_out) and answer not in ["O", "Y", "N"]:
                answer = input(
                    f'Le fichier de destination "{file_out}" existe déjà. Voulez-vous l\'écraser ? [O]ui / [N]on : '
                ).upper()

            if answer.upper() in ["", "O", "Y"]:
                with open(file_out, "wb") as f:
                    print(f'Extraction de "{file_out}" ', end="")
                    pdfWriter.write(f)
                    f.close()
                    print("OK")

    if console_mode == False:
        print("Terminé !")
        os.system("pause")