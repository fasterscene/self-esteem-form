""" Ths is the main file for the form
The form breaks down into four parts to be recorded every few days or so
Nigredo: Repressed elements in your shadow, such as shame, heaviness and negative self-beliefs (black).
Albedo: Your habitual coping mechanisms against pain (white).
Citrinitas: The current blessings in your life in the present moment (yellow).
Rubedo: Your vision of what high self-esteem looks like, which allows you to manifest and attract confidence via conscious visualisation (red).


The form will save the data to CSV (dated)
Ths can then be retrieved and viewed in tabular format (answers given for each catagory)

The final stage will be to create a report on progress or what has changed. Possibly using an LLM to do the heavy lifting

"""

from flask import Flask
from flask import request
from flask import render_template
import csv
from datetime import date

host = '127.0.0.1'
port = '5000'
app = Flask(__name__)
mypath = "saved/log.csv"

@app.route('/')
def home():
    

    #print("got imagesArray")
    return render_template('initiate_form.html',mypath=mypath)

@app.route('/submit', methods=['POST'])
def submit():
    nigredo = request.form.get('nigredo_input') 
    albedo = request.form.get('albedo_input') 
    citrinitas = request.form.get('citrinitas_input') 
    rubedo = request.form.get('rubedo_input') 
    # Save the whole lot to CSV
    done = saveToCSV(nigredo,albedo,citrinitas,rubedo)
    return render_template('completed_form.html', nigredo=nigredo, albedo=albedo, citrinitas=citrinitas, rubedo=rubedo)

def saveToCSV(nigredo,albedo,citrinitas,rubedo):
    today = date.today().strftime("%B %d, %Y")
    with open(mypath, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([today, nigredo, albedo, citrinitas, rubedo])
    return "done"

    
if __name__=="__main__":
    app.run(debug=True, host=host,port=port)