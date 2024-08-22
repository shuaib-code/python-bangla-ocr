import os

def merge_text_files(input_folder, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in os.listdir(input_folder):
            file_path = os.path.join(input_folder, filename)
            
            if os.path.isfile(file_path) and filename.endswith('.txt'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                        outfile.write("\n")
                except UnicodeDecodeError:
                    print(f"Skipping file {filename} due to encoding issues.")

input_folder = 'text_OCR'
output_file = 'merged_text.txt'

merge_text_files(input_folder, output_file)

print(f"All text files in {input_folder} have been merged into {output_file}.")
