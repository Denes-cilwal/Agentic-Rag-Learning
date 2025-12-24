from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

# --- Path resolution (robust) ---
BASE_DIR = Path(__file__).resolve().parent          # folder containing this script
PDF_NAME = "dl-curriculum.pdf"
pdf_path = BASE_DIR / PDF_NAME

# --- Sanity checks ---
print("=== Sanity Checks ===")
print("CWD:", os.getcwd())
print("Script dir:", BASE_DIR)
print("Target PDF path:", pdf_path)
print("Exists?:", pdf_path.exists())
print("Is file?:", pdf_path.is_file())
if pdf_path.exists():
    print("Size (bytes):", pdf_path.stat().st_size)

# Optional: list nearby PDFs to help you spot naming/path issues
nearby_pdfs = sorted([p.name for p in BASE_DIR.glob("*.pdf")])
print("PDFs in script dir:", nearby_pdfs)

# Fail fast with a helpful message
if not pdf_path.exists():
    raise FileNotFoundError(
        f"PDF not found at: {pdf_path}\n"
        f"- Move '{PDF_NAME}' next to this script, or\n"
        f"- Update PDF_NAME / path accordingly."
    )
if not pdf_path.is_file():
    raise ValueError(f"Path exists but is not a file: {pdf_path}")
if pdf_path.stat().st_size == 0:
    raise ValueError(f"PDF file is empty (0 bytes): {pdf_path}")

# --- Load PDF ---
loader = PyPDFLoader(str(pdf_path))
docs = loader.load()



splitter = CharacterTextSplitter(
    chunk_size=200,
    # chunk_overlap set to 0 to avoid overlapping content in chunks
    chunk_overlap=0,
    separator=''
)

# document pages as list is passed to split_documents
result = splitter.split_documents(docs)

print(result[0])