from collections import deque

# Number of connection lines
n = int(input().strip())

# Graph
graph = {}

# Read station connections
for _ in range(n):
    parts = input().strip().split()

    source = parts[0]

    if source not in graph:
        graph[source] = set()

    for station in parts[1:]:
        graph[source].add(station)

        if station not in graph:
            graph[station] = set()

        graph[station].add(source)


# Number of queries
q = int(input().strip())

queries = []

for _ in range(q):
    queries.append(input().strip())


# Number of restriction lines
r = int(input().strip())

# Restrictions:
# restrictions[source] = set of stations that source cannot visit
restrictions = {}

for _ in range(r):
    parts = input().strip().split()

    source = parts[0]
    restricted_stations = set(parts[1:])

    restrictions[source] = restricted_stations


def can_travel(source, destination):
    # Source and destination same
    if source == destination:
        return True

    # Stations restricted for this source
    blocked = restrictions.get(source, set())

    # If destination itself is restricted, cannot travel there
    if destination in blocked:
        return False

    visited = set()
    queue = deque()

    visited.add(source)
    queue.append(source)

    while queue:
        current = queue.popleft()

        for neighbour in graph.get(current, set()):

            # Already visited
            if neighbour in visited:
                continue

            # Source-specific restriction
            if neighbour in blocked:
                continue

            if neighbour == destination:
                return True

            visited.add(neighbour)
            queue.append(neighbour)

    return False


# Process queries in order
for query in queries:

    parts = query.split()

    if len(parts) == 5:
        # Example:
        # prayagraj connects kushinagar
        station1 = parts[0]
        operation = parts[1]
        station2 = parts[2]

        if station1 not in graph:
            graph[station1] = set()

        if station2 not in graph:
            graph[station2] = set()

        if operation == "connects":
            graph[station1].add(station2)
            graph[station2].add(station1)

        elif operation == "disconnects":
            graph[station1].discard(station2)
            graph[station2].discard(station1)

    else:
        # Example:
        # prayagraj to jaunpur
        source = parts[0]
        destination = parts[2]

        if can_travel(source, destination):
            print("yes")
        else:
            print("no")