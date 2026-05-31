from collections import defaultdict
from datetime import datetime

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

def computePartyWindow(parties, geo):
    """
    For each neighborhood, return (earliest_start_hour, latest_end_hour)
    across all its parties.
    """
    party_map = {p["party_id"]: p for p in parties}

    windows = defaultdict(lambda: [float("inf"), float("-inf")])

    for g in geo:
        p     = party_map[g["party_id"]]
        start = datetime.fromisoformat(p["start_timestamp"]).hour
        end   = datetime.fromisoformat(p["end_timestamp"]).hour
        hood  = g["neighborhood_name"]

        windows[hood][0] = min(windows[hood][0], start)
        windows[hood][1] = max(windows[hood][1], end)

    return {hood: tuple(w) for hood, w in windows.items()}

# ─────────────────────────────────────────────
# Part 2: Dead Zone per Town — Sweep Line
# ─────────────────────────────────────────────

def computeDeadTimes(party_windows, geo):
    """
    For each town (city), find total hours within the town's party window
    where NO neighborhood is active.

    Uses sweep line: events = [(time, +1 or -1)]
    active == 0 means dead zone.
    """
    # group neighborhoods by city
    town_hoods = defaultdict(list)
    for g in geo:
        town_hoods[g["city"]].append(g["neighborhood_name"])

    dead_times = {}

    for town, hoods in town_hoods.items():
        intervals = [party_windows[h] for h in hoods if h in party_windows]

        if not intervals:
            dead_times[town] = 0
            continue

        # build sweep line events
        events = []
        for start, end in intervals:
            events.append((start, +1))
            events.append((end,   -1))

        events.sort()

        active    = 0
        dead      = 0
        prev_time = None

        for time, delta in events:
            if active == 0 and prev_time is not None:
                dead += time - prev_time   # gap with no active parties

            active   += delta
            prev_time = time

        dead_times[town] = dead

    return dead_times

# ─────────────────────────────────────────────
# Run
# ─────────────────────────────────────────────

if __name__ == "__main__":
    windows = computePartyWindow(parties, geo)
    print("Party Windows:")
    for hood, (s, e) in windows.items():
        print(f"  {hood}: {s}:00 – {e}:00")

    print()

    dead = computeDeadTimes(windows, geo)
    print("Dead Zones:")
    for town, hours in dead.items():
        print(f"  {town}: {hours} dead hours")

    # Expected:
    # downtown: 8–14, midtown: 10–12, uptown: 18–23
    # merged: (8,14), (18,23)  →  dead = 18 - 14 = 4 hours
