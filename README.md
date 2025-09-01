# Palav(ra)dar

Detects foreign words in PDF texts by analyzing word frequency and highlighting terms that stand out from the main language.

## 🆕 Recent Updates

– No recent update on latest release (v0.0.1).

##  Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Example](#example)  
- [Contributing](#contributing)  
- [License](#license)  

---

##  Overview

**Palav(ra)dar** is a Python script designed for analyzing PDF texts.  
It identifies and highlights words that are likely not in the predominant language of the document, based on frequency analysis.

---

##  Features

- PDF file processing  
- Word frequency analysis  
- Detection of out-of-language terms  
- Output with highlighted foreign words  

---

## Usage

Run the script by providing the path to the PDF file you want to analyze:

```
python Palavradar.py path/to/your_file.pdf
```
The script will analyze the text inside the PDF and highlight - return - words that don’t match the predominant language.

---

##  Requirements

- Python 3.x  
- Necessary dependencies (adjust this list according to your script, e.g.):  
  ```bash
  pip install PyPDF2 nltk

---

** License

MIT License

Copyright (c) 2025 Breno Aguiar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
