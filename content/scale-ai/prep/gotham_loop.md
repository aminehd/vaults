# Scale AI – Gotham Loop Questions

> Sorted by popularity (10 = most common). ✅ = added to practice app.

---

## Full Question List

| Rank | Question | Score | Tags | App |
|------|----------|-------|------|-----|
| 1 | Party Times | 10/10 | `#coding` `#phone` | ✅ Day 2 |
| 2 | Backend Practical Questions | 5/10 | `#coding` `#onsite` | ✅ Day 3, 11 |
| 3 | Poker Hand | 3/10 | `#coding` `#phone` | ✅ Day 4 |
| 4 | Debugging Round | 2/10 | `#coding` `#onsite` | — design |
| 5 | System Design Question List | 2/10 | `#design` `#onsite` | — design |
| 6 | Another Card Game | 1/10 | `#coding` `#onsite` `#ood` `#phone` | ✅ Day 12 |
| 7 | Neuron States | 1/10 | `#coding` `#onsite` `#phone` | ✅ Day 9 |
| 8 | Node Distance | 1/10 | `#coding` `#onsite` `#phone` | ✅ Day 10 |
| 9 | Survival Card Game | 1/10 | `#coding` `#ood` `#phone` | ✅ Day 13 |
| 10 | Implement a Card Game | TBD | `#coding` `#onsite` | ✅ Day 12 |
| — | Task System Simulation | TBD | `#coding` `#phone` | ✅ Day 15 |
| — | Async Job Status Tracker | 5/10 | `#coding` `#onsite` | ✅ Day 8 |
| — | Crowdsourced Data Dedup | 5/10 | `#coding` `#onsite` | ✅ Day 14 |
| — | LLM Batching (System Design) | — | `#design` `#onsite` | ✅ Day 5 |
| — | Task Scheduler | — | `#coding` `#phone` | ✅ Day 1 |
| — | Kth Largest / Add Two Numbers | — | `#coding` `#phone` | ✅ Day 7 |
| — | My Calendar Three | — | `#coding` `#phone` | ✅ Day 6 |
| — | Google Maps API Practical | — | `#coding` `#onsite` | ✅ Day 11 |

---

## All Questions

### Another Card Game
`#coding` `#onsite` `#ood` `#phone` · **Rare · 1/10**

Generate a deck of 52 cards with 13 ranks in each of the four suits: clubs (♣), diamonds (♦), hearts (♥), spades (♠). Then implement two functions: a `draw` function and a `shuffle` function. After that, create 2 Players/Hands where each player draws 5 cards from the deck. The two players then compare their highest cards — whoever has the higher card wins. If they are equal, it's a tie.

---

### Backend Practical Questions
`#coding` `#onsite` · **Common · 5/10**

#### Google Maps API

**Part 1: Fetch Top 20 Restaurants in a Rectangular Area**

Using the Google Maps Places API, write a function that retrieves the top 20 restaurants within a specified rectangular bounding box. The function should accept two lat/lng pairs defining the bounding box and return a list of restaurants sorted by rating.

**Part 2: Filter by Cuisine Type & Price Summary**

Extend your solution to allow filtering by cuisine type (e.g., "Mexican," "Italian," "Japanese") and compute the average price level for each cuisine type. Google's price levels range from 0 (Free) to 4 (Very Expensive).

```python
fetch_top_restaurants(
    bounds=((37.7749, -122.4194), (37.8049, -122.3894)),
    cuisine_types=["Mexican", "Italian", "Japanese"]
)
# Output:
# {
#   "Mexican": {"count": 5, "avg_price_level": 2.4},
#   "Italian": {"count": 6, "avg_price_level": 3.0},
#   "Japanese": {"count": 4, "avg_price_level": 2.8}
# }
```

**Follow-Up Questions:**
1. How would you handle API rate limits efficiently?
2. What if the API doesn't provide a "cuisine" field directly? How could you infer it?
3. How would you modify the function to work in a paginated manner for large areas?

#### LLM API

Two CSV files: one for Tasks, one for Users.
- **Step 1:** Read the files and dump the data into a JSON file.
- **Step 2:** Call an LLM API to classify a specific column from the data, then write the classification results back into the JSON file.

#### Places API

- **(1)** Use the Google Places API to convert resort names and a home address into place IDs.
- **(2)** Use the Routes API to determine driving time between each pair of locations, then find the optimal route to minimize total travel time.

**Solution pattern:**

```python
# Step 1 — get place IDs
response = requests.get(f'{BASE_URL}/places', params={'name': name})
place_id = response.json()['place_id']

# Step 2 — build time matrix (dict of dicts)
time_mat = defaultdict(dict)
for name_x, id_x in location_ids.items():
    for name_y, id_y in location_ids.items():
        r = requests.get(f'{BASE_URL}/routes', params={'from': id_x, 'to': id_y})
        time_mat[name_x][name_y] = r.json()['duration_minutes']

# Step 3 — brute force (small N)
for perm in permutations(resorts):
    path = [home] + list(perm) + [home]
    path_time = sum(time_mat[path[i]][path[i+1]] for i in range(len(path)-1))
    if path_time < best_time:
        best_time = path_time
        best_path = path

# Step 3 — greedy nearest neighbor (large N, O(n²))
unvisited = set(resorts)
current = home
while unvisited:
    nearest = min(unvisited, key=lambda r: time_mat[current][r])
    path.append(nearest)
    unvisited.remove(nearest)
    current = nearest
```

**Gotchas:**
- `params={'name', value}` — set not dict, crashes; use `{'name': value}` with colon
- `perm` is a tuple — `[home] + perm + [home]` crashes; use `list(perm)`
- `path[i][path[i-1]]` with `range(1, len)` — symmetric matrix hides the bug but wrong pattern; use `path[i][path[i+1]]` with `range(len-1)`
- `response.json()` crashes with `JSONDecodeError` if URL has a typo — check spelling of endpoint

**Follow-ups:**
- Large N → greedy O(n²), not brute force O(n!)
- Slow API → `ThreadPoolExecutor` to parallelize requests
- Rate limits → retry with backoff, batch requests

---

### Debugging Round
`#coding` `#onsite` · **Rare · 2/10**

Background: A student course selection management system. Given multiple Python files and CSV files, the code reads the CSVs and finds students meeting course selection criteria. Some functions are pre-marked as correct.

**Test 1/3: Simple Projects Assignment**

Assign all contributors to simple projects only (no required prereq courses).
- Each contributor can only be assigned to one project.
- Projects have a headcount limit that must not be exceeded.
- Contributors assigned in the order they appear (first come, first served).
- Projects processed in descending priority order (higher number = higher priority).

Expected output format:
```json
{ "project_assignments": { "Tangerine Jubilant": [...], "Galaxy Velvet": [...] } }
```

