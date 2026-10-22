"""Task DAG validation for serial/parallel RALPH plans."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable, Mapping


class DAGValidationError(ValueError):
    """Raised when a task plan is not executable."""


@dataclass(frozen=True)
class TaskNode:
    id: str
    parent_id: str | None
    depends_on: tuple[str, ...]
    execution_mode: str
    parallel_group_id: str | None
    input_refs: tuple[str, ...]
    output_schema: Mapping[str, Any]
    preconditions: tuple[str, ...]
    postconditions: tuple[str, ...]
    writes: tuple[str, ...]
    orthogonal_key: str | None

    @classmethod
    def from_mapping(cls, raw: Mapping[str, Any]) -> "TaskNode":
        task_id = str(raw.get("id", ""))
        if not task_id:
            raise DAGValidationError("task node requires id")
        mode = str(raw.get("execution_mode", "serial"))
        if mode not in {"serial", "parallel"}:
            raise DAGValidationError(f"unsupported execution_mode for {task_id}: {mode}")
        return cls(
            id=task_id,
            parent_id=str(raw["parent_id"]) if raw.get("parent_id") is not None else None,
            depends_on=tuple(str(x) for x in raw.get("depends_on", ())),
            execution_mode=mode,
            parallel_group_id=str(raw["parallel_group_id"]) if raw.get("parallel_group_id") is not None else None,
            input_refs=tuple(str(x) for x in raw.get("input_refs", ())),
            output_schema=raw.get("output_schema", {}) if isinstance(raw.get("output_schema", {}), Mapping) else {},
            preconditions=tuple(str(x) for x in raw.get("preconditions", ())),
            postconditions=tuple(str(x) for x in raw.get("postconditions", ())),
            writes=tuple(str(x) for x in raw.get("writes", ())),
            orthogonal_key=str(raw["orthogonal_key"]) if raw.get("orthogonal_key") is not None else None,
        )


@dataclass(frozen=True)
class DAGReport:
    node_ids: tuple[str, ...]
    ready: tuple[str, ...]
    parallel_groups: dict[str, tuple[str, ...]]


def _cycle_check(nodes: Mapping[str, TaskNode]) -> None:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node_id: str) -> None:
        if node_id in visiting:
            raise DAGValidationError(f"task DAG contains a cycle at {node_id}")
        if node_id in visited:
            return
        visiting.add(node_id)
        for dependency in nodes[node_id].depends_on:
            visit(dependency)
        visiting.remove(node_id)
        visited.add(node_id)

    for node_id in nodes:
        visit(node_id)


def validate_plan(plan: Mapping[str, Any], strict: bool = True) -> DAGReport:
    raw_nodes = plan.get("nodes", [])
    if not isinstance(raw_nodes, list):
        raise DAGValidationError("plan.nodes must be an array")
    nodes_list = [TaskNode.from_mapping(raw) for raw in raw_nodes]
    nodes: dict[str, TaskNode] = {}
    for node in nodes_list:
        if node.id in nodes:
            raise DAGValidationError(f"duplicate task id: {node.id}")
        nodes[node.id] = node

    for node in nodes_list:
        for dependency in node.depends_on:
            if dependency not in nodes:
                raise DAGValidationError(f"{node.id} depends on missing task {dependency}")
        if node.parent_id and node.parent_id not in nodes:
            raise DAGValidationError(f"{node.id} has missing parent {node.parent_id}")
        if node.depends_on and strict and (not node.input_refs or not node.output_schema):
            raise DAGValidationError(
                f"{node.id} needs input_refs and output_schema when it consumes another layer"
            )
    _cycle_check(nodes)

    raw_joins = plan.get("joins", [])
    if raw_joins is not None and not isinstance(raw_joins, list):
        raise DAGValidationError("plan.joins must be an array")
    for raw_join in raw_joins or []:
        if isinstance(raw_join, str):
            join_id = raw_join
            declared_dependencies = None
        elif isinstance(raw_join, Mapping):
            join_id = str(raw_join.get("id", raw_join.get("node_id", "")))
            declared_dependencies = raw_join.get("depends_on")
        else:
            raise DAGValidationError("each join must be a node id or object")
        if join_id not in nodes:
            raise DAGValidationError(f"join references missing task: {join_id}")
        dependencies = nodes[join_id].depends_on
        if len(dependencies) < 2:
            raise DAGValidationError(f"join {join_id} must depend on at least two tasks")
        if declared_dependencies is not None:
            declared = tuple(str(item) for item in declared_dependencies)
            if set(declared) != set(dependencies):
                raise DAGValidationError(f"join {join_id} depends_on does not match its node")

    groups: dict[str, list[TaskNode]] = {}
    for node in nodes_list:
        if node.parallel_group_id:
            groups.setdefault(node.parallel_group_id, []).append(node)
    for group_id, members in groups.items():
        if len(members) < 2:
            raise DAGValidationError(f"parallel group {group_id} must contain at least two tasks")
        if any(member.execution_mode != "parallel" for member in members):
            raise DAGValidationError(f"parallel group {group_id} contains a serial task")
        if strict:
            keys = [member.orthogonal_key for member in members]
            if any(key is None for key in keys):
                raise DAGValidationError(f"parallel group {group_id} requires orthogonal_key on every task")
            if len(set(keys)) != len(keys):
                raise DAGValidationError(f"parallel group {group_id} has duplicate orthogonal_key")

    write_owners: dict[str, str] = {}
    for node in nodes_list:
        for path in node.writes:
            if path in write_owners:
                raise DAGValidationError(f"write conflict: {path} used by {write_owners[path]} and {node.id}")
            write_owners[path] = node.id

    completed = set(plan.get("completed", []))
    ready = tuple(
        node.id for node in nodes_list
        if node.id not in completed and all(dependency in completed for dependency in node.depends_on)
    )
    return DAGReport(
        node_ids=tuple(node.id for node in nodes_list),
        ready=ready,
        parallel_groups={group_id: tuple(member.id for member in members) for group_id, members in groups.items()},
    )


def ready_tasks(plan: Mapping[str, Any], completed: Iterable[str] = ()) -> tuple[str, ...]:
    copy = dict(plan)
    copy["completed"] = list(completed)
    return validate_plan(copy, strict=False).ready
