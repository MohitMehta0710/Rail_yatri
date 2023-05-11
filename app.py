from flask import Flask,jsonify
from station_status import station_data
from bike_status import bike_data

app = Flask(__name__)

@app.route('/total_docks_available', methods=['GET'])

def total_docks_avl():
    data=station_data.get('data')
    data=data.get("stations")
    num_docks_available=0
    for i in data:
        num_docks_avail_found=i.get("num_docks_available")
        num_docks_available=num_docks_available + int(num_docks_avail_found)


    return jsonify({"Total_docks_available":num_docks_available})


@app.route('/total_bikes_available',methods=['GET'])
def total_bikes_avl():
    data=station_data.get('data')
    data=data.get("stations")
    num_bikes_available=0
    for i in data:
        num_bikes_avail_found=i.get("num_bikes_available")
        num_bikes_available=num_bikes_available + int(num_bikes_avail_found)

    return jsonify({"Total_bikes_available": num_bikes_available})

@app.route('/total_station_active', methods=['GET'])
def total_station_act():
    data=station_data.get('data')
    data=data.get("stations")
    num_stations_active=0
    for i in data:
        station_status=i.get("station_status")
        if station_status=="active":
            num_stations_active=num_stations_active+1

    return jsonify({"Total_station_active": num_stations_active})


@app.route('/total_bikes_reserved', methods=['GET'])
def bike_status():
    data=bike_data.get('data')
    data=data.get('bikes')
    total_bikes_reserved=0
    for i in data:
        reserved_bike_found=i.get("is_reserved")
        total_bikes_reserved=total_bikes_reserved+int(reserved_bike_found)

    return jsonify({"Total_bikes_reserved": total_bikes_reserved})

if __name__ == '__main__':
    app.run(debug = False,port= 5002) 

