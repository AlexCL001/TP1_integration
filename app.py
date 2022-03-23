from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def accueil():
    # aller à la bd
    return render_template("Accueil.html")

@app.route('/Formulaire/')
def formulaire():
    return render_template("Formulaire.html")

@app.route('/Table/')
def table():
    return render_template("Table.html")

if __name__ == "__main__":
    app.run(debug=True)

# python app.py dans le terminal port 5000