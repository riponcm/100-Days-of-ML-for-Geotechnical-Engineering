# Day 071: RNN — Fundamentals

## Phase: Deep Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Recurrent Neural Network architecture and hidden state
- Processing sequential data: one-to-one, many-to-one, many-to-many
- Backpropagation Through Time (BPTT)
- Vanishing and exploding gradient problems in RNNs
- Sequence padding and packing for variable-length inputs

## Key Takeaways

1. RNNs process sequential data by maintaining a hidden state that captures information from previous time steps.
2. The vanishing gradient problem limits standard RNNs to learning short-range dependencies in sequences.
3. Understanding RNN fundamentals is essential before moving to LSTM and GRU architectures that solve its limitations.

## Code Summary

- Implemented a basic RNN in PyTorch for sequence prediction, demonstrated the vanishing gradient problem, and processed variable-length sequences

## Geotechnical Application

- Processing sequential geotechnical data such as time series from sensors, CPT depth profiles, or construction monitoring records

## Resources

- [Understanding RNNs — Andrej Karpathy](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
- [PyTorch RNN Tutorial](https://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html)

---

> *Day 071 of 100 — 100 Days of ML for Geotechnical Engineering*
