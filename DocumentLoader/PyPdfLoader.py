#  works best with text data only as it use PyPdf under the hood so it is not good with scanned pdf or complex layouts

# simple PDF -> PYPDFLoader
# PDF with table & columns -> PDFPlumberLoader
# scaned/image PDF -> UnstructuredPDFLoader , AmazonTextractPDFLoader
# need layout and image data -> PyMuPDFLoader
# want best structured data -> UnstructuredPDFLoader

from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader('Web_Application_for_Retrieval-Augmented_Generation.pdf')

docs = loader.load()

total = ""

for doc in docs:
    total += doc.page_content + "\n"

print(len(total))