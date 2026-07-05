"""
Product-fit agent.

Job: chooses the single right product for a specific person, not a generic
broadcast of multiple offers. If a life event points to crop-insurance
season, this agent should return one starter crop-insurance product, not a
ranked list.
"""

from typing import Any, Dict


class ProductFitAgent:
    def choose_offer(self, life_event: Dict[str, Any]) -> Dict[str, Any]:
        """
        Given a detected life event, return exactly one recommended product/offer.
        """
        # TODO: implement real product matching logic
        raise NotImplementedError
