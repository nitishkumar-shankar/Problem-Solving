# Bus Traveling System

## Problem Statement
Nina wants to travel the city but is unaware of the bus routes and the associated costs. The goal of this project is to create a bus traveling system that helps users find the shortest path and the least traveling distance from a source location to a destination.

## Overview
The Bus Traveling System is designed to assist users in navigating the city's bus routes efficiently. By inputting a starting point and a destination, users can receive information about the optimal route, including the total distance and estimated travel time. This system aims to enhance the travel experience by providing clear and concise route information.

## Approach
To solve the problem, we implemented a graph-based algorithm where:
- **Nodes** represent bus stops.
- **Edges** represent bus routes between stops, with weights indicating the distance or cost of travel.

I utilized **Dijkstra's algorithm** to find the shortest path from the source to the destination. Dijkstra's algorithm is particularly effective for graphs with non-negative weights and works by iteratively selecting the node with the smallest tentative distance, updating the distances of its neighbors, and repeating this process until the shortest path to the destination is found.

### Time Complexity
The time complexity of the Dijkstra's algorithm implementation in this project is as follows:
- **Using a priority queue (heapq)**: The overall time complexity is **O((V + E) log V)**, where:
  - **V** is the number of vertices (bus stops).
  - **E** is the number of edges (bus routes).
  
This complexity arises because each vertex is added to the priority queue once, and each edge is processed once, with logarithmic time complexity for the priority queue operations.

## How It Works
1. **Input**: The user inputs the source and destination bus stops.
2. **Graph Representation**: The bus routes are represented as a graph, where each bus stop is a node, and each route is an edge with a weight.
3. **Pathfinding**: The system applies Dijkstra's algorithm to calculate the shortest path based on the weights (distance or cost).
4. **Output**: The system returns the optimal route, including the sequence of bus stops, total distance, and estimated travel time.

## Output Screenshot
![Output Screenshot](https://github.com/nitishkumar-shankar/Problem-Solving/blob/main/output.png)

## Conclusion
The Bus Traveling System is a valuable tool for city travelers, providing them with the necessary information to navigate bus routes efficiently. By leveraging graph algorithms, specifically Dijkstra's algorithm, the system ensures that users can find the shortest and most cost-effective paths to their destinations.
