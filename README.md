# GemFinder
Project Overview
Gem Finder is a turn based grid based mini game designed to compare the performance and behavior of two AI solvers: Minimax and Expectimax. The game highlights the difference between adversarial reasoning (Minimax) and probabilistic reasoning (Expectimax) by placing the player in competition with an AI agent.

Gems spawn randomly across the board, hazards move unpredictably, and each solver must choose optimal actions to maximize score while avoiding danger. To ensure fair comparison, each level uses a fixed random seed, making the environment “random but repeatable.”

Responsibilities: 

Allison Arcand — Frontend development, Expectimax solver, testing

Emily Adams — Backend development, Minimax solver, data handling, infrastructure & tooling

Shared — Model development, metrics tracking, final report

The game tracks:

Quantitative
Win/loss ratio

Average score

Time per decision

Depth reached

Qualitative
Minimax’s cautious behavior

Expectimax’s opportunistic behavior

Risk taking differences