"""
Channel-segmentation agent.

Job: decides the right channel for this specific person: a BC home visit,
an app or IVR nudge, or a branch referral. Example from the pitch: a
household with low app usage gets a BC home visit rather than an app nudge.
"""

from typing import Any, Dict, Literal

Channel = Literal["bc_home_visit", "app_nudge", "ivr_nudge", "branch_referral"]


class ChannelAgent:
    def pick_channel(self, person_context: Dict[str, Any]) -> Channel:
        """
        Given context about a person (app usage, location, past interactions),
        return exactly one channel to use for this offer.
        """
        # TODO: implement real channel selection logic
        raise NotImplementedError
