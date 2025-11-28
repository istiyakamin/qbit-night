"""
Hello Quantum World!

This is your first quantum program. It creates a simple quantum circuit
that puts a qubit into superposition and measures it.

Usage:
    python hello_quantum.py

Requirements:
    pip install qiskit
"""

from qiskit import QuantumCircuit
from qiskit.primitives import Sampler


def hello_quantum():
    """Create and run a simple quantum circuit."""
    
    # Create a quantum circuit with 1 qubit and 1 classical bit
    qc = QuantumCircuit(1, 1)
    
    # Apply a Hadamard gate to put the qubit in superposition
    # |0⟩ → (|0⟩ + |1⟩) / √2
    qc.h(0)
    
    # Measure the qubit
    qc.measure(0, 0)
    
    # Print the circuit
    print("Quantum Circuit:")
    print(qc.draw())
    print()
    
    # Run the circuit using a simulator
    sampler = Sampler()
    job = sampler.run(qc, shots=1000)
    result = job.result()
    
    print("Results from 1000 measurements:")
    print(result)
    print()
    print("Since the qubit is in an equal superposition,")
    print("you should see approximately 50% zeros and 50% ones.")
    
    return result


if __name__ == "__main__":
    print("=" * 50)
    print("Hello Quantum World!")
    print("=" * 50)
    print()
    hello_quantum()
    print()
    print("Congratulations! You've run your first quantum program!")
