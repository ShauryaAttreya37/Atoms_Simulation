# Hydrogen Atom Orbital Simulator (Python)

A physics-accurate simulator for visualizing **hydrogen atom orbitals** using the exact analytical solutions of the Schrödinger equation.

This project computes and visualizes:

[
|\psi_{n\ell m}(r,\theta,\phi)|^2
]

the **probability density of an electron** in a hydrogen atom.

---

## Features

* Exact analytical hydrogen wavefunctions
* Supports arbitrary quantum numbers:

  * Principal quantum number: `n`
  * Angular momentum quantum number: `l`
  * Magnetic quantum number: `m`
* Accurate radial and angular components
* 2D orbital slice visualization
* Correct nodal structure:

  * Radial nodes
  * Angular nodes
* Uses atomic units (`a₀ = 1`)
* Physically accurate spherical harmonics
* High-resolution plots

---

## Physics Background

The hydrogen atom wavefunction separates into radial and angular components:

[
\psi_{n\ell m}(r,\theta,\phi)
=============================

R_{n\ell}(r)
\cdot
Y_\ell^m(\theta,\phi)
]

Probability density:

[
\rho =
|\psi|^2
]

Where:

* (R_{n\ell}(r)) is the radial function
* (Y_\ell^m(\theta,\phi)) is the spherical harmonic

---

## Orbital Types Supported

| n | l | orbital |
| - | - | ------- |
| 1 | 0 | 1s      |
| 2 | 0 | 2s      |
| 2 | 1 | 2p      |
| 3 | 0 | 3s      |
| 3 | 1 | 3p      |
| 3 | 2 | 3d      |
| 4 | 0 | 4s      |
| 4 | 1 | 4p      |
| 4 | 2 | 4d      |
| 4 | 3 | 4f      |

---

## Installation

Install dependencies:

```bash
pip install numpy matplotlib scipy
```

---

## Usage

Run the script:

```bash
python orbital_simulator.py
```

Change quantum numbers in code:

```python
n = 2
l = 0
m = 0
```

Examples:

```python
# 1s orbital
n=1; l=0; m=0

# 2s orbital
n=2; l=0; m=0

# 2p orbital
n=2; l=1; m=0

# 3d orbital
n=3; l=2; m=1
```

---

## Example Output

2s orbital:

* Bright center
* Dark radial node
* Outer probability shell

2p orbital:

* Two lobes
* Angular node at nucleus plane

---

## Mathematical Implementation

Radial function:

[
R_{n\ell}(r)
============

\sqrt{
\left(\frac{2}{n}\right)^3
\frac{(n-\ell-1)!}{2n(n+\ell)!}
}
,
e^{-r/n}
,
\left(\frac{2r}{n}\right)^\ell
,
L_{n-\ell-1}^{2\ell+1}
\left(\frac{2r}{n}\right)
]

Angular function:

[
Y_\ell^m(\theta,\phi)
]

Computed using SciPy.

---

## Coordinate System

Simulation uses a spatial grid:

[
(x,z)
]

Converted to spherical coordinates:

[
r = \sqrt{x^2 + y^2 + z^2}
]

[
\theta = \cos^{-1}(z/r)
]

[
\phi = \tan^{-1}(y/x)
]

---

## Visualization

Uses matplotlib heatmap:

```python
plt.imshow(density, cmap="inferno")
```

Higher brightness = higher electron probability.

---

## Example Project Structure

```
hydrogen-orbital-simulator/
│
├── orbital_simulator.py
├── README.md
└── examples/
```

---

## Dependencies

* numpy
* scipy
* matplotlib

---

## Accuracy

This simulator uses exact analytical solutions from quantum mechanics.

No approximations are used beyond numerical discretization.

---

## Future Improvements

* 3D volumetric rendering
* Interactive visualization
* Orbital superposition
* Animation of quantum states
* GPU acceleration

---

## Educational Applications

Useful for:

* Quantum mechanics students
* Physics visualization
* Teaching atomic structure
* Computational physics learning

---

## License

MIT License
