# Authorship Verification

This repository contains the software for an unsupervised authorship verification model.  This system was used in the PAN Author Identification task at CLEF 2015.  The describing paper is available as a [PDF](http://ceur-ws.org/Vol-1391/28-CR.pdf "Paper").


## Usage

Run:

    python panAV.py -i input_folder -o output_folder

for example:

    python panAV.py -i "data/dutch essays/" -o "output/DE/"

Evaluate:

    python -c "from evaluator import evalAV; evalAV(truth_file, answer_file)"

for example:

    python -c "from evaluator import evalAV; evalAV('data/dutch essays/truth.txt', 'output/DE/answers.txt')"

## Requirements

- Python 2.7.12
- The PAN data, available here to [download](http://pan.webis.de/clef15/pan15-web/author-identification.html "corpus")


## Notes

This repository will soon contain all my models from my participation in the various PAN tasks.

- Authorship Verification
- Author Profiling
- Author Profiling cross-genre
- Author Clustering