from typing import Protocol, Dict, Any


class Adapter(Protocol):
    """Adapter interface for LLM providers. Implementations must be test-friendly.
    """

    def generate(self, prompt: str, **kwargs: Any) -> Dict[str, Any]:
        ...


class MockAdapter:
    """Simple synchronous mock adapter used for tests and CI.

    Returns predictable responses and does not call external services.
    """

    def __init__(self, response: str = "mock response"):
        self.response = response

    def generate(self, prompt: str, **kwargs: Any) -> Dict[str, Any]:
        return {"text": self.response, "prompt": prompt}


class OpenAIAdapter:
    """A tiny wrapper around OpenAI completions. Optional; requires `openai`.

    This is intentionally minimal. For production, prefer using a robust
    adapter (backoff, async support, retries, streaming).
    """

    def __init__(self, client, model: str = "gpt-4o-mini"):
        self.client = client
        self.model = model

    def generate(self, prompt: str, **kwargs: Any) -> Dict[str, Any]:
        resp = self.client.create(model=self.model, prompt=prompt, **kwargs)
        return {"text": resp.choices[0].text if hasattr(resp, "choices") else str(resp)}
