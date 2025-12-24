from langchain_community.document_loaders import WebBaseLoader

# Define the URL(s) you want to scrape.
urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://python.langchain.com/docs/integrations/document_loaders/"
]

# Instantiate the WebBaseLoader with the list of URLs.
loader = WebBaseLoader(web_paths=urls)

# Load the documents (this performs the web scraping).
# The result is a list of Document objects.
docs = loader.load()

# Print the number of documents loaded
print(f"Number of documents loaded: {len(docs)}")

# Inspect the content and metadata of the first document
if docs:
    print("\nContent of the first document (excerpt):")
    print(docs[0].page_content[:500] + "...") # Print the first 500 characters
    print("\nMetadata of the first document:")
    print(docs[0].metadata)
