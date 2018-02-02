def breadth_first_search(graph, start, end):
    """
    :param graph: graph represented as list of lists
    :param start: starting node
    :param end: end node 
    """
    queue = []
    visited = {}
    parent = {}

    for node in range(len(graph)):
        visited[node] = False
        parent[node] = None

    queue.append(start)
    while len(queue) != 0:
        current = queue.pop(0)
        if current == end:
            print tracepath(parent, start, end)
            break
        for neighbor in graph[current]:
            if visited[neighbor] == False:
                visited[neighbor] = True
                parent[neighbor] = current
                queue.append(neighbor)
    print visited
    print parent
    print target

def tracepath(parent, start, end):
    """
    Returns elements of the path.

    :param parent: node-parent dict
    :param start: starting node
    :param end: end node
    :rbrtype: list
    """
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path
