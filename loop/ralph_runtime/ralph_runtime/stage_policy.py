"""Pure stage/role/tool policy used by future Hook adapters."""

from __future__ import annotations

from dataclasses import dataclass
import re
import shlex
from typing import Any, Mapping

from .feedback import tool_feedback
from .runtime_config import field_mode_enabled
from .field_tasks import field_task_requires_agent


_COMMANDER_RALPH_COMMANDS = {
    "apply",
    "assemble",
    "events",
    "field-apply",
    "field-init",
    "field-status",
    "graph-apply",
    "prompt",
    "recover-state",
    "render",
    "status",
    "task-next",
    "validate",
    "web-llm-check",
}


def _is_web_llm_check_command(command: str | None) -> bool:
    """Recognise the one external-facing runtime action after CLI validation."""

    return bool(
        command
        and re.search(r"(?:^|\s)(?:[^\s]*/)?ralph\s+web-llm-check(?:\s|$)", str(command))
    )


def _field_gate_active(state: Mapping[str, Any]) -> bool:
    """True when the runtime is in field-centric mode for this project.

    Field mode is the runtime's only normal policy.  Historical card files are
    ignored during state loading and cannot switch a project back to a second
    execution protocol.
    """
    # Historical cards remain auditable but no longer switch execution back to
    # the legacy card-centric policy.
    return field_mode_enabled()


def _is_controlled_ralph_command(command: str | None, role: str) -> bool:
    """Recognise the runtime CLI even when Claude emits an absolute path.

    Claude Code may execute a Bash tool with ``/Users/.../ralph`` or with a
    harmless ``cd <project> && ralph`` prefix.  A literal ``startswith`` check
    treated those equivalent commands as untrusted and blocked the only
    sanctioned field submission step.  Keep the worker narrow: it may invoke
    ``field-apply`` and the auditable ``web-llm-check`` receipt command.
    Commander has an explicit protocol-command allowlist, rather than every
    CLI command: in particular it cannot start nested supervisors with
    ``resume``/``loop`` or self-authorize external browser actions.
    Shell chaining after the CLI is deliberately rejected.
    """
    if not command:
        return False
    text = str(command).strip()
    # Claude Code commonly appends a stderr-only redirect to a status command.
    # It does not alter project data, unlike stdout redirection, so normalize it
    # before the deliberately strict shell-syntax guard below.
    text = re.sub(r"(?:^|\s)2>(?:&1|/dev/null)(?=\s|$)", "", text)
    if any(token in text for token in (";", "|", ">", "<", "\n", "\r")):
        return False
    # Permit the shell wrapper Claude sometimes adds for the project cwd.
    # shlex handles quoted project paths and harmless env/``command`` prefixes
    # more reliably than a regex, while the single-command character check
    # above still rejects shell chaining and redirection.
    text = re.sub(r"^\s*cd\s+(?:'[^']*'|\"[^\"]*\"|[^&]+?)\s*&&\s*", "", text)
    try:
        tokens = shlex.split(text, posix=True)
    except ValueError:
        return False
    while tokens and (
        tokens[0] in {"command", "exec"}
        or re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", tokens[0])
    ):
        tokens.pop(0)
    if not tokens:
        return False
    executable = tokens.pop(0)
    if executable.rsplit("/", 1)[-1] != "ralph":
        return False
    if not tokens:
        return False
    if role == "worker":
        # A graph-node worker has the same narrow ownership model as a field
        # worker, but its durable completion boundary is graph-apply rather
        # than field-apply.
        return tokens[0] in {"field-apply", "graph-apply", "web-llm-check"}
    return tokens[0] in _COMMANDER_RALPH_COMMANDS


