"""Prompt-first RALPH workflow with Markdown as the only user-facing state.

This path deliberately does *not* judge the semantics of a factor breakdown,
research note, plan, or review.  It keeps only a tiny durable cursor so an
inline Stop Hook can remind the same Claude context what to do next.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

try:
    import fcntl
except ImportError:  # pragma: no cover - Windows fallback
    fcntl = None

from .events import append_observation


STATE_FILE = "ralph-loop.md"
ARTIFACT_DIR = Path("loop-artifacts") / "prompt-first"
PROMPT_DIR = Path("loop") / "prompt-first"
REVIEW_DIR = ARTIFACT_DIR / "reviews"
LATEST_REVIEW = ARTIFACT_DIR / "latest-review.md"
REVIEW_LOCK = ARTIFACT_DIR / ".review.lock"
DONE_MARKER = "<!-- ralph: done -->"
REVIEW_START = "<!-- ralph-review"
REVIEW_END = "-->"
PENDING_TASK = "待填写：请用 `ralph loop <项目目录> <任务>` 提供明确任务。"


@dataclass(frozen=True)
class PromptStage:
    id: str
    slug: str
    title: str


STAGES: tuple[PromptStage, ...] = (
    PromptStage(
        "01",
        "factor-decomposition",
        "目标、因素与空缺条件",
    ),
    PromptStage(
        "02",
        "research",
        "资料搜集与网页 AI 交叉询问",
    ),
    PromptStage(
        "02.5",
        "cross-check",
        "交叉核验与矛盾",
    ),
    PromptStage(
        "03",
        "action-plan",
        "具体行动分解",
    ),
    PromptStage(
        "04",
        "execution-review",
        "执行与结果核对",
    ),
    PromptStage(
        "04.5",
        "independent-review",
        "独立复核与下一步",
    ),
)

_STAGE_BY_ID = {stage.id: stage for stage in STAGES}
_STAGE_PROMPT_FILES = {
    "01": "01-goal-decomposition.md",
    "02": "02-information-research.md",
    "02.5": "02.5-cross-check.md",
    "03": "03-action-decomposition.md",
    "04": "04-execution-verification.md",
    "04.5": "04.5-final-review.md",
}
_STATE_START = "<!-- ralph-prompt-state"
_STATE_END = "-->"


def state_path(root: str | Path) -> Path:
    return Path(root).expanduser().resolve() / STATE_FILE


def stage_for(stage_id: str) -> PromptStage:
    try:
        return _STAGE_BY_ID[str(stage_id)]
    except KeyError as exc:
        raise ValueError(f"unknown prompt-first stage: {stage_id}") from exc


def stage_prompt_path(root: str | Path, stage_id: str) -> Path | None:
    """Resolve the editable stage rules, preferring a project override."""

    stage_for(stage_id)
    filename = _STAGE_PROMPT_FILES[str(stage_id)]
    candidates = [
        Path(root).expanduser().resolve() / PROMPT_DIR / filename,
        Path(__file__).resolve().parents[3] / PROMPT_DIR / filename,
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return None


def load_stage_rules(root: str | Path, stage_id: str) -> dict[str, str]:
    """Load the human-editable operation and review rules for one stage."""

    stage = stage_for(stage_id)
    path = stage_prompt_path(root, stage.id)
    if path is None:
        return {
            "path": "",
            "text": (
                f"未找到阶段 {stage.id} 的外部规则文件。请创建 "
                f"`{PROMPT_DIR / _STAGE_PROMPT_FILES[stage.id]}`，"
                "不要把本阶段质检标准写回 Python。"
            ),
        }
    common_candidates = [
        Path(root).expanduser().resolve() / PROMPT_DIR / "00-common-review.md",
        Path(__file__).resolve().parents[3] / PROMPT_DIR / "00-common-review.md",
    ]
    common = next((candidate for candidate in common_candidates if candidate.is_file()), None)
    common_text = common.read_text(encoding="utf-8").strip() if common else ""
    stage_text = path.read_text(encoding="utf-8").strip()
    combined = f"{common_text}\n\n---\n\n{stage_text}".strip() if common_text else stage_text
    source = f"{common}, {path}" if common else str(path)
    return {"path": source, "text": combined}


def artifact_sha256(path: str | Path) -> str:
    text = Path(path).read_text(encoding="utf-8").replace(DONE_MARKER, "").rstrip() + "\n"
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _review_field(block: str, key: str) -> str:
    match = re.search(
        rf"^\s*{re.escape(key)}\s*:\s*(.*?)\s*$",
        block,
        re.IGNORECASE | re.MULTILINE,
    )
    return match.group(1).strip() if match else ""


def _parse_reviewer_block(text: str) -> dict[str, str] | None:
    blocks = re.findall(
        rf"{re.escape(REVIEW_START)}\s*\n(.*?)\n{re.escape(REVIEW_END)}",
        text,
        re.DOTALL,
    )
    if not blocks:
        return None
    block = blocks[-1].strip()
    verdict = _review_field(block, "verdict").lower()
    if verdict not in {"pass", "revise"}:
        verdict = "unknown"
    return {
        "verdict": verdict,
        "reviewed_stage": _review_field(block, "reviewed_stage"),
        "repair_stage": _review_field(block, "repair_stage"),
        "artifact_sha256": _review_field(block, "artifact_sha256"),
        "reviewed_before_done": _review_field(block, "reviewed_before_done"),
        "reviewer_exit_code": _review_field(block, "reviewer_exit_code"),
        "block": block,
    }


def _structured_reviewer_text(raw: str) -> str:
    """Render Claude Code structured Reviewer output as the canonical Markdown input.

    The local provider can spend a long time elaborating when asked for free-form
    Markdown.  The CLI therefore requests a compact structured response, while
    this runtime keeps the durable artifact and review history Markdown-only.
    Keep the free-form parser as a compatibility fallback for older runs/tests.
    """

    try:
        envelope = json.loads(raw)
    except (TypeError, ValueError, json.JSONDecodeError):
        return raw
    if not isinstance(envelope, dict):
        return raw
    payload = envelope.get("structured_output", envelope)
    if isinstance(payload, str):
        try:
            payload = json.loads(payload)
        except (TypeError, ValueError, json.JSONDecodeError):
            return raw
    if not isinstance(payload, dict) or "verdict" not in payload:
        return raw

    verdict = str(payload.get("verdict", "unknown")).lower()
    repair_stage = str(payload.get("repair_stage", "none"))
    report = str(payload.get("report", "")).strip()
    findings = payload.get("findings", [])
    lines = ["# Reviewer report"]
    if report:
        lines.extend(["", report])
    if isinstance(findings, list) and findings:
        lines.extend(["", "## 关键问题与证据缺口"])
        for index, finding in enumerate(findings, 1):
            if not isinstance(finding, dict):
                continue
            location = str(finding.get("location", "未标明位置"))
            impact = str(finding.get("impact", "未说明影响"))
            gap = str(finding.get("evidence_gap", "未说明证据缺口"))
            action = str(finding.get("repair_action", "未说明修复动作"))
            lines.extend(
                [
                    "",
                    f"### 问题 {index}：{location}",
                    f"- 影响：{impact}",
                    f"- 证据缺口：{gap}",
                    f"- 修复动作：{action}",
                ]
            )
    lines.extend(
        [
            "",
            f"<!-- ralph-review",
            f"verdict: {verdict}",
            f"repair_stage: {repair_stage}",
            "-->",
        ]
    )
    return "\n".join(lines)


def latest_reviewer_review(root: str | Path) -> dict[str, str] | None:
    path = Path(root).expanduser().resolve() / LATEST_REVIEW
    if not path.is_file():
        return None
    document = path.read_text(encoding="utf-8")
    parsed = _parse_reviewer_block(document)
    if parsed is None:
        return {
            "verdict": "unknown",
            "reviewed_stage": "",
            "repair_stage": "",
            "artifact_sha256": "",
            "reviewed_before_done": "false",
            "reviewer_exit_code": "",
            "block": "",
            "document": document,
            "path": str(path),
        }
    return {**parsed, "document": document, "path": str(path)}


def _commander_review_digest(document: str, *, max_chars: int = 3600) -> str:
    """Keep the same Commander informed without replaying the full receipt.

    Reviewer reports remain complete in ``latest-review.md`` and the history
    file.  Replaying the entire report on every same-stage repair caused a
    long-lived Claude session to accumulate a second copy of all findings on
    every turn.  Preserve the report summary and a bounded excerpt of each
    finding for the Commander; the independent Reviewer still receives the
    complete Markdown artifact and complete rule files on its next run.
    """

    raw = str(document or "")
    if "## Reviewer 原始输出" in raw:
        raw = raw.split("## Reviewer 原始输出", 1)[1]
    if "## Runtime 捕获的路由声明" in raw:
        raw = raw.split("## Runtime 捕获的路由声明", 1)[0]
    raw = raw.strip()
    if not raw:
        return "（Reviewer 没有提供可显示的文字问题；请读取 latest-review.md。）"

    findings = re.findall(
        r"### 问题[^\n]*.*?(?=\n### 问题|\n<!-- ralph-review|$)",
        raw,
        flags=re.DOTALL,
    )
    if not findings:
        return raw[:max_chars].rstrip()

    intro = raw.split("## 关键问题与证据缺口", 1)[0].strip()
    parts = [intro[:700].rstrip()] if intro else []
    for finding in findings[:6]:
        parts.append(finding.strip()[:520].rstrip())
    digest = "\n\n".join(part for part in parts if part)
    if len(digest) <= max_chars:
        return digest
    return digest[:max_chars].rstrip() + "\n（完整问题与证据缺口见 latest-review.md。）"


def record_reviewer_result(
    root: str | Path,
    output: str,
    *,
    return_code: int = 0,
    error_output: str = "",
) -> dict[str, str]:
    """Persist one independent reviewer result and its routing declaration."""

    project = Path(root).expanduser().resolve()
    state = load_state(project)
    artifact = ensure_stage_document(project, state)
    reviewed_before_done = DONE_MARKER not in artifact.read_text(encoding="utf-8")
    raw = _structured_reviewer_text(output.strip())
    if error_output.strip():
        raw = f"{raw}\n\n## Reviewer stderr\n\n{error_output.strip()}".strip()
    parsed = _parse_reviewer_block(raw)
    verdict = parsed["verdict"] if parsed is not None and return_code == 0 else "unknown"
    if verdict == "pass" and not reviewed_before_done:
        verdict = "unknown"
    repair_stage = parsed.get("repair_stage", "") if parsed is not None else ""
    if verdict == "revise":
        if repair_stage not in _STAGE_BY_ID:
            repair_stage = state["stage"]
    else:
        repair_stage = "none"
    digest = artifact_sha256(artifact)
    canonical = (
        f"{REVIEW_START}\n"
        f"reviewed_stage: {state['stage']}\n"
        f"artifact_sha256: {digest}\n"
        f"verdict: {verdict}\n"
        f"repair_stage: {repair_stage}\n"
        f"reviewed_before_done: {'true' if reviewed_before_done else 'false'}\n"
        f"reviewer_exit_code: {return_code}\n"
        f"{REVIEW_END}\n"
    )
    entry = (
        f"# Independent reviewer · stage {state['stage']}\n\n"
        f"主工件：`{state['current_artifact']}`\n\n"
        "## Reviewer 原始输出\n\n"
        f"{raw or '（reviewer 没有输出）'}\n\n"
        "## Runtime 捕获的路由声明\n\n"
        f"{canonical}"
    )
    _atomic_write(project / LATEST_REVIEW, entry)
    history = project / REVIEW_DIR / f"{state['stage']}-review-history.md"
    previous = history.read_text(encoding="utf-8").rstrip() if history.exists() else ""
    history_text = f"{previous}\n\n---\n\n{entry}".strip() + "\n"
    _atomic_write(history, history_text)
    updated_state = {
        **state,
        "review_status": "complete",
        "review_stage": state["stage"],
        "review_artifact_sha256": digest,
        "review_return_code": str(return_code),
    }
    _atomic_write(state_path(project), _encode_state(updated_state))
    return {
        "verdict": verdict,
        "reviewed_stage": state["stage"],
        "repair_stage": repair_stage,
        "artifact_sha256": digest,
        "reviewer_exit_code": str(return_code),
        "path": str(project / LATEST_REVIEW),
    }


def artifact_relative(stage_id: str) -> str:
    stage = stage_for(stage_id)
    return str(ARTIFACT_DIR / f"{stage.id}-{stage.slug}.md")


def _atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=path.parent, prefix=f".{path.name}.", suffix=".tmp", delete=False,
    ) as handle:
        handle.write(text)
        temporary = Path(handle.name)
    temporary.replace(path)


@contextmanager
def _review_lock(project: Path):
    """Serialize automatic reviewers and re-check state after waiting."""

    path = project / REVIEW_LOCK
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = path.open("a+", encoding="utf-8")
    try:
        if fcntl is not None:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        yield
    finally:
        if fcntl is not None:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        handle.close()


def _observe_review(project: Path, observation_type: str, payload: Mapping[str, Any], output: str | None = None) -> None:
    append_observation(
        project / "loop-events.md",
        observation_type,
        payload,
        output=output,
        artifacts=(str(LATEST_REVIEW),),
    )


def _review_matches_artifact(
    state: Mapping[str, str], artifact: Path, review: Mapping[str, str] | None,
) -> bool:
    return bool(
        review
        and review.get("reviewed_stage") == state["stage"]
        and review.get("artifact_sha256") == artifact_sha256(artifact)
        and review.get("reviewed_before_done") == "true"
        and review.get("reviewer_exit_code") == "0"
        and review.get("verdict") in {"pass", "revise"}
    )


def _set_review_state(
    project: Path,
    state: Mapping[str, str],
    *,
    status: str,
    artifact_digest: str = "",
    attempt: str | None = None,
    return_code: str = "",
) -> dict[str, str]:
    updated = {
        **state,
        "review_status": status,
        "review_stage": state["stage"],
        "review_artifact_sha256": artifact_digest,
        "review_attempt": attempt if attempt is not None else state.get("review_attempt", "0"),
        "review_return_code": return_code,
    }
    _atomic_write(state_path(project), _encode_state(updated))
    return updated


def _remove_premature_done_marker(project: Path, artifact: Path, state: Mapping[str, str]) -> None:
    text = artifact.read_text(encoding="utf-8")
    if DONE_MARKER not in text:
        return
    cleaned = text.replace(DONE_MARKER, "").rstrip() + "\n"
    _atomic_write(artifact, cleaned)
    _observe_review(
        project,
        "prompt_first_done_marker_removed_before_review",
        {
            "stage": state["stage"],
            "revision": state["revision"],
            "reason": "done marker was written before the automatic Reviewer completed",
            "artifact": state["current_artifact"],
        },
    )


def _run_automatic_reviewer(
    project: Path,
    state: Mapping[str, str],
    artifact: Path,
    *,
    trigger: str = "stop-hook",
) -> None:
    """Run the independent Reviewer serially from a runtime hook.

    The Commander and Reviewer intentionally use the same provider-default
    model, so they must not generate concurrently: the current local oMLX
    backend can corrupt its KV cache under concurrent requests.  The runtime
    itself has no idle timeout; Claude Code's host timeout remains an external
    boundary, which is why the Reviewer prompt is deliberately short.
    """

    digest = artifact_sha256(artifact)
    previous_attempt = int(state.get("review_attempt", "0") or "0")
    attempt = str(previous_attempt + 1)
    pending = _set_review_state(
        project,
        state,
        status="pending",
        artifact_digest=digest,
        attempt=attempt,
        return_code="pending",
    )
    environment = os.environ.copy()
    environment["RALPH_PROMPT_FIRST_REVIEW_TRIGGER"] = trigger
    # A separate reviewer must not implicitly compete with the Commander for
    # the same large local model. Keep the default provider behavior intact,
    # but let Herdr/local deployments select a smaller reviewer model without
    # changing the project prompt or creating a second Commander context.
    reviewer_model = environment.get("RALPH_PROMPT_FIRST_REVIEW_MODEL", "").strip()
    reviewer_effort = environment.get("RALPH_PROMPT_FIRST_REVIEW_EFFORT", "").strip()

    _observe_review(
        project,
        "prompt_first_reviewer_pending",
        {
            "stage": pending["stage"],
            "revision": pending["revision"],
            "artifact": pending["current_artifact"],
            "artifact_sha256": digest,
            "attempt": attempt,
            "trigger": trigger,
            "same_commander_context": True,
            "reviewer_model": reviewer_model or "provider-default",
            "reviewer_effort": reviewer_effort or "provider-default",
            "reviewer_transport": environment.get(
                "RALPH_PROMPT_FIRST_REVIEW_TRANSPORT", "auto"
            ),
        },
    )
    command = [
        sys.executable,
        "-m",
        "ralph_runtime.cli",
        "prompt-first",
        "review",
        str(project),
    ]
    if reviewer_model:
        command.extend(["--model", reviewer_model])
    if reviewer_effort:
        command.extend(["--effort", reviewer_effort])
    timeout_raw = environment.get("RALPH_PROMPT_FIRST_REVIEW_TIMEOUT", "600").strip()
    try:
        reviewer_timeout = float(timeout_raw)
    except ValueError:
        reviewer_timeout = 600.0
    if reviewer_timeout <= 0:
        reviewer_timeout = 600.0
    try:
        completed = subprocess.run(
            command,
            cwd=project,
            env=environment,
            text=True,
            capture_output=True,
            check=False,
            timeout=reviewer_timeout,
        )
    except subprocess.TimeoutExpired as exc:
        current = load_state(project)
        _set_review_state(
            project,
            current,
            status="failed",
            artifact_digest=digest,
            attempt=attempt,
            return_code="timeout",
        )
        _observe_review(
            project,
            "prompt_first_reviewer_failed",
            {
                "stage": state["stage"],
                "revision": state["revision"],
                "artifact_sha256": digest,
                "attempt": attempt,
                "error": f"reviewer timeout after {reviewer_timeout:g}s",
                "return_code": "timeout",
            },
            output=str(exc),
        )
        return
    except OSError as exc:
        current = load_state(project)
        _set_review_state(
            project,
            current,
            status="failed",
            artifact_digest=digest,
            attempt=attempt,
            return_code="spawn-error",
        )
        _observe_review(
            project,
            "prompt_first_reviewer_failed",
            {
                "stage": state["stage"],
                "revision": state["revision"],
                "artifact_sha256": digest,
                "attempt": attempt,
                "error": str(exc),
            },
        )
        return

    # The CLI normally persists the canonical receipt.  If the child failed
    # before reaching that code, persist an explicit unknown receipt here so
    # the failure cannot be mistaken for a successful review.
    current_review = latest_reviewer_review(project)
    if (
        not current_review
        or current_review.get("artifact_sha256") != digest
        or current_review.get("reviewed_stage") != state["stage"]
        or current_review.get("verdict") == "unknown"
    ):
        record_reviewer_result(
            project,
            completed.stdout,
            return_code=completed.returncode,
            error_output=completed.stderr,
        )
    current = load_state(project)
    _set_review_state(
        project,
        current,
        status="complete",
        artifact_digest=digest,
        attempt=attempt,
        return_code=str(completed.returncode),
    )
    _observe_review(
        project,
        "prompt_first_reviewer_finished",
        {
            "stage": state["stage"],
            "revision": state["revision"],
            "artifact_sha256": digest,
            "attempt": attempt,
            "review_process_return_code": completed.returncode,
            "review_verdict": (latest_reviewer_review(project) or {}).get("verdict", "unknown"),
            "same_commander_context": True,
        },
        output=(completed.stdout + "\n" + completed.stderr).strip(),
    )


def _run_reviewer_until_routable(
    project: Path,
    state: Mapping[str, str],
    artifact: Path,
    *,
    trigger: str,
    max_attempts: int = 3,
) -> dict[str, str] | None:
    """Retry malformed Reviewer output without leaving the Commander session.

    A local model can occasionally answer the read-only Reviewer prompt with
    prose such as “let me first read the file”.  That is not a pass and must
    never advance a stage, but leaving the state merely ``pending`` lets the
    outer Claude process exit and strands the project.  Retry the same
    provider-default Reviewer serially a small bounded number of times; a
    still-invalid result remains a blocked current-stage state.
    """

    current_state = dict(state)
    current_artifact = artifact
    for _ in range(max(1, max_attempts)):
        review = latest_reviewer_review(project)
        if _review_matches_artifact(current_state, current_artifact, review):
            return review
        _run_automatic_reviewer(
            project,
            current_state,
            current_artifact,
            trigger=trigger,
        )
        current_state = load_state(project)
        current_artifact = ensure_stage_document(project, current_state)
        review = latest_reviewer_review(project)
        if _review_matches_artifact(current_state, current_artifact, review):
            return review
    return latest_reviewer_review(project)


def _encode_state(state: Mapping[str, str]) -> str:
    lines = [
        "# RALPH Prompt-First Loop",
        "",
        _STATE_START,
        f"stage: {state['stage']}",
        f"revision: {state['revision']}",
        f"status: {state['status']}",
        f"current_artifact: {state['current_artifact']}",
        f"review_status: {state.get('review_status', 'idle')}",
        f"review_stage: {state.get('review_stage', '')}",
        f"review_artifact_sha256: {state.get('review_artifact_sha256', '')}",
        f"review_attempt: {state.get('review_attempt', '0')}",
        f"review_return_code: {state.get('review_return_code', '')}",
        _STATE_END,
        "",
        "## 原始任务（请勿改写）",
        "",
        state["task"],
        "",
        "## 机械说明",
        "",
        "这个文件只保存阶段游标，不评价内容质量。阶段内容全部写在当前 Markdown 工件中。",
        "主工件停止写入后，Stop Hook 自动启动独立 Reviewer。Reviewer 读取 loop/prompt-first 中的规则和当前工件，输出问题、证据缺口与 pass/revise 路由。",
        "只有当前工件对应的 Reviewer 明确 pass，且之后写入 `<!-- ralph: done -->`，才进入下一阶段；revise、缺失、过期或无效回执都留在当前阶段。",
        "不要手动编辑本文件的阶段游标或原始任务；它由 Stop Hook 机械维护。普通项目工件可自由读取和写入。",
        "",
    ]
    return "\n".join(lines)


def load_state(root: str | Path) -> dict[str, str]:
    path = state_path(root)
    raw = path.read_text(encoding="utf-8")
    match = re.search(r"<!-- ralph-prompt-state\s*\n(.*?)\n-->", raw, re.DOTALL)
    if match is None:
        raise ValueError(f"{path} is missing the prompt-first state header")
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, separator, value = line.partition(":")
        if separator:
            values[key.strip()] = value.strip()
    required = ("stage", "revision", "status", "current_artifact")
    missing = [key for key in required if not values.get(key)]
    if missing:
        raise ValueError(f"{path} is missing: {', '.join(missing)}")
    stage_for(values["stage"])
    task_match = re.search(
        r"^## 原始任务（请勿改写）\s*\n\n(.*?)(?=\n## 机械说明\s*\n|\Z)",
        raw,
        re.DOTALL | re.MULTILINE,
    )
    task = task_match.group(1).strip() if task_match else ""
    if not task:
        task = "原始任务正文不可读；以当前阶段工件与已记录证据为准，勿编造缺失事实。"
    return {
        "stage": values["stage"],
        "revision": values["revision"],
        "status": values["status"],
        "task": task,
        "current_artifact": values["current_artifact"],
        "review_status": values.get("review_status", "idle"),
        "review_stage": values.get("review_stage", ""),
        "review_artifact_sha256": values.get("review_artifact_sha256", ""),
        "review_attempt": values.get("review_attempt", "0"),
        "review_return_code": values.get("review_return_code", ""),
    }


def _stage_document(stage: PromptStage, task: str) -> str:
    return (
        f"# 阶段 {stage.id} · {stage.title}\n\n"
        f"任务：{task}\n\n"
        "## 当前阶段工作记录\n\n"
        "按照当前阶段的外部规则文件完成工作；这里记录实际过程、证据、产出和未解决问题。\n\n"
        "## Reviewer 回执\n\n"
        "本节由 `ralph prompt-first review .` 生成的独立审阅结果驱动；不要手写 pass。"
    )


def ensure_stage_document(root: str | Path, state: Mapping[str, str]) -> Path:
    project = Path(root).expanduser().resolve()
    relative = state["current_artifact"]
    path = project / relative
    if not path.exists():
        _atomic_write(path, _stage_document(stage_for(state["stage"]), state["task"]))
    return path


def initialize(root: str | Path, task: str) -> dict[str, str]:
    project = Path(root).expanduser().resolve()
    path = state_path(project)
    if path.exists():
        state = load_state(project)
        if task.strip() and state["task"] == PENDING_TASK:
            # ``ralph init`` may create a task-less Markdown scaffold.  Its
            # first explicit loop task is the task, not a late refinement.
            state = {**state, "task": task.strip()}
            _atomic_write(path, _encode_state(state))
            document = ensure_stage_document(project, state)
            if state["stage"] == "01" and DONE_MARKER not in document.read_text(encoding="utf-8"):
                _atomic_write(document, _stage_document(stage_for("01"), state["task"]))
        elif task.strip() and state["task"].strip() != task.strip():
            # Preserve the original task and write the new wording into the
            # current artifact rather than silently replacing an in-progress
            # decomposition.
            document = ensure_stage_document(project, state)
            existing = document.read_text(encoding="utf-8")
            note = f"\n## 最新人类补充\n\n{task.strip()}\n"
            if note.strip() not in existing:
                _atomic_write(document, existing.rstrip() + note)
        return state
    cleaned = task.strip() or PENDING_TASK
    state = {
        "stage": "01",
        "revision": "r1",
        "status": "running",
        "task": cleaned,
        "current_artifact": artifact_relative("01"),
        "review_status": "idle",
        "review_stage": "",
        "review_artifact_sha256": "",
        "review_attempt": "0",
        "review_return_code": "",
    }
    _atomic_write(path, _encode_state(state))
    ensure_stage_document(project, state)
    return state


def render_prompt(root: str | Path, *, reason: str = "继续当前阶段") -> str:
    state = load_state(root)
    stage = stage_for(state["stage"])
    artifact = ensure_stage_document(root, state)
    artifact_text = artifact.read_text(encoding="utf-8")
    rules = load_stage_rules(root, stage.id)
    reviewer = latest_reviewer_review(root)
    digest = artifact_sha256(artifact)
    reviewer_matches = bool(
        reviewer
        and reviewer.get("reviewed_stage") == stage.id
        and reviewer.get("artifact_sha256") == digest
        and reviewer.get("reviewed_before_done") == "true"
        and reviewer.get("reviewer_exit_code") == "0"
    )
    repair_is_current = bool(
        reviewer
        and reviewer.get("verdict") == "revise"
        and reviewer.get("repair_stage") == stage.id
    )
    initial_template = (
        not repair_is_current
        and artifact_text.strip() == _stage_document(stage, state["task"]).strip()
    )
    if repair_is_current:
        review_context = (
            "独立 Reviewer 上一轮判定 revise。必须先处理它列出的所有问题，保持当前阶段，"
            f"不得写 `{DONE_MARKER}`；修复后停止，Stop Hook 会自动再次运行 Reviewer。\n\n"
            # The complete receipt remains on disk.  Inject a bounded digest so
            # repeated same-stage repairs do not duplicate a large report in
            # the same Commander context.
            f"Reviewer 问题摘要（完整回执见 `{LATEST_REVIEW}`）：\n"
            f"{_commander_review_digest(reviewer.get('document', ''))}\n"
        )
    elif reviewer_matches and reviewer and reviewer.get("verdict") == "pass":
        review_context = (
            "独立 Reviewer 已对当前版本判定 pass。不要再修改主工件；"
            f"若内容仍未变化，现在才可以把 `{DONE_MARKER}` 写成最后一行并停止。\n"
        )
    else:
        review_context = (
            "当前版本还没有有效的 Reviewer pass。完成或修订主工件后停止，Stop Hook 会自动运行独立 Reviewer；"
            "Reviewer 未通过时继续当前阶段。\n"
        )
    if initial_template:
        opening = (
            "这是当前阶段的自动模板；阶段游标、任务、目标路径和规则正文已经由 runtime 注入，"
            f"由于 Claude Code 的 Write 工具要求目标文件先被 Read，第一步只调用一次 Read `{state['current_artifact']}`；"
            "不要输出计划、解释或普通文本。Read 完成后，PostToolUse hook 会注入下一步，随后直接唯一调用 Write。\n\n"
        )
        first_step = (
            f"1. 初始模板先只调用一次 Read `{state['current_artifact']}`；不要先写、不要解释。Read 后立即按上面的阶段规则用 Write 写入完整当前阶段 Markdown。\n"
        )
    elif repair_is_current:
        # The same Commander has already read this artifact earlier in the
        # session.  Requiring another Read on every revise round makes the
        # local model spend a long tool turn re-opening unchanged files and
        # can prevent it from ever issuing the repair Write.  Keep the
        # session continuous and prefer one complete Write over a patch-style
        # Edit; only fall back to Read if Claude rejects the Write call.
        opening = (
            "这是同一 Claude 会话中的修订轮次；当前工件已经在本会话读取过。"
            f"下一条 assistant 消息必须直接发出唯一的 Write tool call，完整重写目标 `{state['current_artifact']}`；"
            "不要再次读取当前工件、ralph-loop.md 或规则文件，不要输出计划、解释或普通文本。"
            "只有 Write 被 Claude 拒绝时才允许补一次 Read，然后立即重试 Write。\n\n"
        )
        first_step = (
            "1. 直接依据 Reviewer 回执修复全部问题，用 Write 完整重写当前 Markdown；不要先调用 Read 或使用 Edit 补丁。\n"
        )
    else:
        opening = (
            f"只需读取 `ralph-loop.md` 和当前工件确认状态；读取完成后，下一条 assistant 消息必须直接发出唯一的 Write tool call，"
            f"目标是 `{state['current_artifact']}`。禁止先输出计划、解释、‘让我写入’或任何普通文本。\n\n"
        )
        first_step = (
            f"1. Read `ralph-loop.md` 与当前工件；阶段规则已经在本提示中，不要再次批量读取规则文件。\n"
        )
    rules_path = rules.get("path") or "缺失"
    if repair_is_current:
        rule_context = (
            "--- 当前阶段规则 ---\n"
            f"规则文件仍由 runtime 动态读取：{rules_path}。"
            "本轮 Reviewer 已依据磁盘上的完整规则审阅；不要把后续阶段要求提前写入当前工件。\n"
            "--- 当前阶段规则结束 ---\n\n"
        )
    else:
        rule_context = (
            f"--- 当前阶段操作与质检标准 ---\n{rules['text']}\n"
            "--- 规则结束 ---\n\n"
        )
    return (
        opening
        + "# RALPH Prompt-First\n"
        "保持当前 Claude 会话连续工作；不要等待人工确认，也不要重启、创建字段任务或输出 JSON 协议。"
        "所有阶段操作和质检标准以外部规则为准。\n\n"
        f"当前阶段：{stage.id} · {stage.title}\n"
        f"当前工件：`{state['current_artifact']}`\n"
        f"任务：{state['task']}\n\n"
        f"阶段规则来源：{rules_path}\n\n"
        + rule_context
        + f"{review_context}\n"
        "立即执行：\n"
        + first_step
        + "2. 不要返回说明，立刻用 Write 写入完整当前阶段 Markdown；修订轮次不要使用 Edit 补丁。\n"
        f"3. 主工件完成或修订后停止，不要自行启动 Reviewer；Stop Hook 会自动在独立上下文中只读检查当前工件和规则。\n"
        f"4. Reviewer 为 revise 时，读取 `{LATEST_REVIEW}` 中的问题，修复对应阶段；不得写 `{DONE_MARKER}`，修复后停止并等待自动再次审阅。\n"
        f"5. 只有 Reviewer 对当前版本明确 pass 后，才把 `{DONE_MARKER}` 作为主工件最后一行写入；写完立即停止，不要开始下一阶段。\n"
        "如果你已经说过‘现在写入’却没有发出 Write，立刻纠正并发出 Write；不要结束本轮。\n\n"
        + f"本次提醒原因：{reason}\n"
    )


def advance_if_marked_done(root: str | Path) -> tuple[dict[str, str], bool]:
    """Route only on the model's explicit self-review and done marker.

    This is not a quality gate: the runtime cannot tell whether ``pass`` is
    true.  It merely refuses to advance when the model itself said ``revise``
    or did not make a routing declaration.
    """

    project = Path(root).expanduser().resolve()
    state = load_state(project)
    if state["status"] == "completed":
        return state, False
    document = ensure_stage_document(project, state)
    text = document.read_text(encoding="utf-8")
    review = latest_reviewer_review(project)
    if (
        DONE_MARKER not in text
        or review is None
        or review.get("reviewed_stage") != state["stage"]
        or review.get("artifact_sha256") != artifact_sha256(document)
        or review.get("verdict") != "pass"
        or review.get("reviewed_before_done") != "true"
        or review.get("reviewer_exit_code") != "0"
    ):
        return state, False
    position = next(index for index, stage in enumerate(STAGES) if stage.id == state["stage"])
    if position + 1 >= len(STAGES):
        state = {**state, "status": "completed"}
    else:
        next_stage = STAGES[position + 1]
        state = {
            **state,
            "stage": next_stage.id,
            "current_artifact": artifact_relative(next_stage.id),
        }
    _atomic_write(state_path(project), _encode_state(state))
    if state["status"] != "completed":
        ensure_stage_document(project, state)
    return state, True


def _move_to_repair_stage(root: Path, state: dict[str, str], target: str) -> dict[str, str]:
    if target == state["stage"]:
        return state
    current_index = next(index for index, stage in enumerate(STAGES) if stage.id == state["stage"])
    target_index = next(index for index, stage in enumerate(STAGES) if stage.id == target)
    if target_index > current_index:
        return state
    updated = {
        **state,
        "stage": target,
        "status": "running",
        "current_artifact": artifact_relative(target),
        "review_status": "idle",
        "review_stage": "",
        "review_artifact_sha256": "",
        "review_return_code": "",
    }
    _atomic_write(state_path(root), _encode_state(updated))
    ensure_stage_document(root, updated)
    return updated


def _ralph_continuation_message(state: Mapping[str, str], *, reason: str = "") -> str:
    """Keep Ralph's liveness reminder in the single prompt-first Stop hook.

    The official Ralph plugin and prompt-first must not install two competing
    Stop hooks. This preserves Ralph's same-context continuation behavior while
    prompt-first remains the sole owner of Reviewer routing and advancement.
    """

    suffix = f" 当前原因：{reason}" if reason else ""
    return (
        f"🔄 Ralph continuation · 阶段 {state['stage']} · 修订 {state['revision']}："
        "保持 current Claude context，不要结束当前任务、不要等待人工确认、不要重开 Claude 上下文。"
        "先读取持久化 Markdown 状态，完成一个具体的修复、验证或阶段动作；"
        "只有当前工件通过独立 Reviewer 且写入完成标记后，runtime 才允许推进或结束。"
        f"{suffix}"
    )


def _compact_continuation_message(
    root: Path,
    state: Mapping[str, str],
    *,
    summary: str = "",
) -> str:
    """Return a tiny durable cursor after Claude Code compacts its context."""

    review = latest_reviewer_review(root)
    review_hint = "当前版本等待 Reviewer" if review is None else f"Reviewer={review.get('verdict', 'unknown')}"
    if summary:
        review_hint += "；压缩摘要已持久化到 transcript"
    return (
        f"🔄 RALPH prompt-first 已完成上下文压缩：继续同一 Claude 会话，"
        f"不要重放旧对话。阶段 {state['stage']} · 修订 {state['revision']} · "
        f"工件 `{state['current_artifact']}` · {review_hint}。"
        f"只读取当前 Markdown 与 `{LATEST_REVIEW}`（若存在），完成一个具体修复后 Write，"
        "然后停止等待 Stop Hook；不要重复已经记录的网页/工具尝试，不要自行推进阶段。"
    )


def handle_precompact(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Persist compaction start without blocking Claude's recovery path."""

    raw_root = payload.get("cwd") or payload.get("workspace")
    if not isinstance(raw_root, str) or not raw_root.strip():
        return {}
    root = Path(raw_root).expanduser()
    if not state_path(root).exists():
        return {}
    state = load_state(root)
    append_observation(
        root / "loop-events.md",
        "prompt_first_context_compaction_started",
        {
            "stage": state["stage"],
            "revision": state["revision"],
            "current_artifact": state["current_artifact"],
            "trigger": str(payload.get("trigger") or "unknown")[:80],
            "same_commander_context": True,
        },
    )
    return {}


