import chardet
import kss
import re
import os

input_folder = r"C:\Users\JIHAN\Desktop\전"
output_folder = r"C:\Users\JIHAN\Desktop\후"
unprocessed_folder = r"C:\Users\JIHAN\Desktop\미처리"

count = 0

for filename in os.listdir(input_folder):
    count += 1
    print(count)
    if filename.endswith(".txt"):
        input_path = os.path.join(input_folder, filename)

        output_filename = re.sub(r"\(\d+\)", "", filename)
        output_filename = re.sub(r"1080p.*", "", output_filename)
        output_filename = re.sub(r"\.1080.*", "", output_filename)
        output_filename = re.sub(r"\.720p.*", "", output_filename)
        output_filename = re.sub(r"\.720.*", "", output_filename)
        output_filename = re.sub(r"\.2160p.*", "", output_filename)
        output_filename = re.sub(r"\.2160.*", "", output_filename)
        output_filename = re.sub(r"\.BluRay.*", "", output_filename)
        output_filename = re.sub(r"\.BRRip.*", "", output_filename)
        output_filename = re.sub(r"\.WEB-.*", "", output_filename)
        output_filename = re.sub(r"\.XviD.*", "", output_filename)
        output_filename = re.sub(r"\.x264.*", "", output_filename)
        output_filename = re.sub(r"\.DVDRip.*", "", output_filename)
        output_filename = re.sub(r"\.WEBRip.*", "", output_filename)
        output_filename = re.sub(r"\.BDRip.*", "", output_filename)
        output_filename = re.sub(r"\.HDRip.*", "", output_filename)
        output_filename = re.sub(r"\.Blu-ray.*", "", output_filename)
        output_path = os.path.join(output_folder, output_filename + ".txt")
        unprocessed_path = os.path.join(unprocessed_folder, output_filename + ".txt")

        with open(input_path, 'rb') as f:
            result = chardet.detect(f.read())

        with open(input_path, "r", encoding=result['encoding']) as f:
            text = f.read()
            text = text.replace("\n", " ")
            text = re.sub(r"\s{2,}", " ", text)

            text_without_newline = re.sub(r'\n', '', text)
            num_characters = len(text) - text.count('\n')

        sentences = kss.split_sentences(text)

        if(len(sentences) > num_characters/25):
            with open(output_path, "w", encoding=result['encoding']) as f:
                f.write(f"Number of sentence lines: {len(sentences)}\n")
                f.write(f"Number of avg sentence lines: {num_characters/25}\n\n")
                f.write('\n'.join(sentences))
        else:
            with open(unprocessed_path, "w", encoding=result['encoding']) as f:
                f.write(f"Number of sentence lines: {len(sentences)}\n")
                f.write(f"Number of avg sentence lines: {num_characters/25}\n\n")
                f.write('\n'.join(sentences))






