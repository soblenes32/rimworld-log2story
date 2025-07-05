import openai


def complete_prompt(api_key: str, prompt: str, model: str = "text-davinci-003") -> str:
    """Submit a prompt to the OpenAI completions API and return the response text.

    Parameters
    ----------
    api_key : str
        OpenAI API key to authenticate the request.
    prompt : str
        Text prompt to send to the API.
    model : str, optional
        Model name to use for completion, by default ``text-davinci-003``.

    Returns
    -------
    str
        The text of the completion response.
    """
    openai.api_key = api_key
    response = openai.Completion.create(model=model, prompt=prompt)
    return response.choices[0].text.strip()

