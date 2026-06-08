"""Quantum-inspired MIDI generation — superposition and entanglement."""
import random, math
def process(v, base=60):
    n=[base]
    for x in v:
        # Amplitude = probability of going up, phase = direction
        amplitude = abs(x) * 0.5 + 0.25
        phase = 1 if x >= 0 else -1
        if random.random() < amplitude:
            n.append(n[-1] + phase * int(12 * amplitude))
        else:
            n.append(n[-1])
    return n
if __name__ == '__main__':
    v=[1,0,-1,1,0,-1,1,1]
    for i in range(3):
        print(f"Run {i+1}: {process(v)}")
