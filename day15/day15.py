from aocd import lines, submit
import networkx
with open("sample.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    data = [line.strip() for line in inp]
    data = [x for x in data if x != ""]
    return data

def solve(inp, expanded):
    factor = len(inp)
    def getWeight(v):
        right = v[0] // factor
        down = v[1] // factor
        originalX = v[0] - (right * factor)
        originalY = v[1] - (down * factor)
        unadjustedWeight = (int(inp[originalX][originalY]) + right + down)
        return unadjustedWeight % 9 if unadjustedWeight > 9 else unadjustedWeight

    G = networkx.grid_2d_graph(factor * expanded, factor * expanded)
    shortest = networkx.single_source_dijkstra(G, list(G.nodes())[0], target = list(G.nodes())[-1], weight=lambda u, v, d : getWeight(v))
    return shortest[0]

#use sample input
print(solve(preProcess(readIn), 1))
print(solve(preProcess(readIn), 5))

#submit your input
# submit(partOne(preProcess(lines)))
# submit(partTwo(preProcess(lines), 5))
