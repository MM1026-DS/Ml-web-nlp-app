from flask import Flask,render_template
import pickle
from flask import request

filename = 'model.pkl'
classifier = pickle.load(open(filename, 'rb'))
cv = pickle.load(open('cv-transform.pkl','rb'))

app = Flask(__name__)


@app.route("/")
def hotel():
    return render_template("hotel.html")



@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
    	message = request.form['message']
    	data = [message]
    	vect = cv.transform(data).toarray()
    	my_prediction = classifier.predict(vect)
    	return render_template('result.html', prediction=my_prediction)


if __name__=="__main__":
    app.run()