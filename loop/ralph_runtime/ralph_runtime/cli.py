"""Small CLI for the first RALPH runtime MVP."""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import inspect
import json
import os
import re
import shlex
import shutil
import signal
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping
from zoneinfo import ZoneInfo

try:
    import fcntl
except ImportError:  # pragma: no cover - Windows fallback
    fcntl = None

from .contracts import (
    cards_for_current_stage,
    materialize_contract_documents,
    stage_result_ref,
    stage_submission_template,
)
from .decomposition_benchmark import (
    DEFAULT_SIMPLE_GPU_TASK,
    evaluate_state,
    evaluate_task_spec,
    load_task_spec_file,
)
from .prompt_renderer import PromptRenderer
from .prompt_first import (
    artifact_sha256,
    handle_stop as handle_prompt_first_stop,
    handle_pre_tool as handle_prompt_first_pre_tool,
    handle_precompact as handle_prompt_first_precompact,
    initialize as initialize_prompt_first,
    load_stage_rules,
    handle_post_tool as handle_prompt_first_post_tool,
    handle_postcompact as handle_prompt_first_postcompact,
    load_state as load_prompt_first_state,
    record_reviewer_result,
    render_prompt as render_prompt_first,
    state_path as prompt_first_state_path,
    status_summary as prompt_first_status_summary,
    system_prompt as prompt_first_system_prompt,
)
from .replay_runner import run_fixture_file
from .events import append_observation, apply_and_record, read_events, replay_events
from .dag import DAGValidationError, validate_plan
from .graph_tasks import apply_graph_task, materialize_graph_tasks
from .hooks import run_hook
from .result_artifacts import resolve_result_artifact, state_stage_artifact_dir
from .project_resolver import ProjectResolution, resolve_project
from .nodes import DEFAULT_GRAPH, NodeGraph
from .state import (
    create_state,
    load_legacy_markdown,
    load_state,
    reset_subagent_card,
    save_state,
    set_task,
    start_new_task,
    record_human_input,
    update_subagent_card,
    field_completeness,
    _explode_comma_fields,
)
from .protocol import _external_evidence_issues, collect_validation_issues, parse_action, validate_action
from .task_board import TaskBoardError, read_task_board, select_next_task
from .web_llm import (
    authorize_browser_providers,
    open_browser_login,
    run_prompt_first_web_llm_cross_check,
    run_web_llm_cross_check,
    web_llm_crosscheck_enabled,
)
from .runtime_config import (
    HOOK_MODES,
    STOP_POLICIES,
    default_hook_mode,
    default_stop_policy,
    field_mode_enabled,
    flow_only_mode,
    max_parallel_fields,
)
from .field_tasks import (
    claim_field_task,
    materialize_field_tasks,
    reconcile_applied_field_tasks,
    reopen_deferred_field_tasks,
    reopen_stale_field_tasks,
    update_field_task_metadata_transaction,
    field_task_requires_agent,
)


MAX_EVENT_TAIL = 20


class SupervisorAlreadyRunning(RuntimeError):
    """Raised when a second durable supervisor targets the same project."""


@contextmanager
def _supervisor_lock(root: Path):
    """Allow exactly one ``ralph loop`` owner per project.

    Field reservations are protected by a separate lock, but that is not
    enough for two parent supervisors: both can launch Claude contexts and
    race while reading/writing the same ``loop-state.json``.  The lock is
    advisory and process-owned, so it is released automatically when the
    supervisor exits or is killed.
    """

    lock_path = root / "loop-artifacts" / ".ralph-supervisor.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    handle = lock_path.open("a+", encoding="utf-8")
    try:
        if fcntl is None:  # pragma: no cover - Windows fallback
            raise SupervisorAlreadyRunning(
                "当前平台没有可用的进程锁；请不要同时启动两个 ralph loop。"
            )
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise SupervisorAlreadyRunning(
                f"项目已有 ralph loop 运行：{root}。"
                "请先运行 `ralph status <project>`，不要重复启动 supervisor。"
            ) from exc
        handle.seek(0)
        handle.truncate()
        handle.write(json.dumps({"pid": os.getpid(), "project": str(root)}, ensure_ascii=False))
        handle.flush()
        yield
    finally:
        try:
            if fcntl is not None:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        finally:
            handle.close()


PROJECT_CLAUDE_FALLBACK = """# CLAUDE.md — RALPH project

本项目由 `ralph run` 初始化。

## RALPH 运行规则

- 先读取 `loop-state.json`，当前阶段以其中的 `stage` 为准。
- 允许多轮增量填写，不要求一次生成完整任务分解。
- 若字段草稿不存在，先运行 `ralph field-init .`；把字段增量写入 `loop-artifacts/stages/<stage>/<revision>/fields.json`，然后运行 `ralph field-apply . <字段文件>`。
- 不得用 Write/Edit 直接修改 `loop-state.json`；字段通过 runtime 原子合并。
- 普通缺失字段只按 Hook 提示继续修复；受保护文件、危险副作用和 `ralph apply` 才使用硬门禁。
- 通过阶段时写入同目录 `advance.json`，运行 `ralph apply . <advance.json>`。
- Agent 是可选的窄任务协作者；研究字段和 DAG 节点分别使用自己的受控 JSON，不靠自然语言回执判定完成。
- 人类阻塞只阻塞当前任务，应返回 `blocked_human` 并继续其他 ready 任务。
- 过程记录在 `loop-events.md`，完整输出放在 `loop-artifacts/`。
- 需要诊断时运行 `ralph events . --tail 20` 获取有限摘要，不要复制完整事件日志。

本次任务由启动命令的最后一个参数提供。先理解任务，再从 `loop-state.json` 的当前阶段开始。
"""

# Keep RALPH's Claude sessions on an explicit compaction budget.  The product
# of these two values is the target at which Claude Code requests compaction.
# 100k * 50% gives the requested ~50k-token trigger while leaving the local
# oMLX backend well below its advertised 240k context ceiling.
DEFAULT_AUTO_COMPACT_WINDOW = 100_000
DEFAULT_AUTOCOMPACT_PERCENT = 50


def _state_path(project: str | Path) -> Path:
    path = Path(project).expanduser().resolve()
    return path if path.name == "loop-state.json" else path / "loop-state.json"


def _project_root(project: str | Path) -> Path:
    path = Path(project).expanduser().resolve()
    return path.parent if path.name == "loop-state.json" else path


def _workspace_root() -> Path | None:
    """Find the source workspace when running from the editable installation."""

    current = Path(__file__).resolve()
    for candidate in (current.parents[3], Path("/Users/a1-6/Desktop/workspace")):
        if (candidate / "agents-templates" / "RALPH-project" / "CLAUDE.md").exists():
            return candidate
    return None


def _project_claude_text() -> str:
    workspace = _workspace_root()
    if workspace is not None:
        template = workspace / "agents-templates" / "RALPH-project" / "CLAUDE.md"
        return template.read_text(encoding="utf-8")
    return PROJECT_CLAUDE_FALLBACK


def _claude_executable() -> str:
    """Return Claude Code while allowing a user-specific executable override."""

    configured = os.environ.get("RALPH_CLAUDE_BIN", "claude")
    if Path(configured).is_absolute():
        if Path(configured).exists():
            return configured
    else:
        resolved = shutil.which(configured)
        if resolved:
            return resolved
        for fallback in ("/opt/homebrew/bin/claude", "/usr/local/bin/claude"):
            if Path(fallback).exists():
                return fallback
    raise OSError(
        "找不到 Claude Code 可执行文件。请确认 `claude` 在 PATH 中，"
        "或设置 RALPH_CLAUDE_BIN=/绝对路径/claude。"
    )


def _stage_executor_skill_context() -> tuple[str | None, Path | None]:
    """Load the user-owned stage skill as bounded Claude system context.

    A literal ``/ralph-stage-executor`` inside a generated user prompt is not
    a reliable slash-command invocation: local models may merely quote it or
    ignore it.  The global skill remains the single editable source, while
    this adapter makes its workflow available to every fresh RALPH Commander
    context before the first tool choice.
    """

    override = os.environ.get("RALPH_STAGE_EXECUTOR_SKILL", "").strip()
    candidates = [Path(override).expanduser()] if override else []
    candidates.append(Path.home() / ".claude" / "skills" / "ralph-stage-executor" / "SKILL.md")
    for path in candidates:
        try:
            raw = path.read_text(encoding="utf-8").strip()
        except OSError:
            continue
        if not raw:
            continue
        if raw.startswith("---"):
            _, marker, body = raw.partition("\n---")
            if marker:
                raw = body.lstrip()
        # A skill is guidance, not an unbounded replacement system prompt.
        return (
            "# Required RALPH stage-execution skill\n"
            "Treat the following workflow as mandatory guidance. Runtime Hook "
            "decisions and ralph validation remain authoritative.\n\n"
            + raw[:12_000],
            path,
        )
    return None, None


def _append_stage_executor_skill(command: list[str]) -> Path | None:
    """Attach the global RALPH skill to a fresh Commander without duplicating it."""

    context, path = _stage_executor_skill_context()
    if context:
        command.extend(["--append-system-prompt", context])
    return path


def _ensure_project_scaffold(root: Path) -> list[str]:
    """Create only missing project bootstrap files; never overwrite user files."""

    created: list[str] = []
    claude_path = root / "CLAUDE.md"
    if not claude_path.exists():
        claude_path.write_text(_project_claude_text(), encoding="utf-8")
        created.append(str(claude_path))

    workspace = _workspace_root()
    agents_source = workspace / "agents" if workspace is not None else None
    agents_link = root / ".claude" / "agents"
    if agents_source is not None and agents_source.is_dir() and not agents_link.exists() and not agents_link.is_symlink():
        agents_link.parent.mkdir(parents=True, exist_ok=True)
        agents_link.symlink_to(agents_source, target_is_directory=True)
        created.append(str(agents_link))
    return created


def prepare_project(
    project: str | Path,
    task: str | None = None,
    mode: str = "hybrid",
    record_session: bool = False,
    fresh_if_completed: bool = False,
    stop_policy: str | None = None,
) -> tuple[Path, Path, bool, list[str]]:
    """Ensure a project can start and optionally attach the user's task."""

    root = _project_root(project)
    root.mkdir(parents=True, exist_ok=True)
    state_path = root / "loop-state.json"
    is_new = not state_path.exists()
    reopened_from_completed = False
    task_update_preserved = False
    empty_task_adopted = False
    if is_new:
        legacy_state = load_legacy_markdown(
            root / ".claude" / "ralph-loop.local.md",
            root.name or str(root),
        )
        initial_state = legacy_state or create_state(root.name or str(root), task=task)
        if task:
            initial_state = set_task(initial_state, task)
        if fresh_if_completed and task and initial_state.get("status") == "completed":
            initial_state = start_new_task(initial_state, task)
            reopened_from_completed = True
        save_state(state_path, initial_state)
    elif task:
        current = load_state(state_path)
        if fresh_if_completed and current.get("status") == "completed":
            current = start_new_task(current, task)
            reopened_from_completed = True
            save_state(state_path, current)
        else:
            current_task = current.get("task", {}) if isinstance(current.get("task"), dict) else {}
            current_description = str(current_task.get("description") or "").strip()
            if not current_description:
                # ``ralph init`` deliberately creates a task-less scaffold.
                # The first explicit `ralph loop <project> <task>` must adopt
                # that task rather than treating it as a late refinement of a
                # non-existent job.  Otherwise task-specific modes (such as
                # flow_only) disappear into authoritative_inputs while the
                # field queue is generated with the wrong policy.
                current = set_task(current, task, source="ralph loop")
                save_state(state_path, current)
                empty_task_adopted = True
            elif current_description != task:
                # A repeated ``ralph loop <project> <task>`` may be a
                # refinement, but it may also be an entirely different job.
                # Never overwrite the active task while retaining its old
                # stage/field decomposition: that hybrid state is internally
                # contradictory and makes a Commander validate unrelated
                # fields.  Keep the canonical task immutable until an
                # explicit new-task transition; preserve the new wording as a
                # human input for the current task to integrate or defer.
                updated = record_human_input(current, task, source="ralph loop")
                save_state(state_path, updated)
                task_update_preserved = True

    events_path = root / "loop-events.md"
    events_path.touch(exist_ok=True)
    persisted_state = load_state(state_path)
    materialize_field_tasks(root, persisted_state)
    save_state(state_path, persisted_state)
    materialize_contract_documents(root, persisted_state)
    created = _ensure_project_scaffold(root)
    settings_path = install_hooks(root, mode, stop_policy=stop_policy)
    if record_session:
        append_observation(
            events_path,
            "session_started",
            {
                "project": str(root),
                "new_project_state": is_new,
                "task": task or "",
                "created_files": created,
                "hook_mode": mode,
                "reopened_from_completed": reopened_from_completed,
                "empty_task_adopted": empty_task_adopted,
                "task_update_preserved_as_input": task_update_preserved,
            },
        )
    if empty_task_adopted:
        append_observation(
            events_path,
            "empty_task_adopted",
            {
                "stage": persisted_state.get("stage", {}).get("id"),
                "revision": persisted_state.get("stage", {}).get("revision"),
                "source": "ralph loop",
                "reason": "empty ralph init scaffold adopted its first explicit loop task",
            },
        )
    if task_update_preserved:
        append_observation(
            events_path,
            "task_update_preserved_as_input",
            {
                "stage": persisted_state.get("stage", {}).get("id"),
                "revision": persisted_state.get("stage", {}).get("revision"),
                "canonical_task_preserved": True,
                "reason": "new task text was recorded as human input instead of overwriting active decomposition",
            },
        )
    return root, settings_path, is_new, created


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ralph", description="Minimal RALPH state-machine runtime")
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init")
    init.add_argument("project")
    init.add_argument(
        "--workflow",
        choices=("prompt-first", "field"),
        default="prompt-first",
        help="默认创建 Markdown prompt-first 项目；旧字段运行时用 --workflow field。",
    )

    status = sub.add_parser("status")
    status.add_argument("project")
    status.add_argument(
        "--full",
        action="store_true",
        help="输出完整 loop-state.json；默认只输出不注入大上下文的摘要",
    )

    field_status = sub.add_parser(
        "field-status",
        help="status 的字段中心别名：只输出当前字段/DAG 的有限摘要，避免读取完整事件日志",
    )
    field_status.add_argument("project")
    field_status.add_argument("--full", action="store_true", help="输出完整 loop-state.json")

    events = sub.add_parser(
        "events",
        help="只读取事件日志的有限尾部摘要，避免把完整 loop-events.md 注入模型上下文",
    )
    events.add_argument("project", nargs="?", default=".")
    events.add_argument("--tail", type=int, default=20, help="返回最近多少个事件（最多 20）")

    task_next = sub.add_parser(
        "task-next",
        help="扫描项目 tasks/TASKS.md，返回最高优先级且依赖已满足的任务（只读）",
    )
    task_next.add_argument("project", nargs="?", default=".")

    prompt = sub.add_parser("prompt")
    prompt_sub = prompt.add_subparsers(dest="prompt_command", required=True)
    render = prompt_sub.add_parser("render")
    render.add_argument("project")
    replay = prompt_sub.add_parser("replay")
    replay.add_argument("fixture")

    apply = sub.add_parser("apply")
    apply.add_argument("project")
    apply.add_argument("action_file")

    field_apply = sub.add_parser(
        "field-apply",
        help="字段校验命令：把字段增量文件合并进 loop-state.json 的 attribute_matrix，"
        "校验通过才由 runtime 原子落盘（Commander 不得直接改 loop-state.json）。",
    )
    field_apply.add_argument("project", nargs="?", default=".", help="项目目录（默认当前目录）")
    field_apply.add_argument("fields_file", help="字段增量 JSON：列表，或 {fields:[...]} / {attribute_matrix:[...]}")

    field_init = sub.add_parser(
        "field-init",
        help="创建当前阶段的空字段草稿；已有草稿不覆盖，供 Agent 增量填写后再 field-apply",
    )
    field_init.add_argument("project", nargs="?", default=".", help="项目目录（默认当前目录）")

    field_reconcile = sub.add_parser(
        "field-reconcile",
        help="无损修复已 field-apply 但仍残留 dispatched 的字段任务；保留草稿和事件，仅重新开放待补字段。",
    )
    field_reconcile.add_argument("project", nargs="?", default=".", help="项目目录（默认当前目录）")

    web_llm_check = sub.add_parser(
        "web-llm-check",
        help="调用已配置的两个以上网页 LLM API 或受控 Playwright UI，并把可审计的交叉核验回执写入当前阶段目录",
    )
    web_llm_check.add_argument("project", nargs="?", default=".", help="项目目录（默认当前目录）")
    web_llm_check.add_argument(
        "request_file",
        help="当前阶段目录内的 {claim, context?, providers?} JSON，或含 field.attribute 的单字段 task JSON",
    )

    web_llm_authorize = sub.add_parser(
        "web-llm-authorize",
        help="由人类为本项目授权受控 Playwright 网页 LLM 站点；阶段 Agent 无权自行执行。",
    )
    web_llm_authorize.add_argument("project", nargs="?", default=".", help="项目目录（默认当前目录）")
    web_llm_authorize.add_argument(
        "--providers",
        nargs="+",
        choices=("perplexity", "chatgpt", "gemini"),
        help="授权的网页 LLM；省略时授权全部三个受支持站点。",
    )
    web_llm_authorize.add_argument(
        "--global",
        dest="global_scope",
        action="store_true",
        help="写入用户级授权，供所有项目复用；只有人类可执行。",
    )
    web_llm_authorize.add_argument(
        "--profile-dir",
        help="专用持久 Playwright profile 目录；首次需人类手动登录一次，之后各项目复用。",
    )

    web_llm_login = sub.add_parser(
        "web-llm-login",
        help="打开专用持久 profile 供人类一次性登录；不发送任何 LLM 提问。",
    )
    web_llm_login.add_argument("site", choices=("perplexity", "chatgpt", "gemini"))
    web_llm_login.add_argument(
        "--wait-seconds",
        type=int,
        default=900,
        help="可见登录窗口保留秒数（30–3600，默认 900）。",
    )

    graph_apply = sub.add_parser(
        "graph-apply",
        help="校验并完成一个 DAG 节点；按依赖更新 plan.completed、ready 节点和 Join 状态",
    )
    graph_apply.add_argument("project", nargs="?", default=".", help="项目目录（默认当前目录）")
    graph_apply.add_argument("task_file", help="当前阶段 graph task JSON")

    render_parser = sub.add_parser(
        "render",
        help="把阶段字段 JSON 自动渲染成易读 Markdown（写同级 .md 并打印）。"
        "不指定 json 文件时渲染当前阶段文件 current_artifact。",
    )
    render_parser.add_argument("project", nargs="?", default=".", help="项目目录（默认当前目录）")
    render_parser.add_argument("json_file", nargs="?", default=None, help="要渲染的 JSON（默认用当前阶段文件）")

    watch_parser = sub.add_parser(
        "watch",
        help="通用实时看板：轮询持久化状态/阶段文件/事件（不依赖 stdout），"
        "每 interval 秒刷新一次，任意项目可用，Ctrl-C 退出。",
    )
    watch_parser.add_argument("project", nargs="?", default=".", help="项目目录（默认当前目录）")
    watch_parser.add_argument("--interval", type=float, default=5.0, help="刷新间隔秒（默认 5）")
    watch_parser.add_argument("--lines", type=int, default=42, help="字段快照最多显示行数（默认 42）")

    recover_state = sub.add_parser(
        "recover-state",
        help="状态自愈/重置：loop-state.json 损坏或需回退时，从 .bak 或阶段快照恢复（即重置到上一阶段）。",
    )
    recover_state.add_argument("project", nargs="?", default=".", help="项目目录（默认当前目录）")
    recover_state.add_argument("--stage", default=None, help="恢复到指定阶段快照 loop-artifacts/snapshots/loop-state.<stage>.json")
    recover_state.add_argument("--to-backup", action="store_true", help="优先从 loop-state.json.bak 恢复")

    replay = sub.add_parser("replay")
    replay.add_argument("project")

    assemble = sub.add_parser(
        "assemble",
        help="合并 builder 切片为阶段结果工件（自动注入已有门禁回执）",
    )
    assemble.add_argument("project", nargs="?", default=".", help="项目目录（默认当前目录）")
    assemble.add_argument("--stage", default=None, help="覆盖阶段 id（默认用当前 loop-state.json）")
    assemble.add_argument("--revision", default=None, help="覆盖轮次（默认用当前 loop-state.json）")

    validate = sub.add_parser("validate")
    validate.add_argument("project", nargs="?", default=".", help="项目目录（默认当前目录）")
    validate.add_argument(
        "--result",
        default=None,
        help="校验 loop-artifacts/stages/ 下的阶段结果工件，而不是只检查当前 DAG",
    )
    validate.add_argument(
        "--apply",
        action="store_true",
        help="阶段结果工件校验通过后立即通过 runtime 原子应用",
    )

    benchmark = sub.add_parser(
        "benchmark-decomposition",
        help="只读评估简单 GPU 任务的完整语义分解和字段校验生命周期",
    )
    benchmark.add_argument("project", nargs="?", default=".")
    benchmark.add_argument(
        "--action-file",
        default=None,
        help="评估保存的 task-spec/action JSON，不读取项目状态",
    )
    benchmark.add_argument("--task", default=None, help="覆盖 benchmark 报告中的任务描述")
    benchmark.add_argument("--threshold", type=float, default=0.8, help="通过阈值，默认 0.8")

    hook = sub.add_parser("hook")
    hook.add_argument(
        "event",
        choices=(
            "pretooluse",
            "posttooluse",
            "subagentstart",
            "subagentstop",
            "userpromptsubmit",
            "precompact",
            "postcompact",
            "stop",
        ),
    )
    hook.add_argument("--mode", choices=HOOK_MODES, default=default_hook_mode())
    hook.add_argument("--stop-policy", choices=STOP_POLICIES, default=default_stop_policy())
    hook.add_argument("--no-auto-apply", action="store_true", help="只记录 Stop 输出，不自动应用结构化动作")

    install = sub.add_parser("install-hooks")
    install.add_argument("project")
    install.add_argument("--mode", choices=HOOK_MODES, default="hybrid")
    install.add_argument("--stop-policy", choices=STOP_POLICIES, default=default_stop_policy())

    start = sub.add_parser("start")
    start.add_argument("project", nargs="?", default=".")
    start.add_argument("--mode", choices=HOOK_MODES, default=default_hook_mode())
    start.add_argument("--stop-policy", choices=STOP_POLICIES, default=default_stop_policy())
    start.add_argument("--launch", action="store_true")
    start.add_argument("--prompt", default=None)
    start.add_argument("--effort", choices=("low", "medium", "high", "xhigh", "max"), default=None)
    start.add_argument("--model", default=None, help="仅本次 Claude 会话使用的模型名")
    _add_compaction_arguments(start)

    resume = sub.add_parser(
        "resume",
        help="从 loop-state.json 开一个短上下文的新 Claude 会话，恢复被运行时错误中断的阶段",
    )
    resume.add_argument("project", nargs="?", default=".")
    resume.add_argument("--mode", choices=HOOK_MODES, default=default_hook_mode())
    resume.add_argument("--stop-policy", choices=STOP_POLICIES, default=default_stop_policy())
    resume.add_argument("--prompt", default=None, help="覆盖自动生成的短恢复指令")
    resume.add_argument("--effort", choices=("low", "medium", "high", "xhigh", "max"), default=None)
    resume.add_argument("--model", default=None, help="仅本次 Claude 会话使用的模型名")
    _add_compaction_arguments(resume)

    run = sub.add_parser("run", help="自动初始化项目并用任务描述启动交互式 Claude 会话")
    run.add_argument("project_or_task", help="项目路径，或在省略 task 时直接填写任务描述")
    run.add_argument("task", nargs="?", help="显式项目路径模式下的任务描述")
    run.add_argument("--workspace", default=None, help="自动项目模式使用的 workspace 根目录")
    run.add_argument("--mode", choices=HOOK_MODES, default=default_hook_mode())
    run.add_argument("--stop-policy", choices=STOP_POLICIES, default=default_stop_policy())
    run.add_argument("--effort", choices=("low", "medium", "high", "xhigh", "max"), default=None)
    run.add_argument("--model", default=None, help="仅本次 Claude 会话使用的模型名")
    run.add_argument(
        "--dangerously-skip-permissions",
        action="store_true",
        help="跳过 Claude Code 交互式权限确认（RALPH Hook 仍强制派发/校验规则），便于无人值守可见 TUI",
    )
    _add_compaction_arguments(run)

    loop = sub.add_parser(
        "loop",
        help="持续监督：Stop 默认在同一 Claude 上下文继续；运行时中断才从 loop-state.json 恢复",
    )
    loop.add_argument("project_or_task", help="项目路径，或在省略 task 时直接填写任务描述")
    loop.add_argument("task", nargs="?", help="显式项目路径模式下的任务描述")
    loop.add_argument("--workspace", default=None, help="自动项目模式使用的 workspace 根目录")
    loop.add_argument(
        "--workflow",
        choices=("auto", "prompt-first", "field"),
        default="auto",
        help="auto：新显式项目用 Markdown prompt-first，已有 loop-state.json 保持字段兼容；可显式覆盖。",
    )
    loop.add_argument("--mode", choices=HOOK_MODES, default=default_hook_mode())
    loop.add_argument("--stop-policy", choices=STOP_POLICIES, default=default_stop_policy())
    loop.add_argument("--effort", choices=("low", "medium", "high", "xhigh", "max"), default=None)
    loop.add_argument("--model", default=None, help="仅本次 Claude 会话使用的模型名")
    loop.add_argument("--max-cycles", type=int, default=0, help="最多运行多少个新上下文；0 表示持续运行")
    loop.add_argument(
        "--max-failed-cycles",
        type=int,
        default=0,
        help="连续非零退出多少轮后熔断；默认 0 表示持续恢复、不熔断",
    )
    loop.add_argument("--retry-delay", type=float, default=3.0, help="会话退出后再次启动前等待秒数")
    loop.add_argument("--agent-grace-seconds", type=float, default=5.0, help="回收残留任务卡前等待秒数")
    loop.add_argument("--idle-timeout", type=float, default=0.0, help="无状态/事件活动多久后重启当前上下文；默认 0 表示不启用")
    loop.add_argument("--wait-human", action="store_true", help="遇到 blocked_human 时等待人类，而不是按策略跳过")
    loop.add_argument(
        "--dangerously-skip-permissions",
        action="store_true",
        help="跳过 Claude Code 交互式权限确认（RALPH Hook 仍强制派发/校验规则），便于无人值守可见 TUI",
    )
    _add_compaction_arguments(loop)

    prompt_first = sub.add_parser(
        "prompt-first",
        help="Markdown 阶段卡工作流：无字段/DAG/工具语义校验，只用 Stop Hook 续跑。",
    )
    prompt_first_sub = prompt_first.add_subparsers(dest="prompt_first_command", required=True)
    prompt_first_init = prompt_first_sub.add_parser("init", help="创建 ralph-loop.md 与阶段 01 Markdown 模板")
    prompt_first_init.add_argument("project", nargs="?", default=".")
    prompt_first_init.add_argument("task", nargs="?", default="")
    prompt_first_status = prompt_first_sub.add_parser("status", help="查看 Markdown 阶段游标")
    prompt_first_status.add_argument("project", nargs="?", default=".")
    prompt_first_render = prompt_first_sub.add_parser("render", help="渲染当前阶段的短提示")
    prompt_first_render.add_argument("project", nargs="?", default=".")
    prompt_first_loop = prompt_first_sub.add_parser("loop", help="在同一 Commander/TUI 中持续完成 Markdown 阶段")
    prompt_first_loop.add_argument("project")
    prompt_first_loop.add_argument("task")
    prompt_first_loop.add_argument("--effort", choices=("low", "medium", "high", "xhigh", "max"), default=None)
    prompt_first_loop.add_argument("--model", default=None)
    prompt_first_loop.add_argument("--max-cycles", type=int, default=0)
    prompt_first_loop.add_argument("--retry-delay", type=float, default=3.0)
    prompt_first_loop.add_argument("--idle-timeout", type=float, default=0.0)
    prompt_first_loop.add_argument("--dangerously-skip-permissions", action="store_true")
    _add_compaction_arguments(prompt_first_loop)
    prompt_first_review = prompt_first_sub.add_parser(
        "review",
        help="在独立只读 Claude 上下文中审阅当前阶段并写入 Reviewer 回执",
    )
    prompt_first_review.add_argument("project")
    prompt_first_review.add_argument("--effort", choices=("low", "medium", "high", "xhigh", "max"), default=None)
    prompt_first_review.add_argument("--model", default=None)
    prompt_first_review.add_argument("--dangerously-skip-permissions", action="store_true")
    prompt_first_web = prompt_first_sub.add_parser(
        "web-llm",
        help="用已授权的本地 Playwright/API 网页 LLM 做一次交叉询问，并写 Markdown 回执",
    )
    prompt_first_web.add_argument("project", nargs="?", default=".")
    prompt_first_web.add_argument("question", nargs="?", default="", help="可选的聚焦主张；省略时从当前 Markdown 任务生成")
    prompt_first_web.add_argument("--context", default="", help="给网页 LLM 的简短背景")
    # This is installed into the prompt-first settings file as its sole Hook.
    # It is intentionally a top-level command so Claude Code can invoke it
    # without needing to understand argparse's nested subcommands.
    sub.add_parser("prompt-first-post-tool", help=argparse.SUPPRESS)
    sub.add_parser("prompt-first-pre-tool", help=argparse.SUPPRESS)
    sub.add_parser("prompt-first-precompact", help=argparse.SUPPRESS)
    sub.add_parser("prompt-first-postcompact", help=argparse.SUPPRESS)
    sub.add_parser("prompt-first-stop", help=argparse.SUPPRESS)

    return parser


