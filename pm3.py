from gtts import gTTS
import pdfplumber
from pathlib import Path
from art import tprint


def pdf_to_mp3(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print(f'[+] Original file: {file_path}.name')
        print('[+] Process of converting...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 was created!\n ***SUCCESS***'

    else:
        return 'File not found, choose correct file path!'


def main():
    tprint('PM3-GOLD-EDITION')
    file_path = input("\nEnter a path to pdf file: ")
    language = input("Choose pdf language...en, ru, etc.: ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