def handle_postcompact(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Reconnect a compacted same-context session with only durable state."""

    raw_root = payload.get("cwd") or payload.get("workspace")
    if not isinstance(raw_root, str) or not raw_root.strip():
        return {}
    root = Path(raw_root).expanduser()
    if not state_path(root).exists():
        return {}
    state = load_state(root)
    summary = str(payload.get("compact_summary") or "").strip()
    append_observation(
        root / "loop-events.md",
        "prompt_first_context_compaction_completed",
        {
            "stage": state["stage"],
            "revision": state["revision"],
            "current_artifact": state["current_artifact"],
            "trigger": str(payload.get("trigger") or "unknown")[:80],
            "summary_characters": len(summary),
            "same_commander_context": True,
        },
    )
    message = _compact_continuation_message(root, state, summary=summary)
    return {
        "hookSpecificOutput": {
            "hookEventName": "PostCompact",
            "additionalContext": message,
        },
        "systemMessage": message,
    }


def _research_tool_attempts_since_write(root: Path, state: Mapping[str, str]) -> int:
    """Count bounded external research-tool attempts in the current stage turn.

    This is a liveness counter, not a quality check.  A Fetch/WebSearch call
    may fail for reasons outside the runtime; after a small bounded batch the
    Commander must persist the observed failures instead of looping on the
    same unavailable tool.  The counter resets naturally after the next
    current-artifact Write because the event log is durable and append-only.
    """

    log = root / "loop-events.md"
    if not log.is_file():
        return 0
    try:
        text = log.read_text(encoding="utf-8")
    except OSError:
        return 0
    stage_start = text.find(f"## {state['stage']}-")
    stage_tail = text[stage_start:] if stage_start >= 0 else text
    last_write = stage_tail.rfind('"tool": "Write"')
    if last_write >= 0:
        stage_tail = stage_tail[last_write:]
    return sum(stage_tail.count(f'"tool": "{name}"') for name in ("Fetch", "WebFetch", "WebSearch"))


def handle_pre_tool(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Deny only redundant stage-02 research calls before they start.

    PostToolUse remains the useful same-context reminder after a real result,
    but it cannot cancel another tool call that Claude already queued in the
    same assistant turn.  This narrow PreToolUse guard handles that race.  It
    does not inspect ordinary Bash, Read, Write, Edit, Agent, or content
    quality; it only protects the bounded external-research batch.
    """

    tool_name = str(payload.get("tool_name", ""))
    if tool_name not in {"Fetch", "WebFetch", "WebSearch"}:
        return {}
    raw_root = payload.get("cwd") or payload.get("workspace")
    if not isinstance(raw_root, str) or not raw_root.strip():
        return {}
    root = Path(raw_root).expanduser()
    if not state_path(root).exists():
        return {}
    state = load_state(root)
    if state["stage"] != "02":
        return {}
    attempts = _research_tool_attempts_since_write(root, state)
    if attempts < 4:
        return {}
    context = (
        f"RALPH prompt-first：阶段 02 已记录 {attempts} 次外部研究工具尝试且当前版本尚未 Write。"
        "拒绝继续 Fetch/WebFetch/WebSearch，避免同一轮无限重试。"
        f"请立即用一次 Write 完整写入 `{state['current_artifact']}`，记录真实成功/失败、URL、"
        "观察时间和未解决空缺，然后停止等待 Reviewer；普通命令和文件操作不受此限制。"
    )
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": context,
            "additionalContext": context,
        }
    }


