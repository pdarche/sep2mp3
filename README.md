# sep2mp3
A very small python command line tool for converting Stanford Encyclopedia of Philosophy articles into sound files.  I'm using a mac so it uses _say_ and outputs files to _.aiff_.

## Installation
```bash
python setup.py install
```

## Usage
The tool takes two arugments: a positional argument of the url for the target SEP file and a -o argument for the name of the output file.

```bash
sep2mp3 [article_url] -o [output_file_name]
```

## Example
```bash
sep2mp3 http://plato.stanford.edu/entries/justice-distributive/ -o distributive_justice
```