def _hook_command(event: str, mode: str, stop_policy: str = "inline") -> str:
    command = f"{shlex.quote(sys.executable)} -m ralph_runtime.cli hook {event} --mode {shlex.quote(mode)}"
    if event == "stop":
        command += f" --stop-policy {shlex.quote(stop_policy)}"
    return command


def _with_effort(command: list[str], effort: str | None) -> list[str]:
    selected = effort or os.environ.get("RALPH_CLAUDE_EFFORT")
    if selected:
        command.extend(["--effort", selected])
    return command


def _with_model(command: list[str], model: str | None) -> list[str]:
    """Apply an optional session-only model override without changing user settings."""

    selected = model or os.environ.get("RALPH_CLAUDE_MODEL")
    if selected:
        command.extend(["--model", selected])
    return command


def _with_skip_permissions(command: list[str], skip: bool) -> list[str]:
    """Bypass Claude Code's interactive permission prompts for supervised runs.

    The RALPH hook chain still enforces every dispatch/validation rule; this only
    removes the separate Claude Code permission confirmation so an autonomous
    loop can run unattended under a visible TUI.
    """

    if skip:
        command.append("--dangerously-skip-permissions")
    return command


def _claude_environment(
    auto_compact_window: int | None = None,
    auto_compact_percent: int | None = None,
) -> tuple[dict[str, str], int, int]:
    """Build the environment for a RALPH-controlled Claude session.

    ``CLAUDE_CODE_AUTO_COMPACT_WINDOW`` is the capacity used by Claude Code's
    compaction calculation, while ``CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`` is the
    percentage at which compaction is requested. The defaults therefore aim
    at roughly 50k tokens (100k * 50%), leaving room for the compaction request
    before oMLX reaches the active-prefill memory guard.
    """

    raw_window = (
        auto_compact_window
        if auto_compact_window is not None
        else os.environ.get("RALPH_AUTO_COMPACT_WINDOW", str(DEFAULT_AUTO_COMPACT_WINDOW))
    )
    raw_percent = (
        auto_compact_percent
        if auto_compact_percent is not None
        else os.environ.get("RALPH_AUTOCOMPACT_PCT", str(DEFAULT_AUTOCOMPACT_PERCENT))
    )
    try:
        window = int(raw_window)
    except (TypeError, ValueError) as exc:
        raise ValueError("auto-compact window 必须是正整数 token 数") from exc
    try:
        percent = int(raw_percent)
    except (TypeError, ValueError) as exc:
        raise ValueError("auto-compact percent 必须是 1 到 100 的整数") from exc
    if window <= 0:
        raise ValueError("auto-compact window 必须大于 0")
    if not 1 <= percent <= 100:
        raise ValueError("auto-compact percent 必须在 1 到 100 之间")

    environment = os.environ.copy()
    environment["CLAUDE_CODE_AUTO_COMPACT_WINDOW"] = str(window)
    environment["CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"] = str(percent)
    return environment, window, percent


def _print_compaction_settings(window: int, percent: int) -> None:
    target = window * percent // 100
    print(f"Auto compact: capacity={window} tokens, trigger≈{target} tokens ({percent}%)")


def _add_compaction_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--auto-compact-window",
        type=int,
        default=None,
        help="本次 RALPH 会话用于自动压缩计算的容量；默认 100000，配合 50%% 约在 50k 触发",
    )
    parser.add_argument(
        "--auto-compact-percent",
        type=int,
        default=None,
        help="自动压缩触发百分比（1-100）；默认 50",
    )


def install_hooks(
    project: str | Path,
    mode: str = "hybrid",
    stop_policy: str | None = None,
) -> Path:
    root = Path(project).expanduser().resolve()
    selected_stop_policy = stop_policy or default_stop_policy()
    if selected_stop_policy not in STOP_POLICIES:
        raise ValueError(f"unsupported stop policy: {selected_stop_policy}")
    root.mkdir(parents=True, exist_ok=True)
    state_path = root / "loop-state.json"
    if not state_path.exists():
        save_state(state_path, create_state(root.name or str(root)))
    (root / "loop-events.md").touch(exist_ok=True)
    settings_path = root / ".claude" / "settings.ralph.json"
    settings_path.parent.mkdir(parents=True, exist_ok=True)
    settings = {
        "hooks": {
            "UserPromptSubmit": [{"hooks": [{"type": "command", "command": _hook_command("userpromptsubmit", mode)}]}],
            "PreToolUse": [{"matcher": ".*", "hooks": [{"type": "command", "command": _hook_command("pretooluse", mode)}]}],
            "PostToolUse": [{"matcher": ".*", "hooks": [{"type": "command", "command": _hook_command("posttooluse", mode)}]}],
            "SubagentStart": [{"hooks": [{"type": "command", "command": _hook_command("subagentstart", mode)}]}],
            "SubagentStop": [{"hooks": [{"type": "command", "command": _hook_command("subagentstop", mode)}]}],
            "PreCompact": [{"matcher": ".*", "hooks": [{"type": "command", "command": _hook_command("precompact", mode)}]}],
            "PostCompact": [{"matcher": ".*", "hooks": [{"type": "command", "command": _hook_command("postcompact", mode)}]}],
            "Stop": [
                {
                    "hooks": [
                        {
                            "type": "command",
                            "command": _hook_command("stop", mode, selected_stop_policy),
                        }
                    ]
                }
            ],
        }
    }
    settings_path.write_text(json.dumps(settings, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return settings_path


def _prompt_first_hook_command() -> str:
    return f"{shlex.quote(sys.executable)} -m ralph_runtime.cli prompt-first-stop"


def _prompt_first_post_tool_hook_command() -> str:
    return f"{shlex.quote(sys.executable)} -m ralph_runtime.cli prompt-first-post-tool"


def _prompt_first_pre_tool_hook_command() -> str:
    return f"{shlex.quote(sys.executable)} -m ralph_runtime.cli prompt-first-pre-tool"


def _prompt_first_precompact_hook_command() -> str:
    return f"{shlex.quote(sys.executable)} -m ralph_runtime.cli prompt-first-precompact"


def _prompt_first_postcompact_hook_command() -> str:
    return f"{shlex.quote(sys.executable)} -m ralph_runtime.cli prompt-first-postcompact"


def install_prompt_first_hooks(project: str | Path) -> Path:
    """Install prompt-first routing hooks and a narrow research liveness guard."""

    root = Path(project).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    settings_path = root / ".claude" / "settings.ralph-prompt-first.json"
    settings_path.parent.mkdir(parents=True, exist_ok=True)
    settings = {
        # Manual Herdr ``claude --resume`` must receive the same proactive
        # compaction budget as the supervisor-launched process. Without this
        # project-level env, a long same-context Reviewer loop can reach the
        # provider's hard context limit before Stop Hook gets another chance.
        "env": {
            "CLAUDE_CODE_AUTO_COMPACT_WINDOW": str(DEFAULT_AUTO_COMPACT_WINDOW),
            "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": str(DEFAULT_AUTOCOMPACT_PERCENT),
        },
        "hooks": {
            "PreToolUse": [{
                "matcher": ".*",
                "hooks": [{
                    "type": "command",
                    "command": _prompt_first_pre_tool_hook_command(),
                }],
            }],
            "PostToolUse": [
                {
                    "matcher": ".*",
                    # A prompt-first Write is followed by a synchronous
                    # Reviewer.  A blocking result must end this assistant
                    # turn so Claude's Stop Hook can route the result; true
                    # explicitly tells Claude to keep reasoning in the same
                    # turn and can create an unbounded transcript.
                    "continueOnBlock": False,
                    "hooks": [{
                        "type": "command",
                        "command": _prompt_first_post_tool_hook_command(),
                        "timeout": 600,
                    }],
                }
            ],
            "PreCompact": [{"matcher": ".*", "hooks": [{
                "type": "command",
                "command": _prompt_first_precompact_hook_command(),
            }]}],
            "PostCompact": [{"matcher": ".*", "hooks": [{
                "type": "command",
                "command": _prompt_first_postcompact_hook_command(),
            }]}],
            "Stop": [{"hooks": [{
                "type": "command",
                "command": _prompt_first_hook_command(),
                "timeout": 600,
            }]}],
        }
    }
    settings_path.write_text(json.dumps(settings, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return settings_path


def _ensure_prompt_first_scaffold(root: Path) -> list[str]:
    """Add a concise project instruction without overwriting user guidance."""

    created: list[str] = []
    claude_path = root / "CLAUDE.md"
    if not claude_path.exists():
        claude_path.write_text(
            "# RALPH Prompt-First\n\n"
            "For an untouched automatic template, use the injected cursor, task, target, and stage rules; "
            "because Claude Code's Write requires a prior Read, read the current artifact once and then write it. "
            "For substantive work or a Reviewer revision, "
            "read `ralph-loop.md` and the current Markdown artifact. Work through the "
            "stage in ordinary Markdown. Stop after writing; the Stop Hook launches "
            "an independent Reviewer and persists `latest-review.md`. Append "
            "`<!-- ralph: done -->` only after Reviewer pass. A revise verdict stays "
            "in the same stage. Do not use field/DAG JSON workflows in this project.\n",
            encoding="utf-8",
        )
        created.append(str(claude_path))
    return created


def _prompt_first_skill_context() -> tuple[str, Path | None]:
    workspace = _workspace_root()
    candidates = [
        workspace / ".claude" / "skills" / "ralph-prompt-first" / "SKILL.md"
        if workspace is not None else None,
        Path.home() / ".claude" / "skills" / "ralph-prompt-first" / "SKILL.md",
    ]
    for path in candidates:
        if path is None:
            continue
        try:
            raw = path.read_text(encoding="utf-8").strip()
        except OSError:
            continue
        if raw.startswith("---"):
            _, marker, body = raw.partition("\n---")
            if marker:
                raw = body.lstrip()
        if raw:
            return "# Required RALPH prompt-first skill\n\n" + raw[:6_000], path
    return prompt_first_system_prompt(), None


def _prompt_first_reviewer_prompt(root: Path, state: Mapping[str, str]) -> str:
    artifact = root / state["current_artifact"]
    rules = load_stage_rules(root, state["stage"])
    try:
        artifact_text = artifact.read_text(encoding="utf-8")
    except OSError as exc:
        artifact_text = f"（无法读取当前工件快照：{exc}）"
    current_date = datetime.now(ZoneInfo("Asia/Shanghai")).date().isoformat()
    return (
        "你是 RALPH 的独立阶段 Reviewer，不是 Commander，也不是执行者。\n"
        "运行时已经从磁盘读取并注入了当前阶段规则和 Markdown 工件的精确快照；"
        "直接依据下面的快照审阅，不要调用任何工具。你没有文件写入、搜索、网页或编译权限。"
        "不要说‘我先读取’、不要输出审阅计划，也不要以半截思考结束；快照已经完整提供。"
        "直接返回命令行提供的结构化 Reviewer 回执，不要输出 JSON 之外的文字。\n\n"
        f"项目任务：{state['task']}\n"
        f"当前日期（Asia/Shanghai）：{current_date}\n"
        f"阶段：{state['stage']}\n"
        f"阶段规则文件：{rules['path'] or '缺失'}\n"
        f"当前工件：{artifact}\n\n"
        "--- 阶段规则（仍须以文件内容为准） ---\n"
        f"{rules['text']}\n"
        "--- 阶段规则结束 ---\n\n"
        "--- 当前 Markdown 工件快照（只读） ---\n"
        f"{artifact_text}\n"
        "--- 当前 Markdown 工件快照结束 ---\n\n"
        "审阅时完全依据上面的外部规则，尤其是其中的 Reviewer 质检标准；"
        "不要增加 Python 或本提示词中没有定义的字段门槛。\n"
        "对发现的每个问题说明位置、影响和具体修复行动；如果问题需要回到更早阶段补输入，"
        "repair_stage 写对应更早阶段；如果只需修订当前工件，写当前阶段。只有当前工件可以交给下一阶段时才 pass，"
        "不确定或存在关键缺口时必须 revise。\n\n"
        "这是强制输出协议：即使工件极短或信息不足，也必须给出具体缺口并判定 revise；"
        "不要调用工具、不要返回审阅计划、不要复述整个工件。请只返回命令行提供的 JSON schema，"
        "其中 report 不超过约 800 个中文字符，findings 最多 6 项；完成判断后立即结束。\n"
    )


def _prompt_first_reviewer_schema() -> dict[str, object]:
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "report": {"type": "string"},
            "findings": {
                "type": "array",
                "maxItems": 6,
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "location": {"type": "string"},
                        "impact": {"type": "string"},
                        "evidence_gap": {"type": "string"},
                        "repair_action": {"type": "string"},
                    },
                    "required": ["location", "impact", "evidence_gap", "repair_action"],
                },
            },
            "verdict": {"type": "string", "enum": ["pass", "revise"]},
            "repair_stage": {"type": "string"},
        },
        "required": ["report", "findings", "verdict", "repair_stage"],
    }


def _local_omlx_api_key() -> str:
    configured = os.environ.get("OMLX_API_KEY", "").strip()
    if configured:
        return configured
    settings = Path.home() / ".omlx" / "settings.json"
    try:
        data = json.loads(settings.read_text(encoding="utf-8"))
    except (OSError, ValueError, json.JSONDecodeError):
        return ""
    return str(data.get("auth", {}).get("api_key", "")).strip()


def _local_omlx_reviewer(
    system: str,
    prompt: str,
    *,
    schema: dict[str, object],
    model: str | None,
) -> str | None:
    """Run the Reviewer directly against the local default model, serially."""

    base_url = os.environ.get(
        "RALPH_PROMPT_FIRST_OMLX_URL", "http://127.0.0.1:8000"
    ).rstrip("/")
    headers = {"Content-Type": "application/json"}
    api_key = _local_omlx_api_key()
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    try:
        status_request = urllib.request.Request(f"{base_url}/api/status", headers=headers)
        with urllib.request.urlopen(status_request, timeout=2) as response:
            status = json.loads(response.read().decode("utf-8"))
        default_model = str(status.get("default_model", "")).strip()
        if not default_model:
            return None
        payload = {
            "model": model or default_model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
            "max_tokens": 2048,
            "temperature": 0,
            "chat_template_kwargs": {"enable_thinking": False},
            "response_format": {
                "type": "json_schema",
                "json_schema": {"name": "ralph_reviewer", "schema": schema},
            },
        }
        request = urllib.request.Request(
            f"{base_url}/v1/chat/completions",
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers=headers,
            method="POST",
        )
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode("utf-8"))
        content = result.get("choices", [{}])[0].get("message", {}).get("content")
        return str(content) if content else None
    except (OSError, ValueError, json.JSONDecodeError, KeyError, IndexError, urllib.error.URLError):
        return None


