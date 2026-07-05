"""
BC field copilot agent.

Job: gives the Business Correspondent a live script, document checks, and
CBS (core banking system) auto-fill during the actual field visit.
"""

from typing import Any, Dict


class BCFieldAgent:
    def get_live_script(self, offer: Dict[str, Any]) -> str:
        """
        Return the live script text/steps the BC should follow for this offer.
        """
        # TODO: implement real script generation/lookup
        raise NotImplementedError

    def autofill_cbs_form(self, verified_documents: Dict[str, Any]) -> Dict[str, Any]:
        """
        MOCK: CBS auto-fill is mocked for the prototype. No real core banking
        system integration exists yet. Returns a mock filled-form payload.
        """
        raise NotImplementedError
