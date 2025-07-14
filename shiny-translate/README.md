# Shiny DNA/RNA Translator

This Shiny for Python app demonstrates the translation of a DNA or RNA sequence
into a protein sequence using **Biopython**. It is designed for public outreach
events where visitors can interactively see how codons map to amino acids.

## Running locally

1. Install the required packages (ideally within a virtual environment):

   ```bash
   pip install shiny biopython
   ```

2. Launch the app:

   ```bash
   shiny run --reload app.py
   ```

The app will open in your default web browser.

## Exporting a self-contained site

To create a static site that runs entirely in the browser without any Python
installation, use **shinylive**:

```bash
pip install shinylive
shinylive export . out-dir
```

The contents of `out-dir` can be served from any web server or opened directly
in a browser, making it ideal for offline demonstrations.
