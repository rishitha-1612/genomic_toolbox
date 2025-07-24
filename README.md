Genomic Toolbox

* Genomic Toolbox is a web-based DNA analysis platform developed using Python Flask. It allows users to input original and mutated DNA sequences, visualize differences, translate DNA into protein, and predict potential diseases based on known mutations.
This tool was developed as an interdisciplinary project combining Computer Science and Biotechnology

* Project Objective
The main objective of Genomic Toolbox is to provide a simple interface for students, researchers, and developers to:
Detect point mutations in DNA sequences.
Translate DNA into protein using codon tables.
Predict diseases based on known genetic mutations.
This tool helps bridge the gap between biotechnology and computer science.

* Theoretical Background
1. DNA Structure:
DNA consists of four nucleotide bases – Adenine (A), Thymine (T), Cytosine (C), and Guanine (G). A DNA sequence is essentially a string of these letters.

2. Mutation:
Mutations are alterations in the DNA sequence. A point mutation is when a single nucleotide changes (e.g., A → G).

3. Codons & Proteins:
Every three nucleotides form a codon. Each codon corresponds to a specific amino acid. Start codons initiate translation, and stop codons terminate it.

4. Disease Linkage:
Certain mutations are linked to diseases. If known mutation patterns are detected in a DNA sequence, associated diseases can be predicted.

* Key Features
1. Mutation Checker
Compares original and mutated sequences.
Highlights base-level changes.
Displays total mutation count.

2. Protein Translator
Translates DNA into a protein chain.
Identifies start (green) and stop (red) codons.

3. Disease Predictor
Checks for known disease-causing mutations using disease_data.json.
Displays matched diseases, if any.

* Page-wise Flow
1. index.html – Landing Page
Introduces the application.
Contains "Analyze Your DNA" button.

2. loading.html – Preloader
Shows a transition screen: "Loading your DNA experience..."

3. input.html – Input Form
Two fields:
Original DNA sequence
Mutated DNA sequence

4. dashboard.html – Feature Hub
Shows three options:
Mutation Checker
Protein Translator
Disease Predictor

5. mutation.html
Displays side-by-side comparison of DNA.
Highlights changes.

6. protein.html
Displays protein translation.
Color-coded codons for clarity.

7. disease.html
Checks mutations against known disease patterns.
Displays any matches.

* How It Works
User submits original and mutated DNA.
Python Flask routes data to different pages.

Each feature (Mutation, Translation, Prediction) uses core logic:
Comparison: Character-wise base difference
Translation: Codon-based amino acid mapping
Prediction: JSON lookup for known mutations

* Tech Stack Used
Area- Technology
Frontend- HTML, CSS
Backend- Python (Flask)
Data Storage- JSON (for diseases)
Hosting- Flask Dev Server

* Folder Structure

genomic_toolbox/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── loading.html
│   ├── input.html
│   ├── dashboard.html
│   ├── mutation.html
│   ├── protein.html
│   └── disease.html
│
├── disease_data.json
├── main.py
└── README.md

* Setup Instructions
1. Make sure Python is installed on your system.
2. Open terminal and navigate to the project folder.
3. Install Flask if not already installed:
    pip install flask
4. Run the app:
    python main.py
5. Open your browser and visit:
    http://127.0.0.1:3000

* Credits
Developed by: Rishitha Rasineni & Lakshmi D
Biotechnology Support: Lakshmi D from Kristu Jayanti College
Codon Table Reference: NCBI Codon Usage Table
Mutation dataset: Derived and cleaned from ClinVar Conflicting Variants CSV
Project type: Interdisciplinary bioinformatics web application