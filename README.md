# PFASProphet

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

A tool for giving a score on the likelihood of PFAS (Per- and Polyfluoroalkyl Substances) from mass spectrometry data using machine learning.

## Features
- Obtain a PFAS scores from precursor masses and fragment ions.
- Support for CSV files or direct list inputs.
- Can be run from python directly or Command-line interface (CLI).
- Handles ionised vs. neutral masses (negative ESI mode).
- See examples for usage.

## Installation

```bash
pip install PFASProphet
```

## Usage
### CLI Examples
- **Predict from lists**: `pfasprophet --mass "[248.9461]" --fragments "[[63.9624]]"`
- **Predict from CSV**: `pfasprophet --file data.csv`
- **Help**: `pfasprophet` or `pfasprophet --help`

### Python examples
- See [tests/examples_for_users.py](tests/examples_for_users.py) for copy-paste snippets:
	- Predict from in-memory lists
	- Predict from CSV (default and custom column names)
	- Neutral masses (`is_ionised=False`)
	- Append predictions back to a CSV (`in_file=True`)