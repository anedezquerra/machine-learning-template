## Agents subsystem

This document describes how to safely add autonomous agents to your project.

Key recommendations:

- Opt-in: enable agents by setting `agents.enabled` to `true` in `configs/agents.yaml`.
- Secrets: provide API keys via environment variables or secret stores. Use `python-dotenv` for local development. Never commit secrets.
- Limits: set `max_steps`, `timeout_seconds`, and `allowed_tools` to control agent behavior.
- Testing: use `MockAdapter` to run agent logic in CI without external calls.
- Tools whitelist: avoid allowing agents arbitrary system or network access; explicitly list allowed tools.

Files in this scaffold:

- `configs/agents.yaml` - default config and opt-in toggle.
- `src/agents/adapters.py` - adapter interfaces and `MockAdapter`.
- `src/agents/runner.py` - small agent loop runner for examples and tests.
- `src/agents/langchain_agent.py` - optional LangChain adapter example (requires extras).

Security checklist before enabling agents in production:

1. Ensure API keys are stored securely (env/secret manager).
2. Limit agent steps and runtime with `max_steps` and `timeout_seconds`.
3. Review and limit any tool integrations (file I/O, shell, network).
4. Add monitoring and human-in-the-loop approvals for critical operations.
