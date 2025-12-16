# Django Flight Routes System

## Overview
This project is a Django-based application that models airport routes using a tree structure.
Each airport is represented as a node, where routes are defined using parent-child relationships
with left and right positions.

The system allows:
1. Finding the Nth left or right airport starting from a root airport
2. Finding the airport with the longest duration
3. Finding the shortest-duration airport between two selected airports

## Data Model
- Each airport is stored as an AirportRoute record
- Parent-child self-relation is used to form a tree
- Position (Left / Right) defines the relationship
- Duration is stored as a value on each node

## Features
### 1. Add Airport Route
- Uses Django ModelForm
- Stores airport code, parent, position, and duration

### 2. Nth Left / Right Node
- User selects root airport, direction, and N
- Traverses the tree iteratively
- Returns None if the path does not exist

### 3. Longest Duration Airport
- Uses ORM ordering to efficiently find the maximum duration

### 4. Shortest Duration Between Two Airports
- Compares duration range between two airports
- Returns the minimum duration airport within that range

## Assumptions
- The airport route structure is treated as a binary tree
- Duration is a node-level value, not a path-based calculation
- If traversal depth exceeds tree depth, result is None

## Tech Stack
- Python
- Django
- SQLite (default)
