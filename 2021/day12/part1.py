from collections import defaultdict

graph = defaultdict(list)
small_caves = set()
visited = {'start'}  # prepopulate with start
with open('input', 'r') as data:
    for line in data.readlines():
        a, b = line.strip().split('-')
        graph[a].append(b)
        graph[b].append(a)

        if a.islower():
            small_caves.add(a)
        if b.islower():
            small_caves.add(b)


# just another dfs...
def find_paths(graph, visited, small_caves, node, start='start', end='end'):
    if node == end:
        return 1

    pathcount = 0
    for neighbor in graph[node]:
        if neighbor not in small_caves:
            # big cave, don't care about visited
            pathcount += find_paths(graph, visited, small_caves, neighbor)
        else:
            # its a small cave
            if neighbor not in visited:
                pathcount += find_paths(graph, visited.union({neighbor}), small_caves, neighbor)

    return pathcount


count = find_paths(graph, visited, small_caves, next(iter(visited)))
print(count)
