#CUDA-powered LASER Docker

The docker image can be built using the dbuild.sh script. The Docker image will have the tag _laser/bitext_

```
bash dbuild.sh
```
The docker image can be run using the dcli.sh script. The command is for docker API v1.39. In v1.40 you could use the flag --gpus

```
bash dcli.sh -i /path/to/input -o /path/to/output
```
The input directory should contain all monolingual files you want to align as plaintext files split on sentence level. The naming convention is the language code (ISO 639-3).
This means that if you want to align a German-English file pair the input will be two files: _de_ and _en_
Beware that only the bitexts will be saved to the output directory. If you want the embeddings to persist, you have to bind a host volume to the root directory /embeddings.


###Some dependencies are not met at this point:

transliterate 1.10.2, only used for Greek (pip install transliterate)
jieba 0.39, Chinese segmenter (pip install jieba)
mecab 0.996, Japanese segmenter