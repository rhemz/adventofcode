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
def find_paths(graph, visited, small_caves, node, can_visit_twice=False, start='start', end='end'):
    if node == end:
        return 1

    pathcount = 0
    for neighbor in graph[node]:
        if neighbor not in small_caves and neighbor != 'start':
            # big cave, don't care about visited
            pathcount += find_paths(graph, visited, small_caves, neighbor, can_visit_twice)
        else:
            # its a small cave
            if neighbor not in visited:
                pathcount += find_paths(graph, visited.union({neighbor}), small_caves, neighbor, can_visit_twice)
            elif neighbor not in {start, end} and can_visit_twice:
                pathcount += find_paths(graph, visited.union({neighbor}), small_caves, neighbor, False)

    return pathcount


count = find_paths(graph, visited, small_caves, next(iter(visited)), can_visit_twice=True)
print(count)
