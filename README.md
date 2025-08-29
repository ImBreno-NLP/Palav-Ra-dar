# Palav(Ra)dar
Palav(Ra)dar is a Python script that scans PDF files to detect words written in a different language from the main text.

The script works by:

*Extracting text from a PDF file using PyMuPDF.

*Tokenizing the text into individual words.

*Checking each word against language frequency data using the wordfreq library.

*Detecting words that are more likely to belong to a foreign language (e.g., English words inside a Portuguese text).

*Ignoring numbers and non-alphabetical tokens.

This tool is useful for:

Identifying foreign words in academic or professional documents.

Checking consistency of language in texts.

Detecting unintentional code-switching or borrowed words.

Requirements:

Python 3.8+

PyMuPDF

wordfreq

Breno da Costa Caricchio Aguiar
Linguistics Student at Federal University of São Carlos (UFSCar)
Researcher at NILC-USP(POETISA) (Interinstitutional Center for Computational Linguistics)
