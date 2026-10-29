"""Low-rank SVD approximations of scipy's `ascent` test image.

Writes images/ascent.png, images/svd-ascent-ranks.png, and
images/svd-ascent-singular-values.png.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy import datasets

out = Path(__file__).parent / "images"
A = datasets.ascent().astype(float)
m, n = A.shape
U, s, Vt = np.linalg.svd(A, full_matrices=False)

plt.imsave(out / "ascent.png", A, cmap="gray")

ranks = [5, 20, 50]
full_storage = m * n

fig, axes = plt.subplots(1, 3, figsize=(12, 4.6))

print(f"{'rank':>5} {'storage':>9} {'% of full':>9} {'rel. error':>10}")
for ax, k in zip(axes, ranks):
    Ak = (U[:, :k] * s[:k]) @ Vt[:k, :]
    storage = k * (m + n + 1)
    err = np.sqrt(np.sum(s[k:] ** 2)) / np.sqrt(np.sum(s**2))
    print(f"{k:>5} {storage:>9,} {100 * storage / full_storage:>8.1f}% {err:>10.4f}")
    ax.imshow(Ak, cmap="gray")
    ax.set_title(
        f"Rank {k}\nstorage: {storage:,} ({100 * storage / full_storage:.1f}%)\n"
        f"rel. error {err:.3f}"
    )

for ax in axes:
    ax.axis("off")
fig.tight_layout()
fig.savefig(out / "svd-ascent-ranks.png", dpi=120, bbox_inches="tight")

fig, ax = plt.subplots(figsize=(7, 4))
ax.semilogy(np.arange(1, len(s) + 1), s, color="C0")
ax.set_xlabel("index $i$")
ax.set_ylabel(r"singular value $\sigma_i$")
ax.set_title("Singular values of the ascent image")
fig.tight_layout()
fig.savefig(out / "svd-ascent-singular-values.png", dpi=120)
