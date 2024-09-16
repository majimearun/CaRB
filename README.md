# CaRB - A Crowdsourced Benchmark for Open IE

CaRB : ***C***rowdsourced ***a***utomatic open ***R***elation extraction ***B***enchmark


## Introduction

CaRB is a dataset cum evaluation framework for benchmarking Open Information Extraction systems.

## Requirements

* Python 3.10
* See required python packages [here](requirements.txt).

## Installation

* Create a virtual environment

`conda create -n carb python=3.10`

* Activate vurtual environment

`conda activate carb`

* Install requirements

`pip install -r requirements.txt`

## Evaluating an Open IE Extractor

Prepare your extractions in the following format

* Tab Separated - Read simple tab format file, where each line consists of:

`sent, prob, rel, arg1, arg2, ...`

where `prob` is the confidence of the extraction. For simplicity, set it as `1.00` if your model does not assign any probability of confidence to extractions.

To evaluate your OpenIE system:

1. Run your extractor over the [test sentences](data/test.txt) and store the output into "*your_output*.txt"

``` 
Usage:
   python carb.py --gold=data/gold/test.tsv --out=OUTPUT_FILE --tabbed=system_output/test/*your_output*.txt

Options:
  --gold=GOLD_OIE              The gold reference Open IE file (by default, it should be under ./oie_corpus/all.oie).
  --out=OUTPUT_FILE            The output file, into which the precision recall curve will be written.
  --tabbed=TABBED_OIE	       Read tabbed format from file TABBED_OIE
```



