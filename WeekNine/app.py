#import python dependcies 
import datetime as dt
from sqlite3 import TimestampFromTicks 
import numpy as np 
import pandas as pd 

#import SQLAlchemy dependencies 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session 
from sqlalchemy import create_engine, func

#import flask dependencies 
from flask import Flask, jsonify 

#create engine 
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect database into classes 
Base = automap_base() 
#reflect tables 
Base.prepare(engine, reflect=True)

#reference tables 
Measurement = Base.classes.measurement
Station = Base.classes.station 

#create session link 
session = Session(engine)

#create Flask app 
app = Flask(__name__)

#define routes
@app.route("/")

#welcome route
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API! 
    Available Routes: 
    /api/v1.0/precipitation\n
    /api/v1.0/stations\n
    /api/v1.0/tobs\n
    /api/v1.0/temp/start/end\n
    ''')
# /api/v1.0/ is used to identify that this is v1.0 of 
# the application - this can be updated to support 
# future versions if needed

#RUN FROM ANACONDA POWERSHELL
#NAVIGATE TO DIRECTORY  
# set FLASK_APP=<filename.py>
# flask run 

#set up precipitation route
@app.route("/api/v1.0/precipitation")

#define precipitation function 
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
# jsonify() can be used to format results into a JSON 
# structured file. 
# 127.0.0.1:5000/api/v1.0/precipitation

#set up stations route
@app.route("/api/v1.0/stations")

#define stations function 
def stations(): 
    results = session.query(Station.station).all() 
    #unravel into an array 
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
    #formats list into JSON 

#setup temperature route
@app.route("/api/v1.0/tobs")

#define temp_monthly function 
def temp_monthly(): 
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

#set up statistics route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

#define statistics function 
def stats(start=None, end=None): 
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end: 
        results = session.query(*sel).\
            filter(Measurement.date >= start).all() 
        temps = list(np.ravel(results))
        return jsonify(temps=temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps) 


