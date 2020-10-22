import os
import subprocess
import itertools
import time

def create_embeddings(source_file, language):
    """This will launch a subprocess creating embeddings for an inputfile in plaintext. Embeddings will be created as /embeddings/{language}

    :param source_file: path of the sentence-split source file
    :type source_file: string
    :param language: language code for tokenization
    :type language: string
    """
    output_embeddings = f"/embeddings/{language}"
    subprocess.run(f"python /LASER/source/embed.py --encoder /LASER/models/bilstm.93langs.2018-12-26.pt --output {output_embeddings}  --token-lang {language} < {source_file}", shell=True)

def mine_segments(source_lang, target_lang):
    """This will launch the mine_bitexts script and creates the file in the root output directory

    :param source_lang: source language code (ISO 639-3)
    :type source_lang: string
    :param target_lang: target language code (ISO 639-3)
    :type target_lang: string
    """
    path_source = f"/input/{source_lang}" 
    path_target = f"/input/{target_lang}"
    path_source_embeddings = f"/embeddings/{source_lang}"
    path_target_embeddings = f"/embeddings/{target_lang}"
    path_output = f"/output/bitext.{source_lang}-{target_lang}"
    if not os.path.isfile(path_output):
        print(f"Executing python /LASER/source/mine_bitexts.py --gpu --src-lang {source_lang} --trg-lang {target_lang} --output {path_output} --mode mine --src-embeddings {path_source_embeddings} --trg-embeddings {path_target_embeddings} {path_source} {path_target}")
        start = time.time()
        subprocess.run(f"python /LASER/source/mine_bitexts.py --gpu --src-lang {source_lang} --trg-lang {target_lang} --output {path_output} --mode mine --src-embeddings {path_source_embeddings} --trg-embeddings {path_target_embeddings} {path_source} {path_target}", shell=True)
        end = time.time()
        print(f"Aligning {source_lang} and {target_lang} took {end - start} seconds", file=open('/output/logfile', mode="a"))



if __name__ == "__main__":
    #The inputfiles are expected to be plaintext files. Their name being the language code (ISO 639-3)
    all_languages = os.listdir("/input")
    #The first step is creating the embeddings for the monolingual files.
    for language in all_languages:
        create_embeddings(source_file=os.path.join('/input/', language), language=language)
    list_1 = all_languages
    list_2 = all_languages
    unique_combos = set()
    #Create all possible language combinations. Restarting this script may lead to duplicates. The order of the set is random and the product function creates tuples. The tuple (sl, tl) is not the same as (tl, sl)
    for item in itertools.product(list_1, list_2):
        if item[0] != item[1]:
            if (item[1], item[0]) not in unique_combos:
                unique_combos.add(item)
    for combination in unique_combos:
        mine_segments(source_lang=combination[0], target_lang=combination[1])