def handle_stop(payload: Mapping[str, Any]) -> dict[str, Any]:
    raw_root = payload.get("cwd") or payload.get("workspace")
    if not isinstance(raw_root, str) or not raw_root.strip():
        return {}
    root = Path(raw_root).expanduser()
    if not state_path(root).exists():
        return {}
    state, advanced = advance_if_marked_done(root)
    if state["status"] == "completed":
        return {}
    _observe_review(
        root,
        "prompt_first_ralph_continuation",
        {
            "stage": state["stage"],
            "revision": state["revision"],
            "same_commander_context": True,
            "advanced_before_review": advanced,
        },
    )
    if advanced:
        # The current Stop completed the previous stage.  Do not review the
        # newly-created template before Commander has written that stage.
        # The same Claude context receives the next-stage prompt and its next
        # substantive stop will trigger the automatic Reviewer for that new
        # artifact.
        return {
            "decision": "block",
            "reason": render_prompt(root, reason="上一阶段已由独立 Reviewer pass 和完成标记推进")[:12000],
            "systemMessage": _ralph_continuation_message(
                state, reason="上一阶段已通过，开始下一阶段"
            ),
        }
    artifact = ensure_stage_document(root, state)
    review = latest_reviewer_review(root)
    # The Stop Hook owns Reviewer execution.  The Commander may still invoke
    # the public review command manually, but stage progression never depends
    # on that model action.  Re-check after acquiring the lock so two Stop
    # events cannot launch duplicate reviewers for the same artifact.
    if not _review_matches_artifact(state, artifact, review):
        with _review_lock(root):
            state = load_state(root)
            if state["status"] == "completed":
                return {}
            artifact = ensure_stage_document(root, state)
            review = latest_reviewer_review(root)
            if not _review_matches_artifact(state, artifact, review):
                _remove_premature_done_marker(root, artifact, state)
                _run_reviewer_until_routable(
                    root,
                    state,
                    artifact,
                    trigger="stop-hook",
                )
        state = load_state(root)
        artifact = ensure_stage_document(root, state)
        review = latest_reviewer_review(root)
    if review is not None and review.get("verdict") == "revise":
        target = review.get("repair_stage", "") or state["stage"]
        if target not in _STAGE_BY_ID:
            target = state["stage"]
        state = _move_to_repair_stage(root, state, target)
        stop_reason = (
            f"独立 Reviewer 判定 revise；修复阶段 {state['stage']}，"
            "必须处理回执中的问题后重新运行 review 命令"
        )
    elif (
        review is not None
        and review.get("verdict") == "pass"
        and review.get("reviewed_stage") == state["stage"]
        and review.get("artifact_sha256") == artifact_sha256(artifact)
        and review.get("reviewed_before_done") == "true"
        and DONE_MARKER not in artifact.read_text(encoding="utf-8")
    ):
        stop_reason = "Reviewer 已通过当前版本，但还没有写完成标记；现在只能补上最后一行"
    elif review is not None and review.get("verdict") == "unknown":
        stop_reason = "自动 Reviewer 没有返回可用的 pass/revise 回执；保持当前阶段并在下一次 Stop 时重试"
    elif state.get("review_status") == "pending":
        stop_reason = "独立 Reviewer 仍处于 review-pending；不得退出当前阶段"
    else:
        stop_reason = "当前阶段没有有效的 Reviewer pass；继续修订工件，Stop Hook 会自动重新审阅"
    reason = render_prompt(
        root,
        reason="上一阶段已由独立 Reviewer pass 和完成标记推进" if advanced else stop_reason,
    )
    return {
        "decision": "block",
        "reason": reason[:12000],
        "systemMessage": _ralph_continuation_message(state, reason=stop_reason),
    }


