import requests
from collections import defaultdict
from itertools import permutations

BASE_URL = "http://localhost:5001"
home    = "123 Main St"
resorts = ["Whistler", "Sun Peaks", "Big White"]

# Step 1 — name → place_id
def get_ids():
    ids = {}
    for name in [home] + resorts:
        r = requests.get(f'{BASE_URL}/places', params={'name': name})
        ids[name] = r.json()['place_id']
    return ids

# Step 2 — NxN time matrix
def get_times(ids):
    times = defaultdict(dict)
    for name_a, id_a in ids.items():
        for name_b, id_b in ids.items():
            r = requests.get(f'{BASE_URL}/routes', params={'from': id_a, 'to': id_b})
            times[name_a][name_b] = r.json()['duration_minutes']
    return times

# Step 3a — brute force O(n!)
def best_brute(times):
    best_time = float('inf')
    best_path = None
    for perm in permutations(resorts):
        path = [home] + list(perm) + [home]
        total = sum(times[path[i]][path[i+1]] for i in range(len(path)-1))
        if total < best_time:
            best_time = total
            best_path = path
    return best_path, best_time

# Step 3b — greedy nearest neighbor O(n²)
def best_greedy(times):
    unvisited = set(resorts)
    path = [home]
    current = home
    total = 0
    while unvisited:
        nearest = min(unvisited, key=lambda r: times[current][r])
        total += times[current][nearest]
        path.append(nearest)
        unvisited.remove(nearest)
        current = nearest
    total += times[current][home]
    path.append(home)
    return path, total

ids   = get_ids()
times = get_times(ids)

path, total = best_brute(times)
print(f"Brute:  {' → '.join(path)} ({total} min)")

path, total = best_greedy(times)
print(f"Greedy: {' → '.join(path)} ({total} min)")
