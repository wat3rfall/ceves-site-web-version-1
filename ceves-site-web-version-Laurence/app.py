from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/accueil")
@app.route("/accueil/accueil")
def home():
	return render_template("pages/accueil/accueil.html")

@app.route("/accueil/a_propos")
def a_propos():
	return render_template("pages/accueil/a_propos.html")

@app.route("/accueil/faq_fr")
def faq_fr():
	return render_template("pages/accueil/faq_fr.html")

@app.route("/actualites/actualites")
def actualites():
	return render_template("pages/actualites/actualites.html")

@app.route("/actualites/calendrier")
def calendrier():
	return render_template("pages/actualites/calendrier.html")

@app.route("/boite_a_outils")
@app.route("/boite_a_outils/boite_a_outils")
def boite_a_outils():
	return render_template("pages/boite_a_outils/boite_a_outils.html")

@app.route("/documents")
@app.route("/documents/documents")
def documents():
	return render_template("pages/documents/documents.html")

@app.route("/nous_contacter")
@app.route("/nous_contacter/contact_fr")
def contact_fr():
	return render_template("pages/nous_contacter/contact_fr.html")

@app.route("/simpliquer/entrer")
def entrer():
	return render_template("pages/simpliquer/entrer.html")

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=5000)