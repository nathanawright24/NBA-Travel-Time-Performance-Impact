# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:09:06 2024

@author: NAWri
"""

import pandas as pd
!pip install geopy
from geopy.distance import geodesic

# NBA cities and their approximate coordinates (latitude, longitude)
nba_cities = {
    "Atlanta": (33.7490, -84.3880),
    "Boston": (42.3601, -71.0589),
    "Brooklyn": (40.6782, -73.9442),
    "Charlotte": (35.2271, -80.8431),
    "Chicago": (41.8781, -87.6298),
    "Cleveland": (41.4993, -81.6944),
    "Dallas": (32.7767, -96.7970),
    "Denver": (39.7392, -104.9903),
    "Detroit": (42.3314, -83.0458),
    "Golden State": (37.8044, -122.2711),  # Oakland (near Chase Center in San Francisco)
    "Houston": (29.7604, -95.3698),
    "Indiana": (39.7684, -86.1581),
    "LA Clippers": (34.0522, -118.2437),
    "LA Lakers": (34.0522, -118.2437),
    "Memphis": (35.1495, -90.0490),
    "Miami": (25.7617, -80.1918),
    "Milwaukee": (43.0389, -87.9065),
    "Minnesota": (44.9778, -93.2650),
    "New Orleans": (29.9511, -90.0715),
    "New York": (40.7128, -74.0060),
    "Oklahoma City": (35.4676, -97.5164),
    "Orlando": (28.5383, -81.3792),
    "Philadelphia": (39.9526, -75.1652),
    "Phoenix": (33.4484, -112.0740),
    "Portland": (45.5152, -122.6784),
    "Sacramento": (38.5816, -121.4944),
    "San Antonio": (29.4241, -98.4936),
    "Toronto": (43.6510, -79.3470),
    "Utah": (40.7608, -111.8910),
    "Washington": (38.9072, -77.0369)
}

# Helper function to calculate flight time (approx. 500 mph = 805 km/h)
def flight_time(city1, city2):
    distance_km = geodesic(city1, city2).kilometers
    flight_time_hours = distance_km / 805  # assuming average flight speed
    return round(flight_time_hours * 60)  # convert to minutes

# Initialize a DataFrame to store flight times
city_names = list(nba_cities.keys())
flight_times = pd.DataFrame(index=city_names, columns=city_names)

# Calculate flight times between cities
for city1, coord1 in nba_cities.items():
    for city2, coord2 in nba_cities.items():
        if city1 == city2:
            flight_times.loc[city1, city2] = 0  # Same city
        elif (city1 == "New York" and city2 == "Brooklyn") or (city1 == "Brooklyn" and city2 == "New York"):
            flight_times.loc[city1, city2] = 0  # Set New York <-> Brooklyn travel time to 0
        elif (city1 == "LA Lakers" and city2 == "LA Clippers") or (city1 == "LA Clippers" and city2 == "LA Lakers"):
            flight_times.loc[city1, city2] = 0  # Set LA Lakers <-> LA Clippers travel time to 0
        else:
            flight_times.loc[city1, city2] = flight_time(coord1, coord2)

# Save DataFrame to file path as csv
flight_times.to_csv(r"C:\Users\NAWri\Documents\BGA\NBATravelTime\nba_flight_times.csv")

