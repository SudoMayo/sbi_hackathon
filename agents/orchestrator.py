"""
Orchestrator agent.

Job: owns shared state and routes tasks between every other agent.
This is the entry point of the whole pipeline. A signal comes in here first,
then gets handed off to the life-event, product-fit, and channel-segmentation
agents, then to the compliance gate, then to execution.

Do not let any code path skip the compliance agent before execution.
"""

from typing import Any, Dict


class OrchestratorAgent:
    def __init__(self) -> None:
        # TODO: hold references to the other agents once they exist
        # e.g. self.life_event_agent = LifeEventAgent()
        pass

    def handle_signal(self, signal: Dict[str, Any]) -> Dict[str, Any]:
        """
        Entry point for a new signal (transaction, BC field activity, or app usage).

        Expected flow:
        1. Pass signal to the life-event agent to detect readiness.
        2. If a life event is detected, pass to the product-fit agent for one offer.
        3. Pass to the channel-segmentation agent to pick BC visit / app / IVR / branch.
        4. Pass the resulting decision through the compliance and consent agent.
        5. If cleared, hand off to the vernacular copilot / BC field agent for execution.
        6. Log the outcome for the feedback agent to learn from later.
        """
        # TODO: implement the routing above
        raise NotImplementedError
