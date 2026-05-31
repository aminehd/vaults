# =============================================================================
# TRAVEL OPTIMIZATION — Scale AI Backend Practical
# =============================================================================
#
# BACKGROUND (from real Scale AI interview):
#   You are given a home address and a list of resort names.
#   You must find the optimal driving route that starts at home,
#   visits every resort exactly once, and returns home —
#   minimizing total driving time.
#
# STEP 1 — Convert names to place IDs:
#   For each location (home + all resorts), call:
#     GET http://localhost:5001/places?name=<name>
#     → { "place_id": "pid_whistler" }
#
# STEP 2 — Get driving time between every pair of locations:
#     GET http://localhost:5001/routes?from=<place_id>&to=<place_id>
#     → { "duration_minutes": 45 }
#   Build an NxN matrix (or dict of dicts) of all pairwise times.
#
# STEP 3 — Find the optimal route:
#   - Start and end at home
#   - Visit every resort exactly once
#   - Minimize total driving time
#   - For small N: try all permutations (brute force is fine)
#   - Return the ordered list of location names + total time
#
# EXAMPLE INPUT:
#   home    = "123 Main St"
#   resorts = ["Whistler", "Sun Peaks", "Big White"]
#
# EXAMPLE OUTPUT:
#   Best route: Home → Whistler → Big White → Sun Peaks → Home
#   Total time: 143 minutes
#
# FOLLOW-UP QUESTIONS they may ask:
#   1. What if there are 20 resorts? (brute force is O(n!) — use greedy nearest neighbor)
#   2. How do you handle API rate limits? (batch requests, retry with backoff)
#   3. What if the API is slow? (parallelize with ThreadPoolExecutor)
#   4. How would you cache place IDs you've already looked up?
#
# =============================================================================

from collections import defaultdict
import heapq
import requests
from itertools import permutations
import pprint
from typing import List

BASE_URL = "http://localhost:5001"

home    = "123 Main St"
resorts = ["Whistler", "Sun Peaks", "Big White"]

# TODO: Step 1 — get place IDs

def get_ids():
    home_id = None
    resort_ids = []

    home_response = requests.get(f'{BASE_URL}/places', params={'name': home})
    home_response = home_response.json() 
    home_id = home_response.get('place_id', None)
    for resort_name in resorts:
        response = requests.get(f'{BASE_URL}/places', params={'name': resort_name})
        resort_ids.append(response.json().get('place_id', ''))

    
    location_id = {k: v for (k,v) in zip(resorts, resort_ids)}
    location_id[home] = home_id
    return location_id 

# TODO: Step 2 — build driving time matrix
def get_times(location_id):
    time_matrix = defaultdict(dict)
    
    for name_x, id_x in location_id.items():

        for name_y, id_y in location_id.items():
            response = requests.get(f'{BASE_URL}/routes', params={'from': id_x, 'to': id_y})
            time_diff = response.json().get('duration_minutes','')
            time_matrix[name_x][name_y] = time_diff
            time_matrix[name_y][name_x] = time_diff
    
    
    return time_matrix


# TODO: Step 3 — find optimal route (try all permutations of resorts)
def best_rout_brute(time_mat):
    best_time = float('inf')
    best_path = None

    for perm in permutations( resorts ):
        path = [home] + list( perm ) + [home]


        path_time = sum( time_mat[path[i]][path[i-1]] for i in range(1, len(path)))
        if best_time > path_time:
            best_path = path
        best_time = min(best_time, path_time)
        
    return best_path

def best_route(time_mat):
    start = home
    
    
    q = [(time_mat[home][x], x) for x in resorts] 
    heapq.heapify(q)
    path = [home]
    while q: 
        dist, near = heapq.heappop(q)
        path.append(near)
    before_home = path[-1]
    path += [home]
    return path

location_to_id = get_ids()
times = get_times(location_to_id)
# best_path = best_rout_brute(times)
best_path = best_route(times)
pprint.pprint(best_path)

