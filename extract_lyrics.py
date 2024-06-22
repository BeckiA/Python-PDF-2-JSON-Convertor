import json
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams

def extract_lyrics_from_pdf(pdf_path):
    laparams = LAParams()
    text = extract_text(pdf_path, laparams=laparams)
    lyrics = []
    
    # Split the text by form feed to separate pages
    pages = text.split('\f')
    
    for page in pages:
        lines = page.split('\n')
        if lines:
            current_title = lines[0].strip()
            current_lyrics = "\n".join(lines[1:]).strip()  # Join the rest as lyrics
            
            # Append to the lyrics list only if title and lyrics are not empty
            if current_title and current_lyrics:
                lyrics.append({"title": current_title, "lyrics": current_lyrics})

    return lyrics

# Specify the paths to the PDF and JSON files
pdf_path = "eka_lyrics.pdf"  # Change this to the actual path of your PDF file
json_path = "lyrics_data.json"  # Change this to the desired path to save the JSON file

# Extract lyrics from the PDF
lyrics_data = extract_lyrics_from_pdf(pdf_path)

# Save the extracted lyrics to a JSON file
with open(json_path, 'w', encoding='utf-8') as json_file:
    json.dump(lyrics_data, json_file, ensure_ascii=False, indent=4)

print(f"Lyrics data has been saved to {json_path}")
