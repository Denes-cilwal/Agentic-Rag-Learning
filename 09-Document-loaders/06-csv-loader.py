from pathlib import Path
from langchain_community.document_loaders import CSVLoader

BASE_DIR = Path(__file__).resolve().parent   # folder containing this script
csv_path = BASE_DIR / "Social_Networks_Ads.csv"  # if CSV is in same folder as script

print("CWD:", Path.cwd())
print("Looking for:", csv_path)
print("Exists?:", csv_path.exists())

if not csv_path.exists():
    raise FileNotFoundError(f"CSV not found at: {csv_path}")

loader = CSVLoader(file_path=str(csv_path))
docs = loader.load()

print("Docs:", len(docs))
print(docs[0])