**Test 2/3: All Projects Assignment**

Assign contributors across all projects, including those with required prereqs.
- A contributor can only join a project if they've completed all required courses.
- Each contributor can only join one project.
- Projects must not exceed their headcount.
- Projects handled in descending priority order, contributors in fixed input order.

**Test 3/3: Most Needed Course**

Find the most needed course — if all contributors were assumed to have completed this course, it would allow the maximum number of projects to be filled with the maximum number of contributors. Return the course name (e.g. `'Native Thai Conversation'`).

---

### ✅ Implement a Card Game
`#coding` `#onsite` · **TBD**

Given a pre-set code structure (Card, Hand classes), uses Python `enum`. Need to sort and calculate max.

**Part 1: Play a Trick**

1. A selected player plays a random card — this is the starter (sets the suit).
2. Every following player plays a card of the same suit as the starter.
3. If a player has no cards of the starter's suit, they may play any card.
4. Print: `"Player {X} played {Card}"` for each player.
5. The winner is the player who played the highest rank card of the starter's suit.
6. Print the winner's name. The winner starts the next trick.
7. Repeat until all players have no cards left.

**Part 2: Full Game (13 Rounds)**

- Any player can start a round; the starting player sets the suit.
- All players must follow suit if possible; otherwise play any card.
- The player with the highest rank of the starter's suit wins the round.
- There should be 13 rounds total.

**Part 3: Scoring (Fish Points)**

Points per card played in a round:
- `5` → 5 fish points
- `10` → 10 fish points
- `K` → 10 fish points
- All other cards → 0 points

Requirements:
1. At the end of each round, print the number of points the winner took.
2. At the end of the game, print each player's total points.
3. Print the name of the player(s) with the highest total fish points.

---

#### Key Decisions

**How to derive methods from the problem statement:**
> Every noun → class. Every verb → method on that class.
- *"Every following player plays a card of the same suit"* → `player.play_card(led_suit)`
- *"A selected player plays a random card"* → `player.play_card(led_suit=None)`
- *"The winner starts the next trick"* → `self.lead_player = winner`

- `@dataclass` for `Card` and `Player` — no need to write `self.x = x` for each field
- `__post_init__` for computed fields (`value = ORDER.index(rank)`)
- `field(default_factory=list)` for mutable defaults in dataclass — never use `hand: List = []`
- `led_suit` is born inside `play_trick` from leader's card — not passed as argument
- `play_card(led_suit=None)` means leader, otherwise follow suit
- Fish points from ALL cards played, not just led suit cards

#### Solution

```python
from dataclasses import dataclass, field
from typing import List, Optional
import random

ORDER = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
SUITS = ['hearts', 'clubs', 'diamonds', 'spades']
FISH_POINTS = {'5': 5, '10': 10, 'K': 10}

@dataclass
class Card:
    rank: str
    suit: str
    def __post_init__(self):
        self.value = ORDER.index(self.rank)
    def __repr__(self):
        return f"{self.rank}{self.suit[0]}"

class Deck:
    def __init__(self):
        self.deck = [Card(r, s) for r in ORDER for s in SUITS]
        random.shuffle(self.deck)
    def draw(self):
        return self.deck.pop()

@dataclass
class Player:
    name: str
    hand: List[Card] = field(default_factory=list)
    score: int = 0

    def play_card(self, led_suit):
        if led_suit is None:
            card = self.hand[0]
        else:
            matching = [c for c in self.hand if c.suit == led_suit]
            card = matching[0] if matching else self.hand[0]
        self.hand.remove(card)
        return card

class Game:
    def __init__(self):
        deck = Deck()
        self.players = [Player(f'Player {i}') for i in range(4)]
        for player in self.players:
            player.hand = [deck.draw() for _ in range(13)]
        self.lead_player = self.players[0]

    def play_trick(self):
        played = []
        led_card = self.lead_player.play_card(led_suit=None)
        led_suit = led_card.suit
        played.append((self.lead_player, led_card))

        for player in self.players:
            if player == self.lead_player: continue
            card = player.play_card(led_suit)
            played.append((player, card))

        for player, card in played:
            print(f"{player.name} played {card}")

        # winner = highest card of led suit only
        led_plays = [(p, c) for p, c in played if c.suit == led_suit]
        winner, _ = max(led_plays, key=lambda x: x[1].value)

        # fish points from ALL cards played
        points = sum(FISH_POINTS.get(c.rank, 0) for _, c in played)
        winner.score += points
        self.lead_player = winner
        print(f"{winner.name} wins! +{points} pts")

    def play_game(self):
        for _ in range(13):
            self.play_trick()
        for p in self.players:
            print(f"{p.name}: {p.score} pts")
        top = max(self.players, key=lambda p: p.score)
        print(f"Winner: {top.name}")
```

#### Fish Points
```python
FISH_POINTS = {'5': 5, '10': 10, 'K': 10}
points = sum(FISH_POINTS.get(c.rank, 0) for _, c in played)
# .get(key, 0) → returns 0 if card not in dict
# sum over ALL played cards, not just led suit
```

#### Test-Driven Approach

```python
# 1. test play_card in isolation first
def test_player():
    p = Player('alice')
    p.hand = [Card('7','hearts'), Card('K','spades'), Card('2','hearts')]
    card = p.play_card('hearts')
    assert card.suit == 'hearts'     # followed suit
    assert len(p.hand) == 2          # card removed
    card = p.play_card('clubs')      # no clubs → plays anything
    assert len(p.hand) == 1

# 2. test play_trick with preset hands (no randomness)
def test_trick():
    game = Game()
    game.players[0].hand = [Card('Q', 'clubs')]
    game.players[1].hand = [Card('8', 'clubs')]
    game.players[2].hand = [Card('K', 'clubs')]   # K wins + 10pts
    game.players[3].hand = [Card('5', 'clubs')]   # 5pts
    game.play_trick()
    assert isinstance(game.lead_player, Player)   # type check first!
    assert game.lead_player == game.players[2]    # K wins
    assert game.players[2].score == 15            # K(10) + 5(5) = 15

# 3. test full game separately with fresh Game()
def test_full_game():
    game = Game()
    game.play_game()   # 13 rounds, no crashes
```

#### Common Mistakes

| Mistake | Wrong | Right |
|---|---|---|
| Mutable default in dataclass | `hand: List = []` → shared across instances | `hand: List = field(default_factory=list)` |
| `lead_player` set to tuple | `self.lead_player = played[0]` | `self.lead_player = played[0][0]` |
| Sort ascending, pick [0] as winner | `played.sort(); played[0]` = lowest | `max(played, key=...)` or `reverse=True; played[0]` |
| `assert a, b` | always True — checks truthiness of `a` | `assert a == b` |
| `isinstance(obj, instance)` | `isinstance(game.lead_player, game.players[2])` | `isinstance(game.lead_player, Player)` |
| Fish points only from led suit | filter then sum | sum from ALL `played` before filtering |
| `Tuple(Player, Card)` type hint | crashes — `Tuple()` is not a type | `Tuple[Player, Card]` or just remove hint |
| Test preset hands then call `play_game` | hands empty after trick 1 → crash | `play_game` needs fresh `Game()` with 13 cards each |

