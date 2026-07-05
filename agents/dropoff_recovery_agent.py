"""
Drop-off recovery agent.

Job: detects a stalled onboarding (a customer or BC interaction that started
but didn't finish) and schedules a human follow-up.
"""

from typing import Any, Dict, Optional


class DropoffRecoveryAgent:
    def detect_stall(self, session: Dict[str, Any]) -> bool:
        """
        Given an onboarding session's state, decide whether it has stalled.
        """
        # TODO: implement real stall detection (e.g. time since last step)
        raise NotImplementedError

    def schedule_followup(self, session: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Schedule a human follow-up for a stalled session. Returns the
        follow-up task, or None if no follow-up is needed.
        """
        # TODO: implement real follow-up scheduling
        raise NotImplementedError