def _is_safe_commander_diagnostic(command: str | None) -> bool:
    """Allow a tiny read-only shell surface for Commander orientation.

    Local models commonly use ``cat``/``sed -n`` to inspect the draft returned
    by ``ralph field-status``. Blocking that harmless observation turns a
    recoverable prompt mismatch into repeated Hook feedback. Allow read-only
    inspection of RALPH state/artifacts, but keep arbitrary project files and
    every shell write outside this escape hatch.
    """

    if not command:
        return False
    text = str(command).strip()
    if not text or any(marker in text for marker in ("|", "<", "$", "`", "\n", "\r")):
        return False
    # ``ls path 2>/dev/null; ls other 2>/dev/null`` is the exact harmless
    # shape Claude Code emits while it checks a newly created project.
    text = re.sub(r"(?:^|\s)2>(?:&1|/dev/null)(?=\s|;|$)", "", text)
    if ">" in text:
        return False
    parts = [part.strip() for part in re.split(r"\s*(?:;|&&)\s*", text) if part.strip()]
    if not parts:
        return False
    for part in parts:
        try:
            tokens = shlex.split(part, posix=True)
        except ValueError:
            return False
        if not tokens:
            return False
        executable = tokens[0].rsplit("/", 1)[-1]
        if executable == "ralph":
            if not _is_controlled_ralph_command(part, "commander"):
                return False
            continue
        if executable in {"ls", "pwd", "which"}:
            continue
        if executable in {"cat", "head", "tail"}:
            paths = _readonly_command_paths(executable, tokens[1:])
            if not paths or not all(_is_ralph_readonly_path(path) for path in paths):
                return False
            continue
        if executable == "sed":
            # Only support the common display form: ``sed -n '1,120p' file``.
            # ``-i`` and a general sed program can modify files, so they stay
            # outside the Bash allowance.
            if len(tokens) != 4 or tokens[1] != "-n" or not re.fullmatch(r"[0-9, $p]+", tokens[2]):
                return False
            if not _is_ralph_readonly_path(tokens[3]):
                return False
            continue
        else:
            return False
    return True


def _is_ralph_readonly_path(path: str) -> bool:
    """Keep permissive shell reads inside the active RALPH protocol surface."""

    normalized = str(path).replace("\\", "/").rstrip("/")
    return (
        normalized == "loop-state.json"
        or normalized.endswith("/loop-state.json")
        or normalized == "loop-events.md"
        or normalized.endswith("/loop-events.md")
        or normalized.startswith("loop-artifacts/")
        or "/loop-artifacts/" in normalized
    )


def _readonly_command_paths(executable: str, args: list[str]) -> list[str]:
    """Extract file operands without mistaking ``head -n 40`` for a path."""

    paths: list[str] = []
    index = 0
    while index < len(args):
        token = args[index]
        if token == "--":
            paths.extend(args[index + 1 :])
            break
        if executable in {"head", "tail"} and token in {"-n", "--lines", "-c", "--bytes"}:
            index += 2
            continue
        if token.startswith("-"):
            index += 1
            continue
        paths.append(token)
        index += 1
    return paths


def _is_incremental_stage_file(target_path: str | None, state: Mapping[str, Any]) -> bool:
    """Return whether a Commander write is a bounded draft update.

    The Commander may fill fields over several turns, even while an unrelated
    research field is being dispatched.  It must not edit arbitrary project
    files in that situation; only the current stage's fields/advance drafts
    are part of the state-machine protocol.
    """

    if not target_path:
        return False
    normalized = str(target_path).replace("\\", "/")
    stage = state.get("stage", {}) if isinstance(state.get("stage"), Mapping) else {}
    stage_id = str(stage.get("id", "01"))
    revision = str(stage.get("revision", "r1"))
    marker = f"loop-artifacts/stages/{stage_id}/{revision}/"
    return normalized.endswith("/fields.json") and marker in normalized or (
        normalized.endswith("/advance.json") and marker in normalized
    )


@dataclass(frozen=True)
class ToolDecision:
    decision: str
    reason: str


@dataclass(frozen=True)
class StagePolicy:
    stage_id: str
    commander_tools: tuple[str, ...]
    worker_tools: tuple[str, ...]
    allowed_actions: tuple[str, ...]
    read_only: bool = False


