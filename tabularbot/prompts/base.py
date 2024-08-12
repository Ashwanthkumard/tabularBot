from typing import Optional


class BasePrompt:
    """Use this Interface to create any new prompts that suits your requirement"""
    prompt: Optional[str] = None

    def validate(self, prompt) -> bool:
        return isinstance(prompt, str)
