import pandas as pd
from functions import get_start_end, count_frequency


df_trip = pd.read_csv('Trip_roads.csv')
# df_trip = f = open("Trip_roads.csv", "r")
df_trip = pd.DataFrame(data=df_trip, dtype=object)

df_subtrip = pd.read_csv('Subtrip_roads.csv')
df_subtrip = pd.DataFrame(data=df_subtrip, dtype=object)

df_trip["TripFrequency"] = 1
df_subtrip["SubtripFrequency"] = 1

df_trip_with_start_end = get_start_end(df_trip, "TripCities")
df_subtrip_with_start_end = get_start_end(df_subtrip, "SubtripCities")

df_trip_with_frequency = count_frequency(df_trip_with_start_end, "TripFrequency")
df_subtrip_with_frequency = count_frequency(df_subtrip_with_start_end, "SubtripFrequency")

df_trip_with_frequency = df_trip_with_frequency.drop(columns=["StartCity", "EndCity", "Unnamed: 0"])
df_subtrip_with_frequency = df_subtrip_with_frequency.drop(columns=["StartCity", "EndCity", "Unnamed: 0"])

df_trip_with_frequency.to_csv("trip_with_frequency.csv")
df_subtrip_with_frequency.to_csv("subtrip_with_frequency.csv")