DEFAULT_STAGE_POLICIES = {
    # 01/02/04/05/06 allow bounded Agent work and incremental field writes;
    # loop-state.json remains protected by the dedicated target-path guard.
    "01": StagePolicy("01", ("Agent", "Skill", "ToolSearch", "Read", "Glob", "Grep", "Bash", "Write", "Edit"), ("Read", "Glob", "Grep", "Bash", "Write", "Edit"), ("advance", "rollback", "clarify", "blocked_human", "explore")),
    # Field research workers need their own web/search tools.  The previous
    # card-era policy omitted them, so a correctly dispatched field Agent was
    # repeatedly denied at the tool layer and could never produce evidence.
    "02": StagePolicy("02", ("Agent", "Skill", "ToolSearch", "Read", "Glob", "Grep", "Bash", "WebSearch", "WebFetch", "Write", "Edit"), ("Read", "Glob", "Grep", "ToolSearch", "Bash", "WebSearch", "WebFetch", "Write", "Edit"), ("advance", "rollback", "blocked_human", "candidate", "explore")),
    # Cross-validation stages: the Commander dispatches per-field subagents that
    # consult various web LLMs + authoritative sources, and may also research
    # directly.  Web tools are required here.
    "02.5": StagePolicy("02.5", ("Agent", "Skill", "ToolSearch", "Read", "Glob", "Grep", "Bash", "WebSearch", "WebFetch", "Write", "Edit"), ("Read", "Glob", "Grep", "WebSearch", "WebFetch", "Write", "Edit"), ("advance", "rollback", "blocked_human", "explore")),
    "04.5": StagePolicy("04.5", ("Agent", "Skill", "ToolSearch", "Read", "Glob", "Grep", "Bash", "WebSearch", "WebFetch", "Write", "Edit"), ("Read", "Glob", "Grep", "WebSearch", "WebFetch", "Write", "Edit"), ("advance", "rollback", "blocked_human", "explore")),
    # Broad discovery belongs only to execution.  It remains evidence
    # acquisition, not a substitute for the later verification stage.
    "03": StagePolicy("03", ("Agent", "ToolSearch", "Read", "Glob", "Grep", "Bash", "Skill", "WebSearch", "WebFetch"), ("Read", "Glob", "Grep", "Bash", "Write", "Edit", "Skill", "WebSearch", "WebFetch"), ("advance", "rollback", "blocked_human", "dispatch", "join")),
    "04": StagePolicy("04", ("Agent", "Skill", "ToolSearch", "Read", "Glob", "Grep", "Bash", "WebSearch", "WebFetch", "Write", "Edit"), ("Read", "Glob", "Grep", "Bash", "WebSearch", "WebFetch", "Write", "Edit"), ("advance", "rollback", "blocked_human", "explore")),
    "05": StagePolicy("05", ("Agent", "Skill", "ToolSearch", "Read", "Glob", "Grep", "Bash", "Write", "Edit"), ("Read", "Glob", "Grep", "Write", "Edit"), ("advance", "rollback", "blocked_human", "explore")),
    "06": StagePolicy("06", ("Agent", "Skill", "ToolSearch", "Read", "Glob", "Grep", "Bash", "Write", "Edit"), ("Read", "Glob", "Grep", "Write", "Edit"), ("advance", "rollback", "blocked_human", "explore")),
    # Exploration is read-only for *project/business* outputs, but its
    # required preference/candidate fields still use the same incremental
    # task JSON -> field-apply path as every other stage.
    "exploration": StagePolicy("exploration", ("Agent", "Skill", "ToolSearch", "Read", "Glob", "Grep", "Bash"), ("Read", "Glob", "Grep", "Bash", "Write", "Edit"), ("advance", "candidate", "blocked_human", "explore"), read_only=False),
}


