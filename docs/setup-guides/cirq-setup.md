# Cirq Setup Guide

[Cirq](https://quantumai.google/cirq) is Google's open-source framework for creating, editing, and invoking Noisy Intermediate Scale Quantum (NISQ) circuits. It's particularly well-suited for research and experimentation.

## Prerequisites

- Python 3.9 or later
- pip package manager
- A virtual environment (recommended)

## Installation

### Step 1: Create a Virtual Environment

```bash
python -m venv cirq-env
source cirq-env/bin/activate  # On Windows: cirq-env\Scripts\activate
```

### Step 2: Install Cirq

```bash
pip install cirq
```

### Step 3: Install Additional Components (Optional)

For Google Quantum Engine access:
```bash
pip install cirq-google
```

For visualization:
```bash
pip install cirq[contrib]
```

For all optional dependencies:
```bash
pip install cirq-core[all]
```

## Verify Installation

Run this Python script to verify your installation:

```python
import cirq
print(f"Cirq version: {cirq.__version__}")

# Create qubits
q0, q1 = cirq.LineQubit.range(2)

# Create a circuit
circuit = cirq.Circuit(
    cirq.H(q0),
    cirq.CNOT(q0, q1),
    cirq.measure(q0, q1, key='result')
)

print("Circuit created successfully!")
print(circuit)
```

Expected output:
```
Cirq version: 1.x.x
Circuit created successfully!
0: ───H───@───M('result')───
          │   │
1: ───────X───M─────────────
```

## Your First Quantum Program

```python
import cirq

# Create qubits
q0, q1 = cirq.LineQubit.range(2)

# Build a Bell state circuit
circuit = cirq.Circuit([
    cirq.H(q0),           # Hadamard gate on q0
    cirq.CNOT(q0, q1),    # CNOT with control=q0, target=q1
    cirq.measure(q0, q1, key='m')  # Measure both qubits
])

# Print the circuit
print("Bell State Circuit:")
print(circuit)

# Simulate the circuit
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1000)

# Print results
print("\nMeasurement Results:")
print(result.histogram(key='m'))
```

## Key Concepts in Cirq

### Qubits

Cirq supports multiple qubit types:

```python
# Line qubits (1D arrangement)
q = cirq.LineQubit(0)
qubits = cirq.LineQubit.range(5)

# Grid qubits (2D arrangement)
q = cirq.GridQubit(0, 0)
qubits = cirq.GridQubit.rect(3, 3)

# Named qubits
q = cirq.NamedQubit('my_qubit')
```

### Gates

```python
# Single-qubit gates
cirq.X(q0)      # Pauli X
cirq.Y(q0)      # Pauli Y
cirq.Z(q0)      # Pauli Z
cirq.H(q0)      # Hadamard
cirq.T(q0)      # T gate
cirq.S(q0)      # S gate

# Rotation gates
cirq.rx(0.5)(q0)  # X rotation
cirq.ry(0.5)(q0)  # Y rotation
cirq.rz(0.5)(q0)  # Z rotation

# Two-qubit gates
cirq.CNOT(q0, q1)  # Controlled-NOT
cirq.CZ(q0, q1)    # Controlled-Z
cirq.SWAP(q0, q1)  # SWAP
```

### Circuits

```python
# Create circuit using list of operations
circuit = cirq.Circuit([
    cirq.H(q0),
    cirq.CNOT(q0, q1)
])

# Create circuit using moments (operations in parallel)
circuit = cirq.Circuit([
    cirq.Moment([cirq.H(q0), cirq.H(q1)]),  # Parallel Hadamards
    cirq.Moment([cirq.CNOT(q0, q1)])
])

# Append operations
circuit.append(cirq.measure(q0, q1))
```

## Google Quantum Engine (Optional)

To access Google's quantum hardware:

1. Set up a Google Cloud project
2. Enable the Quantum Engine API
3. Install the Google Cloud SDK
4. Authenticate:

```python
import cirq_google as cg

# Get available processors
processors = cg.get_engine().list_processors()

# Create a circuit optimized for a specific processor
processor = cg.get_engine().get_processor('processor_name')
```

## Common Issues and Solutions

### Issue: Visualization not working
**Solution:** Install matplotlib: `pip install matplotlib`

### Issue: Module 'cirq' has no attribute 'google'
**Solution:** Install cirq-google: `pip install cirq-google`

## Resources

- [Cirq Documentation](https://quantumai.google/cirq)
- [Cirq Tutorials](https://quantumai.google/cirq/start)
- [Cirq GitHub Repository](https://github.com/quantumlib/Cirq)
- [Google Quantum AI](https://quantumai.google/)
