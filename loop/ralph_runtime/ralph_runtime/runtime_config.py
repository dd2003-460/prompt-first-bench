"""Shared runtime policy defaults.

The runtime has one normal execution path: field-centric drafts with a
hybrid Hook policy.  Environment variables remain available for experiments,
but no entry point should silently fall back to the legacy card-centric path.
"""

from __future__ import annotations

import os
import re
from typing import Any, Mapping


HOOK_MODES = ("shadow", "hybrid", "enforce")
STOP_POLICIES = ("inline", "fresh")


def max_parallel_fields() -> int:
    """Bound simultaneous local-model field agents without changing the DAG."""

    try:
        # One worker is the safe default for local MLX/Qwen devices.  The DAG
        # still records parallel groups; users with enough memory can opt into
        # actual concurrency with RALPH_MAX_PARALLEL_FIELDS=2+.
        return max(1, int(os.environ.get("RALPH_MAX_PARALLEL_FIELDS", "1")))
    except ValueError:
        return 1


def max_field_web_attempts() -> int:
    """Bound external-tool calls per field before a deterministic fallback."""

    try:
        return max(1, int(os.environ.get("RALPH_MAX_FIELD_WEB_ATTEMPTS", "3")))
    except ValueError:
        return 3


def field_mode_enabled() -> bool:
    """Return whether incremental field editing is active.

    Field mode is the only supported execution path.  The historical
    ``RALPH_FIELD_GATE`` switch is intentionally ignored so different launch
    commands cannot silently select incompatible orchestration semantics.
    """

    return True


def flow_only_mode(state: Mapping[str, Any]) -> bool:
    """Return true only for an explicitly marked no-web workflow experiment.

    This is intentionally opt-in through the task description.  Production
    research tasks keep the normal evidence gate; a test task that explicitly
    says it does not require web research can still exercise dispatch,
    incremental apply, stage transitions, DAG joins, and exploration without
    inventing URLs.
    """

    if str(state.get("run_mode", "")).strip().lower() in {"flow_only", "test_flow"}:
        return True
    task = state.get("task", {})
    description = str(task.get("description", "")) if isinstance(task, Mapping) else ""
    return "不要求实际网页研究" in description or "flow_only" in description.lower()


def default_hook_mode() -> str:
    value = os.environ.get("RALPH_HOOK_MODE", "hybrid").strip().lower()
    return value if value in HOOK_MODES else "hybrid"


def default_stop_policy() -> str:
    """Choose how normal Claude Stop events continue a RALPH task.

    ``inline`` mirrors the Ralph Loop plugin: Stop is blocked and Claude sees
    a bounded continuation prompt in its existing transcript.  ``fresh`` is
    retained for memory-constrained experiments that deliberately want the
    outer supervisor to start a new context after each completed turn.
    """

    value = os.environ.get("RALPH_STOP_POLICY", "inline").strip().lower()
    return value if value in STOP_POLICIES else "inline"


# These are safety boundaries, not ordinary protocol guidance.  In hybrid
# mode only these classes remain hard-denied; ordinary policy feedback is
# returned as context while the tool is allowed to continue.
HARD_FEEDBACK_CODES = frozenset(
    {
        "STATE_FILE_PROTECTED",
        "STATE_FILE_PROTECTED_FIELD",
        "PROTECTED_PATH",
        "DANGEROUS_SIDE_EFFECT",
        "STAGE_POLICY_MISSING",
        "HUMAN_BLOCK_ACTIVE",
        "FIELD_TASK_MARKER_REQUIRED",
        "FIELD_AGENT_NOT_NEEDED",
        "FIELD_TASK_PATH_CORRECTION",
        "FIELD_WRITE_AFTER_READ",
        "FIELD_READ_LIMIT",
        "FIELD_TASK_DUPLICATE",
        "FIELD_WEB_FAILURE_LOOP",
        "FIELD_WEB_ATTEMPT_LIMIT",
        "FIELD_DISPATCH_FIRST_ESCALATED",
        "FIELD_DISPATCH_FIRST",
        "TOOL_STAGE_SCOPE_FIELD",
        "COMMANDER_BASH_SCOPE_FIELD",
        "ASK_USER_FIELD_GATE",
        "FIELD_TASK_DUPLICATE",
        "FIELD_TASK_CLAIM_LOST",
    }
)


def feedback_code(reason: str) -> str | None:
    match = re.search(r"RALPH_FEEDBACK\[([A-Z0-9_]+)\]", reason or "")
    return match.group(1) if match else None


def effective_tool_decision(decision: str, reason: str, mode: str) -> str:
    """Map an internal policy decision to Claude Code's effective decision."""

    if decision != "deny":
        return decision
    if mode == "shadow":
        return "allow"
    if mode == "hybrid" and feedback_code(reason) not in HARD_FEEDBACK_CODES:
        return "allow"
    return "deny"
