import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

# Settings
NUM_QUBITS = 4
NUM_COLUMNS = 12

# Possible single-qubit gates
GATES = ["H", "X", "Y", "Z"]

fig, ax = plt.subplots(figsize=(12, 5))

# Draw qubit wires
for q in range(NUM_QUBITS):
    ax.plot([0, NUM_COLUMNS], [q, q], linewidth=2)

# Generate random circuit
for col in range(1, NUM_COLUMNS):

    # 25% chance of a CNOT gate
    if random.random() < 0.25:
        control = random.randint(0, NUM_QUBITS - 2)
        target = random.randint(control + 1, NUM_QUBITS - 1)

        # Vertical connection
        ax.plot([col, col], [control, target], linewidth=2)

        # Control dot
        ax.add_patch(Circle((col, control), 0.08))

        # Target symbol
        ax.add_patch(Circle((col, target), 0.18, fill=False))
        ax.plot([col - 0.12, col + 0.12], [target, target])
        ax.plot([col, col], [target - 0.12, target + 0.12])

    else:
        qubit = random.randint(0, NUM_QUBITS - 1)
        gate = random.choice(GATES)

        rect = Rectangle(
            (col - 0.25, qubit - 0.25),
            0.5,
            0.5
        )

        ax.add_patch(rect)

        ax.text(
            col,
            qubit,
            gate,
            ha="center",
            va="center",
            fontsize=10
        )

# Labels
for q in range(NUM_QUBITS):
    ax.text(-0.5, q, f"q{q}", fontsize=12)

ax.set_xlim(-1, NUM_COLUMNS + 1)
ax.set_ylim(-1, NUM_QUBITS)
ax.set_aspect("equal")
ax.axis("off")

plt.title("Random Quantum Circuit")
plt.show()