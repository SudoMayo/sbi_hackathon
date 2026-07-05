"""
Compliance and consent agent.

Job: a hard gate. Checks every action against RBI and DPDP rules before it
ever reaches a customer. This is deterministic rules logic, not an LLM call,
so decisions stay predictable and auditable.

No action from the orchestrator should reach a BC, app, or IVR channel
without clearing this agent first. Every decision made here must be logged
for audit, whether approved or blocked.
"""

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class ComplianceResult:
    approved: bool
    reason: str


class ComplianceAgent:
    def check(self, action: Dict[str, Any]) -> ComplianceResult:
        """
        Given a proposed action (offer + channel + person context), check it
        against RBI outreach/fair-practice rules and DPDP consent requirements.

        MOCK: RBI and DPDP rule sets are placeholders for the prototype.
        Replace with real, versioned rule definitions before any real deployment.
        """
        # TODO: implement real rule checks, always log the outcome
        raise NotImplementedError

    def log_decision(self, action: Dict[str, Any], result: ComplianceResult) -> None:
        """
        Persist an audit record of this compliance decision: what was
        decided, why, and by which agent/rule. Required for every action,
        approved or blocked.
        """
        # TODO: write to an audit log (file/db) for the prototype
        raise NotImplementedError
