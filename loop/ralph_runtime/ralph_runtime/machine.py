"""Small fixed-node StateMachine used by the first MVP."""

from __future__ import annotations

from statemachine import State, StateMachine


STAGES = ("01", "02", "02.5", "03", "04", "04.5", "05", "06")

# Ordered successor for the `advance` action.  The new pipeline inserts the
# cross-validation stages 02.5 (after research) and 04.5 (after verification);
# 05/06 are retained as reachable states for in-flight legacy tasks but are no
# longer on the advance path.
STAGE_SUCCESSOR = {
    "01": "02",
    "02": "02.5",
    "02.5": "03",
    "03": "04",
    "04": "04.5",
    "04.5": "exploration",
    "05": "06",
    "06": "exploration",
}


class PromptWorkflowMachine(StateMachine):
    stage_01 = State("01", initial=True)
    stage_02 = State("02")
    stage_02_5 = State("02.5")
    stage_03 = State("03")
    stage_04 = State("04")
    stage_04_5 = State("04.5")
    stage_05 = State("05")
    stage_06 = State("06")
    blocked_human = State("blocked_human")
    exploration = State("exploration")
    completed = State("completed", final=True)
    stopped = State("stopped", final=True)

    advance_01 = stage_01.to(stage_02)
    advance_02 = stage_02.to(stage_02_5)
    advance_02_5 = stage_02_5.to(stage_03)
    advance_03 = stage_03.to(stage_04)
    advance_04 = stage_04.to(stage_04_5)
    advance_04_5 = stage_04_5.to(exploration)
    advance_05 = stage_05.to(stage_06)  # legacy, off-path
    advance_06 = stage_06.to(exploration)  # legacy, off-path

    retry_01 = stage_01.to(stage_01)
    retry_02 = stage_02.to(stage_02)
    retry_02_5 = stage_02_5.to(stage_02_5)
    retry_03 = stage_03.to(stage_03)
    retry_04 = stage_04.to(stage_04)
    retry_04_5 = stage_04_5.to(stage_04_5)
    retry_05 = stage_05.to(stage_05)
    retry_06 = stage_06.to(stage_06)

    rollback_02 = stage_02.to(stage_01)
    rollback_02_5 = stage_02_5.to(stage_02)
    rollback_03 = stage_03.to(stage_02)
    rollback_04 = stage_04.to(stage_03)
    rollback_04_5 = stage_04_5.to(stage_04)
    rollback_05 = stage_05.to(stage_02)
    rollback_06 = stage_06.to(stage_06)

    block_01 = stage_01.to(blocked_human)
    block_02 = stage_02.to(blocked_human)
    block_02_5 = stage_02_5.to(blocked_human)
    block_03 = stage_03.to(blocked_human)
    block_04 = stage_04.to(blocked_human)
    block_04_5 = stage_04_5.to(blocked_human)
    block_05 = stage_05.to(blocked_human)
    block_06 = stage_06.to(blocked_human)
    block_exploration = exploration.to(blocked_human)

    explore_01 = stage_01.to(exploration)
    explore_02 = stage_02.to(exploration)
    explore_02_5 = stage_02_5.to(exploration)
    explore_03 = stage_03.to(exploration)
    explore_04 = stage_04.to(exploration)
    explore_04_5 = stage_04_5.to(exploration)
    explore_05 = stage_05.to(exploration)
    explore_06 = stage_06.to(exploration)
    explore_exploration = exploration.to(exploration)

    skip_to_01 = blocked_human.to(stage_01)
    skip_to_02 = blocked_human.to(stage_02)
    skip_to_02_5 = blocked_human.to(stage_02_5)
    skip_to_03 = blocked_human.to(stage_03)
    skip_to_04 = blocked_human.to(stage_04)
    skip_to_04_5 = blocked_human.to(stage_04_5)
    skip_to_05 = blocked_human.to(stage_05)
    skip_to_06 = blocked_human.to(stage_06)
    skip_to_exploration = blocked_human.to(exploration)
    explore_blocked = blocked_human.to(exploration)
    stop_blocked = blocked_human.to(stopped)

    resume_exploration = exploration.to(stage_01)
    complete_exploration = exploration.to(completed)
    stop_exploration = exploration.to(stopped)


def internal_state(stage_id: str, status: str = "running") -> str:
    if status == "blocked_human":
        return "blocked_human"
    if status == "exploration":
        return "exploration"
    if status == "completed":
        return "completed"
    if status == "stopped":
        return "stopped"
    if stage_id not in STAGES:
        raise ValueError(f"unsupported fixed MVP stage: {stage_id}")
    # State attribute names cannot contain dots, so "02.5" -> "stage_02_5".
    return f"stage_{stage_id.replace('.', '_')}"


def transition_for_action(stage_id: str, status: str, action: str, next_stage: str | None, rollback_to: str | None) -> str:
    machine = PromptWorkflowMachine(start_value=internal_state(stage_id, status))
    # StateMachine event attributes cannot contain dots, so sanitize stage ids
    # like "02.5" -> "02_5" when building event names.
    ev = lambda base: f"{base}_{stage_id.replace('.', '_')}"
    if action == "advance":
        if stage_id == "exploration" and next_stage == "01":
            event = "resume_exploration"
        elif stage_id == "exploration" and next_stage == "completed":
            event = "complete_exploration"
        else:
            expected = STAGE_SUCCESSOR.get(stage_id)
            event = ev("advance") if next_stage == expected else None
    elif action == "rollback":
        event = ev("rollback") if rollback_to else None
        if stage_id == "01" and rollback_to == "01":
            event = "retry_01"
    elif action == "blocked_human":
        event = "block_exploration" if stage_id == "exploration" else ev("block")
    elif action == "explore":
        event = ev("explore")
    elif action == "skip_blocked":
        if machine.current_state_value != "blocked_human":
            raise ValueError("skip_blocked requires the persisted state to be blocked_human")
        event = f"skip_to_{next_stage.replace('.', '_')}" if next_stage else None
    else:
        return machine.current_state_value
    if event is None or not machine.allowed_events:
        raise ValueError(f"illegal {action} transition from {stage_id}")
    machine.send(event)
    return machine.current_state_value
