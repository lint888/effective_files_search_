import PyPDF2
import os
from typing import List, Union


class pdf_reader():

    def __init__(self, path: Union[str, os.PathLike]) -> List[str]:
        self.path = path



    def read_pdf(self):
        text = []
        with open(self.path, 'rb') as file:
            pdf = PyPDF2.PdfFileReader(file)
            for page_num in range(pdf.numPages):
                page = pdf.getPage(page_num)
                text.append(page.extractText())

        return text

