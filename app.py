from flask import Flask, render_template, url_for, request
import os, joblib


# Vectorizado
news_vectorizer = open(os.path.join("static/models/vectorizer.pkl"),"rb")
news_cv = joblib.load(news_vectorizer)


app = Flask(__name__)

def get_keys(val,my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/clasificar', methods=['GET','POST'])
def clasificar():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        modelchoice = request.form['modelchoice']
        vectorized_text=news_cv.transform([rawtext]).toarray()
        if modelchoice == 'svc':
            news_svc_model = open(os.path.join("static/models/SVC_model.pkl"),"rb")
            news_clf = joblib.load(news_svc_model)

        if modelchoice == 'nb':
            news_nb_model = open(os.path.join("static/models/NB_model.pkl"),"rb")
            news_clf = joblib.load(news_nb_model)  
    
        if modelchoice == 'logit':
            news_log_model = open(os.path.join("static/models/LOG_model.pkl"),"rb")
            news_clf = joblib.load(news_log_model)   

        if modelchoice == 'rf':
            news_rf_model = open(os.path.join("static/models/RF_model.pkl"),"rb")
            news_clf = joblib.load(news_rf_model)    
    
        # Prediction
        prediction_labels = {"Tecnología":0, "Entrenenimiento":1, "Deportes":2, "Salud":3, "Medio ambiente":4, "Política":5, "Ciencia":6}
        prediction = news_clf.predict(vectorized_text)
        final_result = get_keys(prediction,prediction_labels)
    
    return render_template("index.html", rawtext= rawtext.upper(), final_result=final_result)

if __name__ == '__main__':
    app.run(debug=False)