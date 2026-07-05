"""
Feedback and learning agent.

Job: closes the loop. Tracks what actually converted (which script,
channel, and timing worked) and retrains the upstream agents: orchestrator,
life-event, and product-fit.
"""

from typing import Any, Dict


class FeedbackAgent:
    def record_outcome(self, action: Dict[str, Any], converted: bool) -> None:
        """
        Record whether a given action (offer + channel + script) led to a
        successful conversion. This is the raw signal used for retraining.
        """
        # TODO: persist outcomes for later analysis/retraining
        raise NotImplementedError

    def retrain_upstream_agents(self) -> None:
        """
        Use recorded outcomes to update the life-event and product-fit
        agents' decision logic. For the prototype this can start as simple
        rule-weight adjustments rather than full model retraining.
        """
        # TODO: implement retraining/weight-update logic
        raise NotImplementedError