def decide_tool(
    state: Mapping[str, Any],
    role: str,
    tool_name: str,
    *,
    target_path: str | None = None,
    command: str | None = None,
) -> ToolDecision:
    stage_id = str(state.get("stage", {}).get("id", "01"))
    policy = DEFAULT_STAGE_POLICIES.get(stage_id)
    if policy is None:
        return ToolDecision(
            "deny",
            tool_feedback(
                "STAGE_POLICY_MISSING",
                detected=f"当前阶段 `{stage_id}` 没有可执行的工具策略。",
                correction="不要继续试探工具权限，也不要修改状态。",
                next_action="停止当前会话并报告运行时配置缺失。",
                forbidden="绕过 Hook、直接修改 loop-state.json 或自行创建阶段策略。",
            ),
        )
    if state.get("status") in {"completed", "stopped"}:
        return ToolDecision("deny", f"state is {state['status']}")
    if state.get("status") == "blocked_human":
        return ToolDecision(
            "deny",
            tool_feedback(
                "HUMAN_BLOCK_ACTIVE",
                detected="当前阶段已经由状态机标记为 blocked_human，等待人类回答。",
                correction="停止当前工具调用；人类输入会由 UserPromptSubmit 写回并重新打开阶段。",
                next_action="结束当前会话，等待人类回答后再用 `ralph resume <项目路径>`。",
                forbidden="继续 Read/Agent/AskUserQuestion、重派任务或自行执行探索。",
            ),
        )
    if tool_name in {"Write", "Edit"} and target_path and target_path.endswith("loop-state.json"):
        # This is a runtime-owned file for every role.  Workers use their
        # task JSON plus `field-apply`; they never need to mutate the state
        # document directly.
        return ToolDecision(
            "deny",
            tool_feedback(
                "STATE_FILE_PROTECTED_FIELD",
                detected=f"{role} 尝试直接修改 loop-state.json。",
                correction="把增量写入当前阶段 task/fields JSON，再运行 `ralph field-apply`；阶段推进使用 `ralph apply`。",
                next_action="停止当前 Write/Edit，改写受控字段文件并运行校验命令。",
                forbidden="任何角色直接 Write/Edit/cat/echo 修改 loop-state.json。",
            ),
        )
    allowed = policy.commander_tools if role == "commander" else policy.worker_tools
    if role == "commander" and tool_name in {"Write", "Edit"}:
        # Commander is NEVER allowed to write loop-state.json directly.  A full
        # hand-rewrite of the file is what repeatedly produced invalid JSON and
        # killed the loop.  The only sanctioned write path is the runtime: the
        # Commander emits a small delta file and runs `ralph field-apply` (which
        # validates + merges atomically), or advances via the
        # <RALPH_STAGE_RESULT> action.  Other project files (open-questions.md,
        # etc.) stay writable.
        if target_path and target_path.endswith("loop-state.json"):
            return ToolDecision(
                "deny",
                tool_feedback(
                    "STATE_FILE_PROTECTED",
                    detected="工具目标是 loop-state.json。",
                    correction="禁止直接 Write/Edit loop-state.json。字段更新：把改动写成小增量 JSON，运行 "
                    "`ralph field-apply <项目> <字段文件>`（校验通过才原子落盘）。阶段推进用 "
                    "`<RALPH_STAGE_RESULT> advance` 或 `ralph apply`。",
                    next_action="不要改文件，改用字段校验命令。需要重置时运行 `ralph recover-state <项目>`。",
                    forbidden="Write/Edit/cat/echo 修改 loop-state.json。",
                ),
            )
        return ToolDecision("allow", "Commander may write non-state files directly")
    # Field-centric mode: the Commander drives a field table, not a deck of
    # enforced task cards.  The env guard is authoritative, but we also refuse to
    # force-dispatch any orphaned cards so a freshly-migrated project does not
    # deadlock on stale enforce artifacts.
    if _field_gate_active(state):
        # loop-state.json stays write-protected even in field mode: the matrix is
        # committed atomically via the <RALPH_STAGE_RESULT> action, never via Edit.
        if tool_name in {"Write", "Edit"} and target_path and target_path.endswith("loop-state.json"):
            return ToolDecision(
                "deny",
                tool_feedback(
                    "STATE_FILE_PROTECTED_FIELD",
                    detected="工具目标是 loop-state.json。",
                    correction="字段只能由结构化动作经过 runtime 原子写入（输出 <RALPH_STAGE_RESULT> advance，payload.task_spec.attribute_matrix 即新字段表）。",
                    next_action="返回结构化动作，不要直接改文件。",
                    forbidden="Write/Edit/cat/echo 修改 loop-state.json。",
                ),
            )
        if tool_name == "AskUserQuestion":
            return ToolDecision(
                "deny",
                tool_feedback(
                    "ASK_USER_FIELD_GATE",
                    detected=f"{tool_name} 不属于字段中心模式的直接交互工具；框架禁止 Commander 向人类提问。",
                    correction="通用偏好一律采用 soul（AGENTS.md）「默认决策画像」（disposition=assume/assumed_default）；"
                    "未知事实派单字段调研 subagent 带回 evidence_refs；真正需要人类拍板的事项写入 loop-artifacts/open-questions.md。",
                    next_action="把该因素作为字段写入 task_spec.attribute_matrix，或派 Agent 只填这一个 research_required 字段。",
                    forbidden="用 AskUserQuestion 把可推断字段包装成选择题，或绕过阶段契约直接弹出问题。",
                ),
            )
        # Runtime commands are the safe escape hatch from prompt ordering.
        # They must be allowed before the "dispatch research first" hint:
        # otherwise a Commander cannot submit an incremental draft while a
        # sibling research field is running.
        if tool_name == "Bash" and command and _is_controlled_ralph_command(command, role):
            if _is_web_llm_check_command(command) and stage_id not in {"02", "02.5", "04.5"}:
                return ToolDecision(
                    "deny",
                    tool_feedback(
                        "WEB_LLM_STAGE_SCOPE",
                        detected=f"当前阶段是 {stage_id}，却尝试运行网页 LLM 交叉核验。",
                        correction="网页 LLM 仅可用于 02 的受控来源线索恢复，或 02.5 / 04.5 的对抗性核验；先完成当前阶段字段。",
                        next_action="02 中只能用自己的任务 JSON 询问可复核来源线索，随后仍须用具体权威页面验证；其他阶段进入 02.5 或 04.5 后再运行 web-llm-check。",
                        forbidden="在目标澄清、执行或 exploration 阶段发送网页 LLM 问题，或把 LLM 回复当作一手事实来源。",
                    ),
                )
            return ToolDecision("allow", "controlled ralph runtime command")
        if role == "commander" and tool_name == "Bash" and _is_safe_commander_diagnostic(command):
            return ToolDecision("allow", "safe read-only commander diagnostic")
        if role == "commander" and tool_name in {"Write", "Edit"} and _is_incremental_stage_file(target_path, state):
            return ToolDecision("allow", "incremental current-stage draft")
        if role == "commander" and tool_name not in {"Agent", "Write", "Edit"}:
            ready_research = [
                item for item in (state.get("field_tasks") or [])
                if isinstance(item, Mapping)
                and item.get("status") in {"ready", "pending"}
                and field_task_requires_agent(item)
            ]
            if ready_research:
                first = ready_research[0]
                return ToolDecision(
                    "deny",
                    tool_feedback(
                        "FIELD_DISPATCH_FIRST",
                        detected=f"当前阶段还有 {len(ready_research)} 个字段任务未派发。",
                        correction="字段任务必须一字段一 Agent；主 Agent 不读取大文件、不先做总报告。",
                        next_action=(
                            f"下一次工具调用必须是 Agent；prompt 第一行写 "
                            f"`RALPH_FIELD_TASK={first.get('path', '<task-file>')}`，"
                            "子代理完成后直接写任务文件并运行 `ralph field-apply`。"
                        ),
                        forbidden="先用 Read/Bash/网页搜索合并多个字段，或等待一个总报告。",
                    ),
                )
        if tool_name == "Bash" and command and not _is_controlled_ralph_command(command, role):
            ready_research = [
                item for item in (state.get("field_tasks") or [])
                if isinstance(item, Mapping)
                and item.get("status") in {"ready", "pending"}
                and field_task_requires_agent(item)
            ]
            if role == "worker":
                next_action = (
                    "字段 worker 不要用 Bash 读取或写入普通项目文件；只执行自己的受控命令："
                    "`ralph field-apply . <自己的任务文件>`；已配置网页 LLM 时可运行 "
                    "`ralph web-llm-check . <自己的任务文件>`。"
                )
                feedback_code = "WORKER_BASH_SCOPE_FIELD"
                detected = "字段 worker 试图用 Bash 执行未受控的文件读写命令。"
            elif ready_research:
                first = ready_research[0]
                next_action = (
                    "下一次工具调用必须是 Agent；prompt 第一行必须写 "
                    f"`RALPH_FIELD_TASK={first.get('path', '<task-file>')}`，"
                    "只处理这一个字段并运行 `ralph field-apply`。不要再次调用 Bash、Read 或 Grep。"
                )
                feedback_code = "COMMANDER_BASH_SCOPE_FIELD"
                detected = "Commander 试图用 Bash 直接读取或写入项目文件。"
            else:
                next_action = (
                    "当前只有 pending/assumed_default 结构字段：用 Write/Edit 填写当前阶段 fields.json，"
                    "再运行 `ralph field-apply . <fields.json>`；不要派 Agent。也可使用 "
                    "`ralph status/field-status/events/render/field-init/validate/apply`，"
                    "只读 `cat/head/tail/sed -n` RALPH 工件可以；不要用 Bash 写入或绕过 field-apply。"
                )
                feedback_code = "COMMANDER_BASH_SCOPE_FIELD"
                detected = "Commander 试图用 Bash 直接读取或写入项目文件。"
            return ToolDecision(
                "deny",
                tool_feedback(
                    feedback_code,
                    detected=detected,
                    correction="字段流程只允许用受控 `ralph` 命令；字段草稿由 Write/Edit 写入阶段目录，"
                    "再用 `ralph field-apply` 校验合并。",
                    next_action=next_action,
                    forbidden="Bash 直接写 loop-state.json、工件文件或批量复制上下文。",
                ),
            )
        # Field-centric research: external facts (latest GPU, price quotes) are
        # filled by narrow single-field subagents, but the Commander may also use
        # web research directly when the field context is small.  Both are allowed.
        if tool_name in allowed or tool_name in {"WebSearch", "WebFetch"}:
            return ToolDecision("allow", "tool allowed in field-centric mode")
        return ToolDecision(
            "deny",
            tool_feedback(
                "TOOL_STAGE_SCOPE_FIELD",
                detected=f"{tool_name} 不允许由 {role} 在阶段 `{stage_id}`（字段中心模式）使用。",
                correction="遵守当前阶段的工具白名单；字段中心模式下 Commander 直接维护字段表，不强制卡片。",
                next_action="选择阶段允许的工具，或直接输出 <RALPH_STAGE_RESULT> advance。",
                forbidden="试探其他工具、把工具调用改写成 Bash，或修改状态文件。",
            ),
        )
    # The branch above is the only execution policy.  Keeping a second
    # card-centric fallback here used to make stale task-card files appear to
    # control a migrated project.  Field mode is unconditional, so reaching
    # this line indicates a programming error rather than a recoverable policy
    # decision.
    return ToolDecision(
        "deny",
        tool_feedback(
            "FIELD_POLICY_INTERNAL",
            detected="字段中心 Hook 未能解析当前工具策略。",
            correction="不要绕过 Hook 或修改状态文件；使用受控 ralph 命令并报告运行时错误。",
            next_action="运行 `ralph status .`，必要时使用 `ralph resume .` 从持久化状态恢复。",
            forbidden="回退到旧任务卡、直接修改 loop-state.json 或用 Bash 伪造状态。",
        ),
    )
