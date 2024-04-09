import PyPDF2
import os
from typing import List, Union


class pdf_reader():

    def __init__(self, path: Union[str, os.PathLike]) -> List[str]:
        self.path = path



    def read_pdf(self):
        text = []
        with open(self.path, 'rb') as file:
            pdf = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf.pages)):
                page = pdf.pages[page_num]
                text.append(page.extract_text())
                print(text)

        return text

