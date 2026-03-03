from pathlib import Path

from src.agents.runner import run_agent_with_mock


def test_run_agent_with_mock():
    out = run_agent_with_mock("hello", config_path=Path("configs/agents.yaml"))
    assert out is not None
    assert "hello" not in out  # mock returns fixed greeting
