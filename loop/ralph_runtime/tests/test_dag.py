import pytest

from ralph_runtime.dag import DAGValidationError, ready_tasks, validate_plan


def base_plan():
    return {
        "nodes": [
            {"id": "T1.1", "execution_mode": "parallel", "parallel_group_id": "G1", "orthogonal_key": "price", "writes": ["price.json"]},
            {"id": "T1.2", "execution_mode": "parallel", "parallel_group_id": "G1", "orthogonal_key": "driver", "writes": ["driver.json"]},
            {"id": "J1", "depends_on": ["T1.1", "T1.2"], "input_refs": ["T1.1.output", "T1.2.output"], "output_schema": {"type": "object"}, "writes": ["join.json"]}
        ]
    }


def test_parallel_group_and_join_are_valid():
    report = validate_plan(base_plan())
    assert report.parallel_groups["G1"] == ("T1.1", "T1.2")
    assert report.ready == ("T1.1", "T1.2")
    assert ready_tasks(base_plan(), ["T1.1", "T1.2"]) == ("J1",)


def test_cycle_is_rejected():
    with pytest.raises(DAGValidationError, match="cycle"):
        validate_plan({"nodes": [
            {"id": "A", "depends_on": ["B"]},
            {"id": "B", "depends_on": ["A"]},
        ]}, strict=False)


def test_parallel_write_conflict_is_rejected():
    plan = base_plan()
    plan["nodes"][1]["writes"] = ["price.json"]
    with pytest.raises(DAGValidationError, match="write conflict"):
        validate_plan(plan)


def test_cross_layer_requires_contract():
    with pytest.raises(DAGValidationError, match="input_refs"):
        validate_plan({"nodes": [{"id": "A"}, {"id": "B", "depends_on": ["A"]}]})
