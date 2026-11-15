# Day 079: Graph Neural Networks Basics

## Phase: Deep Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Graph data structures: nodes, edges, adjacency matrices
- Message passing and neighborhood aggregation
- Graph Convolutional Networks (GCN)
- Node-level, edge-level, and graph-level tasks
- PyTorch Geometric (PyG) library basics

## Key Takeaways

1. GNNs naturally handle data with relational structure, such as connected sensor networks or spatial borehole relationships.
2. Message passing enables each node to learn from its neighbors, capturing spatial dependencies in site investigation data.
3. Graph representations can model the spatial relationships between boreholes, sensors, or geological features.

## Code Summary

- Built a simple GNN using PyTorch Geometric, applied it to node classification on a graph of sensor data, and visualized message passing

## Geotechnical Application

- Modeling spatial relationships between boreholes or sensor stations as graphs for improved predictions that account for spatial dependencies

## Resources

- [PyTorch Geometric Documentation](https://pytorch-geometric.readthedocs.io/)
- [A Gentle Introduction to GNNs — Distill](https://distill.pub/2021/gnn-intro/)

---

> *Day 079 of 100 — 100 Days of ML for Geotechnical Engineering*
