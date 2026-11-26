"""Write a single one-star review of the Moon to entry.txt.

Deterministic: the same fixed line is written on every run, with no
input, no network, no randomness and no clock. Standard library only.
"""

import os

ENTRY = "One star. Freezing at night, boiling by day, and no thermostat in sight."

# The gate counts characters, so the entry must stay one line and short.
assert "\n" not in ENTRY and len(ENTRY) <= 120

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