---

### Neuron States
`#coding` `#onsite` `#phone` · **Rare · 1/10**

Given a 2D matrix, convert it from its current state to the next state. Each number is a "neuron" — firing if > 0, not firing if 0.

Rules for next state:
- **Firing neuron (> 0):** set to `6` if exactly 3 neighbours are firing.
- **Non-firing neuron (= 0):** decrement by 2 (min 0) if 1 or 0 neighbours are firing.
- **Any neuron:** decrement by 1 (min 0) if more than 3 neighbours are firing.

Given `input_state`, return `next_state`.

---

### Node Distance
`#coding` `#onsite` `#phone` · **Rare · 1/10**

Given a tree represented as a dict and two nodes, find the shortest distance between them.

**Follow-ups:**
1. Given two sets `a=[a1,a2]` and `b=[b1,b2]`, find the shortest distance between any pair `(x, y)` where `x ∈ a` and `y ∈ b`.
2. Extend to arbitrary-length sets `a` and `b`.

---

### ✅ Party Times
`#coding` `#phone` · **Popular! · 10/10**

#### The Question

You run a mobile app called **Party Time** where people post about parties happening in their area. Users record when a party starts and ends, along with metadata. This is a two-part coding question.

**Part 1 — Compute Party Window**

Determine the party window for each neighborhood. A party window is the range from the **earliest party start** to the **latest party end** in that neighborhood.

Example: two parties at 10AM–1PM and 4PM–8PM → party window = 10AM–8PM.

Inputs:
- List of party info: `party_id`, `start_timestamp`, `end_timestamp`
- List of geo info: `neighborhood_name`, `city`, `state`, `party_id`

Output: `{ neighborhood_name: (start_hour, end_hour) }`

Assumptions:
- All timestamps are on the hour, in ISO datetime format
- All parties start and end on the same day
- Party windows are per neighborhood (earliest start → latest end)

**Part 2 — Compute Dead Zone Time**

A dead zone is a time range within a town's overall party window when **no neighborhood** in that town has an active party window.

Example:
- `neighborhood_a`: 8AM–2PM
- `neighborhood_b`: 6PM–11PM
- → dead zone = 2PM–6PM = **4 hours**

Output: `{ town: total_dead_zone_hours }`

Key rules:
- Only count gaps **between** party windows, not before the first or after the last
- If windows overlap, **merge them first** before computing gaps
- Example: `(3,8), (5,7), (10,13)` → merged: `(3,8), (10,13)` → deadzone = `10-8 = 2 hrs`

Follow-up: How would you design the architecture and testing strategy for production?

---

#### Solution — Plain Python (sweep line)

**Key ideas to remember:**
- Join two lists on `party_id` using a dict
- Parse ISO timestamp → hour: `datetime.fromisoformat(s).hour`
- Part 1: `min(start)` / `max(end)` per neighborhood
- Part 2: sweep line — events `(time, +1/-1)`, count `active`, gap when `active == 0`

```python
from collections import defaultdict
from datetime import datetime

# Part 1: earliest start → latest end per neighborhood
def computePartyWindow(parties, geo):
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

# Part 2: sweep line — find gaps where active == 0
def computeDeadTimes(party_windows, geo):
    town_hoods = defaultdict(list)
    for g in geo:
        town_hoods[g["city"]].append(g["neighborhood_name"])

    dead_times = {}
    for town, hoods in town_hoods.items():
        intervals = [party_windows[h] for h in hoods if h in party_windows]
        if not intervals:
            dead_times[town] = 0
            continue

        events = []
        for start, end in intervals:
            events.append((start, +1))
            events.append((end,   -1))
        events.sort()

        active, dead, prev_time = 0, 0, None
        for time, delta in events:
            if active == 0 and prev_time is not None:
                dead += time - prev_time      # gap = dead zone
            active   += delta
            prev_time = time

        dead_times[town] = dead
    return dead_times
```

---

#### Solution — Pandas

**Key ideas to remember:**

```python
# 1. list of dicts → DataFrame
df = pd.DataFrame(parties)           # each dict = one row, keys = columns

# 2. join two DataFrames
df = parties_df.merge(geo_df, on="party_id")   # like SQL JOIN on party_id

# 3. parse ISO string per row → new column
df["start"] = df["start_timestamp"].apply(lambda x: datetime.fromisoformat(x).hour)

# 4. groupby → GroupBy object (nothing computed yet)
grouped = df.groupby("neighborhood_name")      # type: DataFrameGroupBy

# 5. compute on a single column → Series (index = group keys)
starts = grouped["start"].min()                # type: Series  {hood: min_start}

# 6. np.int64 → plain Python int  (two ways)
starts = grouped["start"].min().astype(int)    # convert whole Series upfront
# OR at lookup time:
int(starts[hood])                              # convert one value

# 7. iterate over groups — use starts.index not the raw column (raw has duplicates)
return {hood: (int(starts[hood]), int(ends[hood])) for hood in starts.index}
```

```python
import pandas as pd
from datetime import datetime

def computePartyWindow_pandas(parties, geo):
    df = pd.DataFrame(geo).merge(pd.DataFrame(parties), on="party_id")
    df["start"] = df["start_timestamp"].apply(lambda x: datetime.fromisoformat(x).hour)
    df["end"]   = df["end_timestamp"].apply(lambda x: datetime.fromisoformat(x).hour)

    # Option A — one column at a time, returns a Series indexed by neighborhood
    starts = df.groupby("neighborhood_name")["start"].min().astype(int)  # np.int64 → Python int
    ends   = df.groupby("neighborhood_name")["end"].max().astype(int)
    return {hood: (starts[hood], ends[hood]) for hood in starts.index}

    # Option B — agg: both columns at once, returns a DataFrame
    result = df.groupby("neighborhood_name").agg(
        start=("start", "min"),   # new col "start" = min of "start"
        end=("end",   "max")    # new col "end"   = max of "end"
    )
    # result is a DataFrame indexed by neighborhood_name
    # result.loc["downtown"] → Row(start=8, end=14)
    return {hood: (row["start"], row["end"]) for hood, row in result.iterrows()}
```

