import copy
import json
from pathlib import Path

from ralph_runtime.decomposition_benchmark import (
    DEFAULT_SIMPLE_GPU_TASK,
    evaluate_state,
    evaluate_task_spec,
)
from ralph_runtime.state import create_state


FIXTURE = Path(__file__).parent / "fixtures" / "decomposition_simple_gpu.json"


def fixture_spec():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def test_simple_gpu_fixture_passes_semantic_benchmark():
    fixture = fixture_spec()
    result = evaluate_task_spec(fixture["task_spec"], task=fixture["task"])

    assert result.passed is True
    assert result.score >= 0.8
    assert all(check["passed"] for check in result.checks)
    assert result.findings == ()


def test_benchmark_rejects_summary_with_empty_semantic_roles():
    fixture = fixture_spec()
    spec = copy.deepcopy(fixture["task_spec"])
    spec["semantic_map"]["uncertainty"] = []

    result = evaluate_task_spec(spec)

    assert result.passed is False
    assert any(item["code"] == "ROLE_EMPTY" for item in result.findings)


def test_benchmark_rejects_missing_hidden_attributes_and_scenarios():
    fixture = fixture_spec()
    spec = copy.deepcopy(fixture["task_spec"])
    spec["attribute_matrix"] = [
        leaf
        for leaf in spec["attribute_matrix"]
        if not any(word in str(leaf) for word in ("模型", "显存", "内存", "兼容", "功耗", "性能"))
    ]
    spec["scenarios"] = [{"id": "S1", "name": "默认场景"}]

    result = evaluate_task_spec(spec)

    assert result.passed is False
    codes = {item["code"] for item in result.findings}
    assert "HIDDEN_ATTRIBUTE_GAP" in codes
    assert "SCENARIO_COVERAGE_GAP" in codes


def test_benchmark_rejects_questions_for_explicit_or_researchable_facts():
    fixture = fixture_spec()
    spec = copy.deepcopy(fixture["task_spec"])
    spec["open_questions"] = [
        {
            "question": "是否需要 GPU？",
            "why_it_matters": "决定是否购买硬件",
            "recommended_option": "先确认",
        }
    ]

    result = evaluate_task_spec(spec)

    assert result.passed is False
    assert any(item["code"] == "UNNECESSARY_HUMAN_QUESTION" for item in result.findings)


def test_state_benchmark_uses_field_task_lifecycle_without_legacy_auditor():
    fixture = fixture_spec()
    state = create_state("decomposition-fixture", task=DEFAULT_SIMPLE_GPU_TASK)
    state["task_spec"] = copy.deepcopy(fixture["task_spec"])
    state["task_spec"]["status"] = "clarified"

    state["field_tasks"] = []
    result = evaluate_state(state)
    assert result.passed is True
    assert not any(item["code"] == "AUDITOR_NOT_COMPLETED" for item in result.findings)
