"""
Vernacular conversation agent (copilot).

Job: dialect-aware voice guidance for BC-assisted and IVR interactions.
Guides the conversation, verifies documents, and helps fill the CBS form
in real time. Week 3 of the 30-day plan starts this in Hindi.
"""

from typing import Any, Dict


class VernacularCopilot:
    def __init__(self, language: str = "hi") -> None:
        self.language = language

    def start_conversation(self, offer: Dict[str, Any]) -> Dict[str, Any]:
        """
        Begin a guided onboarding conversation for the given offer, in the
        configured language. Returns the conversation/session state.
        """
        # TODO: wire to the Anthropic API for real dialogue generation
        raise NotImplementedError

    def verify_documents(self, documents: Dict[str, Any]) -> bool:
        """
        MOCK: document verification (OCR + liveness) is mocked for the
        prototype. Replace with a real verification service later.
        """
        raise NotImplementedError
