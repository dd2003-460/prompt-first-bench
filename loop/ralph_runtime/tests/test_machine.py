from ralph_runtime.machine import PromptWorkflowMachine, transition_for_action


def test_state_machine_advances_fixed_nodes():
    machine = PromptWorkflowMachine()
    machine.send("advance_01")
    machine.send("advance_02")
    assert machine.current_state_value == "stage_03"


def test_state_machine_can_block_and_skip():
    machine = PromptWorkflowMachine()
    machine.send("block_01")
    machine.send("skip_to_02")
    assert machine.current_state_value == "stage_02"


def test_transition_adapter_uses_library_machine():
    assert transition_for_action("01", "running", "advance", "02", None) == "stage_02"
    assert transition_for_action("02", "running", "rollback", None, "01") == "stage_01"


def test_exploration_resumes_the_ordered_flow():
    assert transition_for_action("exploration", "exploration", "advance", "01", None) == "stage_01"
