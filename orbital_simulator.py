"""Plot a two-dimensional slice through a hydrogen wavefunction."""

from __future__ import annotations

import argparse
from math import factorial
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import genlaguerre

try:
    from scipy.special import sph_harm_y
except ImportError:  # SciPy < 1.15
    from scipy.special import sph_harm

    def sph_harm_y(l: int, m: int, theta: np.ndarray, phi: np.ndarray) -> np.ndarray:
        """Adapt the legacy SciPy argument order to ``sph_harm_y``."""
        return sph_harm(m, l, phi, theta)


def validate_quantum_numbers(n: int, l: int, m: int) -> None:
    """Raise ``ValueError`` when ``(n, l, m)`` is not a valid hydrogen state."""
    if n < 1:
        raise ValueError("n must be at least 1")
    if not 0 <= l < n:
        raise ValueError("l must satisfy 0 <= l < n")
    if abs(m) > l:
        raise ValueError("m must satisfy -l <= m <= l")


def radial_wavefunction(n: int, l: int, radius: np.ndarray) -> np.ndarray:
    """Return the normalized hydrogen radial wavefunction in atomic units."""
    validate_quantum_numbers(n, l, 0)
    rho = 2.0 * radius / n
    normalization = np.sqrt(
        (2.0 / n) ** 3
        * factorial(n - l - 1)
        / (2.0 * n * factorial(n + l))
    )
    laguerre = genlaguerre(n - l - 1, 2 * l + 1)(rho)
    return normalization * np.exp(-radius / n) * rho**l * laguerre


def wavefunction_slice(
    n: int,
    l: int,
    m: int,
    *,
    extent: float = 15.0,
    resolution: int = 500,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Evaluate ``psi`` on the x-z plane (y=0), in Bohr-radius units."""
    validate_quantum_numbers(n, l, m)
    axis = np.linspace(-extent, extent, resolution)
    x, z = np.meshgrid(axis, axis)
    radius = np.hypot(x, z)
    theta = np.arccos(np.clip(z / np.where(radius == 0.0, 1.0, radius), -1.0, 1.0))
    phi = np.zeros_like(theta)
    psi = radial_wavefunction(n, l, radius) * sph_harm_y(l, m, theta, phi)
    return axis, axis, psi


def plot_orbital(
    n: int,
    l: int,
    m: int,
    *,
    extent: float = 15.0,
    resolution: int = 500,
    output: Path | None = None,
) -> None:
    """Plot the signed real wavefunction and probability density."""
    x, z, psi = wavefunction_slice(
        n, l, m, extent=extent, resolution=resolution
    )
    density = np.abs(psi) ** 2

    plt.style.use("dark_background")
    figure, axes = plt.subplots(1, 2, figsize=(12, 5), constrained_layout=True)
    signed = axes[0].imshow(
        np.real(psi),
        extent=[x.min(), x.max(), z.min(), z.max()],
        origin="lower",
        cmap="RdBu_r",
    )
    probability = axes[1].imshow(
        density,
        extent=[x.min(), x.max(), z.min(), z.max()],
        origin="lower",
        cmap="inferno",
    )
    axes[0].set_title(rf"$\mathrm{{Re}}(\psi_{{{n}{l}{m}}})$")
    axes[1].set_title(rf"$|\psi_{{{n}{l}{m}}}|^2$")
    for axis_plot in axes:
        axis_plot.set_xlabel(r"$x/a_0$")
        axis_plot.set_ylabel(r"$z/a_0$")
    figure.colorbar(signed, ax=axes[0], shrink=0.8)
    figure.colorbar(probability, ax=axes[1], shrink=0.8)

    if output is not None:
        output.parent.mkdir(parents=True, exist_ok=True)
        figure.savefig(output, dpi=180)
        print(f"Saved {output}")
    else:
        plt.show()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=2, help="principal quantum number")
    parser.add_argument("--l", type=int, default=1, help="orbital quantum number")
    parser.add_argument("--m", type=int, default=0, help="magnetic quantum number")
    parser.add_argument("--extent", type=float, default=15.0, help="half-width in a0")
    parser.add_argument("--resolution", type=int, default=500, help="pixels per axis")
    parser.add_argument("--output", type=Path, help="save the figure instead of opening it")
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_args()
    plot_orbital(
        arguments.n,
        arguments.l,
        arguments.m,
        extent=arguments.extent,
        resolution=arguments.resolution,
        output=arguments.output,
    )
