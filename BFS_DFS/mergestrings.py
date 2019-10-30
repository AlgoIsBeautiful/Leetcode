#!/bin/python

import sys

def connectedCities(n, g, originCities, destinationCities):
    # Complete this function
    res = []
    graph = {i+1:[] for i in range(n)}
    for i in originCities:
        for j in range(n):
            if i != j+1 and computeGCD(i, j+1) > g:
                graph[i].append(j+1)
            
    for i in range(len(originCities)):
        paths = find_all_paths(graph, originCities[i], destinationCities[i])
        if len(paths) > 0:
            res.append(1)
        else:
            res.append(0)

    return res

def computeGCD(x, y):   
   while(y): 
       x, y = y, x % y   
   return x 

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths