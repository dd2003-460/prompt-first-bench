"""Project-local Markdown task board intake for the exploration node.

The board is intentionally small and boring: it reads ``tasks/TASKS.md``
without asking an Agent to infer state from prose, selects only tasks whose
dependencies are complete, and claims a selected row atomically.  It is an
adapter around the workflow, not a second workflow state machine.
"""

from __future__ import annotations

import os
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


class TaskBoardError(ValueError):
    """Raised when a task board cannot be read or safely updated."""


_ID_RE = re.compile(r"\b[A-Za-z][A-Za-z0-9_.-]*\b")
_PRIORITY_RE = re.compile(r"\bP(?P<number>\d+)\b", flags=re.IGNORECASE)
_CHECKBOX_RE = re.compile(r"^(?P<prefix>\s*-\s*\[)(?P<mark>[ xX~])(?P<suffix>\]\s*)(?P<body>.*)$")


def _clean_cell(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip())


def _split_table_cells(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or "|" not in stripped[1:]:
        return None
    body = stripped[1:]
    if body.endswith("|"):
        body = body[:-1]
    return [_clean_cell(cell) for cell in body.split("|")]


def _header_index(header: Iterable[str], aliases: set[str]) -> int | None:
    normalized = [re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "", value.lower()) for value in header]
    for index, value in enumerate(normalized):
        if value in aliases:
            return index
    return None


def _is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{2,}:?", cell.replace(" ", "")) for cell in cells)


def _normalize_status(raw: str, checkbox_mark: str | None = None) -> str:
    value = f"{raw} {checkbox_mark or ''}".strip().lower()
    if checkbox_mark and checkbox_mark.lower() == "x":
        return "completed"
    if checkbox_mark == "~":
        return "in_progress"
    if any(token in value for token in ("✅", "完成", "completed", "done")):
        return "completed"
    if any(token in value for token in ("人类", "等待确认", "阻塞", "blocked")):
        return "blocked_human"
    if any(token in value for token in ("🔄", "进行", "progress", "in_progress")):
        return "in_progress"
    if any(token in value for token in ("📋", "就绪", "ready", "可执行")):
        return "ready"
    if any(token in value for token in ("⏳", "待办", "pending", "todo")):
        return "pending"
    return "pending"


def _extract_priority(raw: str) -> str:
    match = _PRIORITY_RE.search(raw)
    return f"P{match.group('number')}" if match else "P9"


def _extract_dependencies(raw: str) -> tuple[str, ...]:
    value = raw.strip()
    if not value or value in {"-", "—", "–", "无", "none", "None"}:
        return ()
    values: list[str] = []
    for match in _ID_RE.finditer(value):
        token = match.group(0)
        if token.lower() in {"depends", "on", "dependency", "依赖"}:
            continue
        if token not in values:
            values.append(token)
    return tuple(values)


def _priority_number(priority: str) -> int:
    match = _PRIORITY_RE.fullmatch(priority)
    return int(match.group("number")) if match else 9


@dataclass(frozen=True)
class TaskBoardItem:
    task_id: str
    title: str
    status: str
    status_raw: str
    priority: str
    depends_on: tuple[str, ...]
    board_path: str
    line_number: int
    table_status_index: int | None = None
    checkbox: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "title": self.title,
            "status": self.status,
            "status_raw": self.status_raw,
            "priority": self.priority,
            "depends_on": list(self.depends_on),
            "source_path": self.board_path,
            "line_number": self.line_number,
        }

    def selection(self, reason: str | None = None) -> dict[str, Any]:
        value = self.to_dict()
        value.update(
            {
                "source": "task_board",
                "reason": reason or f"来自 {self.board_path} 的最高优先级、依赖已满足任务",
            }
        )
        return value


def _item_from_table(
    cells: list[str],
    line_number: int,
    board_path: str,
    indexes: dict[str, int | None],
) -> TaskBoardItem | None:
    id_index = indexes["id"]
    title_index = indexes["title"]
    if id_index is None or title_index is None or id_index >= len(cells) or title_index >= len(cells):
        return None
    task_id = re.sub(r"[`*_]", "", cells[id_index]).strip()
    title = cells[title_index].strip()
    if not task_id or not title or task_id.lower() in {"id", "编号"}:
        return None
    status_index = indexes["status"]
    priority_index = indexes["priority"]
    dependency_index = indexes["depends_on"]
    status_raw = cells[status_index] if status_index is not None and status_index < len(cells) else ""
    priority_raw = cells[priority_index] if priority_index is not None and priority_index < len(cells) else ""
    dependency_raw = cells[dependency_index] if dependency_index is not None and dependency_index < len(cells) else ""
    return TaskBoardItem(
        task_id=task_id,
        title=title,
        status=_normalize_status(status_raw),
        status_raw=status_raw,
        priority=_extract_priority(priority_raw or "P9"),
        depends_on=_extract_dependencies(dependency_raw),
        board_path=board_path,
        line_number=line_number,
        table_status_index=status_index,
        checkbox=False,
    )


def _item_from_checkbox(body: str, mark: str, line_number: int, board_path: str) -> TaskBoardItem | None:
    match = re.match(r"(?P<id>[A-Za-z][A-Za-z0-9_.-]*)\s*(?:[:：\-]\s*)?(?P<title>.*)$", body.strip())
    if not match or not match.group("title").strip():
        return None
    title = match.group("title").strip()
    priority = _extract_priority(body)
    dependency_match = re.search(r"(?:依赖|depends_on|depends on)\s*[:：]?\s*(.*)$", body, flags=re.IGNORECASE)
    dependency_raw = dependency_match.group(1) if dependency_match else ""
    return TaskBoardItem(
        task_id=match.group("id"),
        title=title,
        status=_normalize_status(body, mark),
        status_raw=f"[{mark}]",
        priority=priority,
        depends_on=_extract_dependencies(dependency_raw),
        board_path=board_path,
        line_number=line_number,
        checkbox=True,
    )


def parse_task_board(text: str, board_path: str = "tasks/TASKS.md") -> list[TaskBoardItem]:
    """Parse Markdown tables and simple checkbox boards into task items."""

    lines = text.splitlines()
    items: list[TaskBoardItem] = []
    header: list[str] | None = None
    indexes: dict[str, int | None] = {}
    for line_number, line in enumerate(lines, start=1):
        checkbox = _CHECKBOX_RE.match(line)
        if checkbox:
            item = _item_from_checkbox(checkbox.group("body"), checkbox.group("mark"), line_number, board_path)
            if item:
                items.append(item)
            continue
        cells = _split_table_cells(line)
        if cells is None:
            continue
        if header is None:
            normalized = " ".join(cells).lower()
            if not any(token in normalized for token in ("id", "编号")):
                continue
            if not any(token in normalized for token in ("任务", "task", "title", "目标")):
                continue
            header = cells
            indexes = {
                "id": _header_index(header, {"id", "编号", "taskid", "任务编号"}),
                "title": _header_index(header, {"任务", "task", "title", "目标", "任务名称"}),
                "status": _header_index(header, {"状态", "status", "state"}),
                "priority": _header_index(header, {"优先级", "priority", "prio"}),
                "depends_on": _header_index(header, {"依赖", "dependson", "dependencies", "前置条件"}),
            }
            continue
        if _is_separator(cells):
            continue
        item = _item_from_table(cells, line_number, board_path, indexes)
        if item:
            items.append(item)
    return items


def read_task_board(project_root: str | Path, board_path: str = "tasks/TASKS.md") -> list[TaskBoardItem]:
    root = Path(project_root).expanduser().resolve()
    candidate = (root / board_path).resolve()
    if root not in candidate.parents and candidate != root:
        raise TaskBoardError("task board path must stay inside the project")
    if not candidate.exists():
        return []
    if not candidate.is_file():
        raise TaskBoardError(f"task board is not a file: {candidate}")
    return parse_task_board(candidate.read_text(encoding="utf-8"), board_path=board_path)


def select_next_task(project_root: str | Path, board_path: str = "tasks/TASKS.md") -> TaskBoardItem | None:
    """Return the highest-priority ready task with completed dependencies."""

    items = read_task_board(project_root, board_path)
    by_id = {item.task_id: item for item in items}
    eligible: list[TaskBoardItem] = []
    for item in items:
        if item.status not in {"ready", "pending"}:
            continue
        if any(dependency not in by_id or by_id[dependency].status != "completed" for dependency in item.depends_on):
            continue
        eligible.append(item)
    eligible.sort(key=lambda item: (_priority_number(item.priority), 0 if item.status == "ready" else 1, item.line_number, item.task_id))
    return eligible[0] if eligible else None


def _replace_table_status(line: str, item: TaskBoardItem, value: str) -> str:
    cells = _split_table_cells(line)
    if cells is None or item.table_status_index is None or item.table_status_index >= len(cells):
        raise TaskBoardError(f"cannot locate status column for task {item.task_id}")
    cells[item.table_status_index] = value
    indentation = line[: len(line) - len(line.lstrip())]
    return indentation + "| " + " | ".join(cells) + " |\n"


def _replace_checkbox_status(line: str) -> str:
    match = _CHECKBOX_RE.match(line)
    if not match:
        raise TaskBoardError("cannot locate checkbox status")
    return f"{match.group('prefix')}~{match.group('suffix')}{match.group('body')}\n"


def claim_task_reference(
    project_root: str | Path,
    task_id: str,
    source_path: str = "tasks/TASKS.md",
    claimant: str = "ralph",
) -> dict[str, Any]:
    """Mark one selected board task in progress, atomically and idempotently."""

    root = Path(project_root).expanduser().resolve()
    board = (root / source_path).resolve()
    if root not in board.parents or not board.exists():
        raise TaskBoardError(f"task board does not exist inside project: {source_path}")
    original = board.read_text(encoding="utf-8")
    items = parse_task_board(original, board_path=source_path)
    item = next((candidate for candidate in items if candidate.task_id == task_id), None)
    if item is None:
        raise TaskBoardError(f"task {task_id!r} was not found in {source_path}")
    if item.status == "completed":
        raise TaskBoardError(f"task {task_id!r} is already completed")
    if item.status == "blocked_human":
        raise TaskBoardError(f"task {task_id!r} is blocked by human input")
    if item.status == "in_progress" and "RALPH:" in item.status_raw:
        return item.to_dict() | {"claim_status": "already_claimed"}
    next_item = select_next_task(root, source_path)
    if next_item is None or next_item.task_id != item.task_id:
        expected = next_item.task_id if next_item is not None else "none"
        raise TaskBoardError(
            f"task {task_id!r} is not the next eligible board task; expected {expected!r}"
        )
    lines = original.splitlines(keepends=True)
    if item.checkbox:
        lines[item.line_number - 1] = _replace_checkbox_status(lines[item.line_number - 1])
    else:
        marker = str(claimant).strip() or "ralph"
        lines[item.line_number - 1] = _replace_table_status(
            lines[item.line_number - 1], item, f"🔄 进行中（RALPH:{marker}）"
        )
    encoded = "".join(lines)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{board.name}.", suffix=".tmp", dir=board.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, board)
    finally:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)
    return item.to_dict() | {"claim_status": "claimed", "claimant": claimant}