**Return types:**
```
df.groupby("neighborhood_name")              → GroupBy object (no data yet)
df.groupby("neighborhood_name")["start"]     → SeriesGroupBy
df.groupby("neighborhood_name")["start"].min() → Series  (index=neighborhood, values=min)
df.groupby("neighborhood_name").agg(...)     → DataFrame (index=neighborhood, cols=your names)
```

# Part 2 — still plain Python sweep line (pandas has no native interval gap tool)

---

#### Mental model — sweep line

```
(8,14), (10,12), (18,23)

events: (8,+1),(10,+1),(12,-1),(14,-1),(18,+1),(23,-1)
sorted: 8  10  12  14  18  23

time=8:  active=0→1
time=10: active=1→2
time=12: active=2→1
time=14: active=1→0  ← prev_time=14
time=18: active=0, gap = 18-14 = 4 ✓  active→1
time=23: active=1→0

dead = 4 hours
```

**Run:** `python Coding/party_times.py`

---

#### Solution — Pandas Sweep Line (find_empty variant)

Groups by town, builds sweep line events per town, counts dead hours.

```python
import pandas as pd
from collections import defaultdict
from datetime import datetime

def find_empty(parties, geo):
    parties_df = pd.DataFrame(parties)   # list of dicts → DataFrame, keys become columns
    geo_df = pd.DataFrame(geo)
    df = parties_df.merge(geo_df, on='party_id')
    df['start'] = df['start_timestamp'].apply(lambda x: datetime.fromisoformat(x).hour)
    df['end'] = df['end_timestamp'].apply(lambda x: datetime.fromisoformat(x).hour)

    # aggregate events by town
    town_events = defaultdict(list)
    for _, row in df.iterrows():                    # iterrows() → (index, Series) pairs
        town_events[row['city']].append((row['start'], +1))
        town_events[row['city']].append((row['end'], -1))

    # sort: starts before ends at same hour
    for key in town_events:
        town_events[key].sort(key=lambda x: (x[0], -x[1]))

    # sweep line per town
    off_hours = {}
    for town, events in town_events.items():
        num_parties = 0
        dead_start = None
        total_off = 0

        for hour, delta in events:
            if delta == 1 and num_parties == 0 and dead_start is not None:
                total_off += hour - dead_start   # dead zone ends
                dead_start = None
            num_parties += delta
            if num_parties == 0:
                dead_start = hour                # dead zone starts

        off_hours[town] = total_off

    return off_hours
```

---

#### Common Mistakes

| Mistake | Wrong | Right |
|---|---|---|
| Iterate df rows | `for row in df` → gives column name strings | `for _, row in df.iterrows()` |
| Iterate df rows | `for _, row in df.items()` → gives `(col_name, Series)` | `for _, row in df.iterrows()` |
| Hardcoded dict key | `town_events["city"].append(...)` | `town_events[row["city"]].append(...)` |
| Iterate dict to index | `for k, _ in d.items(): d[k]` | `for k in d: d[k]` or `for k, v in d.items(): use v` |
| list of dicts → df | `pd.DataFrame(parties, columns=[...])` | `pd.DataFrame(parties)` — keys become columns automatically |
| Sort stability | `events.sort()` → ends before starts at same hour | `sort(key=lambda x: (x[0], -x[1]))` |
| Dead code | `return x; print(x)` | print before return |
| Open file by name only | `open(name)` inside `os.listdir` loop | `open(os.path.join(test_dir, name))` — listdir gives filenames, not full paths |

#### Loading JSON test files from a directory

```python
import json
import os

# single file — no function needed, with block closes file after load
with open('test_data/party_times/test_basic_gap.json') as f:
    test = json.load(f)                        # test is a plain dict

result = find_empty(test['parties'], test['geo'])
print(result == test['expected'])

# run all tests in a folder
test_dir = "test_data/party_times/"

def run_tests(test_dir):
    file_names = sorted(os.listdir(test_dir))  # listdir → filenames only, not full paths
    for name in file_names:
        with open(os.path.join(test_dir, name)) as f:  # join to get full path
            test_i = json.load(f)

        parties = test_i['parties']
        geo = test_i['geo']                    # bug: calling find_empty(parties, geo) not geo_s
        result = find_empty(parties, geo)
        expected = test_i['expected']
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}  {name}  →  {result}")

run_tests(test_dir)
```

**What you learned:**
- `os.listdir(dir)` → list of filenames only (not full paths) — need `os.path.join(dir, name)` to open
- `with open(...) as f: data = json.load(f)` — file closes automatically after the `with` block, rest of code is normal indent
- `json.load(f)` for files, `json.loads(s)` for strings
- `sorted(os.listdir(...))` to get consistent test ordering

#### Tests

```python
# 1. basic gap
parties = [
    {"party_id": 1, "start_timestamp": "2024-01-01T08:00:00", "end_timestamp": "2024-01-01T14:00:00"},
    {"party_id": 2, "start_timestamp": "2024-01-01T18:00:00", "end_timestamp": "2024-01-01T23:00:00"},
]
geo = [{"party_id": 1, "city": "Springfield"}, {"party_id": 2, "city": "Springfield"}]
assert find_empty(parties, geo) == {"Springfield": 4}  # gap 14→18 = 4hrs

# 2. overlapping — no dead zone
parties = [
    {"party_id": 1, "start_timestamp": "2024-01-01T08:00:00", "end_timestamp": "2024-01-01T14:00:00"},
    {"party_id": 2, "start_timestamp": "2024-01-01T10:00:00", "end_timestamp": "2024-01-01T18:00:00"},
]
geo = [{"party_id": 1, "city": "A"}, {"party_id": 2, "city": "A"}]
assert find_empty(parties, geo) == {"A": 0}

# 3. multiple gaps
# parties: 8-10, 12-14, 16-20 → gaps: 10→12 + 14→16 = 4hrs
assert find_empty(parties, geo) == {"A": 4}

# 4. back-to-back — no gap
# party ends at 14, next starts at 14 → dead zone = 0
assert find_empty(parties, geo) == {"A": 0}

# 5. single party — no gap possible
assert find_empty(parties, geo) == {"A": 0}
```

---

**Part 1: Compute Party Window**

A party window is the time range from the earliest party start to the latest party end in a neighborhood.

Given JSON party data, implement `computePartyWindow` — return a dict mapping each neighborhood to a `(start_hour, end_hour)` tuple.

Inputs:
- List of party info: `party_id`, `start_timestamp`, `end_timestamp`
- List of geo info per party: `neighborhood_name`, `city`, `state`, `party_id`

Assumptions:
- All timestamps are on the hour, in ISO datetime format.
- All parties start and end on the same day.
- Party windows are per neighborhood (earliest start → latest end).

**Part 2: Compute Dead Zone Time**

A dead zone is a time range within a town's overall party window when **no** neighborhood in that town has an active party window.

Implement `computeDeadTimes` — maps towns to total dead zone hours. Takes Part 1 output as input.

