# KD-Tree and Quad-Tree Implementations in Python

This repository contains Python implementations of KD-Tree and Quad-Tree, two powerful data structures for efficient spatial data management and query processing. These implementations demonstrate foundational operations such as insertion, deletion, and nearest neighbor queries, which are crucial in applications like geographical data analysis, computer graphics, and machine learning.

## Features

### KD-Tree
KD-Tree is a space-partitioning data structure for organizing points in a k-dimensional space. This implementation supports:
- Building the tree based on data points.
- Insertion and deletion of points.
- Finding minimum and maximum points.
- Nearest neighbor search.
- Tree rebalancing.

### Quad-Tree
Quad-Tree is primarily used for managing two-dimensional space, useful in applications like image processing and GIS. This implementation provides:
- Boundary management for spatial partitioning.
- Insertion and deletion of points.
- Nearest neighbor search using efficient traversal.
- Functions for tree rebalancing and node gathering.

## Getting Started

Clone the repository to start using KD-Tree and Quad-Tree in your projects:

```bash
git clone https://github.com/NikosBakalis/K-D_Tree-Quad_Tree.git
```

## Usage

### KD-Tree

Navigate to the `KD_Tree` directory:

- `buildTree.py`: Use to construct the initial tree from a set of points.
- `insert.py`, `delete.py`: Use to modify the tree by adding or removing points.
- `findMinimum.py`, `maxim.py`: Use for querying properties like minimum or maximum points.
- `kNNQuery.py`: Use for performing k-nearest neighbor searches.
- `medianBuild.py`, `rebalance.py`, `searchPoint.py`: Additional utilities for managing and querying the tree.

### Quad-Tree

Navigate to the `Quad_Tree` directory:

- `QuadTree.py`: Core class defining the Quad-Tree.
- `insert.py`, `delete.py`: Modify the tree by adding or removing points.
- `knnSearch.py`, `search.py`: Execute nearest neighbor and other search queries.
- `boundaries.py`, `functions.py`, `gatherTreeNodes.py`, `rebalance.py`, `traverseTree.py`: Support various operational needs and tree traversal techniques.

## Contributing

Contributions are welcome! Feel free to fork the repository, add features, fix bugs, or improve the documentation. Please submit a pull request with your changes.
