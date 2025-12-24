from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# create loader object for Directory
loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    # since all the files are PDFs, we can specify the loader class here
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)