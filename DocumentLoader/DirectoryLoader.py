# "**/*.txt" -> all .txt files in all subfolders
# "*.pdf" -> all .pdf files in root directory
# "data/*.csv" -> all .csv files in data/  folder
# "**/*" -> all files any type

# ** = recursive search through sub folders

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for doc in docs:
    print(doc.page_content)