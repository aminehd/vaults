from collections import defaultdict
from datetime import datetime
import json
import pprint
import pandas as pd
import os

# ─────────────────────────────────────────────
# Sample Data
# ─────────────────────────────────────────────

parties = [
    {"party_id": "p1", "start_timestamp": "2024-01-01T08:00", "end_timestamp": "2024-01-01T14:00"},
    {"party_id": "p2", "start_timestamp": "2024-01-01T10:00", "end_timestamp": "2024-01-01T12:00"},
    {"party_id": "p3", "start_timestamp": "2024-01-01T18:00", "end_timestamp": "2024-01-01T23:00"},
]

geo = [
    {"party_id": "p1", "neighborhood_name": "downtown", "city": "NYC", "state": "NY"},
    {"party_id": "p2", "neighborhood_name": "midtown",  "city": "NYC", "state": "NY"},
    {"party_id": "p3", "neighborhood_name": "uptown",   "city": "NYC", "state": "NY"},
]

# ─────────────────────────────────────────────
# Part 1: Party Window per Neighborhood
# ─────────────────────────────────────────────
# TODO: return {neighborhood: (earliest_start, latest_end)}
# ─────────────────────────────────────────────
# Part 2: Dead Zone per Town (sweep line)
# ─────────────────────────────────────────────
# TODO: return {town: total_dead_hours}
# ─────────────────────────────────────────────
# Part 3: Load from JSON files and run tests
# ─────────────────────────────────────────────
# TODO: load test_data/party_times/*.json and assert results



def party_window(parties, geo):
    
    party_map = {p['party_id']: p for p in parties}
    res = defaultdict(lambda:[ float('inf'), -float('inf')])
    pprint.pprint(party_map)
    for party in geo:
        hood = party['neighborhood_name']
        party_id = party['party_id']

        start_time = datetime.fromisoformat( party_map[party_id]['start_timestamp'] ).hour
        end_time = datetime.fromisoformat(party_map[party_id]['end_timestamp']).hour

        res[hood][0] = min(res[hood][0], start_time)
        res[hood][1] = max(res[hood][0] , end_time)
    return res

def party_window_pandas(parties, geo):
    parties = pd.DataFrame(parties)
    geo_df = pd.DataFrame(geo)
    
    df = parties.merge(geo_df, on="party_id")
    df["start"] = df["start_timestamp"].apply(lambda x: datetime.fromisoformat(x).hour)
    df["end_time"] = df["end_timestamp"].apply(lambda x:datetime.fromisoformat(x).hour)
    hoods = df["neighborhood_name"]
    # df.groupby("neighborhood_name").agg(
    #     start = ("start", "min"),
    #     end = ("end_time", "max")
    #     )
    grouped = df.groupby('neighborhood_name')
    starts = grouped['start'].min().astype(int)
    ends = grouped['end_time'].max().astype(int)

    print(starts.index) 
    return {hood : (int( starts[hood] ), int( ends[hood] )) for hood in hoods}
# pprint.pprint(party_window_pandas(parties, geo))

def find_empty(parties, geo):
    parties = pd.DataFrame(parties)
    geo_df = pd.DataFrame(geo)
    df = parties.merge(geo_df, on='party_id')
    df['start'] = df['start_timestamp'].apply(lambda x: datetime.fromisoformat(x).hour)
    df['end'] = df['end_timestamp'].apply(lambda x: datetime.fromisoformat(x).hour)
    town_window = defaultdict(list)
    for _, row in df.iterrows():
        town_window[row["city"]].append((row['start'], +1))
        town_window[row[ "city" ]].append((row['end'], -1))
    for key,_ in town_window.items():
        town_window[key].sort()
    off_hours = {}    
    for town, events in town_window.items():
        dead_start = None
        num_parties = 0
        total_off = 0
        
        for hour, delta in events:
            if num_parties == 0 and dead_start is not None and delta == 1:
                total_off += hour -  dead_start
                dead_start = None
            num_parties += delta

            if num_parties == 0 and delta == -1:
                dead_start = hour
    
        off_hours[town] = total_off 
        
        
    return off_hours
    print(town_window)
    
        
        


pprint.pprint(find_empty(parties, geo))
parties = [
    {"party_id": 1, "start_timestamp": "2024-01-01T08:00:00", "end_timestamp": "2024-01-01T14:00:00"},
    {"party_id": 2, "start_timestamp": "2024-01-01T18:00:00", "end_timestamp": "2024-01-01T23:00:00"},
]
geo = [
    {"party_id": 1, "city": "Springfield"},
    {"party_id": 2, "city": "Springfield"},
]
assert find_empty(parties, geo) == {"Springfield": 4}  # gap 14→18 = 4hrs


test_dir = "test_data/party_times/"
def run_tests(test_dir):

    file_names = sorted( os.listdir(test_dir) )
    
    for name in file_names:
        with open(os.path.join(test_dir, name)) as f:
            test_i = json.load(f) 
        
        parties = test_i['parties']
        geos = test_i['geo']
        find_empty(parties, geo)

run_tests(test_dir)
    
