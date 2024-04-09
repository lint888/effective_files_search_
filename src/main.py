from fastapi import FastAPI
from core.read_pdf import pdf_reader

app=FastAPI()




pdf_reader = pdf_reader("core/BERT original.pdf")
@app.get("/effective_search")
async def search_root():

    result = pdf_reader.read_pdf()
    print(result)

    return {"pdf_content": result}