Example:
- `neighborhood_a`: 8AM–2PM, `neighborhood_b`: 6PM–11PM → dead zone = 4 hours (2PM–6PM)

Key rules:
- Only count gaps **between** party windows, not before the first or after the last.
- If windows overlap, merge them first before computing gaps.

```
(3,8), (5,7), (10,13) → merged: (3,8), (10,13) → deadzone = 10-8 = 2 hrs
```

**Follow-up:** How would you design the architecture and testing strategy for this in production?

---

### ✅ Poker Hand
`#coding` `#phone` · **Uncommon · 3/10**

Given a set of six poker hand rules (flush, straight, full house, four-of-a-kind, straight flush, royal flush), determine whether a given hand satisfies at least one rule.

**Follow-up 1:** Modify the approach to account for wildcards (Jokers) that can represent any card.

**Follow-up 2:** Given two players' hands and an ordering of the poker hand rules, compare the two hands.

**Follow-up 3 — Joker wildcard:**

A Joker can be any rank/suit. Key insight: **don't brute force — measure the gap.**

```python
def is_flush_with_joker(self):
    non_joker_suits = [s for s in self.suits if s != 'JOKER']
    return len(set(non_joker_suits)) == 1   # joker just matches the rest

def is_straight_with_joker(self):
    non_joker = sorted([ORDER.index(r) for r in self.ranks if r != 'JOKER'])
    jokers = self.ranks.count('JOKER')
    gaps = sum(non_joker[i+1] - non_joker[i] - 1 for i in range(len(non_joker)-1))
    return len(set(non_joker)) + jokers == 5 and gaps <= jokers
    # gaps = holes in the sequence, each joker fills one hole
    # e.g. [5,7,8,9] + 1 joker → gap=1 (5→7) → joker fills it → straight!
```

---

#### Solution

**Key ideas:**
- Use a class — primitives (`is_flush`, `is_straight`) are reused by combos (`is_straight_flush`, `is_royal_flush`)
- `__init__` precomputes everything: `rank_order` (sorted indices), `rank_count` (Counter), `suit_counts` (Counter)
- NEVER do `int(rank)` — J/Q/K/A crash. Use `ORDER.index(rank)` instead
- Consecutive 5 cards → `max - min == 4` (not 5)
- Never `.sort()` strings for ranks — `'10' < '2'` alphabetically

```python
from collections import Counter

ORDER = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class PokerHand:
    def __init__(self, hand):
        self.ranks = [card[0] for card in hand]
        self.suits = [card[1] for card in hand]
        self.rank_order = sorted([ORDER.index(r) for r in self.ranks])
        self.rank_count = Counter(self.rank_order)
        self.suit_counts = Counter(self.suits)

    def is_flush(self):
        return len(self.suit_counts) == 1

    def is_straight(self):
        return len(set(self.rank_order)) == 5 and self.rank_order[-1] - self.rank_order[0] == 4

    def is_straight_flush(self):
        return self.is_flush() and self.is_straight()

    def is_royal_flush(self):
        return self.is_flush() and set(self.ranks) == {'10', 'J', 'Q', 'K', 'A'}

    def is_four_of_kind(self):
        return 4 in self.rank_count.values()

    def is_full_house(self):
        return set(self.rank_count.values()) == {2, 3}
```

**Combo = primitive AND primitive — never rewrite the logic.**

#### Common Mistakes

