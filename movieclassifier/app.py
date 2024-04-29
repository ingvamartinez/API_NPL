"""Librerias"""
import pickle
import sqlite3
import os
from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import numpy as np
from vectorizer import vect

app = Flask(__name__)

#Preparamos el Clasificador

cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir,'pkl_objects','classifier.pkl'),'rb'))
db = os.path.join(cur_dir,'reviews.sqlite')

def classify(document):
    """
    Cargamos el modelo Clasificador
    """
    label = {0:'Negative', 1:'Positive'}
    X = vect.transform([document])
    y = clf.predict(X)[0]
    proba = np.max(clf.predict_proba(X))
    return label[y], proba

def train(document, y):
    """
    Entrenamos el modelo
    """
    X = vect.transform([document])
    clf.partial_fit(X,[y])

def sql_entry(path, document, y):
    """
    Insertamos los nuevos datos en la base de datos
    """
    conn=sqlite3.connect(path)
    c=conn.cursor()
    c.execute("INSERT INTO review_db (review,sentiment,date)"\
              " VALUES(?, ?, DATETIME('now'))",(document,y))
    conn.commit()
    conn.close()

#######Flask

class ReviewForm(Form):
    """clase de validacion"""
    moviereview = TextAreaField('',[validators.DataRequired(),
                                    validators.length(min=15)])
    
@app.route('/')
def index():
    """revier del form"""
    form = ReviewForm(request.form)
    return render_template('reviewform.html',form=form)



@app.route('/results', methods=['POST'])
def results():
    """Se imprime los resultados del predictor"""
    form=ReviewForm(request.form)
    if request.method == 'POST' and form.validate():
        review=request.form['moviereview']
        y, proba =classify(review)
        return render_template('results.html', content=review,
                               prediction=y,
                               probability=round(proba*100,2))
    return render_template('reviewform.html', form=form)

@app.route('/thanks', methods=['POST'])
def feedback():
    """ 
    Funcion para el feedback de la prediccion 
    """
    feedback_user = request.form['feedback_button']
    review = request.form['review']
    prediction = request.form['prediction']

    inv_label = {'Negative':0,'Positive':1}
    y = inv_label[prediction]
    if feedback_user == 'Incorrect':
        y = int(not y)
        train(review,y)
        sql_entry(db,review,y)
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True)




