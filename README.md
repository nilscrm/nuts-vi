# Hamiltonian Monte Carlo Sampling in Vine

This repository is almost a direct port of Colin Carroll's
[minimc](https://github.com/ColCarroll/minimc) to Vine. In addition, the
excellent summary
[A Conceptual Introduction to Hamiltonian Monte Carlo](https://arxiv.org/abs/1701.02434)
by Michael Betancourt was very helpful to get a good overview of the topic and I
can highly recommend it.

## Prerequisites

This code base uses language features only available in the
`vector-add-sub-scalar` branch of Vine so make sure to install that branch from
source.

## Run examples

```sh
vine run minimc/examples.vi > samples.txt
uv run python plots.py
```
