"""Lightweight training placeholder.

Replace this with real training loop and model code. Keep functions small
and testable.
"""
from pathlib import Path
import yaml


def run(config_path: Path, dry_run: bool = False):
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    print("Loaded config:", cfg.get("experiment", {}).get("name"))
    if dry_run:
        print("Dry run - not training")
        return

    # Placeholder training steps
    epochs = cfg.get("training", {}).get("epochs", 1)
    for epoch in range(1, epochs + 1):
        print(f"Epoch {epoch}/{epochs} - training... (placeholder)")

    print("Training complete. Save your model and metrics.")
