#!/usr/bin/python3

import requests
import click
from datetime import datetime
from tabulate import tabulate as tab

BR_CLASSES = ['AC_B', 'AC_S', 'F_CHAIR', 'F_SEAT', 'SNIGDHA', 'S_CHAIR', 'SHOVAN']
BR_API_TRAINS = 'https://www.esheba.cnsbd.com/v1/trains'
BR_API_SEATS = 'https://www.esheba.cnsbd.com/v1/seat-availability'
BR_API_FROM_STATIONS = 'https://www.esheba.cnsbd.com/v1/from-stations'
BR_API_TO_STATIONS = 'https://www.esheba.cnsbd.com/v1/to-stations'

@click.group()
def app():
    pass

@app.command(help='Search for trains')
@click.option('--from', '-f', 'src', type=str, required=True)
@click.option('--to', '-t', 'dest', type=str, required=True)
@click.option('--date', '-d', 'date', type=str, default=datetime.now().strftime('%Y-%m-%d'))
@click.option('--adult', '-a', 'adult', type=int, default=1)
@click.option('--child', '-c', 'child', type=int, default=0)
@click.option('--class', '-cs', 'class_', type=click.Choice(BR_CLASSES), default='S_CHAIR')
def search(src, dest, date, adult, child, class_):
    params = (
        ('journey_date', date),
        ('from_station', src),
        ('to_station', dest),
        ('class', class_),
        ('adult', adult),
        ('child', child),
    )
    response = requests.get(BR_API_TRAINS, params=params)
    data = []
    headers = ['Train #', 'Train Name', 'Departure Time', 'Duration', 'Train Left']
    for train in response.json():
        data.append([
            train['trn_no'],
            train['trn_name'],
            train['dpt_time'],
            train['duration'],
            train['isTrainLeft']
        ])
    print(tab(data, headers=headers))

@app.command(help='Show available seats')
@click.option('--train', '-n', 'train', type=int, required=True)
@click.option('--from', '-f', 'src', type=str, required=True)
@click.option('--to', '-t', 'dest', type=str, required=True)
@click.option('--date', '-d', 'date', type=str, default=datetime.now().strftime('%Y-%m-%d'))
def seats(train, src, dest, date):
    data = {
        'train_no': F"{train}.",
        'stn_from': src,
        'stn_to': dest,
        'journey_date': date
    }
    response = requests.post(BR_API_SEATS, json=data)
    data = []
    headers = ['Class', 'Fare (Adult)', 'Fare (Child)', 'Counter Seat', 'Mobile Seat']
    for seat in response.json()['DATA']:
        data.append([
            seat['CLASS'],
            seat['FARE'],
            seat['FARE_C'],
            seat['COUNTER_SEAT'],
            seat['MOBILE_SEAT']
        ])
    print(tab(data, headers=headers))

@app.command(help='Show from_stations codes')
def from_stations():
    response = requests.get(BR_API_FROM_STATIONS)
    stations = [[i['stn_code'], i['stn_name']] for i in response.json()]
    print(tab(stations, headers=['Code', 'Station Name']))
    
@app.command(help='Show to_stations codes')
@click.option('--to', '-t', 'dest', type=str, required=True)
def to_stations(dest):
    response = requests.get(F"{BR_API_TO_STATIONS}/{dest}")
    stations = [[i['stn_code'], i['dest']] for i in response.json()]
    print(tab(stations, headers=['Code', 'Destination Name']))
    
if __name__ == "__main__":
    app()
