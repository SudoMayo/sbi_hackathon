"""
Life-event agent.

Job: detects life events and financial signals that indicate a person is
ready to be acquired as a customer. Example from the pitch: a seasonal
transaction pattern suggesting crop-insurance season is starting for a
household with no active policy.
"""

from typing import Any, Dict, Optional


class LifeEventAgent:
    def detect(self, signal: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Look at a raw signal (transaction pattern, BC field note, app usage gap)
        and decide whether it represents a life event worth acting on.

        Returns a life-event dict if one is detected, otherwise None.
        """
        # TODO: implement real detection logic (rules first, ML/LLM later)
        raise NotImplementedError
