"""
Quantum Random Number Generator

This program demonstrates true random number generation using quantum mechanics.
Unlike classical pseudo-random generators, quantum randomness is fundamentally
unpredictable and cannot be reproduced.

Usage:
    python quantum_random.py

Requirements:
    pip install qiskit
"""

from qiskit import QuantumCircuit
from qiskit.primitives import Sampler


def generate_random_bit():
    """
    Generate a single random bit using quantum superposition.
    
    Returns:
        int: 0 or 1, determined by quantum measurement
    """
    qc = QuantumCircuit(1, 1)
    qc.h(0)        # Create equal superposition
    qc.measure(0, 0)
    
    sampler = Sampler()
    job = sampler.run(qc, shots=1)
    result = job.result()
    
    # Get the measurement outcome
    # The result contains quasi-probabilities; get the most likely outcome
    quasi_dist = result.quasi_dists[0]
    return max(quasi_dist, key=quasi_dist.get)


def generate_random_number(num_bits=8):
    """
    Generate a random integer using quantum bits.
    
    Parameters:
        num_bits: Number of bits (default 8, gives 0-255)
    
    Returns:
        int: Random integer from 0 to 2^num_bits - 1
    """
    qc = QuantumCircuit(num_bits, num_bits)
    
    # Put all qubits in superposition
    for i in range(num_bits):
        qc.h(i)
    
    # Measure all qubits
    qc.measure(range(num_bits), range(num_bits))
    
    sampler = Sampler()
    job = sampler.run(qc, shots=1)
    result = job.result()
    
    # Get the measurement outcome
    quasi_dist = result.quasi_dists[0]
    return max(quasi_dist, key=quasi_dist.get)


def generate_random_bytes(num_bytes=16):
    """
    Generate random bytes using quantum measurements.
    
    Parameters:
        num_bytes: Number of bytes to generate
    
    Returns:
        bytes: Random bytes
    """
    random_values = []
    for _ in range(num_bytes):
        random_values.append(generate_random_number(8))
    return bytes(random_values)


def demonstrate_randomness():
    """Demonstrate quantum random number generation."""
    
    print("=" * 50)
    print("QUANTUM RANDOM NUMBER GENERATOR")
    print("=" * 50)
    print()
    
    # Show the circuit
    print("The quantum circuit for generating a random bit:")
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    print(qc.draw())
    print()
    
    # Generate some random bits
    print("Generating 10 random bits:")
    bits = [generate_random_bit() for _ in range(10)]
    print(f"Random bits: {bits}")
    print()
    
    # Generate a random byte (0-255)
    print("Generating random numbers (0-255):")
    for i in range(5):
        num = generate_random_number(8)
        print(f"  Random number {i+1}: {num}")
    print()
    
    # Statistical analysis
    print("Statistical Analysis (1000 random bits):")
    qc_stats = QuantumCircuit(1, 1)
    qc_stats.h(0)
    qc_stats.measure(0, 0)
    
    sampler = Sampler()
    job = sampler.run(qc_stats, shots=1000)
    result = job.result()
    
    print(result)
    print()
    print("A perfectly random bit generator should produce")
    print("approximately 50% zeros and 50% ones.")
    print()
    
    print("=" * 50)
    print("WHY QUANTUM RANDOMNESS IS SPECIAL")
    print("=" * 50)
    print("""
Classical random number generators are actually "pseudo-random":
- They use deterministic algorithms
- Given the same seed, they produce the same sequence
- They can theoretically be predicted

Quantum random numbers are TRULY random:
- Based on fundamental laws of quantum mechanics
- Impossible to predict, even in principle
- Each measurement is an independent random event

This has important applications in:
- Cryptography
- Monte Carlo simulations
- Gaming
- Scientific research
""")


if __name__ == "__main__":
    demonstrate_randomness()