def prompt_first_review_project(
    project: str | Path,
    *,
    effort: str | None = None,
    model: str | None = None,
    skip_permissions: bool = False,
) -> int:
    """Run a read-only independent reviewer and persist its routing receipt."""

    root = Path(project).expanduser().resolve()
    state = load_prompt_first_state(root)
    artifact = root / state["current_artifact"]
    system = (
        "You are an independent, adversarial RALPH stage reviewer. "
        "The stage rule Markdown supplied in the user prompt is authoritative. "
        "Do not edit, create, delete, or execute project files. Report concrete "
        "findings and never manufacture evidence. The parent Commander will "
        "receive your report and must repair before it can advance."
    )
    reviewer_prompt = _prompt_first_reviewer_prompt(root, state)
    reviewer_schema = json.dumps(
        _prompt_first_reviewer_schema(),
        ensure_ascii=False,
        separators=(",", ":"),
    )
    transport = os.environ.get("RALPH_PROMPT_FIRST_REVIEW_TRANSPORT", "auto").strip().lower()
    if transport in {"auto", "omlx"}:
        local_output = _local_omlx_reviewer(
            system,
            reviewer_prompt,
            schema=_prompt_first_reviewer_schema(),
            model=model,
        )
        if local_output is not None:
            summary = record_reviewer_result(root, local_output, return_code=0)
            print(
                json.dumps(
                    {
                        **summary,
                        "artifact": state["current_artifact"],
                        "artifact_sha256": artifact_sha256(artifact),
                        "reviewer_transport": "omlx",
                    },
                    ensure_ascii=False,
                    indent=2,
                    sort_keys=True,
                )
            )
            return 0 if summary["verdict"] in {"pass", "revise"} else 2

    command = [
        _claude_executable(),
        "-p",
        "--output-format",
        "json",
        "--json-schema",
        reviewer_schema,
        "--no-session-persistence",
        "--permission-mode",
        "plan",
        "--setting-sources",
        "user",
        "--disable-slash-commands",
        "--tools",
        "",
        # The Reviewer is a read-only one-turn classifier.  Inheriting Claude's
        # full default system prompt (skills, agent registry, environment and
        # tool descriptions) needlessly expands the local model context and can
        # push a substantive Markdown review past Claude Code's 600s Stop-hook
        # ceiling.  Keep the same provider-default model, but give this role a
        # minimal system prompt; the complete stage rules and artifact snapshot
        # remain in the user prompt below.
        "--system-prompt",
        system,
        reviewer_prompt,
    ]
    command = _with_skip_permissions(
        _with_model(_with_effort(command, effort), model),
        skip_permissions,
    )
    completed = subprocess.run(
        command,
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    summary = record_reviewer_result(
        root,
        completed.stdout,
        return_code=completed.returncode,
        error_output=completed.stderr,
    )
    print(
        json.dumps(
            {
                **summary,
                "artifact": state["current_artifact"],
                "artifact_sha256": artifact_sha256(artifact),
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if summary["verdict"] in {"pass", "revise"} else 2


def recover_card(
    project: str | Path,
    card_id: str,
    reason: str,
    force_dispatched: bool = False,
) -> dict[str, object]:
    """Safely reopen a stale task card after a controller failure."""

    root = _project_root(project)
    state_path = root / "loop-state.json"
    state = load_state(state_path)
    cards = state.get("subagent_cards", {})
    card = cards.get(card_id) if isinstance(cards, dict) else None
    if not isinstance(card, dict):
        raise ValueError(f"unknown task card: {card_id}")
    prior_status = str(card.get("status", "pending"))
    if prior_status == "dispatched" and not force_dispatched:
        raise ValueError(
            f"task card {card_id} is 'dispatched'; only completed or failed cards can be recovered. "
            "确认子代理已退出且没有 SubagentStop 回执后，请显式使用 --force-dispatched。"
        )
    if card.get("is_stage_gate"):
        safe_card_id = card_id.replace("/", "_")
        receipts = sorted((root / "loop-artifacts" / "gate-reviews").glob(f"{safe_card_id}-*.json"))
        if receipts:
            joined = ", ".join(str(path.relative_to(root)) for path in receipts)
            raise ValueError(
                "任务卡已有有效门禁回执，不能用 recover-card 覆盖；"
                f"请通过正常阶段动作处理。回执：{joined}"
            )
    prior_agent_id = card.get("agent_id")
    updated = reset_subagent_card(state, card_id, allow_dispatched=force_dispatched)
    save_state(state_path, updated)
    materialize_contract_documents(root, updated)
    append_observation(
        root / "loop-events.md",
        "subagent_card_recovered",
        {
            "task_card_id": card_id,
            "prior_status": prior_status,
            "prior_agent_id": prior_agent_id,
            "reason": reason,
            "gate_receipt_present": False,
        },
    )
    return {
        "project": str(root),
        "card_id": card_id,
        "prior_status": prior_status,
        "status": "pending",
        "reason": reason,
    }


def _valid_gate_receipt(root: Path, card_id: str) -> tuple[str, dict[str, object]] | None:
    """Find the latest trustworthy gate receipt for a task card.

    The event journal is authoritative for the existence of a receipt; the
    JSON artifact is checked again before a stale dispatched card is
    reconciled. This path is only called by the outer supervisor after the
    Claude process it owns has exited.
    """

    event_path = root / "loop-events.md"
    try:
        events = read_events(event_path)
    except (OSError, ValueError):
        events = []
    references: list[str] = []
    for event in reversed(events):
        if event.get("type") != "subagent_gate_review_received":
            continue
        observation = event.get("observation")
        if not isinstance(observation, dict) or str(observation.get("task_card_id", "")) != card_id:
            continue
        reference = observation.get("artifact_ref")
        if reference:
            references.append(str(reference))
            break
    if not references:
        safe_card_id = card_id.replace("/", "_")
        references = [
            str(path.relative_to(root))
            for path in sorted((root / "loop-artifacts" / "gate-reviews").glob(f"{safe_card_id}-*.json"))
        ]
    for reference in references:
        artifact = root / reference
        try:
            raw = json.loads(artifact.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(raw, dict):
            continue
        if str(raw.get("reviewer_card_id", "")) != card_id:
            continue
        if raw.get("verdict") not in {"pass", "rollback", "blocked_human"}:
            continue
        checks = raw.get("checks")
        if not isinstance(checks, list) or not checks:
            continue
        return reference, raw
    return None


def reconcile_stale_cards(
    project: str | Path,
    *,
    reason: str = "supervisor observed that the owning Claude process exited",
) -> list[dict[str, object]]:
    """Reconcile task cards left dispatched after a dead or terminated session.

    A valid gate receipt is promoted to completed. Without one, the card is
    reopened as pending. The supervisor is the only caller that may make this
    judgment automatically, because it has just observed the process it
    launched exit and can wait a short grace period first.
    """

    if field_mode_enabled():
        # Legacy card records are historical evidence only.  They must not
        # re-enter the active execution path during a field-centric resume.
        return []
    root = _project_root(project)
    state_path = root / "loop-state.json"
    state = load_state(state_path)
    stage = state.get("stage", {})
    stage_id = str(stage.get("id", ""))
    revision = str(stage.get("revision", ""))
    cards = state.get("subagent_cards", {})
    if not isinstance(cards, dict):
        return []
    results: list[dict[str, object]] = []
    for card_id, raw_card in list(cards.items()):
        if not isinstance(raw_card, dict):
            continue
        if str(raw_card.get("status")) != "dispatched":
            continue
        if str(raw_card.get("stage_id")) != stage_id or str(raw_card.get("revision")) != revision:
            continue
        receipt = _valid_gate_receipt(root, str(card_id)) if raw_card.get("is_stage_gate") else None
        prior_agent_id = raw_card.get("agent_id")
        if receipt is not None:
            artifact_ref, review = receipt
            updated = update_subagent_card(
                state,
                str(card_id),
                "completed",
                agent_id=str(prior_agent_id) if prior_agent_id else None,
            )
            updated_card = updated["subagent_cards"][str(card_id)]
            updated_card["gate_review_ref"] = artifact_ref
            updated_card["gate_verdict"] = str(review.get("verdict"))
            updated_card["reconciled_from"] = "dispatched"
            save_state(state_path, updated)
            materialize_contract_documents(root, updated)
            state = updated
            outcome = "completed"
            detail: dict[str, object] = {
                "gate_review_ref": artifact_ref,
                "gate_verdict": review.get("verdict"),
            }
        else:
            updated = reset_subagent_card(state, str(card_id), allow_dispatched=True)
            save_state(state_path, updated)
            materialize_contract_documents(root, updated)
            state = updated
            outcome = "pending"
            detail = {"gate_review_ref": None}
        observation = {
            "task_card_id": str(card_id),
            "prior_status": "dispatched",
            "prior_agent_id": prior_agent_id,
            "outcome": outcome,
            "reason": reason,
            **detail,
        }
        append_observation(root / "loop-events.md", "subagent_card_reconciled", observation)
        results.append({"card_id": str(card_id), "outcome": outcome, **detail})
    return results


def task_next(project: str | Path) -> dict[str, object]:
    """Read the local task board without changing state or claiming a task."""

    root = _project_root(project)
    state = load_state(root / "loop-state.json")
    board_path = "tasks/TASKS.md"
    items = read_task_board(root, board_path)
    selected = select_next_task(root, board_path)
    selection = selected.selection() if selected else None
    if selected is not None:
        reason = "已找到最高优先级且依赖已满足的 ready/pending 任务；由探索节点提交后才会 claim。"
    elif not items:
        reason = "项目没有可读取的 tasks/TASKS.md，探索节点应输出 preference_brief 和 candidate 任务。"
    else:
        reason = "任务板存在，但没有可执行的 ready/pending 任务；探索节点应输出 preference_brief 和 candidate 任务。"
    return {
        "project": str(root),
        "stage": {
            "id": state.get("stage", {}).get("id"),
            "revision": state.get("stage", {}).get("revision"),
        },
        "board": board_path,
        "task_count": len(items),
        "ready": selected is not None,
        "selection": selection,
        "reason": reason,
    }


def benchmark_decomposition(
    project: str | Path = ".",
    *,
    action_file: str | Path | None = None,
    task: str | None = None,
    threshold: float = 0.8,
) -> dict[str, object]:
    """Run the read-only simple-task decomposition benchmark.

    With a project argument this grades the persisted ``loop-state.json`` and
    also checks that the requirements auditor card really completed.  With
    ``--action-file`` it grades a saved task-spec/action payload only, which is
    useful before a project is created or for deterministic fixture replay.
    """

    if not 0 < threshold <= 1:
        raise ValueError("benchmark threshold 必须在 0 和 1 之间")
    if action_file is not None:
        candidate, file_task = load_task_spec_file(action_file)
        result = evaluate_task_spec(
            candidate,
            task=task or file_task or DEFAULT_SIMPLE_GPU_TASK,
            threshold=threshold,
        )
        source = str(Path(action_file).expanduser().resolve())
        project_ref = None
    else:
        root = _project_root(project)
        state = load_state(root / "loop-state.json")
        result = evaluate_state(state, task=task, threshold=threshold)
        source = str(root / "loop-state.json")
        project_ref = str(root)
    report = result.to_dict()
    report["source"] = source
    report["project"] = project_ref
    report["read_only"] = True
    return report


def _bounded_event_text(value: object, limit: int = 600) -> str:
    text = str(value or "").replace("\x00", " ").strip()
    if len(text) <= limit:
        return text
    return text[:limit] + "\n[… 事件摘要已截断 …]"


def _event_summary(event: dict[str, object]) -> dict[str, object]:
    """Return audit metadata without replaying full Agent/tool output."""

    summary: dict[str, object] = {
        "event_id": event.get("event_id"),
        "type": event.get("type"),
        "timestamp": event.get("timestamp"),
    }
    for key in ("stage", "revision"):
        if event.get(key) is not None:
            summary[key] = event.get(key)

    action = event.get("action")
    if isinstance(action, dict):
        summary["action"] = {
            key: action.get(key)
            for key in ("action", "status", "stage_id", "revision", "next_stage", "rollback_to")
            if action.get(key) is not None
        }

    observation = event.get("observation")
    if isinstance(observation, dict):
        observation_summary: dict[str, object] = {}
        for key in (
            "tool_name",
            "role",
            "decision",
            "reason",
            "task_card_id",
            "agent_id",
            "task_card_status",
            "kind",
            "stop_reason",
            "recovery",
            "state_preserved",
        ):
            if observation.get(key) is not None:
                value = observation.get(key)
                observation_summary[key] = _bounded_event_text(value) if key in {"reason", "stop_reason"} else value
        if observation_summary:
            summary["observation"] = observation_summary

    output = event.get("output_excerpt")
    if output:
        summary["output_excerpt"] = _bounded_event_text(output)
    return summary


def assemble_stage_result(
    project: str | Path,
    stage_id: str | None = None,
    revision: str | None = None,
) -> dict[str, object]:
    """Merge builder slices into the canonical stage result artifact.

    Builders write one ``payload`` slice each to
    ``loop-artifacts/stages/<stage>/<rev>/<key>.json``.  This command is the
    only place the large result is assembled, so the Commander never has to
    author it inline.  If a valid independent gate review exists it is injected
    into ``payload.stage_review`` automatically.
    """

    root = _project_root(project)
    state = load_state(root / "loop-state.json")
    stage = state.get("stage", {})
    if stage_id is None:
        stage_id = str(stage.get("id", ""))
    if revision is None:
        revision = str(stage.get("revision", "r1"))

    base = stage_submission_template(state)
    slice_dir = root / "loop-artifacts" / "stages" / stage_id / revision
    merged_keys: list[str] = []
    if slice_dir.is_dir():
        for path in sorted(slice_dir.glob("*.json")):
            key = path.stem
            if key in {"manifest"}:
                continue
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            base.setdefault("payload", {})[key] = data
            merged_keys.append(key)

    gate_review_injected = False
    gate = next(
        (
            card
            for card in cards_for_current_stage(state)
            if card.get("is_stage_gate")
            and str(card.get("stage_id")) == stage_id
            and str(card.get("revision")) == revision
        ),
        None,
    )
    if gate is not None:
        receipt = _valid_gate_receipt(root, str(gate["id"]))
        if receipt is not None:
            _, review = receipt
            base.setdefault("payload", {})["stage_review"] = review
            gate_review_injected = True

    result_path = root / stage_result_ref(stage_id, revision)
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(
        json.dumps(base, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return {
        "project": str(root),
        "result_file": str(result_path.relative_to(root)),
        "merged_keys": merged_keys,
        "gate_review_injected": gate_review_injected,
    }


def events_tail(project: str | Path, limit: int = 20) -> dict[str, object]:
    """Read only the latest bounded event summaries for an active Commander."""

    if limit <= 0:
        raise ValueError("events --tail 必须大于 0")
    bounded_limit = min(limit, MAX_EVENT_TAIL)
    root = _project_root(project)
    event_path = root / "loop-events.md"
    all_events = read_events(event_path)
    selected = all_events[-bounded_limit:]
    return {
        "project": str(root),
        "event_log": str(event_path),
        "total_events": len(all_events),
        "returned_events": len(selected),
        "tail_limit": bounded_limit,
        "events": [_event_summary(event) for event in selected],
        "note": "这是有限摘要；完整 Agent/tool 输出只保存在 loop-artifacts 或事件摘录中。",
    }


def status_summary(state: Mapping[str, Any], project: str | Path) -> dict[str, object]:
    """Return a bounded status view suitable for a Commander prompt.

    ``loop-state.json`` intentionally contains complete stage input, field
    tasks, DAG metadata and history.  Printing it from the command suggested
    by Hook used to re-inject all of that into Claude's context.  Status is a
    dashboard, not a state export; ``ralph status --full`` remains available
    for humans and diagnostics.
    """

    stage = state.get("stage") if isinstance(state.get("stage"), Mapping) else {}
    tasks = state.get("field_tasks") if isinstance(state.get("field_tasks"), list) else []
    graph = state.get("graph_tasks") if isinstance(state.get("graph_tasks"), list) else []
    task_spec = state.get("task_spec") if isinstance(state.get("task_spec"), Mapping) else {}
    matrix = task_spec.get("attribute_matrix") if isinstance(task_spec.get("attribute_matrix"), list) else []
    counts: dict[str, int] = {}
    for item in tasks:
        if isinstance(item, Mapping):
            status = str(item.get("status") or "unknown")
            counts[status] = counts.get(status, 0) + 1
    graph_counts: dict[str, int] = {}
    for item in graph:
        if isinstance(item, Mapping):
            status = str(item.get("status") or "unknown")
            graph_counts[status] = graph_counts.get(status, 0) + 1
    description = state.get("task", {}).get("description", "") if isinstance(state.get("task"), Mapping) else ""
    description = str(description).replace("\n", " ").strip()
    if len(description) > 240:
        description = description[:237] + "..."
    return {
        "project": str(Path(project).expanduser().resolve()),
        "task": description,
        "status": state.get("status"),
        "stage": {
            "id": stage.get("id"),
            "revision": stage.get("revision"),
            "name": stage.get("name"),
            "next_stage": stage.get("on_success"),
        },
        "last_action": state.get("last_action"),
        "last_event_id": state.get("last_event_id"),
        "fields": {"total": len(matrix), "tasks": len(tasks), "by_status": counts},
        "graph": {"tasks": len(graph), "by_status": graph_counts},
        "current_artifact": state.get("current_artifact"),
        "event_log": str((Path(project).expanduser().resolve() / "loop-events.md")),
        "hint": "需要完整状态时运行 ralph status <project> --full；需要事件时运行 ralph events <project> --tail 20。",
    }


def start_project(
    project: str | Path,
    mode: str,
    launch: bool,
    prompt: str | None,
    effort: str | None = None,
    model: str | None = None,
    auto_compact_window: int | None = None,
    auto_compact_percent: int | None = None,
    stop_policy: str | None = None,
) -> int:
    root, settings_path, _, _ = prepare_project(project, mode=mode, stop_policy=stop_policy)
    environment, compact_window, compact_percent = _claude_environment(
        auto_compact_window,
        auto_compact_percent,
    )
    command = _with_model(
        _with_effort(
            [_claude_executable(), "--settings", str(settings_path), "--setting-sources", "user,project,local"],
            effort,
        ),
        model,
    )
    _append_stage_executor_skill(command)
    if prompt:
        command.extend(["-p", prompt])
    print("RALPH project:", root)
    print("Hook settings:", settings_path)
    _print_compaction_settings(compact_window, compact_percent)
    print("Command:", " ".join(shlex.quote(item) for item in command))
    if launch:
        return subprocess.call(command, cwd=root, env=environment)
    return 0


def resume_project(
    project: str | Path,
    mode: str,
    prompt: str | None,
    effort: str | None = None,
    model: str | None = None,
    auto_compact_window: int | None = None,
    auto_compact_percent: int | None = None,
    stop_policy: str | None = None,
) -> int:
    """Start a fresh Claude context while preserving the project state.

    Claude's previous transcript is deliberately not continued here. The
    project files are the durable context; sending the old transcript again
    is exactly what can trigger oMLX's prefill guard after a long run.
    """

    root, settings_path, _, _ = prepare_project(
        project,
        mode=mode,
        record_session=True,
        stop_policy=stop_policy,
    )
    environment, compact_window, compact_percent = _claude_environment(
        auto_compact_window,
        auto_compact_percent,
    )
    state = load_state(root / "loop-state.json")
    recovery_prompt = prompt or PromptRenderer().compact_recovery_prompt(
        state,
        reason="从上一个会话的运行时中断恢复；以持久化状态为准。",
        error_kind="runtime",
        fresh_session=True,
    ).text
    command = _with_model(
        _with_effort(
            [
                _claude_executable(),
                "--settings",
                str(settings_path),
                "--setting-sources",
                "user,project,local",
            ],
            effort,
        ),
        model,
    )
    _append_stage_executor_skill(command)
    # A positional prompt starts an interactive session. Do not use
    # `--continue`: that would re-send the oversized transcript we are
    # recovering from.
    command.append(recovery_prompt)
    print("RALPH project:", root)
    print("Hook settings:", settings_path)
    _print_compaction_settings(compact_window, compact_percent)
    print("Starting a fresh Claude context from loop-state.json.")
    return subprocess.call(command, cwd=root, env=environment)


def _resolve_run_project(project_or_task: str | Path, task: str | None, workspace: str | Path | None) -> tuple[Path, str, ProjectResolution | None]:
    if task is not None:
        return Path(project_or_task), task, None
    task_text = str(project_or_task).strip()
    if not task_text:
        raise ValueError("ralph run requires a non-empty task description")
    start = Path(workspace).expanduser().resolve() if workspace is not None else Path.cwd()
    resolution = resolve_project(
        task_text,
        start=start,
        fallback_workspace=_workspace_root() if workspace is None else workspace,
    )
    return resolution.project, task_text, resolution


def run_project(
    project_or_task: str | Path,
    task: str | None = None,
    mode: str = "hybrid",
    workspace: str | Path | None = None,
    effort: str | None = None,
    model: str | None = None,
    auto_compact_window: int | None = None,
    auto_compact_percent: int | None = None,
    skip_permissions: bool = False,
    stop_policy: str | None = None,
) -> int:
    """Initialize/reuse a project and start Claude; task-only mode auto-resolves it."""

    project, task, resolution = _resolve_run_project(project_or_task, task, workspace)
    task = task.strip()
    if not task:
        raise ValueError("ralph run requires a non-empty task description")
    root, settings_path, is_new, created = prepare_project(
        project,
        task=task,
        mode=mode,
        record_session=True,
        fresh_if_completed=True,
        stop_policy=stop_policy,
    )
    environment, compact_window, compact_percent = _claude_environment(
        auto_compact_window,
        auto_compact_percent,
    )
    command = _with_skip_permissions(
        _with_model(
            _with_effort(
                [
                    _claude_executable(),
                    "--settings",
                    str(settings_path),
                    "--setting-sources",
                    "user,project,local",
                ],
                effort,
            ),
            model,
        ),
        skip_permissions,
    )
    _append_stage_executor_skill(command)
    command.append(task)
    print("RALPH project:", root)
    if resolution is not None:
        print("RALPH workspace:", resolution.workspace)
        print("Project decision:", "reuse" if not resolution.created else "create")
        print("Decision reason:", resolution.reason)
    print("Project state:", "initialized" if is_new else "reused")
    if created:
        print("Created:", ", ".join(created))
    print("Hook settings:", settings_path)
    _print_compaction_settings(compact_window, compact_percent)
    print("Starting interactive Claude session with the supplied task.")
    return subprocess.call(command, cwd=root, env=environment)


def _resolve_loop_project(
    project_or_task: str | Path,
    task: str | None,
    workspace: str | Path | None,
) -> tuple[Path, str, ProjectResolution | None]:
    """Resolve either an existing project path or a new task description."""

    candidate = Path(project_or_task).expanduser()
    candidate_state = _state_path(candidate)
    if task is None and candidate_state.exists():
        state = load_state(candidate_state)
        task_record = state.get("task", {})
        description = task_record.get("description") if isinstance(task_record, dict) else None
        if not isinstance(description, str) or not description.strip():
            raise ValueError("项目 loop-state.json 没有可恢复的 task.description")
        return _project_root(candidate), description.strip(), None
    if task is None and (
        candidate.is_absolute()
        or str(project_or_task).startswith(("./", "../", "~/"))
    ):
        raise ValueError(
            f"`{project_or_task}` 看起来是项目路径，但没有任务描述；请使用："
            f"ralph loop {project_or_task!s} '<任务描述>'。"
            "如果只想用一个输入自动创建项目，请直接运行 `ralph loop '<任务描述>'`。"
        )
    return _resolve_run_project(project_or_task, task, workspace)


def _count_event_markers(path: Path, marker: str) -> int:
    """Count occurrences of ``marker`` in an event log (0 if unreadable)."""
    try:
        with open(path, encoding="utf-8", errors="ignore") as fh:
            return sum(1 for line in fh if marker in line)
    except OSError:
        return 0


def _field_dispatch_stall_requested(root: Path, event_path: Path) -> bool:
    """Detect a recoverable Commander dispatch stall without parsing all events.

    A local model can acknowledge a field correction in prose, or simply keep
    thinking, without writing the next incremental draft.  This is different
    from an active child or a slow web search: the combination of ready fields
    and no active field children is enough to start the bounded watchdog.  The
    caller supplies the grace interval, so a normal long reasoning window can
    be configured while a silent Commander cannot consume the general idle
    timeout.  Pending structural fields are included; only
    ``research_required`` fields may create an Agent, so this watchdog never
    recreates the old auditor dispatch path.
    """

    try:
        state = load_state(root / "loop-state.json")
    except (OSError, ValueError):
        return False
    tasks = state.get("field_tasks", [])
    if not isinstance(tasks, list):
        return False
    ready = [
        task for task in tasks
        if isinstance(task, Mapping)
        and str(task.get("status", "")) in {"ready", "pending"}
    ]
    active = [
        task for task in tasks
        if isinstance(task, Mapping)
        and str(task.get("status", "")) in {"dispatching", "dispatched"}
    ]
    if not ready or active:
        return False
    try:
        # The event file is append-only and can be large.  The latest cycle
        # marker and feedback are always near the tail, so avoid read_events()
        # here and read only a bounded suffix on each watchdog tick.
        with event_path.open("rb") as handle:
            handle.seek(0, 2)
            handle.seek(max(0, handle.tell() - 160_000))
            tail = handle.read().decode("utf-8", errors="ignore")
    except OSError:
        return False
    cycle_pos = tail.rfind("supervisor_cycle_started")
    if cycle_pos < 0:
        return False
    # The cycle marker is also a cheap guard against a stale ready queue from
    # an older session.  Once this supervisor cycle is active, the queue is the
    # durable work signal; no additional natural-language rejection is needed
    # before the watchdog starts.
    return True


def _field_agent_stall_requested(root: Path, *, exclude_ids: set[str] | None = None) -> bool:
    """Detect a field child that cannot make durable progress.

    Once a field has reached the bounded web-failure path, the only valid next
    action is to save an incomplete draft with ``field-apply``.  A child that
    keeps the task ``dispatched`` without applying that draft is recoverable at
    the next supervisor boundary.  The same applies to a child that has not
    changed its task record for a long time: Claude can remain in an internal
    thinking/tool-retry loop without producing a SubagentStop receipt, which
    otherwise leaves the parent Stop Hook waiting forever.

    This is deliberately only a *request* for a fresh Claude context.  The
    field draft and queue remain durable, and ``reopen_stale_field_tasks``
    reopens the task after the child context is terminated.  The timeout is
    configured by ``RALPH_FIELD_AGENT_STALL_SECONDS`` (disabled by default).
    """

    try:
        state = load_state(root / "loop-state.json")
    except (OSError, ValueError):
        return False
    tasks = state.get("field_tasks", [])
    if not isinstance(tasks, list):
        return False
    excluded = {str(item) for item in (exclude_ids or set())}
    now = datetime.now(timezone.utc)
    for task in tasks:
        if not isinstance(task, Mapping) or str(task.get("id", "")) in excluded:
            continue
        if _field_task_stall_requested(task, now=now):
            return True
    return False


def _field_task_stall_requested(task: Mapping[str, Any], *, now: datetime | None = None) -> bool:
    """Return whether one dispatched field has exceeded its durable heartbeat.

    This helper is shared by the parent-Commander watchdog and the separately
    launched fallback workers.  Previously only the parent was watched; an
    automatic worker could therefore remain alive after its parent restarted,
    leaving the task permanently ``dispatched`` even though it had produced
    no new draft or ``field-apply`` receipt.
    """

    if str(task.get("status", "")) not in {"dispatching", "dispatched"}:
        return False
    if int(task.get("apply_count", 0) or 0) > int(task.get("apply_count_at_dispatch", 0) or 0):
        return False
    if int(task.get("web_failures", 0) or 0) >= 2:
        return True
    # ``0`` explicitly disables the heartbeat watchdog.  A live fallback
    # worker is checked immediately after its reservation is written, so
    # comparing its brand-new timestamp against a zero-second timeout would
    # otherwise reap every worker before it can make its first Read/Write.
    timeout = _field_agent_stall_seconds()
    if timeout <= 0:
        return False
    updated_at = task.get("updated_at")
    if not updated_at:
        return False
    try:
        heartbeat = datetime.fromisoformat(str(updated_at).replace("Z", "+00:00"))
        if heartbeat.tzinfo is None:
            heartbeat = heartbeat.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        return False
    current = now or datetime.now(timezone.utc)
    return (current - heartbeat).total_seconds() >= timeout


def _field_agent_stall_seconds() -> float:
    """Read the configurable no-progress watchdog interval."""

    try:
        return max(0.0, float(os.environ.get("RALPH_FIELD_AGENT_STALL_SECONDS", "0")))
    except ValueError:
        return 0.0


def _terminate_process_group(process: subprocess.Popen[Any], *, timeout: float = 10.0) -> None:
    """Terminate a Claude process and any nested Claude children it owns."""

    group_id: int | None = None
    if os.name != "nt":
        try:
            group_id = os.getpgid(process.pid)
            # Older workers (and small test doubles) may have inherited the
            # supervisor's process group.  Killing that group would also kill
            # the supervisor or the invoking shell.  Only group-kill a worker
            # that was explicitly started in its own session.
            if group_id == os.getpgrp():
                group_id = None
            else:
                os.killpg(group_id, signal.SIGTERM)
        except (OSError, ProcessLookupError):
            group_id = None
    if group_id is None:
        process.terminate()
    try:
        process.wait(timeout=timeout)
    except subprocess.TimeoutExpired:
        if group_id is not None:
            try:
                os.killpg(group_id, signal.SIGKILL)
            except (OSError, ProcessLookupError):
                pass
        else:
            process.kill()
        process.wait(timeout=timeout)


_HARD_CONTEXT_ERROR_MARKERS = (
    "Prompt too long",
    "exceeds max context window",
    "maximum context length",
    "context length exceeded",
    "prompt is too long",
)


def _context_error_excerpt(text: str) -> str | None:
    """Return a bounded hard-context error line, if one is present."""

    for line in reversed(str(text or "").splitlines()):
        candidate = line.strip()
        if candidate and any(marker.lower() in candidate.lower() for marker in _HARD_CONTEXT_ERROR_MARKERS):
            return candidate[:600]
    return None


def _claude_transcript_for_process(pid: int) -> Path | None:
    """Resolve Claude's JSONL transcript from its per-process session record."""

    metadata_path = Path.home() / ".claude" / "sessions" / f"{pid}.json"
    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        session_id = str(metadata.get("sessionId") or "").strip()
    except (OSError, ValueError, json.JSONDecodeError):
        return None
    if not session_id:
        return None
    projects_root = Path.home() / ".claude" / "projects"
    if not projects_root.is_dir():
        return None
    # Claude Code stores the file beneath a sanitized cwd directory.  A
    # filename search avoids reimplementing that sanitization and is bounded
    # to one project transcript rather than reading the whole history.
    try:
        for candidate in projects_root.rglob(f"{session_id}.jsonl"):
            if candidate.is_file():
                return candidate
    except OSError:
        return None
    return None


def _run_claude_supervised(
    command: list[str],
    *,
    cwd: Path,
    env: dict[str, str],
    idle_timeout: float,
    protected_field_task_ids: set[str] | None = None,
    auto_workers: dict[str, dict[str, Any]] | None = None,
) -> tuple[int, bool]:
    """Run Claude while watching the durable state/event files for progress.

    The legacy ``fresh`` Stop policy lets Claude idle after a completed turn.
    In that mode we watch for ``ralph_stop_handled`` and relaunch after a
    short grace period. The default ``inline`` policy returns ``decision:
    block`` instead, so it deliberately emits no marker and this supervisor
    leaves the existing Claude process running. Durable state changes cancel
    a pending legacy relaunch; noisy event-log writes alone do not count as
    progress, so repeated Hook feedback cannot create an infinite loop.
    """

    # Put Commander and every Claude child it launches in their own process
    # group.  A watchdog restart must not leave a nested Agent alive after the
    # parent context is replaced; otherwise the durable field remains
    # ``dispatched`` and the next context sees a ghost worker.
    process = subprocess.Popen(
        command,
        cwd=cwd,
        env=env,
        start_new_session=(os.name != "nt"),
    )
    last_activity = time.monotonic()
    # Event logging is intentionally noisy: every PreToolUse denial and
    # bounded feedback message appends to loop-events.md.  Treating that file
    # as generic activity lets a weak model keep an idle loop alive forever by
    # repeating the same rejected tool call.  Durable state changes are the
    # progress signal; the stop marker is watched separately below.
    last_state_mtime = 0.0
    state_path = cwd / "loop-state.json"
    event_path = cwd / "loop-events.md"
    try:
        last_state_mtime = state_path.stat().st_mtime
    except OSError:
        pass
    stop_marker = "ralph_stop_handled"
    relaunch_grace = 6.0
    last_stop_count = _count_event_markers(event_path, stop_marker)
    pending_relaunch_at: float | None = None
    field_stall_since: float | None = None
    field_agent_stall_since: float | None = None
    try:
        # Watchdogs are opt-in: an agent needs room to diagnose an earlier
        # attempt in the same context instead of being force-restarted merely
        # for taking a long research or reasoning turn.
        field_stall_timeout = max(0.0, float(os.environ.get("RALPH_FIELD_DISPATCH_STALL_SECONDS", "0")))
    except ValueError:
        field_stall_timeout = 0.0

    def _terminate() -> tuple[int, bool]:
        group_id: int | None = None
        if os.name != "nt":
            try:
                group_id = os.getpgid(process.pid)
                os.killpg(group_id, signal.SIGTERM)
            except (OSError, ProcessLookupError):
                group_id = None
        if group_id is None:
            process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            if group_id is not None:
                try:
                    os.killpg(group_id, signal.SIGKILL)
                except (OSError, ProcessLookupError):
                    pass
            else:
                process.kill()
            process.wait(timeout=10)
        return process.returncode if process.returncode is not None else 124, True

    while True:
        return_code = process.poll()
        if return_code is not None:
            return return_code, False
        # Reap independently launched field workers while the Commander is
        # still alive.  Previously this happened only at a supervisor cycle
        # boundary, so a local model that stalled after WebSearch could hold
        # a dispatched field indefinitely even though its timeout had passed.
        if auto_workers:
            _reap_auto_field_workers(cwd, auto_workers)
        try:
            newest_state_mtime = state_path.stat().st_mtime
        except OSError:
            newest_state_mtime = last_state_mtime
        if newest_state_mtime > last_state_mtime:
            last_state_mtime = newest_state_mtime
            last_activity = time.monotonic()
            # Claude is producing output -> cancel any pending relaunch.
            pending_relaunch_at = None
        cur_stop = _count_event_markers(event_path, stop_marker)
        if cur_stop > last_stop_count:
            last_stop_count = cur_stop
            if pending_relaunch_at is None:
                pending_relaunch_at = time.monotonic() + relaunch_grace
        now = time.monotonic()
        if pending_relaunch_at is not None and now >= pending_relaunch_at:
            return _terminate()
        # Do not wait for the general 30-minute idle timeout when the model
        # has explicitly been told to dispatch a ready field but produced no
        # child call.  A fresh context is the safe recovery boundary; the
        # durable field files and task queue remain unchanged.
        if field_stall_timeout > 0 and _field_dispatch_stall_requested(cwd, event_path):
            if field_stall_since is None:
                field_stall_since = now
            elif now - field_stall_since >= field_stall_timeout:
                append_observation(
                    event_path,
                    "supervisor_field_dispatch_stall_recovery",
                    {
                        "timeout_seconds": field_stall_timeout,
                        "state_preserved": True,
                        "next_action": "fresh_context",
                        "reason": "field dispatch feedback repeated without an active child",
                    },
                )
                return _terminate()
        else:
            field_stall_since = None
        field_agent_stall_timeout = _field_agent_stall_seconds()
        # Top-level auto workers are separate processes.  They must not make
        # the parent Commander immune to the no-progress watchdog: replacing
        # the parent context is safe because the worker's dispatched task is
        # durable and cannot be claimed again.  The protected IDs are still
        # used at the cycle boundary so a live worker is not reopened.
        if field_agent_stall_timeout > 0 and _field_agent_stall_requested(cwd):
            if field_agent_stall_since is None:
                field_agent_stall_since = now
            elif now - field_agent_stall_since >= field_agent_stall_timeout:
                append_observation(
                    event_path,
                    "supervisor_field_agent_stall_recovery",
                    {
                        "timeout_seconds": field_agent_stall_timeout,
                        "state_preserved": True,
                        "next_action": "fresh_context",
                        "reason": "field Agent reached web-failure fuse or exceeded no-progress window without field-apply",
                    },
                )
                return _terminate()
        else:
            field_agent_stall_since = None
        if idle_timeout > 0 and now - last_activity >= idle_timeout:
            return _terminate()
        time.sleep(min(5.0, max(0.25, idle_timeout / 10 if idle_timeout > 0 else 5.0)))


def _run_prompt_first_supervised(
    command: list[str],
    *,
    cwd: Path,
    env: dict[str, str],
    idle_timeout: float,
) -> tuple[int, bool]:
    """Run a prompt-first Commander without field/card watchdogs.

    A normal Stop is blocked by the Markdown Stop Hook and remains in this
    process.  The outer loop only sees genuine process exit, or an explicitly
    configured idle watchdog; a zero timeout never replaces live reasoning.
    """

    process = subprocess.Popen(command, cwd=cwd, env=env, start_new_session=(os.name != "nt"))
    cursor = prompt_first_state_path(cwd)
    try:
        last_mtime = cursor.stat().st_mtime
    except OSError:
        last_mtime = 0.0
    last_activity = time.monotonic()
    transcript_path: Path | None = None
    transcript_offset: int | None = None

    def _new_hard_context_error() -> str | None:
        """Read only newly appended transcript bytes for an unrecoverable error."""

        nonlocal transcript_path, transcript_offset
        if transcript_path is None:
            transcript_path = _claude_transcript_for_process(process.pid)
        if transcript_path is None:
            return None
        try:
            size = transcript_path.stat().st_size
            if transcript_offset is None:
                # Include the current tail in case the metadata appeared just
                # after Claude wrote the error, but never reread a large
                # transcript on every watchdog tick.
                transcript_offset = max(0, size - 128_000)
            elif size < transcript_offset:
                transcript_offset = 0
            if size <= transcript_offset:
                return None
            with transcript_path.open("rb") as handle:
                handle.seek(transcript_offset)
                text = handle.read(size - transcript_offset).decode("utf-8", errors="replace")
            transcript_offset = size
        except OSError:
            return None
        return _context_error_excerpt(text)

    while True:
        return_code = process.poll()
        if return_code is not None:
            return return_code, False
        context_error = _new_hard_context_error()
        if context_error is not None:
            append_observation(
                cwd / "loop-events.md",
                "prompt_first_context_error_recovery",
                {
                    "process_pid": process.pid,
                    "error_excerpt": context_error,
                    "state_preserved": True,
                    "next_action": "fresh_context_from_markdown",
                },
            )
            _terminate_process_group(process)
            return 75, True
        try:
            newest_mtime = cursor.stat().st_mtime
        except OSError:
            newest_mtime = last_mtime
        if newest_mtime > last_mtime:
            last_mtime = newest_mtime
            last_activity = time.monotonic()
        if idle_timeout > 0 and time.monotonic() - last_activity >= idle_timeout:
            _terminate_process_group(process)
            return process.returncode if process.returncode is not None else 124, True
        time.sleep(min(5.0, max(0.25, idle_timeout / 10 if idle_timeout > 0 else 5.0)))


def prompt_first_loop_project(
    project: str | Path,
    task: str,
    *,
    effort: str | None = None,
    model: str | None = None,
    max_cycles: int = 0,
    retry_delay: float = 3.0,
    idle_timeout: float = 0.0,
    skip_permissions: bool = False,
    auto_compact_window: int | None = None,
    auto_compact_percent: int | None = None,
) -> int:
    """Run the Markdown-only default workflow for a new project."""

    if max_cycles < 0 or retry_delay < 0 or idle_timeout < 0:
        raise ValueError("max-cycles、retry-delay 和 idle-timeout 不能小于 0")
    root = Path(project).expanduser().resolve()
    with _supervisor_lock(root):
        state = initialize_prompt_first(root, task)
        created = _ensure_prompt_first_scaffold(root)
        settings_path = install_prompt_first_hooks(root)
        event_path = root / "loop-events.md"
        event_path.touch(exist_ok=True)
        environment, compact_window, compact_percent = _claude_environment(
            auto_compact_window, auto_compact_percent,
        )
        append_observation(
            event_path,
            "prompt_first_session_started",
            {
                "stage": state["stage"],
                "revision": state["revision"],
                "state_file": "ralph-loop.md",
                "current_artifact": state["current_artifact"],
                "created_files": created,
                "tool_gates": False,
                "semantic_validation": False,
                "idle_timeout": idle_timeout,
            },
        )
        print("RALPH prompt-first project:", root)
        print("Auto compact:", f"capacity={compact_window}, trigger≈{compact_window * compact_percent // 100} tokens")
        print("Idle watchdog:", "disabled" if idle_timeout == 0 else f"{idle_timeout:g} seconds")
        cycle = 0
        while max_cycles == 0 or cycle < max_cycles:
            state = load_prompt_first_state(root)
            if state["status"] == "completed":
                print("RALPH prompt-first completed:", root)
                return 0
            prompt = render_prompt_first(
                root,
                reason="新项目从当前 Markdown 阶段开始" if cycle == 0 else "上一个 Claude 进程已退出；从 Markdown 游标继续",
            )
            command = _with_skip_permissions(
                _with_model(
                    _with_effort(
                        [
                            _claude_executable(),
                            "--settings", str(settings_path),
                            "--setting-sources", "user,project,local",
                        ],
                        effort,
                    ),
                    model,
                ),
                skip_permissions,
            )
            skill_context, skill_path = _prompt_first_skill_context()
            command.extend(["--append-system-prompt", skill_context, prompt])
            cycle += 1
            append_observation(
                event_path,
                "prompt_first_commander_started",
                {
                    "cycle": cycle,
                    "stage": state["stage"],
                    "revision": state["revision"],
                    "skill": str(skill_path) if skill_path is not None else "builtin",
                    "same_context_stop_policy": "inline",
                },
            )
            print(f"RALPH prompt-first cycle {cycle}: launching Claude")
            return_code, timed_out = _run_prompt_first_supervised(
                command, cwd=root, env=environment, idle_timeout=idle_timeout,
            )
            append_observation(
                event_path,
                "prompt_first_commander_finished",
                {
                    "cycle": cycle,
                    "return_code": return_code,
                    "timed_out": timed_out,
                    "next_action": "fresh_context_only_after_process_exit",
                },
            )
            if max_cycles and cycle >= max_cycles:
                return 0
            if retry_delay:
                time.sleep(min(retry_delay, 60.0))
    return 0


def _field_engine_tick(root: Path, state: dict) -> bool:
    """Field-centric per-cycle reconcile + auto-advance.

    Runs once per supervisor cycle in field-centric mode (before the
    Commander context launches):

    - Explodes comma-separated field ``attribute`` values into independent
      sub-fields, written back into ``loop-state.json`` (deterministic,
      model-free proliferation).  Without this the field gate could never reach
      "complete" because the model writes comma lists directly and never emits
      the structured advance token that would otherwise trigger the explosion.
    - When the current stage is ``01`` and every field is dispositioned (no
      ``pending`` / no ``research_required`` without ``evidence_refs``), advances
      automatically -- the model does NOT need to emit ``<RALPH_STAGE_RESULT>``.
    - In the explicit ``flow_only`` test mode, the same mechanical gate also
      advances later field stages after their inferred drafts are applied. This
      keeps a no-web workflow from stopping only because the Commander failed
      to compose a redundant ``advance.json``.

    Stages 02-06 keep their normal contract validation (the field gate only
    short-cuts stage 01), so they are not trivially skipped.

    Returns True if it advanced the stage this tick.
    """

    state_path = root / "loop-state.json"
    live = load_state(state_path)
    before_spec = live.get("task_spec")
    before_tasks = live.get("field_tasks")
    materialize_field_tasks(root, live)
    # Persist stage-entry synthesis (especially stage 02 research fields) so
    # the next Hook/Commander sees the same queue instead of rebuilding a
    # transient in-memory list on every cycle.
    if live.get("task_spec") != before_spec or live.get("field_tasks") != before_tasks:
        save_state(state_path, live)
    spec = live.get("task_spec")
    if not isinstance(spec, Mapping):
        return False
    matrix = spec.get("attribute_matrix")
    if not isinstance(matrix, list):
        return False
    exploded = _explode_comma_fields(matrix)
    if exploded != matrix:
        live["task_spec"] = dict(live.get("task_spec", {}))
        live["task_spec"]["attribute_matrix"] = exploded
        save_state(state_path, live)
    if isinstance(state, dict):
        state.setdefault("task_spec", {})
        state["task_spec"]["attribute_matrix"] = exploded

    stage = live.get("stage", {})
    current = str(stage.get("id", ""))
    if current != "01" and not flow_only_mode(live):
        return False
    if current == "03" and flow_only_mode(live):
        plan = live.get("plan") if isinstance(live.get("plan"), Mapping) else {}
        nodes = plan.get("nodes") if isinstance(plan, Mapping) else None
        joins = plan.get("joins") if isinstance(plan, Mapping) else None
        if not isinstance(nodes, list) or len(nodes) < 3 or not isinstance(joins, list) or not joins:
            # Field completeness alone cannot certify a task decomposition;
            # the structured DAG must first pass field-apply's validator.
            return False
        node_ids = {str(node.get("id", "")) for node in nodes if isinstance(node, Mapping)}
        completed = {str(node_id) for node_id in (plan.get("completed") or [])}
        results = plan.get("task_results") if isinstance(plan.get("task_results"), Mapping) else {}
        if not node_ids or not node_ids.issubset(completed):
            return False
        # graph-apply is the only normal producer of task_results and checks
        # every declared write. Requiring its receipts prevents a flow-only
        # test from advancing with a diagram but no executed node artifacts.
        for node_id in node_ids:
            result = results.get(node_id) if isinstance(results, Mapping) else None
            refs = result.get("artifact_refs") if isinstance(result, Mapping) else None
            if not isinstance(refs, list) or not refs:
                return False
            for ref in refs:
                candidate = (root / str(ref)).resolve()
                if root not in candidate.parents or not candidate.is_file() or candidate.stat().st_size <= 0:
                    return False
    verdict = field_completeness(exploded, stage.get("required_outputs") or [])
    if not verdict["complete"]:
        return False
    if current == "04.5" and flow_only_mode(live):
        # The normal graph deliberately returns 04.5 to exploration so a real
        # project can keep discovering work. A closed-world E2E fixture has a
        # finite contract: after its final independent cross-check, close the
        # run without silently cycling through exploration -> 01 again.
        live["status"] = "completed"
        save_state(state_path, live)
        append_observation(
            root / "loop-events.md",
            "flow_only_final_completed",
            {"stage": current, "revision": stage.get("revision"), "state_preserved": True},
        )
        print("[field-gate] flow-only final stage completed")
        return True
    next_stage = str(stage.get("on_success") or "")
    if not next_stage or next_stage == current:
        return False
    action = {
        "action": "advance",
        "status": "passed",
        "stage_id": current,
        "revision": str(stage.get("revision", "r1")),
        "next_stage": next_stage,
        "payload": {
            "stage_review": (
                "字段门禁自动通过：本阶段所有 required 字段均已 disposition 完成"
                "（无 pending、无 research_required 未带 evidence）。运行时按字段完成自动推进，"
                "不再要求模型输出 <RALPH_STAGE_RESULT> token。"
            )
        },
    }
    apply_and_record(
        state_path,
        root / "loop-events.md",
        action,
        raw_output=json.dumps(action, ensure_ascii=False),
    )
    print(f"[field-gate] auto-advanced {current} -> {next_stage} (fields complete)")
    return True


def _auto_field_workers_enabled() -> bool:
    # The one-command workflow must not depend on a weak Commander remembering
    # to dispatch its first field Agent. Keep the bounded worker fallback on by
    # default; set RALPH_AUTO_FIELD_WORKERS=0 for diagnostics or pure-Commander
    # experiments.
    value = os.environ.get("RALPH_AUTO_FIELD_WORKERS", "1").strip().lower()
    return value in {"1", "true", "yes", "on"}


def _auto_pending_field_workers_enabled() -> bool:
    """Allow the fallback worker to finish structural pending fields.

    Commander remains the preferred editor for ``pending`` fields.  A weak
    local Commander can nevertheless terminate immediately after a Hook
    correction; without this fallback the durable queue would stay ready
    forever.  The worker still writes one task JSON and must pass
    ``field-apply`` before the field is considered complete.
    """

    value = os.environ.get("RALPH_AUTO_PENDING_FIELD_WORKERS", "1").strip().lower()
    return value in {"1", "true", "yes", "on"}


AUTO_FIELD_WORKER_SYSTEM_PROMPT = """你是 RALPH 的单字段执行 worker。

只处理用户消息中给出的一个 RALPH_FIELD_TASK 文件。不要规划总任务，不要读取
loop-state.json、loop-events.md、CLAUDE.md、AGENTS.md 或其他任务文件，不要向人类
提问，不要派发子代理。

固定动作顺序：
1. Read 这个 task JSON；
2. 如果字段是 research_required，最多使用两次 WebSearch/WebFetch；禁止用 Bash、curl、
   python、grep 或其他 shell 命令搜索网页。工具不可用或没有可靠来源时，保留
   research_required、空 evidence_refs，并在 rationale 说明待补原因；不要伪造来源；
3. 立即用 Write 或 Edit 修改同一个 JSON 的 field 对象，至少填写真实的 attribute、
   rationale、disposition（confirmed/inferred/assumed_default/research_required 之一），
   已有字段保留；
4. 用 Bash 执行消息中给出的 ralph field-apply 命令；如果校验报错，只修复报错列出的
当前字段并再次执行同一个命令。

当用户消息说 flow-only/不要求实际网页研究时，这条闭环测试规则优先：不调用网页，
必须使用 disposition=inferred、evidence_refs=[]，并在 rationale 写“仅用于验证流程”。
不要把这类 synthetic 字段写成 research_required。

不要只返回自然语言。完成 field-apply 后直接结束。"""


def _auto_field_worker_environment(environment: Mapping[str, str]) -> dict[str, str]:
    """Keep local Claude settings available to the bounded worker.

    The worker now loads the project RALPH settings so PreToolUse/PostToolUse
    can provide the incremental Write -> field-apply feedback.  Copying the
    scalar user env values is still needed because the project settings file
    contains hooks, not the local endpoint/model configuration.
    """

    result = dict(environment)
    settings_path = Path.home() / ".claude" / "settings.json"
    try:
        settings = json.loads(settings_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return result
    values = settings.get("env") if isinstance(settings, Mapping) else None
    if isinstance(values, Mapping):
        for key, value in values.items():
            if isinstance(key, str) and isinstance(value, (str, int, float, bool)):
                result.setdefault(key, str(value))
    return result


def _auto_field_worker_prompt(task: Mapping[str, Any], project_root: Path) -> str:
    path = str(task.get("path", ""))
    task_path = (project_root / path).resolve()
    # Claude's Bash tool can execute with the workspace cwd even when the
    # Claude process was launched from the project.  Never make the critical
    # field-apply step depend on that ambient cwd.
    apply_command = f"ralph field-apply {shlex.quote(str(project_root))} {shlex.quote(str(task_path))}"
    disposition = str(task.get("disposition", ""))
    if bool(task.get("flow_only")):
        if str(task.get("role", "")) == "task_graph":
            graph_json = json.dumps(
                {
                    "revision": str(task.get("revision", "r1")),
                    "nodes": [
                        {
                            "id": "T1.1",
                            "depends_on": [],
                            "execution_mode": "parallel",
                            "parallel_group_id": "G1",
                            "orthogonal_key": "dimension_a",
                            "input_refs": ["loop-artifacts/stages/02.5/r1/fields.json"],
                            "output_schema": {"result": "string"},
                            "preconditions": [],
                            "postconditions": ["独立输出 A"],
                            "writes": ["loop-artifacts/stages/03/r1/outputs/T1.1.json"],
                        },
                        {
                            "id": "T1.2",
                            "depends_on": [],
                            "execution_mode": "parallel",
                            "parallel_group_id": "G1",
                            "orthogonal_key": "dimension_b",
                            "input_refs": ["loop-artifacts/stages/02.5/r1/fields.json"],
                            "output_schema": {"result": "string"},
                            "preconditions": [],
                            "postconditions": ["独立输出 B"],
                            "writes": ["loop-artifacts/stages/03/r1/outputs/T1.2.json"],
                        },
                        {
                            "id": "J1",
                            "depends_on": ["T1.1", "T1.2"],
                            "execution_mode": "serial",
                            "input_refs": [
                                "loop-artifacts/stages/03/r1/outputs/T1.1.json",
                                "loop-artifacts/stages/03/r1/outputs/T1.2.json",
                            ],
                            "output_schema": {"joined": "string"},
                            "preconditions": ["T1.1 和 T1.2 均完成"],
                            "postconditions": ["合并为下游输入"],
                            "writes": ["loop-artifacts/stages/03/r1/outputs/J1.json"],
                        },
                    ],
                    "parallel_groups": [{"id": "G1", "members": ["T1.1", "T1.2"]}],
                    "joins": [{"id": "J1", "depends_on": ["T1.1", "T1.2"]}],
                },
                ensure_ascii=False,
            )
            return (
                f"RALPH_FIELD_TASK={path}\n"
                f"这是 flow-only 流程实验，只处理 `{task.get('concept', '')}`；不要调用网页工具，不要读取其他文件。"
                "严格执行三步并在第 3 步结束："
                f"1) Read `{path}`；2) 立即 Write/Edit 同一文件的 `field`，保留 concept/role，"
                f"加入结构化 `task_graph` 对象（必须包含两个正交并行节点 T1.1、T1.2，parallel_group_id=G1，"
                f"以及等待两者的 Join 节点 J1）。建议 payload：{graph_json}。"
                f"disposition 使用 inferred，填写 rationale，evidence_refs 保持空数组；"
                f"3) Bash 执行 `{apply_command}`。若命令报错，只按 DAG 校验错误增量修复同一文件后重试；"
                "禁止只输出自然语言、重复 Read 或修改 loop-state.json。"
            )
        return (
            f"RALPH_FIELD_TASK={path}\n"
            f"这是 flow-only 流程实验，只处理 `{task.get('concept', '')}`；不要调用 WebSearch/WebFetch，"
            "不要用 Bash/curl/python 搜索，不要读取其他文件。严格执行三步并在第 3 步结束："
            f"1) Read `{path}`；2) 立即 Write/Edit 同一文件的 field，保留真实 attribute，填写 rationale，"
            "disposition 使用 inferred，evidence_refs 保持空数组，并标明仅用于验证流程；"
            f"3) Bash 执行 `{apply_command}`。若命令报错，只按报错修复同一文件后重试；"
            "禁止只输出自然语言、重复 Read 或修改 loop-state.json。"
        )
    if disposition == "pending":
        role = task.get("role", "")
        if isinstance(task.get("field"), Mapping):
            role = task["field"].get("role", role)
        # Keep this prompt deliberately short.  The former version repeated
        # the system prompt and research fallback instructions, which made a
        # small local model spend its whole turn reasoning instead of taking
        # the first Write action.
        return (
            f"RALPH_FIELD_TASK={path}\n"
            f"只处理 `{task.get('concept', '')}`（role={role}）。不搜索网页，不读其他文件。\n"
            f"严格执行三步并在第 3 步结束：1) Read `{path}`；"
            f"2) 立即 Write/Edit 同一文件的 `field`，把占位 attribute 改成最小真实内容，填写 rationale，"
            f"disposition 使用 `confirmed` 或 `inferred`，保留 evidence_refs=[]；"
            f"3) Bash 执行 `{apply_command}`。\n"
            "若命令报错，只按报错修正同一文件后重试；禁止只输出自然语言、重复 Read 或修改 loop-state.json。"
        )
    research_instruction = (
        "只处理这个 research_required 字段；先读取任务文件，最多使用两次 WebSearch/WebFetch。"
        "禁止用 Bash/curl/python/grep 搜索网页；没有可用工具或可靠来源时不要伪造 URL，"
        "写回 research_required、空 evidence_refs 和待补原因，仍运行 field-apply。"
    )
    return (
        f"RALPH_FIELD_TASK={path}\n"
        f"{research_instruction} 结果只写回 `{path}` 的 `field` 对象，然后 Bash 执行 "
        f"`{apply_command}`。不要读取完整 loop-state.json 或 loop-events.md，"
        "不要规划总报告；完成 field-apply 后直接结束。"
    )


def _auto_field_worker_timeout_seconds() -> float:
    """Read an optional worker timeout independently of its parent.

    The parent Commander may be replaced frequently while a worker is doing
    useful long reasoning, so this timeout is deliberately separate from the
    parent field-stall timeout.  It is disabled by default: a user who wants
    a hard capacity boundary can opt in with the environment variable.
    """

    try:
        return max(0.0, float(os.environ.get("RALPH_AUTO_FIELD_WORKER_TIMEOUT", "0")))
    except ValueError:
        return 0.0


def _launch_auto_field_workers(
    root: Path,
    settings_path: Path,
    environment: Mapping[str, str],
    *,
    model: str | None,
    effort: str | None,
    skip_permissions: bool,
    workers: dict[str, dict[str, Any]],
) -> list[str]:
    """Launch bounded top-level field workers as a recovery fallback.

    Commander remains the normal dispatcher.  This fallback is opt-in and is
    used when a weak/local Commander repeatedly fails to emit ``Agent``.  It
    launches the same narrow field prompt in an independent Claude process,
    while preserving the exact field-task lifecycle and Hook validation.
    """

    if not _auto_field_workers_enabled():
        return []
    state = load_state(root / "loop-state.json")
    tasks = [
        item for item in state.get("field_tasks", [])
        if isinstance(item, Mapping)
        and str(item.get("status", "")) in {"ready", "pending"}
        and (
            field_task_requires_agent(item)
            or (
                _auto_pending_field_workers_enabled()
                and str(item.get("disposition", "")).strip().lower() == "pending"
            )
        )
    ]
    capacity = max(0, max_parallel_fields() - len(workers))
    if capacity <= 0:
        return []
    launched: list[str] = []
    for candidate in tasks[:capacity]:
        task_id = str(candidate.get("id", ""))
        if not task_id or task_id in workers:
            continue
        auto_id = f"auto-field-{hashlib.sha1(task_id.encode()).hexdigest()[:12]}"
        _, claimed = claim_field_task(root, task_id, dispatch_name=auto_id)
        if claimed is None:
            continue
        update_field_task_metadata_transaction(
            root,
            task_id,
            status="dispatched",
            agent_id=auto_id,
            dispatch_name=auto_id,
        )
        claimed = next(
            (
                item
                for item in load_state(root / "loop-state.json").get("field_tasks", [])
                if isinstance(item, Mapping) and str(item.get("id")) == task_id
            ),
            claimed,
        )
        worker_env = _auto_field_worker_environment(environment)
        worker_env["RALPH_ROLE"] = "worker"
        worker_env["RALPH_AGENT_ID"] = auto_id
        worker_effort = effort or os.environ.get("RALPH_AUTO_FIELD_EFFORT", "low")
        command = _with_skip_permissions(
            _with_model(
                _with_effort(
                    [
                        _claude_executable(),
                        "--settings",
                        str(settings_path),
                        "--setting-sources",
                        "user,project,local",
                        "--system-prompt",
                        AUTO_FIELD_WORKER_SYSTEM_PROMPT,
                        "--tools",
                        "Read,Write,Edit,Bash,WebSearch,WebFetch",
                        "--allowedTools",
                        "Read",
                        "Write",
                        "Edit",
                        "Bash",
                        "WebSearch",
                        "WebFetch",
                        "--permission-mode",
                        "bypassPermissions",
                        "--no-session-persistence",
                    ],
                    worker_effort,
                ),
                model,
            ),
            skip_permissions,
        )
        # A fallback worker is still a RALPH Claude context, not a blind
        # subprocess.  Give it the same canonical stage skill as the
        # Commander before its narrow task prompt.  Keep ``-p`` last: placing
        # an option after it makes Claude parse the option as the prompt value.
        _append_stage_executor_skill(command)
        command.extend(["-p", _auto_field_worker_prompt(claimed, root)])
        log_dir = root / "loop-artifacts" / "worker-logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        log_handle = (log_dir / f"{task_id}.log").open("ab")
        try:
            process = subprocess.Popen(
                command,
                cwd=root,
                env=worker_env,
                stdout=log_handle,
                stderr=subprocess.STDOUT,
                # A fallback worker may itself launch a Claude child.  Give
                # it a private group so stale-worker recovery cannot leave a
                # nested process consuming local-model memory.
                start_new_session=(os.name != "nt"),
            )
        except OSError as exc:
            # Claiming a task is itself a state mutation.  If the external
            # Claude executable cannot be started, release that claim in the
            # same recovery path instead of leaving a permanent dispatched
            # phantom behind.
            log_handle.close()
            update_field_task_metadata_transaction(
                root,
                task_id,
                status="ready",
                clear_agent_id=True,
                clear_agent_ids=True,
                last_error=f"自动 worker 启动失败：{exc}",
            )
            append_observation(
                root / "loop-events.md",
                "auto_field_worker_start_failed",
                {"field_task_id": task_id, "agent_id": auto_id, "error": str(exc)},
            )
            continue
        update_field_task_metadata_transaction(
            root,
            task_id,
            worker_pid=process.pid,
        )
        workers[task_id] = {
            "process": process,
            "log": log_handle,
            "agent_id": auto_id,
            "started_at": time.monotonic(),
        }
        append_observation(
            root / "loop-events.md",
            "auto_field_worker_started",
            {"field_task_id": task_id, "agent_id": auto_id, "pid": process.pid},
        )
        launched.append(task_id)
    return launched


def _reap_auto_field_workers(root: Path, workers: dict[str, dict[str, Any]]) -> set[str]:
    """Reap finished fallback workers and return IDs still owned by live ones."""

    live_ids: set[str] = set()
    for task_id, record in list(workers.items()):
        process = record.get("process")
        if not isinstance(process, subprocess.Popen):
            workers.pop(task_id, None)
            continue
        return_code = process.poll()
        if return_code is None:
            # A field can be reopened by a lifecycle Hook or a new supervisor
            # context while the old Claude process is still alive.  Keeping
            # that orphan around makes the next ready task look duplicated
            # and wastes local-model memory.  The persisted task lifecycle is
            # authoritative: a live worker is valid only while its task is
            # still dispatched to that worker.
            live_state = load_state(root / "loop-state.json")
            live_task = next(
                (
                    item for item in live_state.get("field_tasks", [])
                    if isinstance(item, Mapping) and str(item.get("id", "")) == str(task_id)
                ),
                None,
            )
            if not isinstance(live_task, Mapping) or str(live_task.get("status", "")) not in {
                "dispatching",
                "dispatched",
            }:
                _terminate_process_group(process)
                log_handle = record.get("log")
                if hasattr(log_handle, "close"):
                    log_handle.close()
                append_observation(
                    root / "loop-events.md",
                    "auto_field_worker_orphan_reaped",
                    {
                        "field_task_id": task_id,
                        "agent_id": record.get("agent_id"),
                        "task_status": live_task.get("status") if isinstance(live_task, Mapping) else "missing",
                        "state_preserved": True,
                    },
                )
                workers.pop(task_id, None)
                continue
            # The parent-Commander watchdog can restart while a fallback
            # worker is still alive.  Do not treat that process as proof of
            # progress: if its durable task heartbeat is stale, it is the
            # worker itself that is stuck.  Release the slot while preserving
            # its task JSON/draft for the next bounded attempt.
            if _field_task_stall_requested(live_task):
                _terminate_process_group(process)
                log_handle = record.get("log")
                if hasattr(log_handle, "close"):
                    log_handle.close()
                update_field_task_metadata_transaction(
                    root,
                    task_id,
                    status="ready",
                    clear_agent_id=True,
                    clear_agent_ids=True,
                    last_error="自动 worker 心跳超时，已保留增量草稿并释放字段重试",
                )
                append_observation(
                    root / "loop-events.md",
                    "auto_field_worker_stall_reaped",
                    {
                        "field_task_id": task_id,
                        "agent_id": record.get("agent_id"),
                        "timeout_seconds": _field_agent_stall_seconds(),
                        "state_preserved": True,
                        "next_action": "ready_retry",
                    },
                )
                workers.pop(task_id, None)
                continue
            started_at = record.get("started_at")
            timeout = _auto_field_worker_timeout_seconds()
            if (
                timeout > 0
                and isinstance(started_at, (int, float))
                and time.monotonic() - float(started_at) >= timeout
            ):
                _terminate_process_group(process)
                log_handle = record.get("log")
                if hasattr(log_handle, "close"):
                    log_handle.close()
                # Preserve an already-written draft even when the worker
                # stalled before it managed to run ``field-apply``.  This is
                # still validated by the same command and therefore cannot
                # corrupt loop-state.json; invalid JSON simply remains a
                # repairable draft for the next context.
                task_path: Path | None = None
                live_before_apply = load_state(root / "loop-state.json")
                for item in live_before_apply.get("field_tasks", []):
                    if isinstance(item, Mapping) and str(item.get("id", "")) == task_id:
                        candidate = item.get("path")
                        if candidate:
                            task_path = root / str(candidate)
                        break
                auto_applied = False
                if task_path is not None and task_path.exists():
                    try:
                        result = apply_fields(root, task_path)
                        auto_applied = bool(result.get("ok"))
                        append_observation(
                            root / "loop-events.md",
                            "auto_field_draft_applied_on_timeout",
                            {
                                "field_task_id": task_id,
                                "agent_id": record.get("agent_id"),
                                "fields_file": str(task_path.relative_to(root)),
                                "remaining": result.get("remaining"),
                            },
                        )
                    except (OSError, ValueError, KeyError) as exc:
                        append_observation(
                            root / "loop-events.md",
                            "auto_field_draft_apply_failed_on_timeout",
                            {
                                "field_task_id": task_id,
                                "agent_id": record.get("agent_id"),
                                "error": str(exc),
                            },
                        )
                live_after_apply = load_state(root / "loop-state.json")
                task_after_apply = next(
                    (
                        item for item in live_after_apply.get("field_tasks", [])
                        if isinstance(item, Mapping) and str(item.get("id", "")) == task_id
                    ),
                    {},
                )
                # A completed draft must not be regressed to ready merely
                # because its worker failed to exit.  Incomplete or invalid
                # drafts are reopened for the next bounded attempt.
                final_status = (
                    "completed"
                    if auto_applied and str(task_after_apply.get("status", "")) == "completed"
                    else "ready"
                )
                update_field_task_metadata_transaction(
                    root,
                    task_id,
                    status=final_status,
                    clear_agent_id=True,
                    clear_agent_ids=True,
                    last_error=(
                        None
                        if final_status == "completed"
                        else f"自动 worker 超过 {timeout:g} 秒未完成 field-apply，已释放并重试"
                    ),
                )
                append_observation(
                    root / "loop-events.md",
                    "auto_field_worker_timeout",
                    {
                        "field_task_id": task_id,
                        "agent_id": record.get("agent_id"),
                        "timeout_seconds": timeout,
                        "state_preserved": True,
                    },
                )
                workers.pop(task_id, None)
                continue
            live_ids.add(task_id)
            continue
        log_handle = record.get("log")
        if hasattr(log_handle, "close"):
            log_handle.close()
        # ``--bare`` workers do not reliably emit the normal SubagentStop
        # lifecycle event.  If the process exits without increasing
        # apply_count, release its durable reservation immediately instead of
        # leaving a dispatched ghost until the next Commander cycle.
        finished_state = load_state(root / "loop-state.json")
        finished_task = next(
            (
                item for item in finished_state.get("field_tasks", [])
                if isinstance(item, Mapping) and str(item.get("id", "")) == str(task_id)
            ),
            None,
        )
        if (
            isinstance(finished_task, Mapping)
            and str(finished_task.get("status", "")) in {"dispatching", "dispatched"}
            and int(finished_task.get("apply_count", 0) or 0)
            <= int(finished_task.get("apply_count_at_dispatch", 0) or 0)
        ):
            update_field_task_metadata_transaction(
                root,
                task_id,
                status="ready",
                clear_agent_id=True,
                clear_agent_ids=True,
                field_read_count=0,
                last_error="自动 worker 退出但未提交 field-apply，已恢复字段并交给新的短上下文",
            )
            append_observation(
                root / "loop-events.md",
                "auto_field_worker_finished_without_apply",
                {
                    "field_task_id": task_id,
                    "agent_id": record.get("agent_id"),
                    "return_code": return_code,
                    "state_preserved": True,
                    "next_action": "ready_retry",
                },
            )
        append_observation(
            root / "loop-events.md",
            "auto_field_worker_finished",
            {
                "field_task_id": task_id,
                "agent_id": record.get("agent_id"),
                "return_code": return_code,
            },
        )
        workers.pop(task_id, None)
    return live_ids


def _wait_for_auto_field_workers(root: Path, workers: dict[str, dict[str, Any]]) -> None:
    """Wait for fallback workers without starting a second Claude context.

    On small local-model devices a fallback worker and a fresh Commander are
    not independent useful work: they compete for the same weights/KV cache.
    The old loop launched both in the same supervisor iteration.  Keep the
    durable queue active, reap finished/stalled workers, and return only when
    the worker slot is released.  The outer loop then decides whether to
    start a new Commander or retry another bounded worker.
    """

    while workers:
        _reap_auto_field_workers(root, workers)
        if workers:
            time.sleep(1.0)


def _auto_graph_workers_enabled() -> bool:
    """Return whether the stage-03 node recovery worker is enabled."""

    value = os.environ.get("RALPH_AUTO_GRAPH_WORKERS", "1").strip().lower()
    return value in {"1", "true", "yes", "on"}


def _auto_graph_worker_timeout_seconds() -> float:
    """Bound a graph-node recovery worker without discarding its artifacts."""

    try:
        return max(0.0, float(os.environ.get("RALPH_AUTO_GRAPH_WORKER_TIMEOUT", "0")))
    except ValueError:
        return 0.0


AUTO_GRAPH_WORKER_SYSTEM_PROMPT = """你是 RALPH 的单个 DAG 节点执行 worker。

只处理用户消息中给出的一个 RALPH_GRAPH_TASK 文件。不要读取
loop-state.json、loop-events.md、CLAUDE.md、AGENTS.md 或其他节点任务，不要派发
子代理，不要向人类提问。

固定动作顺序：
1. Read 这个 graph task JSON；
2. 只在消息给出的 writes 路径写出非空交付文件；
3. Edit 同一个 graph task JSON，填写非空 output 和 evidence；
4. 用 Bash 运行消息给出的 ralph graph-apply 命令。

如果校验失败，只修改当前节点 JSON 或其声明的 writes 文件，然后重试。完成
graph-apply 后直接结束；绝不直接修改 loop-state.json。"""


def _auto_graph_worker_prompt(task: Mapping[str, Any], project_root: Path) -> str:
    """Render the bounded, write-backed prompt for one ready graph node."""

    path = str(task.get("path", ""))
    task_path = (project_root / path).resolve()
    writes = [str(item) for item in task.get("writes", []) if isinstance(item, str) and item.strip()]
    graph_apply = f"ralph graph-apply {shlex.quote(str(project_root))} {shlex.quote(str(task_path))}"
    flow_only = "这是 flow-only 流程实验；不调用网页工具、不伪造来源。" if str(task.get("stage_id")) == "03" else ""
    return (
        f"RALPH_GRAPH_TASK={path}\n"
        f"只执行节点 `{task.get('node_id', '')}`。{flow_only} 严格执行四步并在第 4 步结束："
        f"1) Read `{path}`；"
        f"2) 只用 Write 创建每个声明写入路径（{json.dumps(writes, ensure_ascii=False)}）的非空 JSON 交付物；"
        f"3) Edit 同一任务 JSON，填写非空 `output` 和 `evidence`；"
        f"4) Bash 执行 `{graph_apply}`。"
        "若命令报错，只按依赖、output 或 writes 缺失提示修复当前节点后重试；"
        "禁止修改 loop-state.json、其他节点任务或未声明路径。"
    )


def _launch_auto_graph_workers(
    root: Path,
    settings_path: Path,
    environment: Mapping[str, str],
    *,
    model: str | None,
    effort: str | None,
    skip_permissions: bool,
    workers: dict[str, dict[str, Any]],
) -> list[str]:
    """Launch one bounded worker for a ready DAG node after field recovery.

    Graph tasks derive their ready state from ``plan.completed`` and therefore
    need no second mutable reservation protocol.  The supervisor waits for
    each worker, so selecting one ready node is deterministic and never races
    another local Claude process.
    """

    if not _auto_graph_workers_enabled() or workers:
        return []
    state = load_state(root / "loop-state.json")
    task = next(
        (
            item for item in state.get("graph_tasks", [])
            if isinstance(item, Mapping) and str(item.get("status", "")) == "ready"
        ),
        None,
    )
    if not isinstance(task, Mapping):
        return []
    task_id = str(task.get("id", ""))
    if not task_id:
        return []
    auto_id = f"auto-graph-{hashlib.sha1(task_id.encode()).hexdigest()[:12]}"
    worker_env = _auto_field_worker_environment(environment)
    worker_env["RALPH_ROLE"] = "worker"
    worker_env["RALPH_AGENT_ID"] = auto_id
    worker_effort = effort or os.environ.get("RALPH_AUTO_GRAPH_EFFORT", "low")
    command = _with_skip_permissions(
        _with_model(
            _with_effort(
                [
                    _claude_executable(),
                    "--settings",
                    str(settings_path),
                    "--setting-sources",
                    "user,project,local",
                    "--system-prompt",
                    AUTO_GRAPH_WORKER_SYSTEM_PROMPT,
                    "--tools",
                    "Read,Write,Edit,Bash",
                    "--allowedTools",
                    "Read",
                    "Write",
                    "Edit",
                    "Bash",
                    "--permission-mode",
                    "bypassPermissions",
                    "--no-session-persistence",
                ],
                worker_effort,
            ),
            model,
        ),
        skip_permissions,
    )
    _append_stage_executor_skill(command)
    command.extend(["-p", _auto_graph_worker_prompt(task, root)])
    log_dir = root / "loop-artifacts" / "worker-logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_handle = (log_dir / f"{task_id}.log").open("ab")
    try:
        process = subprocess.Popen(
            command,
            cwd=root,
            env=worker_env,
            stdout=log_handle,
            stderr=subprocess.STDOUT,
            start_new_session=(os.name != "nt"),
        )
    except OSError as exc:
        log_handle.close()
        append_observation(
            root / "loop-events.md",
            "auto_graph_worker_start_failed",
            {"graph_task_id": task_id, "agent_id": auto_id, "error": str(exc)},
        )
        return []
    workers[task_id] = {
        "process": process,
        "log": log_handle,
        "agent_id": auto_id,
        "started_at": time.monotonic(),
    }
    append_observation(
        root / "loop-events.md",
        "auto_graph_worker_started",
        {"graph_task_id": task_id, "node_id": task.get("node_id"), "agent_id": auto_id, "pid": process.pid},
    )
    return [task_id]


def _reap_auto_graph_workers(root: Path, workers: dict[str, dict[str, Any]]) -> None:
    """Close finished graph-worker logs and recover the local-model slot."""

    for task_id, record in list(workers.items()):
        process = record.get("process")
        if not isinstance(process, subprocess.Popen):
            workers.pop(task_id, None)
            continue
        return_code = process.poll()
        started_at = record.get("started_at")
        timeout = _auto_graph_worker_timeout_seconds()
        if return_code is None and timeout > 0 and isinstance(started_at, (int, float)) and time.monotonic() - float(started_at) >= timeout:
            _terminate_process_group(process)
            return_code = process.returncode
            event_type = "auto_graph_worker_timeout"
        elif return_code is None:
            continue
        else:
            event_type = "auto_graph_worker_finished"
        log_handle = record.get("log")
        if hasattr(log_handle, "close"):
            log_handle.close()
        append_observation(
            root / "loop-events.md",
            event_type,
            {
                "graph_task_id": task_id,
                "agent_id": record.get("agent_id"),
                "return_code": return_code,
                "state_preserved": True,
            },
        )
        workers.pop(task_id, None)


def _wait_for_auto_graph_workers(root: Path, workers: dict[str, dict[str, Any]]) -> None:
    """Serialize graph recovery workers on memory-constrained local models."""

    while workers:
        _reap_auto_graph_workers(root, workers)
        if workers:
            time.sleep(1.0)


def _reap_persisted_auto_workers(root: Path, state: Mapping[str, Any]) -> list[int]:
    """Reap fallback workers left by a previous supervisor process."""

    reaped: list[int] = []
    tasks = state.get("field_tasks", []) if isinstance(state.get("field_tasks"), list) else []
    for task in tasks:
        if not isinstance(task, Mapping) or str(task.get("status", "")) not in {"dispatching", "dispatched"}:
            continue
        try:
            pid = int(task.get("worker_pid", 0) or 0)
        except (TypeError, ValueError):
            pid = 0
        if pid <= 0:
            continue
        try:
            os.kill(pid, signal.SIGTERM)
            reaped.append(pid)
        except ProcessLookupError:
            pass
        except OSError:
            continue
        update_field_task_metadata_transaction(
            root,
            str(task.get("id", "")),
            status="ready",
            clear_agent_id=True,
            clear_agent_ids=True,
            last_error="上一监督器已退出，已回收持久化 worker 并保留增量草稿",
            worker_pid=0,
        )
    if reaped:
        append_observation(
            root / "loop-events.md",
            "auto_field_worker_persisted_orphan_reaped",
            {"pids": reaped, "state_preserved": True, "next_action": "ready_retry"},
        )
    return reaped


def _loop_project_impl(
    project_or_task: str | Path,
    task: str | None = None,
    mode: str = "hybrid",
    workspace: str | Path | None = None,
    effort: str | None = None,
    model: str | None = None,
    auto_compact_window: int | None = None,
    auto_compact_percent: int | None = None,
    max_cycles: int = 0,
    retry_delay: float = 3.0,
    agent_grace_seconds: float = 5.0,
    idle_timeout: float = 0.0,
    wait_human: bool = False,
    skip_permissions: bool = False,
    max_failed_cycles: int = 0,
    stop_policy: str | None = None,
    _resolved: tuple[Path, str, ProjectResolution | None] | None = None,
) -> int:
    """Keep advancing a project while preserving normal Claude sessions.

    Normal Stop events use the inline Hook and remain in the same transcript.
    This outer loop is only the durable recovery boundary for a process lost
    to an API reset, memory guard, terminal closure, or a configured watchdog;
    state and artifacts let such a recovery start with a bounded fresh prompt.
    """

    if max_cycles < 0:
        raise ValueError("max-cycles 不能小于 0")
    if max_failed_cycles < 0:
        raise ValueError("max-failed-cycles 不能小于 0")
    if retry_delay < 0 or agent_grace_seconds < 0 or idle_timeout < 0:
        raise ValueError("retry-delay、agent-grace-seconds 和 idle-timeout 不能小于 0")
    if _resolved is None:
        project, task_text, resolution = _resolve_loop_project(project_or_task, task, workspace)
    else:
        project, task_text, resolution = _resolved
    root, settings_path, is_new, created = prepare_project(
        project,
        task=task_text,
        mode=mode,
        record_session=True,
        fresh_if_completed=True,
        stop_policy=stop_policy,
    )
    if agent_grace_seconds:
        # Startup reconciliation is safe for a project whose previous owner
        # is no longer this supervisor process.
        time.sleep(min(agent_grace_seconds, 60.0))
    # The active protocol is field-centric.  Legacy task cards are retained
    # only for migration/audit inspection and must not be reactivated or
    # mutated when a field-centric project starts.
    startup_reconciled = []
    startup_state = load_state(root / "loop-state.json")
    startup_reconciled.extend(_reap_persisted_auto_workers(root, startup_state))
    startup_state = load_state(root / "loop-state.json")
    stale_field_tasks = reopen_stale_field_tasks(root, startup_state)
    deferred_field_tasks = reopen_deferred_field_tasks(root, startup_state)
    if stale_field_tasks or deferred_field_tasks:
        save_state(root / "loop-state.json", startup_state)
        append_observation(
            root / "loop-events.md",
            "field_tasks_reopened_on_startup",
            {
                "field_task_ids": stale_field_tasks,
                "deferred_field_task_ids": deferred_field_tasks,
                "reason": "new supervisor context reopened stale and deferred field tasks",
            },
        )
    environment, compact_window, compact_percent = _claude_environment(
        auto_compact_window,
        auto_compact_percent,
    )
    # A new project used to receive only the raw user task, while every later
    # cycle received the compact field-state recovery prompt.  That asymmetry
    # makes a local Commander spend its first context on unbounded research
    # before it has materialized the stage fields.  Start with the same small,
    # durable state cue as a continuation: it preserves the user's task in
    # loop-state.json but gives an immediately executable, idempotent first
    # action instead of relying on Hook rejections to teach the workflow.
    first_prompt = (
        PromptRenderer().compact_recovery_prompt(
            startup_state,
            reason="新项目首次启动；从当前阶段的最小状态动作开始，不要先做无界搜索或总报告。",
            error_kind="initial",
            fresh_session=True,
            root=str(root),
        ).text
        if is_new
        else None
    )
    cycle = 0
    consecutive_failed_cycles = 0
    auto_workers: dict[str, dict[str, Any]] = {}
    auto_graph_workers: dict[str, dict[str, Any]] = {}
    suppress_auto_fallback = False
    print("RALPH loop project:", root)
    if resolution is not None:
        print("RALPH workspace:", resolution.workspace)
        print("Project decision:", "reuse" if not resolution.created else "create")
        print("Decision reason:", resolution.reason)
    print("Startup reconciliation:", json.dumps(startup_reconciled, ensure_ascii=False))
    print("Auto compact:", f"capacity={compact_window}, trigger≈{compact_window * compact_percent // 100} tokens")
    print("Continuous supervisor active; use Ctrl-C to stop the supervisor.")
    print("Idle watchdog:", "disabled" if idle_timeout == 0 else f"{idle_timeout:g} seconds")

    while max_cycles == 0 or cycle < max_cycles:
        _reap_auto_field_workers(root, auto_workers)
        _reap_auto_graph_workers(root, auto_graph_workers)
        state = load_state(root / "loop-state.json")
        # Field-centric mode is the only normal execution path.  The runtime
        # reconciles drafts and can auto-advance stage 01 when its fields are
        # complete; all later stages require an explicit validated apply.
        if _field_engine_tick(root, state):
            continue
        status = str(state.get("status", "running"))
        if status in {"completed", "stopped"}:
            print("RALPH terminal state:", status)
            return 0
        if status == "blocked_human":
            if wait_human:
                print("RALPH waiting for human input; state preserved at", root)
                return 3
            stage = state.get("stage", {})
            next_stage = str(stage.get("on_human_block") or "exploration")
            action = {
                "action": "skip_blocked",
                "status": "skipped",
                "stage_id": str(stage.get("id", "")),
                "revision": str(stage.get("revision", "r1")),
                "next_stage": next_stage,
                "rollback_to": None,
                "evidence": ["ralph loop auto-skip policy"],
                "artifact_refs": [],
                "message": "当前人类阻塞不阻塞其他工作，按持续运行策略跳过并进入后续可执行节点。",
            }
            apply_and_record(
                root / "loop-state.json",
                root / "loop-events.md",
                action,
                raw_output=json.dumps(action, ensure_ascii=False),
            )
            print("Auto-skipped blocked_human ->", next_stage)
            continue

        # Optional recovery fallback for a local Commander that repeatedly
        # thinks instead of emitting the required Agent tool call.  Workers
        # are still bounded by the same max-parallel setting and use the same
        # field task files/Hook validation as Commander-launched children.
        if _auto_field_workers_enabled() and cycle > 0 and not suppress_auto_fallback:
            # The first context belongs to Commander.  Starting a fallback
            # worker before Commander has had a chance to dispatch creates two
            # local Claude processes on small machines and can trigger an MLX
            # KV/memory guard even though the field queue is valid.  After a
            # context boundary, the same durable queue becomes eligible for
            # the bounded fallback worker.
            launched_auto_workers = _launch_auto_field_workers(
                root,
                settings_path,
                environment,
                model=model,
                effort=effort,
                skip_permissions=skip_permissions,
                workers=auto_workers,
            )
            if launched_auto_workers:
                # Do not launch a Commander in the same iteration.  A local
                # Qwen/MLX process must finish or be reaped before another
                # Claude context is allowed to allocate KV cache.
                _wait_for_auto_field_workers(root, auto_workers)
                suppress_auto_fallback = True
                continue
        if _auto_graph_workers_enabled() and not suppress_auto_fallback:
            launched_auto_graph_workers = _launch_auto_graph_workers(
                root,
                settings_path,
                environment,
                model=model,
                effort=effort,
                skip_permissions=skip_permissions,
                workers=auto_graph_workers,
            )
            if launched_auto_graph_workers:
                # A graph node may create a declared output consumed by its
                # join. Wait for graph-apply to atomically recalculate ready
                # nodes before considering another Commander context.
                _wait_for_auto_graph_workers(root, auto_graph_workers)
                suppress_auto_fallback = True
                continue

        recovery_prompt = PromptRenderer().compact_recovery_prompt(
            state,
            reason="上一轮 Claude 已结束；从持久化状态继续，不复述旧 transcript。",
            error_kind="continuation",
            fresh_session=True,
            root=str(root),
        ).text
        initial_prompt = first_prompt is not None
        prompt = first_prompt or recovery_prompt
        first_prompt = None
        command = _with_skip_permissions(
            _with_model(
                _with_effort(
                    [
                        _claude_executable(),
                        "--settings",
                        str(settings_path),
                        "--setting-sources",
                        "user,project,local",
                    ],
                    effort,
                ),
                model,
            ),
            skip_permissions,
        )
        skill_path = _append_stage_executor_skill(command)
        command.append(prompt)
        cycle += 1
        append_observation(
            root / "loop-events.md",
            "supervisor_cycle_started",
            {
                "cycle": cycle,
                "max_cycles": max_cycles,
                "stage": state.get("stage", {}).get("id"),
                "revision": state.get("stage", {}).get("revision"),
                "prompt_kind": "initial_state" if initial_prompt and cycle == 1 else "fresh_recovery",
                "stage_executor_skill": str(skill_path) if skill_path is not None else None,
            },
        )
        print(f"RALPH cycle {cycle}: launching fresh Claude context")
        supervisor_kwargs = {
            "cwd": root,
            "env": environment,
            "idle_timeout": idle_timeout,
            "protected_field_task_ids": set(auto_workers),
            "auto_workers": auto_workers,
        }
        # Keep small test/integration adapters that implement the original
        # three-argument runner usable. The production supervisor accepts the
        # bounded worker arguments; a compatible adapter simply cannot manage
        # those optional recovery workers itself.
        parameters = inspect.signature(_run_claude_supervised).parameters
        if "protected_field_task_ids" not in parameters:
            supervisor_kwargs.pop("protected_field_task_ids")
        if "auto_workers" not in parameters:
            supervisor_kwargs.pop("auto_workers")
        return_code, timed_out = _run_claude_supervised(command, **supervisor_kwargs)
        if return_code == 0:
            consecutive_failed_cycles = 0
        else:
            consecutive_failed_cycles += 1
        # A Commander boundary is the next opportunity for the bounded
        # fallback worker.  The flag only suppresses the immediate retry after
        # one worker attempt, preventing an infinite worker-only loop.
        suppress_auto_fallback = False
        if agent_grace_seconds:
            time.sleep(min(agent_grace_seconds, 60.0))
        if timed_out:
            append_observation(
                root / "loop-events.md",
                "supervisor_idle_timeout",
                {
                    "cycle": cycle,
                    "idle_timeout_seconds": idle_timeout,
                    "return_code": return_code,
                    "state_preserved": True,
                    "next_action": "fresh_context",
                },
            )
        # Do not reconcile legacy task cards from the active field workflow.
        # Their historical state remains available for audit but cannot affect
        # the current queue or stage transition.
        reconciled = []
        # Field Agents are owned by the Claude context that launched them.  If
        # that context ended because Stop Hook hit Claude's safety cap, an API
        # reset, or a memory guard, SubagentStop may never arrive.  Reopen the
        # live field files at this supervisor boundary so the next fresh
        # context can dispatch them again instead of inheriting a phantom
        # ``dispatched`` state forever.
        try:
            after_cycle_state = load_state(root / "loop-state.json")
            live_auto_worker_ids = _reap_auto_field_workers(root, auto_workers)
            reopened_fields = reopen_stale_field_tasks(
                root,
                after_cycle_state,
                exclude_ids=live_auto_worker_ids,
            )
            deferred_fields = reopen_deferred_field_tasks(root, after_cycle_state)
            if reopened_fields or deferred_fields:
                save_state(root / "loop-state.json", after_cycle_state)
                append_observation(
                    root / "loop-events.md",
                    "field_tasks_reopened_after_cycle",
                    {
                        "field_task_ids": reopened_fields,
                        "deferred_field_task_ids": deferred_fields,
                        "reason": "Claude context ended without SubagentStop",
                        "cycle": cycle,
                        "auto_workers": sorted(live_auto_worker_ids),
                    },
                )
        except (OSError, ValueError) as exc:
            reopened_fields = [f"error: {exc}"]
            deferred_fields = []
        append_observation(
            root / "loop-events.md",
            "supervisor_cycle_finished",
            {
                "cycle": cycle,
                "return_code": return_code,
                "reconciled_cards": reconciled,
                "reopened_fields": reopened_fields,
                "deferred_fields_reopened": deferred_fields,
                "next_action": "fresh_context" if max_cycles == 0 or cycle < max_cycles else "supervisor_limit",
            },
        )
        print(
            f"RALPH cycle {cycle} ended with return code {return_code}; "
            f"reopened {len(reopened_fields)} field task(s)."
        )
        if max_cycles and cycle >= max_cycles:
            print("Reached --max-cycles; persistent state remains resumable.")
            return 0
        if max_failed_cycles and consecutive_failed_cycles >= max_failed_cycles:
            append_observation(
                root / "loop-events.md",
                "supervisor_circuit_breaker",
                {
                    "cycle": cycle,
                    "return_code": return_code,
                    "consecutive_failed_cycles": consecutive_failed_cycles,
                    "max_failed_cycles": max_failed_cycles,
                    "state_preserved": True,
                    "next_action": "manual_recovery",
                },
            )
            print(
                "RALPH circuit breaker: "
                f"{consecutive_failed_cycles} consecutive failed cycles; "
                "persistent state remains resumable."
            )
            return 1
        if retry_delay:
            time.sleep(min(retry_delay, 60.0))
    return 0


def loop_project(
    project_or_task: str | Path,
    task: str | None = None,
    mode: str = "hybrid",
    workspace: str | Path | None = None,
    effort: str | None = None,
    model: str | None = None,
    auto_compact_window: int | None = None,
    auto_compact_percent: int | None = None,
    max_cycles: int = 0,
    retry_delay: float = 3.0,
    agent_grace_seconds: float = 5.0,
    idle_timeout: float = 0.0,
    wait_human: bool = False,
    skip_permissions: bool = False,
    max_failed_cycles: int = 0,
    stop_policy: str | None = None,
) -> int:
    """Run one project under an exclusive durable supervisor lock."""

    resolved = _resolve_loop_project(project_or_task, task, workspace)
    root = _project_root(resolved[0])
    with _supervisor_lock(root):
        return _loop_project_impl(
            project_or_task,
            task,
            mode,
            workspace,
            effort,
            model,
            auto_compact_window,
            auto_compact_percent,
            max_cycles,
            retry_delay,
            agent_grace_seconds,
            idle_timeout,
            wait_human,
            skip_permissions,
            max_failed_cycles=max_failed_cycles,
            stop_policy=stop_policy,
            _resolved=resolved,
        )


def _print_project_error(project: str | Path, error: Exception) -> None:
    raw_project = str(project)
    print(f"RALPH 无法启动项目 {raw_project!r}：{error}", file=sys.stderr)
    if raw_project.startswith("/") and Path(raw_project).parent == Path("/"):
        print(
            "提示：以 `/` 开头表示系统根目录下的绝对路径。请使用相对路径 `./gpu硬件调研`，"
            "或使用可写目录，例如 `$HOME/gpu硬件调研`。",
            file=sys.stderr,
        )
    else:
        print(
            "提示：确认项目路径位于可写目录；新项目可以使用 `./项目名` 或 `$HOME/项目名`。",
            file=sys.stderr,
        )


def validate_result_artifact(
    project: str | Path,
    result_file: str | Path,
    *,
    apply: bool = False,
) -> dict[str, object]:
    """Mechanically validate one stage result artifact, optionally apply it.

    Returns every field problem (not just the first) so the model can fix the
    whole payload in one pass via the fill-in workflow.
    """

    root = _project_root(project)
    path = resolve_result_artifact(root, result_file)
    raw = path.read_text(encoding="utf-8")
    action = parse_action(raw)
    state_path = root / "loop-state.json"
    state = load_state(state_path)
    issues = collect_validation_issues(action, state)
    report: dict[str, object] = {
        "valid": not issues,
        "project": str(root),
        "result_file": str(path.relative_to(root)),
        "issues": issues,
        "action": action.to_dict(),
        "applied": False,
    }
    if issues:
        return report
    if apply:
        updated = apply_and_record(
            state_path,
            root / "loop-events.md",
            raw,
            raw_output=raw,
        )
        report["applied"] = True
        report["state"] = {
            "status": updated.get("status"),
            "stage": updated.get("stage"),
            "last_event_id": updated.get("last_event_id"),
        }
    return report


def _fields_from_any(obj: object) -> list[dict]:
    """Extract the field list from any accepted JSON shape.

    Accepts: a bare list of fields, ``{fields:[...]}``, ``{attribute_matrix:[...]}``,
    or a full ``task_spec`` object (``{attribute_matrix:[...]}``)."""
    if isinstance(obj, list):
        return [f for f in obj if isinstance(f, dict)]
    if isinstance(obj, dict):
        for key in ("fields", "attribute_matrix"):
            val = obj.get(key)
            if isinstance(val, list):
                return [f for f in val if isinstance(f, dict)]
        if "task_spec" in obj and isinstance(obj["task_spec"], dict):
            am = obj["task_spec"].get("attribute_matrix")
            if isinstance(am, list):
                return [f for f in am if isinstance(f, dict)]
    return []


def render_matrix_md(
    fields: list[dict],
    *,
    title: str = "阶段字段快照",
    source: str = "",
) -> str:
    """Render a field list into a clean, human-readable markdown.

    This is the readable twin of the machine JSON: the agent only writes JSON,
    and this produces the ``.md`` the human reads.  Grouped by ``role``."""
    import datetime as _dt

    fields = [f for f in fields if isinstance(f, dict)]
    lines: list[str] = []
    lines.append(f"# {title}")
    lines.append("")
    if source:
        lines.append(f"> 由 `ralph render` 自动从 `{source}` 生成，请勿手改。")
        lines.append("")
    lines.append(f"> 生成时间：{_dt.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")

    # 概览
    pending = [f for f in fields if str(f.get("disposition")) in ("pending", "research_required")]
    roles: dict[str, list[dict]] = {}
    for f in fields:
        roles.setdefault(str(f.get("role") or "未分类"), []).append(f)
    lines.append("## 概览")
    lines.append("")
    lines.append(f"- 字段总数：**{len(fields)}**")
    lines.append(f"- 待办（pending / research_required）：**{len(pending)}**")
    if roles:
        lines.append(f"- 分组：{'、'.join(f'{k}×{len(v)}' for k, v in roles.items())}")
    lines.append("")

    # 明细，按 role 分组
    lines.append("## 字段明细")
    lines.append("")
    for role, group in roles.items():
        lines.append(f"### {role}")
        lines.append("")
        lines.append("| 要素 (concept) | 属性 | 状态 | 置信度 | 影响 | 可逆 |")
        lines.append("|---|---|---|---|---|---|")
        for f in group:
            concept = str(f.get("concept") or "")
            attr = str(f.get("attribute") or "")
            disp = str(f.get("disposition") or "")
            conf = f.get("confidence")
            conf = "" if conf is None else (f"{float(conf):.2f}" if isinstance(conf, (int, float)) else str(conf))
            impact = str(f.get("impact") or "")
            rev = "是" if f.get("reversible") else ("否" if f.get("reversible") is False else "")
            # 多行属性用 <br> 折行
            attr = attr.replace("\n", "<br>")
            lines.append(f"| {concept} | {attr} | {disp} | {conf} | {impact} | {rev} |")
        lines.append("")

    # 证据与备注
    has_notes = any(f.get("rationale") or f.get("evidence_refs") for f in fields)
    if has_notes:
        lines.append("## 证据与备注")
        lines.append("")
        for f in fields:
            concept = str(f.get("concept") or "")
            rationale = str(f.get("rationale") or "").strip()
            refs = f.get("evidence_refs") or []
            if not rationale and not refs:
                continue
            lines.append(f"### {concept}")
            if rationale:
                lines.append("")
                lines.append(rationale)
            if refs:
                lines.append("")
                lines.append("证据：")
                for r in refs:
                    if isinstance(r, dict):
                        url = r.get("url") or r.get("ref") or ""
                        note = r.get("note") or r.get("title") or ""
                        lines.append(f"- [{note or url}]({url})" if url else f"- {note}")
                    else:
                        lines.append(f"- {r}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


@contextmanager
def _field_apply_lock(root: Path):
    """Serialize concurrent per-field merges from parallel subagents."""

    lock_path = root / "loop-artifacts" / ".field-apply.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    handle = lock_path.open("a+", encoding="utf-8")
    try:
        if fcntl is not None:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        yield
    finally:
        if fcntl is not None:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        handle.close()


def apply_fields(project: str | Path, fields_file: str | Path) -> dict[str, object]:
    """Validate and atomically merge one incremental field draft.

    Parallel field agents may call this command at the same time.  The lock
    covers the load/merge/save transaction, so one agent cannot overwrite a
    sibling agent's newly accepted field.
    """

    root = _project_root(project)
    with _field_apply_lock(root):
        return _apply_fields_unlocked(root, fields_file)


def _is_cross_validation_field(field: Mapping[str, Any], stage_id: str) -> bool:
    if stage_id not in {"02.5", "04.5"}:
        return False
    role = str(field.get("role") or "").strip().lower()
    concept = str(field.get("concept") or "").strip()
    return role in {"cross_validation", "cross_validation_out", "validation"} or concept in {
        "cross_validation",
        "cross_validation_out",
    }


def _successful_web_llm_receipt(root: Path, reference: Any) -> bool:
    """Validate a real, successful cross-check receipt without trusting prose."""

    if not isinstance(reference, str) or not reference.strip():
        return False
    candidate = (root / reference).resolve()
    if root not in candidate.parents or not candidate.is_file():
        return False
    try:
        document = json.loads(candidate.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, ValueError):
        return False
    providers = document.get("successful_provider_ids") if isinstance(document, Mapping) else None
    return (
        isinstance(document, Mapping)
        and document.get("kind") == "ralph_web_llm_cross_check"
        and isinstance(providers, list)
        and len({str(item) for item in providers if str(item).strip()}) >= 2
    )


def _validate_cross_validation_receipts(root: Path, stage_id: str, field: Mapping[str, Any]) -> None:
    """Enforce web-LLM use when a human-authorized provider pair is available."""

    if not _is_cross_validation_field(field, stage_id) or not web_llm_crosscheck_enabled(root):
        return
    refs = field.get("evidence_refs")
    valid = [ref for ref in refs if _successful_web_llm_receipt(root, ref)] if isinstance(refs, list) else []
    if not valid:
        raise ValueError(
            "本项目已配置至少两个经人类授权的网页 LLM；交叉验证字段必须引用 "
            "`ralph web-llm-check` 产生的成功回执（其中含 >=2 successful_provider_ids）。"
            "登录未完成或网页失败时不要写“已询问 LLM”，保留 research_required / uncertain 并记录失败。"
        )


def _apply_fields_unlocked(root: Path, fields_file: str | Path) -> dict[str, object]:
    """Field-validation command used by the Commander in field-centric mode.

    The Commander never edits ``loop-state.json`` directly.  It writes a small
    delta file (only the fields it changed) and runs this command, which
    validates every field, merges by ``concept`` into ``task_spec.attribute_matrix``
    (replacing on match, appending otherwise; ``{"delete": true}`` removes), then
    commits atomically via :func:`save_state`.  This makes a corrupt write
    impossible: the runtime owns the only write path."""

    state = load_state(root / "loop-state.json", graph=DEFAULT_GRAPH)
    fields_path = Path(fields_file).expanduser()
    if not fields_path.is_absolute():
        fields_path = root / fields_path
    fields_path = fields_path.resolve()
    allowed_dir = state_stage_artifact_dir(root, state).resolve()
    if allowed_dir not in fields_path.parents:
        raise ValueError(
            f"字段草稿必须位于当前阶段目录 `{allowed_dir.relative_to(root)}` 或其 tasks 子目录；"
            f"请把文件移动到该目录后再运行 `ralph field-apply {root} <fields.json>`"
        )
    try:
        raw = json.loads(fields_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"字段草稿 JSON 语法错误：第 {exc.lineno} 行、第 {exc.colno} 列：{exc.msg}。"
            f"只修复 `{fields_path}` 的 JSON 语法，然后重运行："
            f"ralph field-apply {root} {fields_file}"
        ) from exc
    if isinstance(raw, list):
        fields = raw
    elif isinstance(raw, dict):
        fields = raw.get("fields") or raw.get("attribute_matrix")
        if fields is None and isinstance(raw.get("field"), dict):
            fields = [raw["field"]]
        if fields is None and raw.get("concept"):
            fields = [raw]
        fields = fields or []
    else:
        raise ValueError("fields file must be a list or {fields:[...]}/{attribute_matrix:[...]}")
    if not isinstance(fields, list):
        raise ValueError("fields must be a list")

    spec = state.setdefault("task_spec", {})
    if not isinstance(spec, dict):
        spec = {}
        state["task_spec"] = spec
    matrix = spec.setdefault("attribute_matrix", [])
    if not isinstance(matrix, list):
        matrix = []
        spec["attribute_matrix"] = matrix

    by_concept = {
        str(f.get("concept")): i
        for i, f in enumerate(matrix)
        if isinstance(f, dict)
    }
    current_stage = str(state.get("stage", {}).get("id", "")) if isinstance(state.get("stage"), dict) else ""
    flow_only = flow_only_mode(state)
    added = removed = 0
    allowed_dispositions = {"confirmed", "inferred", "assumed_default", "research_required", "pending"}
    seen_concepts: set[str] = set()
    for f in fields:
        if not isinstance(f, dict):
            raise ValueError(f"field entry must be an object: {f!r}")
        if f.get("delete"):
            concept = str(f.get("concept"))
            if not concept or concept == "None":
                raise ValueError("删除字段必须提供非空 concept")
            if concept in by_concept:
                matrix.pop(by_concept[concept])
                removed += 1
            continue
        graph_payload = None
        is_task_graph = str(f.get("role", "")) == "task_graph" or str(f.get("concept", "")) == "task_graph"
        if is_task_graph:
            if str(f.get("role", "")) != "task_graph":
                raise ValueError(
                    "concept=task_graph 的字段 role 必须精确为 task_graph；"
                    "自然语言 decomposition/coverage 不能代替可执行 DAG。"
                )
            for key in ("task_graph", "graph", "value"):
                if isinstance(f.get(key), Mapping):
                    graph_payload = f[key]
                    break
            if graph_payload is None:
                raise ValueError(
                    "task_graph 字段必须包含结构化 task_graph/graph/value 对象；"
                    "不要把节点描述塞进 attribute 文本。"
                )
            # A graph field may omit the human-readable attribute because its
            # actual value is the structured `task_graph` object.
            if graph_payload is not None and not f.get("attribute"):
                f = dict(f)
                f["attribute"] = "validated execution DAG"
        for req in ("concept", "attribute", "disposition", "role"):
            if not f.get(req):
                raise ValueError(f"field missing required key '{req}': {f!r}")
        concept = str(f.get("concept"))
        if concept in seen_concepts:
            raise ValueError(f"字段草稿中 concept 重复：{concept!r}；同一字段只保留最后一个版本")
        seen_concepts.add(concept)
        if f.get("disposition") not in allowed_dispositions:
            raise ValueError(
                f"字段 {concept!r} 的 disposition 无效：{f.get('disposition')!r}；"
                f"允许值：{', '.join(sorted(allowed_dispositions))}"
            )
        # In an explicitly closed-world flow test a worker may still follow
        # the generic evidence rule from a surrounding skill and save a
        # synthetic leaf as research_required. That is not an unresolved
        # real-world claim: preserving it verbatim would recreate the same
        # task forever even though the prompt forbids web access. Normalize at
        # the atomic merge boundary so the durable state reflects the declared
        # test semantics while retaining the worker's rationale.
        if flow_only and f.get("disposition") == "research_required":
            f = dict(f)
            f["disposition"] = "inferred"
            rationale = str(f.get("rationale") or "").strip()
            marker = "仅用于验证流程"
            f["rationale"] = rationale if marker in rationale else (f"{rationale}；{marker}".strip("；"))
        if (
            os.environ.get("RALPH_ROLE", "").strip().lower() == "worker"
            and flow_only_mode(state)
            and f.get("disposition") == "pending"
            and (
                str(f.get("attribute", "")).startswith("请填写 ")
                or str(f.get("rationale", "")).startswith("由运行时为缺失")
            )
        ):
            raise ValueError(
                f"字段 {concept!r} 仍是空 pending 占位；worker 必须先用 Write/Edit 填写真实 attribute 和 rationale，"
                "并将 disposition 设为 inferred，再重试同一个 field-apply。Commander 的其他空字段可以保留 pending。"
            )
        # ``pending`` is an intentional editable placeholder.  The field
        # protocol is incremental: a Commander may submit one completed field
        # while leaving other required outputs empty for a later turn.  The
        # stage gate, not field-apply, decides whether the remaining pending
        # placeholders are sufficient to advance.
        if graph_payload is not None:
            try:
                validate_plan(graph_payload, strict=True)
            except (DAGValidationError, TypeError, ValueError) as exc:
                raise ValueError(
                    f"字段 {concept!r} 的 task_graph 校验失败：{exc}。"
                    "只修复 nodes、depends_on、parallel_group_id、orthogonal_key、writes 或 output_schema，"
                    "然后重新运行 field-apply；状态尚未写入。"
                ) from exc
            state["plan"] = json.loads(json.dumps(graph_payload, ensure_ascii=False))
        refs = f.get("evidence_refs", [])
        if not isinstance(refs, list):
            raise ValueError(f"字段 {concept!r} 的 evidence_refs 必须是数组")
        # Fail fast for fabricated "confirmed" research.  A worker may still
        # save a failed lookup as research_required with no refs (so the next
        # context can retry); only an asserted external fact is rejected here.
        if not flow_only and str(f.get("disposition") or "") in {"confirmed", "inferred", "assumed_default"}:
            evidence_issues = _external_evidence_issues([f], current_stage)
            if evidence_issues:
                raise ValueError("；".join(evidence_issues))
        if not flow_only:
            _validate_cross_validation_receipts(root, current_stage, f)
        confidence = f.get("confidence")
        if confidence is not None and (not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1):
            raise ValueError(f"字段 {concept!r} 的 confidence 必须是 0 到 1 之间的数字")
        if concept in by_concept:
            matrix[by_concept[concept]] = f
        else:
            matrix.append(f)
            by_concept[concept] = len(matrix) - 1
        added += 1

    materialize_field_tasks(root, state)
    materialize_graph_tasks(root, state)
    save_state(root / "loop-state.json", state)
    # Record an accepted incremental submission on the exact field task file.
    # SubagentStop uses this receipt to distinguish a valid incomplete draft
    # from an Agent that merely returned natural language without applying it.
    applied_at = datetime.now(timezone.utc).isoformat()
    relative_fields_path = str(fields_path.relative_to(root))
    applied_task_id: str | None = None
    for field_task in state.get("field_tasks", []):
        if not isinstance(field_task, Mapping) or str(field_task.get("path")) != relative_fields_path:
            continue
        current_count = int(field_task.get("apply_count", 0) or 0) + 1
        applied_task_id = str(field_task["id"])
        state = update_field_task_metadata_transaction(
            root,
            applied_task_id,
            apply_count=current_count,
            last_applied_at=applied_at,
        )
        break

    # A supervisor-launched top-level field worker has no Claude
    # ``SubagentStop`` lifecycle event.  Let its successful field-apply release
    # the durable reservation so the worker's Stop Hook can exit normally.
    # Incomplete evidence is deferred for a later supervisor context; it is
    # never treated as a successful research result.
    if applied_task_id and os.environ.get("RALPH_ROLE", "").strip().lower() == "worker":
        live_after_apply = load_state(root / "loop-state.json")
        task_record = next(
            (item for item in live_after_apply.get("field_tasks", [])
             if isinstance(item, Mapping) and str(item.get("id")) == applied_task_id),
            None,
        )
        concept = str(task_record.get("concept", "")) if isinstance(task_record, Mapping) else ""
        matrix_after_apply = (live_after_apply.get("task_spec") or {}).get("attribute_matrix", [])
        field_after_apply = next(
            (item for item in matrix_after_apply
             if isinstance(item, Mapping) and str(item.get("concept", "")) == concept),
            None,
        ) if isinstance(matrix_after_apply, list) else None
        disposition = str(field_after_apply.get("disposition", "")) if isinstance(field_after_apply, Mapping) else ""
        refs = field_after_apply.get("evidence_refs") if isinstance(field_after_apply, Mapping) else []
        flow_only = bool(task_record.get("flow_only")) if isinstance(task_record, Mapping) else False
        complete = disposition in {"confirmed", "inferred", "assumed_default"} or (
            flow_only and disposition == "research_required"
        ) or (
            disposition == "research_required" and isinstance(refs, list) and bool(refs)
        )
        update_field_task_metadata_transaction(
            root,
            applied_task_id,
            status="completed" if complete else "deferred",
            clear_agent_id=True,
            clear_agent_ids=True,
            last_error=None if complete else "worker 已保存增量草稿，等待后续上下文补充证据",
        )

    # 自动把当前字段草稿渲染成易读 .md（agent 只写 JSON，人读 MD）。best-effort。
    rendered_md: str | None = None
    try:
        fields = _fields_from_any(state.get("task_spec", {}))
        if fields:
            md = render_matrix_md(
                fields,
                title=f"{current_stage or '?'} 阶段字段快照",
                source=str(fields_path.relative_to(root)),
            )
            md_path = fields_path.with_suffix(".md")
            md_path.write_text(md, encoding="utf-8")
            rendered_md = str(md_path)
    except Exception:
        rendered_md = None

    stage = state.get("stage") if isinstance(state.get("stage"), dict) else {}
    completeness = field_completeness(matrix, stage.get("required_outputs") or [])
    result: dict[str, object] = {
        "ok": True,
        "added": added,
        "removed": removed,
        "total": len(matrix),
        "remaining": completeness,
        "next": (
            "继续填写 remaining.required_outputs / pending / researching / splittable"
            if not completeness["complete"]
            else "字段门禁已通过；阶段 02+ 写 advance.json 后运行 ralph apply"
        ),
    }
    if rendered_md:
        result["rendered_md"] = rendered_md
    append_observation(
        root / "loop-events.md",
        "field_increment_applied",
        {
            "stage": current_stage,
            "revision": stage.get("revision") if isinstance(stage, Mapping) else None,
            "fields_file": str(fields_path.relative_to(root)),
            "concepts": [
                str(field.get("concept"))
                for field in fields
                if isinstance(field, Mapping) and field.get("concept")
            ],
            "added": added,
            "removed": removed,
            "remaining": completeness,
            "state_changed": True,
            "output_excerpt_source": "field_apply_result",
        },
        output=json.dumps(result, ensure_ascii=False, sort_keys=True),
        artifacts=[str(fields_path.relative_to(root))] + ([rendered_md] if rendered_md else []),
    )
    return result


def init_fields(project: str | Path) -> dict[str, object]:
    """Create the safe, stage-scoped incremental draft without overwriting it."""

    root = _project_root(project)
    state_path = root / "loop-state.json"
    if not state_path.exists():
        prepare_project(root, mode="hybrid")
    state = load_state(state_path, graph=DEFAULT_GRAPH)
    directory = state_stage_artifact_dir(root, state)
    directory.mkdir(parents=True, exist_ok=True)
    fields_path = directory / "fields.json"
    created = False
    if not fields_path.exists():
        fields_path.write_text('{\n  "fields": []\n}\n', encoding="utf-8")
        created = True
    return {
        "ok": True,
        "created": created,
        "fields_file": str(fields_path),
        "stage": state.get("stage", {}),
        "next": f"填写该文件后运行 `ralph field-apply {root} {fields_path}`",
    }


def recover_state_cmd(
    project: str | Path,
    *,
    stage: str | None = None,
    to_backup: bool = False,
) -> dict[str, object]:
    """Restore a corrupted or unwanted ``loop-state.json``.

    Without flags, prefers ``loop-state.json.bak`` then the latest stage
    snapshot.  ``--stage <id>`` restores ``loop-artifacts/snapshots/loop-state.<id>.json``
    (the last saved state while in that stage) — i.e. "reset to a previous stage"."""

    root = _project_root(project)
    path = root / "loop-state.json"
    if not path.exists():
        return {"ok": False, "error": "no loop-state.json to recover"}

    def _restore(src: Path, label: str) -> dict[str, object]:
        data = json.loads(src.read_text(encoding="utf-8"))
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return {"ok": True, "source": label}

    if to_backup:
        bak = path.with_name(path.name + ".bak")
        if not bak.exists():
            return {"ok": False, "error": "no loop-state.json.bak"}
        return _restore(bak, "loop-state.json.bak")

    if stage:
        snap = root / "loop-artifacts" / "snapshots" / f"loop-state.{stage}.json"
        if not snap.exists():
            return {"ok": False, "error": f"no snapshot for stage {stage}"}
        return _restore(snap, f"loop-artifacts/snapshots/loop-state.{stage}.json")

    bak = path.with_name(path.name + ".bak")
    if bak.exists():
        return _restore(bak, "loop-state.json.bak")
    snap_dir = root / "loop-artifacts" / "snapshots"
    snaps = sorted(snap_dir.glob("loop-state.*.json"), reverse=True) if snap_dir.is_dir() else []
    if snaps:
        return _restore(snaps[0], str(snaps[0].relative_to(root)))
    return {"ok": False, "error": "nothing to recover from"}


def render_cmd(project: str | Path, json_file: str | Path | None = None) -> dict[str, object]:
    """Render a stage field JSON into a human-readable markdown.

    With ``json_file`` it reads that file (any accepted shape).  Without it, it
    reads the current stage artifact referenced by ``loop-state.json``.  The
    markdown is written next to the source as ``<stem>.md`` and also printed."""
    root = _project_root(project)

    if json_file:
        src = Path(json_file)
        if not src.is_absolute():
            src = root / src
        if not src.exists():
            return {"ok": False, "error": f"json file not found: {src}"}
        obj = json.loads(src.read_text(encoding="utf-8"))
        source_name = str(src.relative_to(root)) if root in src.parents else str(src)
        title = f"{src.stem} 字段快照"
    else:
        state = load_state(root / "loop-state.json", graph=DEFAULT_GRAPH)
        draft = state_stage_artifact_dir(root, state) / "fields.json"
        ca = str(draft.relative_to(root)) if draft.exists() else state.get("current_artifact")
        if not ca:
            return {"ok": False, "error": "当前没有阶段字段文件；先运行 ralph field-init"}
        src = root / str(ca)
        if not src.exists():
            return {"ok": False, "error": f"artifact not found: {src}"}
        obj = json.loads(src.read_text(encoding="utf-8"))
        source_name = ca
        title = f"{state.get('stage', {}).get('id', '?')} 阶段字段快照"

    fields = _fields_from_any(obj)
    if not fields:
        return {"ok": False, "error": "no fields found to render"}
    md = render_matrix_md(fields, title=title, source=source_name)
    md_path = src.with_suffix(".md")
    md_path.write_text(md, encoding="utf-8")
    print(md, end="")
    return {"ok": True, "md": str(md_path), "fields": len(fields)}


def watch_cmd(project: str | Path, *, interval: float = 5.0, max_lines: int = 42) -> int:
    """Live, TUI-free dashboard for any running ralph session.

    Polls the durable state / artifact / event files (never the agent's stdout)
    and refreshes a compact view every ``interval`` seconds.  Works for any
    project; ``Ctrl-C`` exits."""
    import os as _os
    import time as _time

    root = _project_root(project)
    try:
        while True:
            _os.system("clear" if _os.name == "posix" else "cls")
            print(f"===== {_time.strftime('%Y-%m-%d %H:%M:%S')} | {root.name} =====")
            try:
                state = load_state(root / "loop-state.json", graph=DEFAULT_GRAPH)
                stage = state.get("stage") if isinstance(state.get("stage"), dict) else {}
                print(
                    f"阶段: {stage.get('id')} {stage.get('revision')} | 状态: {state.get('status')} "
                    f"| 文件: {state.get('current_artifact')}"
                )
            except Exception as exc:  # noqa: BLE001
                print(f"[状态读取失败] {exc}")
                state = {}
            print("\n----- 当前字段快照 -----")
            try:
                ca = state.get("current_artifact")
                if ca and (root / str(ca)).exists():
                    obj = json.loads((root / str(ca)).read_text(encoding="utf-8"))
                    fields = _fields_from_any(obj)
                    if fields:
                        md = render_matrix_md(fields, title=f"{stage.get('id', '?')} 阶段字段快照", source=ca)
                        print("\n".join(md.splitlines()[:max_lines]))
            except Exception as exc:  # noqa: BLE001
                print(f"[渲染失败] {exc}")
            print("\n----- 最近事件 -----")
            try:
                ev = events_tail(str(root), 6)
                for e in ev.get("events", [])[-6:]:
                    obs = e.get("observation") or {}
                    print(f" - {e.get('type')} | {obs.get('tool_name') or obs.get('role')} @ {str(e.get('timestamp', ''))[11:19]}")
            except Exception as exc:  # noqa: BLE001
                print(f"[事件读取失败] {exc}")
            _time.sleep(interval)
    except KeyboardInterrupt:
        return 0


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "prompt-first-stop":
        try:
            payload = json.loads(sys.stdin.read() or "{}")
            print(json.dumps(handle_prompt_first_stop(payload), ensure_ascii=False))
            return 0
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
            return 1
    if args.command == "prompt-first-pre-tool":
        try:
            payload = json.loads(sys.stdin.read() or "{}")
            print(json.dumps(handle_prompt_first_pre_tool(payload), ensure_ascii=False))
            return 0
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
            return 1
    if args.command == "prompt-first-precompact":
        try:
            payload = json.loads(sys.stdin.read() or "{}")
            print(json.dumps(handle_prompt_first_precompact(payload), ensure_ascii=False))
            return 0
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
            return 1
    if args.command == "prompt-first-postcompact":
        try:
            payload = json.loads(sys.stdin.read() or "{}")
            print(json.dumps(handle_prompt_first_postcompact(payload), ensure_ascii=False))
            return 0
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
            return 1
    if args.command == "prompt-first-post-tool":
        try:
            payload = json.loads(sys.stdin.read() or "{}")
            print(json.dumps(handle_prompt_first_post_tool(payload), ensure_ascii=False))
            return 0
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
            return 1
    if args.command == "prompt-first":
        try:
            if args.prompt_first_command == "init":
                state = initialize_prompt_first(args.project, args.task)
                print(json.dumps(prompt_first_status_summary(args.project), ensure_ascii=False, indent=2, sort_keys=True))
                return 0
            if args.prompt_first_command == "status":
                print(json.dumps(prompt_first_status_summary(args.project), ensure_ascii=False, indent=2, sort_keys=True))
                return 0
            if args.prompt_first_command == "render":
                print(render_prompt_first(args.project), end="")
                return 0
            if args.prompt_first_command == "review":
                return prompt_first_review_project(
                    args.project,
                    effort=args.effort,
                    model=args.model,
                    skip_permissions=args.dangerously_skip_permissions,
                )
            if args.prompt_first_command == "loop":
                return prompt_first_loop_project(
                    args.project,
                    args.task,
                    effort=args.effort,
                    model=args.model,
                    max_cycles=args.max_cycles,
                    retry_delay=args.retry_delay,
                    idle_timeout=args.idle_timeout,
                    skip_permissions=args.dangerously_skip_permissions,
                    auto_compact_window=args.auto_compact_window,
                    auto_compact_percent=args.auto_compact_percent,
                )
            if args.prompt_first_command == "web-llm":
                question = args.question.strip()
                context = args.context
                if not question:
                    current = load_prompt_first_state(args.project)
                    question = (
                        "请审阅当前任务的关键主张与不确定性，指出需要独立来源核验的部分："
                        f"{current['task']}"
                    )
                    context = context or f"当前阶段：{current['stage']}；请给出克制、可核验的审阅线索。"
                print(json.dumps(
                    run_prompt_first_web_llm_cross_check(args.project, question, context),
                    ensure_ascii=False,
                    indent=2,
                    sort_keys=True,
                ))
                return 0
        except (OSError, ValueError, SupervisorAlreadyRunning) as exc:
            _print_project_error(getattr(args, "project", "."), exc)
            return 2
    if args.command == "init":
        if args.workflow == "prompt-first":
            prompt_state = prompt_first_state_path(args.project)
            if prompt_state.exists():
                print(f"state already exists: {prompt_state}", file=sys.stderr)
                return 2
            if _state_path(args.project).exists():
                print(
                    f"field state already exists: {_state_path(args.project)}; use the existing legacy project or a new directory",
                    file=sys.stderr,
                )
                return 2
            initialize_prompt_first(args.project, "")
            print(prompt_state)
            return 0
        path = _state_path(args.project)
        if path.exists():
            print(f"state already exists: {path}", file=sys.stderr)
            return 2
        prepare_project(path.parent, mode="hybrid")
        print(path)
        return 0
    if args.command in {"status", "field-status"}:
        state_path = _state_path(args.project)
        state = load_state(state_path)
        if not args.full:
            # Materialize only the bounded queue view needed by the dashboard;
            # do not save the complete state or inject it into stdout.
            root = state_path.parent
            materialize_field_tasks(root, state)
            materialize_graph_tasks(root, state)
        view = state if args.full else status_summary(state, args.project)
        print(json.dumps(view, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    if args.command == "events":
        try:
            print(json.dumps(events_tail(args.project, args.tail), ensure_ascii=False, indent=2, sort_keys=True))
            return 0
        except (OSError, ValueError) as exc:
            print(f"RALPH 无法读取有限事件摘要：{exc}", file=sys.stderr)
            return 2
    if args.command == "task-next":
        try:
            print(json.dumps(task_next(args.project), ensure_ascii=False, indent=2, sort_keys=True))
            return 0
        except (OSError, TaskBoardError, ValueError) as exc:
            print(f"RALPH 无法读取任务板：{exc}", file=sys.stderr)
            return 2
    if args.command == "prompt" and args.prompt_command == "render":
        rendered = PromptRenderer().render(load_state(_state_path(args.project)))
        print(rendered.text, end="")
        print(f"prompt_sha256={rendered.sha256}", file=sys.stderr)
        return 0
    if args.command == "prompt" and args.prompt_command == "replay":
        updated, prompt_hash, action = run_fixture_file(args.fixture)
        print(json.dumps({"prompt_sha256": prompt_hash, "action": action.to_dict(), "state": updated}, ensure_ascii=False, indent=2))
        return 0
    if args.command == "apply":
        try:
            report = validate_result_artifact(args.project, args.action_file, apply=True)
            print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
            return 0 if report.get("valid") else 1
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(
                json.dumps(
                    {
                        "valid": False,
                        "applied": False,
                        "error": (
                            f"提交文件无法解析或校验：{exc}。只修复 `{args.action_file}`，"
                            f"然后重运行 `ralph apply {args.project} {args.action_file}`。"
                        ),
                    },
                    ensure_ascii=False,
                    indent=2,
                ),
                file=sys.stderr,
            )
            return 1
    if args.command == "field-apply":
        try:
            report = apply_fields(args.project, args.fields_file)
            print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
            return 0
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
            return 1
    if args.command == "field-init":
        try:
            print(json.dumps(init_fields(args.project), ensure_ascii=False, indent=2, sort_keys=True))
            return 0
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
            return 1
    if args.command == "field-reconcile":
        try:
            root = _project_root(args.project)
            state_path = root / "loop-state.json"
            state = load_state(state_path)
            materialize_field_tasks(root, state)
            reconciled = reconcile_applied_field_tasks(root, state)
            if reconciled:
                save_state(state_path, state)
                append_observation(
                    root / "loop-events.md",
                    "field_tasks_reconciled_after_late_agent_receipt",
                    {"tasks": reconciled, "state_preserved": True},
                )
            print(json.dumps({"ok": True, "reconciled": reconciled, "state_preserved": True}, ensure_ascii=False, indent=2))
            return 0
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
            return 1
    if args.command == "web-llm-check":
        try:
            print(json.dumps(run_web_llm_cross_check(args.project, args.request_file), ensure_ascii=False, indent=2, sort_keys=True))
            return 0
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
            return 1
    if args.command == "web-llm-authorize":
        try:
            print(json.dumps(
                authorize_browser_providers(
                    args.project,
                    args.providers,
                    global_scope=args.global_scope,
                    browser_profile=args.profile_dir,
                ),
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            ))
            return 0
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
            return 1
    if args.command == "web-llm-login":
        try:
            print(json.dumps(
                open_browser_login(args.site, wait_seconds=args.wait_seconds),
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            ))
            return 0
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
            return 1
    if args.command == "graph-apply":
        try:
            print(json.dumps(apply_graph_task(args.project, args.task_file), ensure_ascii=False, indent=2, sort_keys=True))
            return 0
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
            return 1
    if args.command == "recover-state":
        try:
            report = recover_state_cmd(args.project, stage=args.stage, to_backup=args.to_backup)
            print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
            return 0 if report.get("ok") else 1
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
            return 1
    if args.command == "render":
        try:
            report = render_cmd(args.project, args.json_file)
            if not report.get("ok"):
                print(json.dumps(report, ensure_ascii=False, indent=2), file=sys.stderr)
                return 1
            return 0
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
            return 1
    if args.command == "watch":
        return watch_cmd(args.project, interval=args.interval, max_lines=args.lines)
    if args.command == "assemble":
        try:
            report = assemble_stage_result(args.project, stage_id=args.stage, revision=args.revision)
            print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
            return 0
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(f"RALPH 无法合成阶段结果：{exc}", file=sys.stderr)
            return 2
    if args.command == "replay":
        path = _state_path(args.project)
        state = load_state(path)
        events = read_events(path.parent / "loop-events.md")
        replayed = replay_events(create_state(path.parent.name or str(path.parent)), events)
        print(json.dumps({"event_count": len(events), "state": replayed}, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    if args.command == "validate":
        try:
            if args.result:
                result = validate_result_artifact(args.project, args.result, apply=args.apply)
                print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
                return 0
            if args.apply:
                raise ValueError("--apply 必须和 --result 一起使用")
            state = load_state(_state_path(args.project))
            report = validate_plan(state.get("plan", {}), strict=False)
            print(json.dumps({"nodes": report.node_ids, "ready": report.ready, "parallel_groups": report.parallel_groups}, ensure_ascii=False, indent=2))
            return 0
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(json.dumps({"valid": False, "error": str(exc)}, ensure_ascii=False, indent=2), file=sys.stderr)
            return 1
    if args.command == "benchmark-decomposition":
        try:
            report = benchmark_decomposition(
                args.project,
                action_file=args.action_file,
                task=args.task,
                threshold=args.threshold,
            )
            print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
            return 0 if report["passed"] else 1
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(f"RALPH 无法运行分解 benchmark：{exc}", file=sys.stderr)
            return 2
    if args.command == "hook":
        print(
            run_hook(
                args.event,
                sys.stdin.read(),
                args.mode,
                auto_apply=not args.no_auto_apply,
                stop_policy=args.stop_policy,
            )
        )
        return 0
    if args.command == "install-hooks":
        print(install_hooks(args.project, args.mode, stop_policy=args.stop_policy))
        return 0
    if args.command == "start":
        try:
            return start_project(
                args.project,
                args.mode,
                args.launch,
                args.prompt,
                args.effort,
                args.model,
                args.auto_compact_window,
                args.auto_compact_percent,
                stop_policy=args.stop_policy,
            )
        except (OSError, ValueError) as exc:
            _print_project_error(args.project, exc)
            return 2
    if args.command == "resume":
        try:
            return resume_project(
                args.project,
                args.mode,
                args.prompt,
                args.effort,
                args.model,
                args.auto_compact_window,
                args.auto_compact_percent,
                stop_policy=args.stop_policy,
            )
        except (OSError, ValueError) as exc:
            _print_project_error(args.project, exc)
            return 2
    if args.command == "run":
        try:
            return run_project(
                args.project_or_task,
                args.task,
                args.mode,
                args.workspace,
                args.effort,
                args.model,
                args.auto_compact_window,
                args.auto_compact_percent,
                args.dangerously_skip_permissions,
                stop_policy=args.stop_policy,
            )
        except (OSError, ValueError) as exc:
            _print_project_error(args.project_or_task, exc)
            return 2
    if args.command == "loop":
        requested_workflow = args.workflow
        explicit_root = Path(args.project_or_task).expanduser()
        has_field_state = _state_path(explicit_root).exists()
        has_prompt_state = prompt_first_state_path(explicit_root).exists()
        workflow = requested_workflow
        if workflow == "auto":
            # Preserve legacy projects.  A newly named explicit project gets
            # the concise Markdown workflow by default; task-only legacy
            # invocations keep their existing resolver behavior.
            workflow = "field" if has_field_state or args.task is None else "prompt-first"
            if has_prompt_state and not has_field_state:
                workflow = "prompt-first"
        if workflow == "prompt-first":
            try:
                prompt_task = args.task
                if prompt_task is None:
                    if not has_prompt_state:
                        raise ValueError("prompt-first 新项目需要显式任务：ralph loop <project> <task>")
                    prompt_task = load_prompt_first_state(explicit_root)["task"]
                return prompt_first_loop_project(
                    explicit_root,
                    prompt_task,
                    effort=args.effort,
                    model=args.model,
                    max_cycles=args.max_cycles,
                    retry_delay=args.retry_delay,
                    idle_timeout=args.idle_timeout,
                    skip_permissions=args.dangerously_skip_permissions,
                    auto_compact_window=args.auto_compact_window,
                    auto_compact_percent=args.auto_compact_percent,
                )
            except KeyboardInterrupt:
                print("RALPH prompt-first supervisor interrupted by user; stopping.")
                return 130
            except (OSError, ValueError, SupervisorAlreadyRunning) as exc:
                _print_project_error(explicit_root, exc)
                return 2
        # Unexpected exceptions are retried from durable state, while an
        # explicit circuit-breaker result is terminal for this invocation.
        while True:
            try:
                rc = loop_project(
                    args.project_or_task,
                    args.task,
                    args.mode,
                    args.workspace,
                    args.effort,
                    args.model,
                    args.auto_compact_window,
                    args.auto_compact_percent,
                    args.max_cycles,
                    args.retry_delay,
                    args.agent_grace_seconds,
                    args.idle_timeout,
                    args.wait_human,
                    args.dangerously_skip_permissions,
                    max_failed_cycles=args.max_failed_cycles,
                    stop_policy=args.stop_policy,
                )
                if rc == 0:
                    return 0
                print(
                    f"RALPH supervisor stopped with code {rc}; "
                    "persistent state remains resumable."
                )
                return rc
            except KeyboardInterrupt:
                print("RALPH supervisor interrupted by user; stopping.")
                return 130
            except SupervisorAlreadyRunning as exc:
                print(f"RALPH supervisor 未启动：{exc}", file=sys.stderr)
                return 2
            except Exception as exc:  # noqa: BLE001 - supervisor must self-heal
                print(f"RALPH supervisor crashed: {exc!r}; restarting in 10s")
                time.sleep(10)
                continue
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
