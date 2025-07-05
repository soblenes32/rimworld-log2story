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
    assert captured["model"] == "text-davinci-003"
    assert captured["prompt"] == "hello"