def handle_post_tool(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Nudge the same Commander after a stage Read or artifact write.

    Some local tool-use adapters return the Read result and then leave the
    interactive session between assistant turns.  A prompt-first PostToolUse
    hook supplies a bounded continuation hint in the same Claude context; it
    never advances a stage, reviews content, or starts a new process.
    """

    tool_name = str(payload.get("tool_name", ""))
    if tool_name not in {"Read", "Write", "Edit", "Fetch", "WebFetch", "WebSearch"}:
        return {}
    raw_root = payload.get("cwd") or payload.get("workspace")
    if not isinstance(raw_root, str) or not raw_root.strip():
        return {}
    root = Path(raw_root).expanduser()
    if not state_path(root).exists():
        return {}
    state = load_state(root)
    artifact = ensure_stage_document(root, state)
    tool_input = payload.get("tool_input")
    read_path = ""
    if isinstance(tool_input, Mapping):
        read_path = str(tool_input.get("file_path") or tool_input.get("path") or "")
    try:
        is_current_artifact = Path(read_path).expanduser().resolve() == artifact.resolve()
        resolved_read_path = Path(read_path).expanduser().resolve()
    except (OSError, RuntimeError):
        is_current_artifact = False
        resolved_read_path = Path()
    prompt_artifacts = (root / ARTIFACT_DIR).resolve()
    is_web_llm_receipt = (
        tool_name == "Read"
        and resolved_read_path.name == "02-web-llm-cross-check.md"
        and prompt_artifacts in resolved_read_path.parents
    )
    if not is_current_artifact and not is_web_llm_receipt:
        if state["stage"] == "02" and tool_name in {"Fetch", "WebFetch", "WebSearch"}:
            append_observation(
                root / "loop-events.md",
                "prompt_first_research_tool",
                {
                    "tool": tool_name,
                    "stage": state["stage"],
                    "revision": state["revision"],
                    "same_commander_context": True,
                },
            )
            attempts = _research_tool_attempts_since_write(root, state)
            context = (
                f"RALPH prompt-first：阶段 02 外部研究工具第 {attempts} 次尝试已返回。"
                "只记录真实结果，不把空结果当作证据。"
            )
            if attempts >= 4:
                context += (
                    "本轮研究工具尝试已达到上限；不要再 Fetch/WebSearch/web-llm。"
                    f"立即用一次 Write 完整写入 `{state['current_artifact']}`，记录成功、失败、URL、"
                    "观察时间和未解决空缺，然后停止等待 Reviewer。"
                )
                return {
                    "decision": "block",
                    "reason": context,
                    "hookSpecificOutput": {
                        "hookEventName": "PostToolUse",
                        "additionalContext": context,
                    },
                }
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": context,
                }
            }
        return {}
    # A premature done marker is precisely the case that must be handed to
    # Stop Hook: record the write and force the turn to end so the hook can
    # remove the marker, run Reviewer, and route the same context.  Read after
    # a valid done marker is harmless and does not need a nudge.
    if tool_name == "Read" and DONE_MARKER in artifact.read_text(encoding="utf-8"):
        return {}
    append_observation(
        root / "loop-events.md",
        "prompt_first_post_tool",
        {
            "tool": tool_name,
            "artifact": state["current_artifact"] if is_current_artifact else str(resolved_read_path.relative_to(root)),
            "stage": state["stage"],
            "revision": state["revision"],
            "same_commander_context": True,
        },
        artifacts=[state["current_artifact"]],
    )
    if is_web_llm_receipt:
        response = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": (
                    "RALPH prompt-first：网页 LLM 回执已读完。只使用回执中明确记录的成功/失败状态；"
                    "不要重复运行 web-llm，也不要对同一主张继续无边界地换关键词搜索。"
                    "同一主张的 WebSearch 最多一次替换关键词；若仍为 0 结果，立即把失败原因、"
                    "实际观察时间和未解决状态写入当前阶段 Markdown，随后停止等待 Reviewer。"
                    f"下一条应直接用一次 Write 完整写入 `{state['current_artifact']}`。"
                ),
            }
        }
        return response
    if tool_name in {"Write", "Edit"}:
        context = (
            "RALPH prompt-first：当前阶段 Markdown 工件已经写入。"
            "现在立即结束本轮，不要继续思考、读取、运行命令或写其他文件；"
            "Stop Hook 会自动启动 Reviewer。Reviewer revise 时保持或回退到指定阶段，"
            "不要自行推进；只有 pass 后才可写完成标记。"
        )
    else:
        context = (
            "RALPH prompt-first：当前阶段规则已注入；你已经读完当前 Markdown 工件。"
            "下一条 assistant 消息必须直接发出唯一的 Write tool call，写回当前工件；"
            "不要返回计划、解释或普通文本，不要启动 Reviewer，不要推进阶段。"
        )
    response = {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": context,
        }
    }
    if tool_name in {"Write", "Edit"}:
        # Claude Code may keep thinking after a PostToolUse reminder, so a
        # Stop Hook alone is not a sufficient liveness guarantee.  Review
        # synchronously here as a fallback; the Stop Hook remains the final
        # router and will see the matching receipt without launching a
        # duplicate review.  The review result is fed back into this same
        # Commander context through additionalContext.
        with _review_lock(root):
            state = load_state(root)
            artifact = ensure_stage_document(root, state)
            review = latest_reviewer_review(root)
            if not _review_matches_artifact(state, artifact, review):
                _remove_premature_done_marker(root, artifact, state)
                state = load_state(root)
                artifact = ensure_stage_document(root, state)
                _run_reviewer_until_routable(
                    root,
                    state,
                    artifact,
                    trigger="post-tool-fallback",
                )
            review = latest_reviewer_review(root)
        if review is not None:
            verdict = review.get("verdict", "unknown")
            if verdict == "revise":
                context = (
                    "RALPH prompt-first：当前阶段 Markdown 已写入，PostToolUse fallback 已完成独立 Reviewer。"
                    "Reviewer 判定 revise；保持同一阶段。下一条 assistant 消息必须直接发出唯一的 Write tool call，"
                    f"完整重写 `{state['current_artifact']}` 修复下列问题；不要 Read、不要 Edit、不要输出解释、不要推进阶段。"
                    "写入后停止，PostToolUse fallback 会再次审阅：\n"
                    f"{_commander_review_digest(review.get('document', ''))}"
                )
            elif verdict == "pass":
                context = (
                    "RALPH prompt-first：PostToolUse fallback 已完成独立 Reviewer 并判定 pass。"
                    f"下一条 assistant 消息必须直接用 Write 将 `{DONE_MARKER}` 写成 `{state['current_artifact']}` 的最后一行，随后停止；不要推进阶段。"
                )
            else:
                context = (
                    "RALPH prompt-first：PostToolUse fallback 的 Reviewer 回执无效。"
                    f"保持阶段 {state['stage']}，下一条直接用 Write 修复 `{state['current_artifact']}`；不要 Read、不要推进阶段。"
                )
            response["hookSpecificOutput"]["additionalContext"] = context
            # Claude Code supports PostToolUse blocking with continueOnBlock:
            # true.  This interrupts a long post-write reasoning turn and
            # feeds the already-completed Reviewer route back into the same
            # Commander context, without spawning or resuming a new session.
            response["decision"] = "block"
            response["reason"] = context
    return response


def status_summary(root: str | Path) -> dict[str, str | bool]:
    state = load_state(root)
    artifact = ensure_stage_document(root, state)
    review = latest_reviewer_review(root)
    return {
        **state,
        "artifact_exists": artifact.is_file(),
        "done_marker_present": DONE_MARKER in artifact.read_text(encoding="utf-8"),
        "review_verdict": review["verdict"] if review is not None else "missing",
        "review_stage": review.get("reviewed_stage", "") if review is not None else "",
        "review_artifact": review.get("artifact_sha256", "") if review is not None else "",
    }


def system_prompt() -> str:
    return (
        "Use the RALPH prompt-first workflow. For an untouched automatic template, use the injected cursor, task, target, "
        "and stage rules, read the current artifact once because Claude Code's Write requires a prior Read, then write it; "
        "for substantive work or a Reviewer revision, "
        "read the current loop/prompt-first stage rules and Markdown artifact. "
        "Do not invent JSON state machines, field roles, or semantic validation. After substantive work, stop; "
        "the Stop Hook automatically launches an independent Reviewer that must return pass or revise. "
        "A revise result keeps or rolls back to the declared repair stage and must be fixed before reviewing again. "
        "Only reviewer pass for the unchanged artifact permits the done marker. Never manually edit ralph-loop.md; "
        "the Stop Hook maintains its cursor. After reviewer pass plus the done marker, end the turn immediately."
    )
