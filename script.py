# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 11:44:44 2023

@author: alakaddechi
"""
#Importer les biblitheques
from queue import PriorityQueue
from time import perf_counter

#Definition du graphe
graph = {
    '1': ['2','5'],
    '2': ['1','3'],
    '3': ['2','4'],
    '4': ['3', '9'],
    '5': ['1', '10'],
    '6': ['5', '7',],
    '7': ['2', '13'],
    '8': ['3','7', '9'],
    '9': ['4', '14'],
    '10': ['5', '15'],
    '11': ['10','16'],
    '12': ['6','11'],
    '13': ['8','12', '14', '17'],
    '14': ['9','18'],
    '15': ['10', '16'],
    '16': ['15', '17'],
    '17': ['16', '18'],
    '18':  ['14', '17']
}
#Initialtion de temps de debut d'execution pour DFS
start = perf_counter()
# DFS Algorthim Question
def dfs(graph, start, goal):
    visited = []
    path = []
    f=PriorityQueue()
    f.put((0, start, path, visited))
    while not f.empty():
        depth, current_node, path, visited = f.get()
        
        if current_node == goal:
            return path + [current_node]
        visited = visited + [current_node]
        child_nodes = graph[current_node]
        
        for node in child_nodes:
            if node not in visited:
                if node == goal:
                    return path + [node]
                depth_of_node = len(path)
                f.put((depth_of_node, node, path + [node], visited))
    return path
path=dfs(graph, '1', '18')
#fin de l'execution du programme(temps d'exécution)
end = perf_counter()
elapsed = end - start  #Temps d exection en ms pour DFS
print("Resultat BFS \n")
print('path', path)
print('Nombre des noeuds visités:',len(path))
print('Temps d execution pour DFS',elapsed)
print("\n")
print("*************************************************")
print("\n")
#BFS Algorithm 
visited = [] # List for visited nodes.
queue = []     #Initialize a queue
started = perf_counter()
def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '1')    # function calling
ended = perf_counter()
elapse= ended-started #♥Temps de execution en ms pour BFS
print("\n")
print('Nombres des noeuds visités',len(visited))
print("Le temps d execution pour BFS est:", elapse)
#Ces algorithmes ne fournissent pas la meilleure solution car ce sont des algorithmes aveugles,
# on aura besoin des algorithmes optimales