| Mistake | Wrong | Right |
|---|---|---|
| Convert rank to int | `int('J')` → crashes | `ORDER.index('J')` → 9 |
| Consecutive check | `max - min == 5` | `max - min == 4` |
| Sort ranks as strings | `self.ranks.sort()` → `'10' < '2'` | `sorted([ORDER.index(r) for r in ranks])` |
| Flush check | `len(self.suit_counts.values()) == 1` | `len(self.suit_counts) == 1` (simpler) |
| Four of a kind | `4 in ... or 5 in ...` | just `4 in ...` (5-of-a-kind doesn't exist) |
| `rank_count` keys | `Counter(self.rank_order)` uses indices | fine, but `Counter(self.ranks)` uses strings — both work |

#### Interview testing strategy
Don't loop all samples. Test one true + one false per function:
```python
p = PokerHand(sample_full_house); print(p.is_full_house())  # True
p = PokerHand(sample_flush);      print(p.is_full_house())  # False
```

---

#### Amineh's Solution (with joker)

Key decisions:
- `rank_order` stores indices (ints), sorted
- `no_joker` filters out Jack index to simulate joker filtering (use `'JOKER'` string in prod)
- gap loop: iterate pairs, accumulate `gap += diff - 1`, return `False` on duplicate ranks

```python
ORDER = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

class PokerHand:
    def __init__(self, hand):
        self.hand = hand
        self.ranks = [card[0] for card in hand]
        self.suits = [card[1] for card in hand]
        self.rank_order = sorted([ORDER.index(x) for x in self.ranks])
        self.rank_count = Counter(self.rank_order)
        self.no_joker = [x for x in self.rank_order if ORDER[x] != 'JOKER']
        self.suit_counts = Counter(self.suits)

    def is_flush(self):
        return len(self.suit_counts) == 1

    def is_straight_with_joker(self):
        gap = 0
        for i in range(1, len(self.no_joker)):
            diff = self.no_joker[i] - self.no_joker[i-1]
            if diff == 0: return False          # duplicate rank → not a straight
            gap += diff - 1
        jokers = len(self.rank_order) - len(self.no_joker)
        return gap <= jokers

    def is_straight_flush(self):
        return self.is_flush() and self.is_straight_with_joker()

    def is_royal_flush(self):
        return self.is_flush() and set(self.ranks) == {'10','J','Q','K','A'}

    def is_four_of_kind(self):
        return 4 in self.rank_count.values()

    def is_full_house(self):
        return set(self.rank_count.values()) == {2, 3}
```

#### OOP-enhanced version (with Card class)

```python
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = ORDER.index(rank) if rank != 'JOKER' else -1
    def __repr__(self):
        return f"{self.rank}{self.suit[0]}"   # "Kh", "5s"

class PokerHand:
    def __init__(self, cards):
        self.cards = cards
        self.no_joker = sorted([c for c in cards if c.rank != 'JOKER'], key=lambda c: c.value)
        self.joker_count = sum(1 for c in cards if c.rank == 'JOKER')
        self.suit_counts = Counter(c.suit for c in cards)
        self.rank_count = Counter(c.value for c in self.no_joker)

    @property
    def values(self):
        return [c.value for c in self.no_joker]

    def is_flush(self):
        return len(self.suit_counts) == 1

    def is_straight_with_joker(self):
        v = self.values
        gap = sum(v[i+1] - v[i] - 1 for i in range(len(v)-1))
        return len(set(v)) + self.joker_count == 5 and gap <= self.joker_count

    def is_four_of_kind(self):
        return 4 in self.rank_count.values()

    def is_full_house(self):
        return set(self.rank_count.values()) == {2, 3}

    def check_hand(self):
        rules = [
            ('royal flush',    self.is_royal_flush),
            ('straight flush', self.is_straight_flush),
            ('four of a kind', self.is_four_of_kind),
            ('full house',     self.is_full_house),
            ('flush',          self.is_flush),
        ]
        return [name for name, fn in rules if fn()] or ['nothing']
```

#### Joker versions of four_of_kind and full_house

```python
def is_four_of_kind_with_joker(self):
    return max(self.rank_count.values(), default=0) + self.joker_count >= 4

def is_full_house_with_joker(self):
    counts = sorted(self.rank_count.values(), reverse=True)
    if not counts: return False
    jokers = self.joker_count
    if counts[0] + jokers < 3: return False
    jokers_used = max(0, 3 - counts[0])
    remaining = jokers - jokers_used
    second = counts[1] if len(counts) > 1 else 0
    return second + remaining >= 2
```

#### Recurring bugs to watch out for

| Bug | Wrong | Right |
|---|---|---|
| `Counter` sorted by keys not values | `sorted(Counter(x))` → sorts keys | `sorted(Counter(x).values())` |
| Joker count via rank_count | `self.rank_count['J']` or `self.rank_count[9]` | `self.joker_count` attribute |
| `counts[1]` IndexError when one group | `counts[1] + remaining >= 2` → crashes | `second = counts[1] if len(counts) > 1 else 0` |
| Mixing strings and indices | storing indices then checking `!= 'JOKER'` | keep strings everywhere, convert only at comparison |
| `int(rank)` on face cards | `int('J')` → ValueError | `ORDER.index('J')` → 9 |
| Consecutive check off by one | `max - min == 5` | `max - min == 4` |
| `.sort()` on strings | `'10' < '2'` alphabetically | `sorted([ORDER.index(r) for r in ranks])` |
| `Counter(x)` counts keys not occurrences | `Counter([1,1,2])` → `{1:2, 2:1}` ✓ but `sorted(Counter([1,1,2]))` → `[1, 2]` (keys!) | `.values()` to get counts |

---

### Survival Card Game
`#coding` `#ood` `#phone` · **Rare · 1/10**

A team of multiple players plays a card game with `player + 1` lives and up to `x` skips (given as input).

**Rules:**
- Each round, players draw cards and play in a fixed order.
- Each player's hand is always sorted ascending; they must play their smallest available card.
- A round is **lost** if any player's card is not strictly larger than the previous player's.
- On a lost round, the team can either:
  - Lose a life, or
  - Use a skip (players draw new cards and skip the round).
- The game runs for `Y` rounds total.
- Game over if all lives are lost before completing all rounds.

**Output:** Determine whether the team can survive all `Y` rounds. If the number of non-increasing sequences exceeds `skips + lives`, the team loses.

---

### System Design Question List
`#design` `#onsite` · **Rare · 2/10**

#### Model System

> **Confirmed real interview question (seen in screenshot)**

At Scale, ML models are trained in-house to classify content. The workflow has two parts:

1. **Embedding Generation** — vector representations of data (text or images). Given N files → N embeddings.
2. **Classification** — given N embeddings → N dictionaries of `{label: confidence_score}`. Labels from a taxonomy of M labels. Confidence score is normalized 0–1.

Both are **black-box services** that scale with multiple requests:
- **Black Box 1 — Embedding Generation:** Input: File(s) → Output: Embedding(s). Max **200 files** per request.
- **Black Box 2 — Classification:** Input: Embedding(s) → Output: Dictionary Result(s). Max **2000 embeddings** per request.

**Goal:** Build a production API system to surface these models to customers.

Requirements:
- Support **low-latency** (sub 1 second) AND **high-throughput** (1000 assets/second) modes — customer chooses
- Optimize costs as system owner
- Store model results and embeddings for future debugging and model analysis
- Use Zoom whiteboard or excalidraw.com

**Key design considerations:**
- BB1 max 200 files → batch input if customer sends more
- BB2 max 2000 embeddings → batch embeddings if needed
- Low-latency mode: call BBs inline, return synchronously
- High-throughput mode: async queue → worker pool → store results → notify
- Cost optimization: cache embeddings (same file = same embedding), batch aggressively
- Storage: embeddings + classification results in object store (S3) for analysis

---

#### Metered Billing System

Design a metered billing system.

---

#### LLM Input/Output

There is a black-box LLM (sync call). Design a system that:
1. Asynchronously receives user input.
2. Internally splits the input into hundreds of pieces and calls the LLM black box for each.
3. Sends the aggregated results back to the user via notification.

---

### Task System Simulation
`#coding` `#phone` · **TBD**

Each task goes through three sequential stages: **L0 → L1 → L2**. A task is complete when L2 is finished.

Simulate the environment and run until all tasks are completed.

**Rules:**
- 1:1 mapping between task stages and workers (one worker per stage at a time, that worker can't work on anything else simultaneously).
- A worker can only work on a task if they have **never worked on that task before**.
- Each worker takes 1 min per stage.
- Tasks are greedily assigned to any free eligible worker.
- On every timestamp where activity happens: print the timestamp and all assignments/completions.
- At the end, print total time taken.

**Sample Input 1:**
```
tasks = [Task('A')]
workers = [Worker('X'), Worker('Y'), Worker('Z')]
```
**Sample Output 1:**
```
0
Assigning X to Task A for L0
1
Worker X finished Task A for L0
Assigning Y to Task A for L1
2
Worker Y finished Task A for L1
Assigning Z to Task A for L2
3
Worker Z finished Task A for L2
Total time taken: 3 min
```

**Sample Input 2:**
```
tasks = [Task('A'), Task('B')]
workers = [Worker('X'), Worker('Y'), Worker('Z')]
```
**Sample Output 2 (one possible correct answer):**
```
0
Assigning X to Task A for L0
Assigning Y to Task B for L0
1
Worker X finished Task A for L0
Worker Y finished Task B for L0
Assigning Z to Task A for L1
Assigning X to Task B for L1
2
Worker Z finished Task A for L1
Worker X finished Task B for L1
Assigning Y to Task A for L2
Assigning Z to Task B for L2
3
Worker Y finished Task A for L2
Worker Z finished Task B for L2
Total time taken: 3 min
```

---

#### Task Scheduler — Practice Round Log (April 10, 2026 · 7:13–8:13 AM)

Track your reps here. Each round = one scratch attempt.

---

**Round 1 — Phase 1 only (~40 min)**

What you built in order:
1. `TaskScheduler` dataclass with `pending_heap` — got the `field(default_factory=list)` right immediately
2. `add_task` with `heappush(-priority, name, task)` — correct
3. `next_task` with `heappop` — initially peeked with `[0]` instead of popping (caught it)
4. `Status(Enum)` with P/I/C — added after the fact, should be first
5. `Task` dataclass with `status` field — added after the fact

What you missed / had to be reminded:
- `self` missing in `add_task` on first write
- `Status` and `Task` written AFTER `TaskScheduler` — write them top-down next time
- `Tuple(int, str)` → should be `Tuple[int, str]` (still not fixed at end of round)
- `add_task` didn't `return task` on first write
- Missing `complete_task` method entirely at end of round
- Missing `tasks: Dict[str, Task]` and `completed: set` on `TaskScheduler`
- `s2 = s.add_task(...)` → `s2` was `None` because `add_task` didn't return — assert silently passed wrong value

What you got right without prompting:
- `field(default_factory=list)` on first try
- `heappush(-priority, name, task)` negation correct
- `heappop` fix (after being told about `[0]`)
- `task.status = Status.I` in `next_task` — correct lifecycle instinct

**Target for Round 2:** Write top-down (Status → Task → TaskScheduler), finish Phase 1 in under 20 min including `complete_task`, then move to Phase 2 deps.

---

**Round 2 — Phase 1 complete + Phase 2 attempt (in progress)**

What you built in order:
1. Status → Task → TaskScheduler — top-down order, improved from Round 1
2. Phase 1 complete with `complete_task` — got `task_map`, `completed` set, lifecycle correct
3. Commented out `heappop`, switched to heap scan loop for dep logic — good instinct

What you missed / had to be reminded:
- `return Task` (capital T) — returned the class object, not the task instance; always lowercase
- `is_ready` on `Task` always returns `True` — `Task` has no access to `completed` set, can't check deps from inside the task
- `dep` arg not passed to `Task(...)` constructor — `Task(name=name, priority=priority)` ignored deps entirely
- `in_degree` not added to `Task` yet — `is_ready` needs it
- `unblock_next[task_name] = task` — overwrites if multiple tasks share a blocker; must be a list: `unblock_next[task_name] = []` then `.append(task)`
- Test asserted `s.unblock_next['A'] == s2` — wrong, value is a list so should be `== [s2]`

What you got right without prompting:
- Commented out `heappop` and scanned manually — exact right strategy to get dep logic working first
- `task.status = Status.I` in scan loop before returning
- `pending_heap.pop(i)` to remove found task from heap
- Phase 1 tests passing cleanly before moving to Phase 2

Key insight for `is_ready`:
- Don't check deps list against `completed` set inside `Task` — `Task` doesn't own that state
- Use `in_degree` counter: `is_ready = self.in_degree == 0`
- `in_degree` starts as `len(deps)`, decremented by `complete_task` when a blocker finishes

**Target for Round 3:** Full solution in one pass — Status → Task (with in_degree) → TaskScheduler (with unlocks map) → add_task (Kahn's push) → next_task (heappop, no scan) → complete_task (decrement + push). Under 20 min.

---

**Round 3 — Full Phase 1 + Phase 2 complete**

Your layering story (tell this in the interview):

```
1. TaskScheduler stub + test
   → fields: pending_heap, completed (set), task_map (dict)

2. add_task Phase 1
   → Task(name, priority), heappush(-priority, name, task), task_map[name]=task

3. next_task Phase 1
   → heappop, mark IN_PROGRESS, return task

4. complete_task Phase 1
   → mark COMPLETED, completed.add(name)

5. Tests passing for Phase 1 ✓

6. Add dep support to Task
   → dep=[], indegree, is_ready() = indegree == 0
   → update add_task to pass dep= to Task constructor
   → FIRST update indegree correctly before pushing to heap

7. add_task Phase 2
   → only push to heap if indegree == 0
   → build unblock_next map: dep → [list of Tasks blocked by it]

8. next_task Phase 2
   → heappop still works — heap only ever has ready tasks (Kahn's guarantees it)
   → no scan needed

9. complete_task Phase 2
   → loop unblock_next[task_name], decrement each blocked.indegree
   → if indegree hits 0 → heappush it

10. Tests passing for Phase 2 ✓
```

Key things to say out loud:
- "I'll keep the heap clean — only push tasks whose indegree is 0, so `next_task` can just pop"
- "I need a reverse map: when A completes, I instantly know who to unblock"
- "I update indegree before deciding whether to push"

---

#### Task Scheduler — Incremental Design Narrative

Tell this story in the interview — shows you think step by step:

```
0. Task class            → name, priority, deps=[], status=PENDING
   TaskScheduler         → tasks_heap (list), just store everything

1. naive list scan       → works but O(n), pops blocked tasks forever (lost!)
2. is_ready stub         → get structure right first, fill logic later
3. tasks_map (dict)      → O(1) lookup by name instead of scanning list
4. blocked_by/unlocks    → reverse map: when A completes, instantly know who to unblock
5. in_degree on Task     → counter on each task, hits 0 = ready to push to heap

5.5 commented out heappop, kept structure, scanned manually to get logic right:
   # pri_neg, name, task = heapq.heappop(self.tasks)  ← commented out
   for i, (pri_neg, name, task) in enumerate(self.tasks):
       if self._is_ready(task): ...
   → once logic worked, brought heappop back
   → lesson: comment out the complex part, prove the logic first, restore later

6. heap only has indegree==0 tasks:
   - add_task: only heappush if in_degree == 0
   - complete_task: decrement in_degree of dependents,
     if in_degree hits 0 → heappush that task
   → heap is always clean, get_next just pops
```

Each step solves a real problem:
- Lost tasks → Kahn's (only push ready tasks)
- Slow lookup → dict
- Slow complete_task → reverse map instead of scanning all tasks
- Readiness check → in_degree

**Task lifecycle — PENDING → IN_PROGRESS → COMPLETED:**
- `get_next()` pops from heap, marks `Status.IN_PROGRESS`, returns task — that's it
- Worker does actual work outside the scheduler
- Worker then calls `complete_task(task_id)` — marks `COMPLETED`, unblocks dependents
- These are two separate worker actions, not one — never call `complete_task` inside `get_next`

**Typing gotcha:**
- `Tuple(int, str)` → crashes, it's `Tuple[int, str]` (square brackets)
- `sort(key=lambda x: -x[0])` when x[0] is already `-priority` → double negation, wrong order
- `field(default=[])` → shared across instances, use `field(default_factory=list)`

**Say in interview:**
> "I started with Task and TaskScheduler with a basic heap. I commented out heappop first and scanned manually to get the deps logic right, then brought heappop back once it worked. Then I added in_degree so only ready tasks go in the heap, and a reverse map so complete_task instantly knows who to unblock."

#### Task Scheduler — Bugs & Lessons

| Bug | Wrong | Right |
|---|---|---|
| No return in `get_next` | function returns `None` silently — easy to miss since Python doesn't warn | `return task` at end — always check your methods return what they should |
| `get_next` calls `complete_task` | task marked complete on pickup — wrong lifecycle | two separate worker actions: `get_next` → IN_PROGRESS, caller does work, then calls `complete_task` → COMPLETED |
| Marking COMPLETED in `get_next` | `task.status = Status.COMPLETED` on pop | mark `Status.IN_PROGRESS` in `get_next`; only mark `COMPLETED` inside `complete_task` after work is done |
| Sorting negated heap values | `sort(key=lambda x: -x[0])` where x[0] is already `-priority` → reverses | `sort(key=lambda x: x[0])` |
| `Status.C` in `get_next` | marks completed on pickup | mark `in_progress` in get_next, `completed` only in `complete_task` |
| `task.Status` | uppercase S | `task.status` |
| `Tuple(str, Task)` type hint | parentheses — crashes | `Tuple[str, Task]` square brackets |
| `Dict[str: list]` | colon inside type hint | `Dict[str, list]` comma |
| Mutable default in dataclass | `tasks: list = []` shared across instances | `tasks: list = field(default_factory=list)` |
| `completed` as list | O(n) lookup | `set` for O(1), store name not task |
| Heap pop loses blocked tasks | pop → check deps → not ready → task gone forever | Kahn's: only push ready tasks |
| `assert a, b` | always True — checks truthiness of `a` | `assert a == b` |
| `isinstance(obj, instance)` | second arg must be a TYPE | `isinstance(obj, ClassName)` |
| `__post__init__` | double underscore typo | `__post_init__` |
| Class variable vs dataclass field | `name = ''` — shared, not in `__init__` | `name: str` |
| `self.lives - 1` | evaluates, doesn't assign | `self.lives -= 1` |
| Unnecessary import | `from numpy import block` | remove it |

---

### Async Job Status Tracker
`#coding` `#onsite` · **Common · 5/10**

You're building a job tracking service for long-running data processing jobs on a labeling platform. Jobs transition through states and clients poll for status updates.

**Part 1 — Job State Machine**

Implement a `JobTracker` class that manages job lifecycles.

Valid transitions:
```
PENDING → RUNNING → SUCCEEDED
PENDING → RUNNING → FAILED
PENDING → CANCELLED
RUNNING → CANCELLED
```
No other transitions are valid.

```python
class JobTracker:
    def create_job(self, job_id: str, metadata: dict) -> dict:
        # Create in PENDING state. Raise ValueError if job_id already exists.

    def transition(self, job_id: str, new_state: str) -> dict:
        # Raise ValueError on invalid transitions or unknown job_id.

    def get_status(self, job_id: str) -> dict:
        # Return current job state and metadata. Raise KeyError if not found.

    def list_jobs_by_state(self, state: str) -> list[dict]:
        # Return all jobs in given state, sorted by creation time ascending.
```

Each job record: `job_id`, `state`, `metadata`, `created_at`, `updated_at`.

**Part 2 — Stuck Job Detection**

```python
def find_stuck_jobs(tracker: JobTracker, current_time: float, timeout_seconds: int) -> list[str]:
```

A job is "stuck" if it has been in `RUNNING` state for longer than `timeout_seconds` without a state change. Return job_ids sorted by how long they've been stuck (longest first).

**Part 3 — Job History**

Extend `JobTracker` to record state transition history. `get_job_history(job_id)` returns list of `{from_state, to_state, timestamp}` dicts in order.

**Follow-ups:**
1. Retry logic — auto-transitioning FAILED → PENDING up to N times?
2. 10,000 concurrent jobs, clients polling every second — horizontal scale architecture?

**Constraints:** Use `time.time()` for timestamps (mock in tests). `metadata` must not be mutated after creation.

**Practice app:** Day 8 — `job-tracker`

---

### Conversation Thread Summarizer
`#coding` `#onsite` · **Popular! · 10/10**

You are building a backend tool that processes customer support conversation threads and produces structured summaries for an LLM fine-tuning dataset.

**Part 1 – Parse Conversation Threads**

Input thread shape:
```json
{
  "thread_id": "th_001",
  "messages": [
    {"message_id": "m_1", "sender_type": "customer", "text": "My order hasn't arrived.", "timestamp": "2024-08-01T09:00:00Z"},
    {"message_id": "m_2", "sender_type": "agent",    "text": "I'm sorry. Can you share your order ID?", "timestamp": "2024-08-01T09:02:00Z"},
    {"message_id": "m_3", "sender_type": "customer", "text": "It's #ORD-5521.", "timestamp": "2024-08-01T09:03:00Z"}
  ],
  "resolved": true,
  "category": "shipping"
}
```

`extract_thread_features(thread) -> dict` returns:
```python
{
  "thread_id": "th_001",
  "message_count": 3,
  "customer_message_count": 2,
  "agent_message_count": 1,
  "first_response_time_seconds": 120,   # first customer msg → first agent msg
  "total_duration_seconds": 180,        # first msg → last msg
  "avg_customer_message_length_chars": 28,
  "resolved": True,
  "category": "shipping"
}
```

If no agent messages: `first_response_time_seconds = None`. Messages are **not** guaranteed to be sorted by timestamp.

**Part 2 – Build Conversation Turns**

`build_turns(thread) -> list[dict]` groups consecutive messages from the same sender into turns, joining their text with a space:
```python
[
  {"turn": 1, "sender_type": "customer", "combined_text": "My order hasn't arrived.", "message_count": 1},
  {"turn": 2, "sender_type": "agent",    "combined_text": "I'm sorry. Can you share your order ID?", "message_count": 1},
  {"turn": 3, "sender_type": "customer", "combined_text": "It's #ORD-5521.", "message_count": 1},
]
```

**Part 3 – Dataset Quality Filtering**

`filter_quality_threads(threads, min_turns, max_first_response_seconds, resolved_only) -> (list[dict], dict)`

Returns threads meeting all criteria + a rejection summary:
```python
{
  "kept": 840,
  "rejected_too_few_turns": 42,
  "rejected_slow_response": 18,
  "rejected_unresolved": 100,
}
```

A thread failing multiple criteria counts only once, in the first matching rejection bucket (order as listed above).

**Constraints:** Messages unsorted by timestamp. Unicode text. 0 agent messages = abandoned thread.

**Follow-ups:**
1. How would you detect and handle PII before using as training data?
2. How would you scale this to millions of threads per day?
3. What additional quality signals would you add?

**Practice app:** Day 16 — `thread-summarizer`

---
