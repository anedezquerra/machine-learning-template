"""Minimal CLI entrypoint for running experiments.

This module provides a lightweight command-line interface that delegates
to training/evaluation entrypoints. It's intentionally small so projects can
replace or extend it with Click, Typer, or Hydra later.
"""
import argparse
import sys
from pathlib import Path

from . import train


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Run ML project tasks")
    sub = parser.add_subparsers(dest="command")

    run = sub.add_parser("run", help="Run training")
    run.add_argument("--config", default="configs/default.yaml")
    run.add_argument("--dry-run", action="store_true")

    sub.add_parser("version", help="Print project version")

    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    if args.command == "run":
        config_path = Path(args.config)
        train.run(config_path, dry_run=args.dry_run)
    elif args.command == "version":
        print("machine-learning-template 0.1.0")
    else:
        print("No command provided. Use --help.")


if __name__ == "__main__":
    main(sys.argv[1:])
