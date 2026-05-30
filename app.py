from src.exception import CustomException
from src.constant import *
from src.logger import logging
from src.pipeline.train_pipeline import TrainingPipeline
from src.pipeline.predict_pipeline import PredictionPipeline


import sys,os

from flask import Flask,render_template,jsonify,request,send_file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/train')
def tain_route():
    try:
        training_pipeline = TrainingPipeline()
        accuracy = training_pipeline.run_pipeline()*100
        return 'trainig completed'
    
    except Exception as e:
        raise CustomException(e,sys)
    


@app.route('/predict',methods=['POST','GET'])
def upload():
    try:
         if request.method=='POST':
              prediction_pipeline = PredictionPipeline(request)

              prediction_file_detail = prediction_pipeline.run_pipeline()

              logging.info('prediction completed.Downloading prediction files')

              return 'prediction completed.Downloading prediction files'
         
         else :
              pass

    except Exception as e:
        raise CustomException(e,sys)




if __name__=='__main__':
        app.run(host='0.0.0.0',port=5000,debug=True)