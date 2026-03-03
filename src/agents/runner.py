"""Agents runner: load config, execute agent loop with adapters.

This module shows a small, testable agent loop. It's designed to be
framework-agnostic so you can plug LangChain or other orchestrators later.
"""
from pathlib import Path
import yaml
import time
from typing import Optional

from .adapters import Adapter, MockAdapter


class AgentRunner:
    def __init__(self, adapter: Adapter, config: dict):
        self.adapter = adapter
        self.config = config or {}
        self.max_steps = self.config.get("max_steps", 5)
        self.timeout = self.config.get("timeout_seconds", 30)

    def run(self, prompt: str) -> Optional[str]:
        start = time.time()
        step = 0
        response = None
        while step < self.max_steps and (time.time() - start) < self.timeout:
            step += 1
            out = self.adapter.generate(prompt)
            response = out.get("text") or str(out)
            # In a real agent you'd inspect and decide whether to continue.
            break

        return response


def load_config(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def run_agent_with_mock(prompt: str, config_path: Optional[Path] = None) -> str:
    cfg = load_config(config_path) if config_path else {}
    agent_cfg = cfg.get("agents", {}).get("defaults", {}) if cfg else {}
    adapter = MockAdapter(response="hello from mock agent")
    runner = AgentRunner(adapter, agent_cfg)
    return runner.run(prompt)
