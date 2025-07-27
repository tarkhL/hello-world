import argparse
from pathlib import Path
from PyPDF2 import PdfReader


def pdf_to_text(pdf_path: Path, txt_path: Path) -> None:
    reader = PdfReader(str(pdf_path))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ''
        text += '\n'
    txt_path.write_text(text)


def main():
    parser = argparse.ArgumentParser(description="Extract text from PDF to a text file")
    parser.add_argument("pdf", type=Path, help="Input PDF file")
    parser.add_argument("txt", type=Path, nargs="?", help="Output text file (default: same name with .txt)")
    args = parser.parse_args()

    pdf_path = args.pdf
    txt_path = args.txt if args.txt else pdf_path.with_suffix('.txt')

    pdf_to_text(pdf_path, txt_path)
    print(f"Text written to {txt_path}")


if __name__ == "__main__":
    main()
