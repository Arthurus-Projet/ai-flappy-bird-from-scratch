<div align="center">

# 🐤 AI Flappy Bird from Scratch

**Watch birds evolve from hopeless to flawless through the power of neuroevolution!**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-green?style=for-the-badge&logo=pygame&logoColor=white)](https://pygame.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

An implementation of **Flappy Bird** where birds learn to play using **genetic algorithms** and **neural networks** — built entirely from scratch, without any ML library.

<br>

<img width="450" alt="Demo" src="https://github.com/user-attachments/assets/02bb015f-7bf2-4784-b099-6fbd297df75e" />

*Generation 6 with 12 birds still alive — watch them evolve!*

<br>

</div>

---

## 🧠 How It Works

### Neural Network Architecture

Each bird is controlled by a simple **feedforward neural network**:

```
     INPUTS                  HIDDEN LAYER                 OUTPUT
 ┌────────────┐             ┌────────────┐             ┌────────────┐
 │  Distance  │───┐     ┌───│            │───┐         │            │
 │  to pipe   │   ├─────┤   │  4 neurons │   ├─────────│   Jump?    │
 └────────────┘   │     └───│            │───┘         │  (0 or 1)  │
 ┌────────────┐   │         └────────────┘             └────────────┘
 │  Vertical  │───┘
 │  distance  │
 └────────────┘
```

> **Output:** `1` → Bird jumps | `0` → Bird does nothing

### Genetic Algorithm

<table>
<tr>
<td align="center">🔍<br><b>Selection</b></td>
<td align="center">🥚<br><b>Crossover</b></td>
<td align="center">🧬<br><b>Mutation</b></td>
<td align="center">🔄<br><b>Repeat</b></td>
</tr>
<tr>
<td>Select birds with best fitness score</td>
<td>Average weights of 2 parents to create offspring</td>
<td>Randomly modify some weights</td>
<td>New generation plays until perfection</td>
</tr>
</table>

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/Arthurus-Projet/ai-flappy-bird-from-scratch.git
cd ai-flappy-bird-from-scratch

# Install dependencies
pip install pygame numpy

# Run the simulation
python main.py
```

---

## 📁 Project Structure

```
📦 ai-flappy-bird-from-scratch
 ┣ 🎮 main.py                  → Game loop & orchestration
 ┣ 🧠 reseau_neuronal.py       → Neural network from scratch
 ┣ 🧬 algorithme_genetique.py  → Selection, crossover, mutation
 ┣ 🚧 tuyau.py                 → Pipe obstacles
 ┣ 🎨 animations.py            → Rendering & sprites
 ┗ 📸 illustrations/           → Screenshots
```

---

## ⚙️ Configuration

| Parameter | Description | Default |
|:---------:|:-----------:|:-------:|
| `POPULATION_SIZE` | Birds per generation | 50-100 |
| `MUTATION_RATE` | Weight mutation probability | 0.1-0.2 |
| `HIDDEN_NEURONS` | Hidden layer size | 4 |

---

## 🔬 Evolution Progress

| Generation | Behavior |
|:----------:|:---------|
| **1-3** | 🎲 Random flying, instant crashes |
| **4-10** | 📈 Learning to jump near pipes |
| **10-20** | 🎯 Consistent navigation |
| **20+** | 🏆 Near-perfect gameplay |

---

## 📚 Learn More

- [Neuroevolution](https://en.wikipedia.org/wiki/Neuroevolution) — Wikipedia
- [NEAT Algorithm](https://nn.cs.utexas.edu/downloads/papers/stanley.cec02.pdf) — Advanced technique

---

<div align="center">

**Made with ❤️ and Python**

</div>
