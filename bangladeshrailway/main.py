#!/usr/bin/python3

import requests
import click
from datetime import datetime
from tabulate import tabulate as tab

ETICKET_API = 'https://railspaapi.shohoz.com/v1.0/web'
ETICKET_API_SEARCH = ETICKET_API + '/search-route?from_city={src}&to_city={dest}'
ETICKET_API_BOOKINGS = ETICKET_API + '/bookings/search-trips-v2?from_city={src}&to_city={dest}&date_of_journey={date}&seat_class=S_CHAIR'
ETICKET_CLASSES = ['AC_B', 'AC_S', 'F_CHAIR', 'F_SEAT', 'SNIGDHA', 'S_CHAIR', 'SHOVAN']

@click.group()
def app():
    pass

@app.command(help='Search for trains')
@click.option('--from', '-f', 'src', type=str, required=True)
@click.option('--to', '-t', 'dest', type=str, required=True)
@click.option('--date', '-d', 'date', type=str, default=datetime.now().strftime('%d-%b-%Y'))
@click.option('--adult', '-a', 'adult', type=int, default=1)
@click.option('--child', '-c', 'child', type=int, default=0)
def search(src, dest, date, adult, child):
    response = requests.get(ETICKET_API_SEARCH.format(src=src, dest=dest)).json()
    
    if 'error' in response:
        click.echo(click.style(response, fg='red'))
        return
    
    if response['data'] == 'Route found':
        response = requests.get(
            ETICKET_API_BOOKINGS.format(
                src=src,
                dest=dest,
                date=date,
            )).json()
        
        if 'error' in response:
            click.echo(click.style(response, fg='red'))
            return
        
        data = []
        
        for train in response['data']['trains']:
            seats = []
            
            for seat_types in train['seat_types']:
                seat_counts = seat_types['seat_counts']
                seats.append(f"{seat_types['type']} ({seat_counts['online']})")
            
            data.append([
                train['trip_number'],
                train['departure_date_time'],
                train['travel_time'],
                '\n'.join(seats)
            ])
            
        headers = ['Train Name', 'Departure Time', 'Duration', 'Seat Type', 'Seats']
        print(tab(data, headers=headers))

if __name__ == "__main__":
    app()
