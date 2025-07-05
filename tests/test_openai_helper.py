import types

import src.openai_helper as openai_helper


class DummyResponse:
    def __init__(self, text):
        self.choices = [types.SimpleNamespace(text=text)]


def test_complete_prompt(monkeypatch):
    captured = {}

    def fake_create(**kwargs):
        captured.update(kwargs)
        return DummyResponse("result text")

    monkeypatch.setattr(openai_helper.openai.Completion, "create", fake_create)

    text = openai_helper.complete_prompt("key", "hello")

    assert text == "result text"
    assert captured["model"] == "gpt-4.1"
    assert captured["prompt"] == "hello"


def test_complete_prompt_custom_model(monkeypatch):
    captured = {}

    def fake_create(**kwargs):
        captured.update(kwargs)
        return DummyResponse("alt")

    monkeypatch.setattr(openai_helper.openai.Completion, "create", fake_create)

    text = openai_helper.complete_prompt("key", "hi", model="gpt-3.5")

    assert text == "alt"
    assert captured["model"] == "gpt-3.5"
    assert captured["prompt"] == "hi"

