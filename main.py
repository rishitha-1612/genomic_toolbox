from flask import Flask, render_template, request
import json

app = Flask(__name__)
data_store = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loading')
def loading():
    return render_template('loading.html')

@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data_store['original'] = request.form['original'].upper()
    data_store['mutated'] = request.form['mutated'].upper()
    return render_template('dashboard.html')

@app.route('/mutation')
def mutation_page():
    original = data_store.get("original", "")
    mutated = data_store.get("mutated", "")

    highlighted = ""
    count = 0
    for i in range(min(len(original), len(mutated))):
        if original[i] != mutated[i]:
            highlighted += f"<span class='highlight'>{mutated[i]}</span>"
            count += 1
        else:
            highlighted += mutated[i]

    return render_template("mutation.html", original=original, mutated=mutated, result=highlighted, count=count)

@app.route('/protein')
def protein_page():
    codon_table = {
        "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
        "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
        "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",
        "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R",
        "CTA": "L", "CTC": "L", "CTG": "L", "CTT": "L",
        "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
        "CAC": "H", "CAT": "H", "CAA": "Q", "CAG": "Q",
        "CGA": "R", "CGC": "R", "CGG": "R", "CGT": "R",
        "GTA": "V", "GTC": "V", "GTG": "V", "GTT": "V",
        "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",
        "GAC": "D", "GAT": "D", "GAA": "E", "GAG": "E",
        "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",
        "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
        "TTC": "F", "TTT": "F", "TTA": "L", "TTG": "L",
        "TAC": "Y", "TAT": "Y", "TAA": "", "TAG": "", "TGA": ""
    }

    mutated = data_store.get("mutated", "")
    codons = []
    amino_acids = []

    for i in range(0, len(mutated), 3):
        codon = mutated[i:i+3]
        if len(codon) == 3:
            codons.append(codon)
            amino_acids.append(codon_table.get(codon, "-"))

    return render_template("protein.html", codons=codons, amino_acids=amino_acids)

@app.route('/disease')
def disease_page():
    original = data_store.get("original", "")
    mutated = data_store.get("mutated", "")

    try:
        with open('disease_data.json') as f:
            disease_list = json.load(f)
    except Exception as e:
        return f"<h2>Error loading disease data: {e}</h2>"

    matches = []

    for d in disease_list:
        pos = d.get("pos", 0) - 1

        if pos < 0 or pos >= len(original) or pos >= len(mutated):
            continue

        original_base = original[pos]
        mutated_base = mutated[pos]

        change = d.get("change", "")
        if ">" not in change:
            continue

        expected_from, expected_to = change.split(">")

        if original_base == expected_from and mutated_base == expected_to:
            matches.append({
                "gene": d.get("gene", "Unknown"),
                "pos": d.get("pos", "?"),
                "change": change,
                "disease": d.get("disease") or d.get("name", "Unknown")
            })

    return render_template("disease.html", matches=matches)

@app.route('/dashboard')
def dashboard_page():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)

