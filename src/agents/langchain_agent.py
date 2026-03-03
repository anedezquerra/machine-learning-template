"""Example LangChain integration adapter.

This file demonstrates how a small adapter could wrap LangChain usage.
It's intentionally optional and isolated so projects can remove it if they
prefer another orchestrator.
"""
try:
    from langchain import OpenAI
    from langchain.chains import LLMChain
    from langchain.prompts import PromptTemplate
except Exception:  # pragma: no cover - optional dependency
    OpenAI = None
    LLMChain = None
    PromptTemplate = None


class LangChainAdapter:
    def __init__(self, model: str = "gpt-4o-mini", **kwargs):
        if OpenAI is None:
            raise RuntimeError("langchain is not installed")
        self.llm = OpenAI(model_name=model, **kwargs)

    def generate(self, prompt: str, **kwargs):
        if LLMChain is None or PromptTemplate is None:
            raise RuntimeError("langchain components not installed")
        prompt_template = PromptTemplate(input_variables=["input"], template="{input}")
        chain = LLMChain(llm=self.llm, prompt=prompt_template)
        out = chain.run(input=prompt)
        return {"text": out}
