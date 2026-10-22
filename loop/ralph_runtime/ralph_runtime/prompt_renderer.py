"""Bounded, field-centric prompts for the RALPH runtime."""

from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from .feedback import protocol_feedback
from .nodes import DEFAULT_GRAPH
from .runtime_config import flow_only_mode, max_parallel_fields
from .field_tasks import field_task_requires_agent


SOUL_PATH = Path(os.environ.get("RALPH_SOUL_PATH", "/Users/a1-6/Desktop/workspace/AGENTS.md"))
_LOOP_1_DIR = Path(__file__).resolve().parents[2] / "1-loop" / "loop-legacy"
STAGE_PROMPT_FILES = {
    "00": "00-综述.md",
    "01": "01-目标与背景分解.md",
    "02": "02-未知信息调研.md",
    "02.5": "02.5-交叉验证.md",
    "03": "03-执行任务分解.md",
    "04": "04-验证与交叉验证.md",
    "04.5": "04.5-交叉验证.md",
    "exploration": "exploration.md",
}


@dataclass(frozen=True)
class RenderedPrompt:
    text: str
    sha256: str


def _read_soul_defaults() -> str:
    try:
        text = SOUL_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""
    marker = "## 默认决策画像"
    start = text.find(marker)
    if start < 0:
        return ""
    rest = text[start + len(marker):]
    end = rest.find("\n## ")
    return rest[:end if end >= 0 else None].strip()


def _soul_defaults_bullets() -> list[str]:
    block = _read_soul_defaults()
    if not block:
        return []
    return ["   soul 默认决策画像（通用默认，缺偏好时直接套用）："] + [
        f"   {line.rstrip()}" for line in block.splitlines() if line.strip()
    ]


def _read_stage_prompt_file(stage_id: str) -> str:
    """Read the full 1-loop legacy stage prompt file without truncation.

    The repository keeps the original loop documents as research history,
    but their old card-centric instructions must not be copied into a live
    model prompt.  Keep the methodology and examples, remove only obsolete
    dispatch/receipt lines, and normalize their artifact references.
    Also remove validation/check requirements (e.g. "检查", "必须遵守")
    that are enforced by the runtime, not by the prompt.
    """
    filename = STAGE_PROMPT_FILES.get(str(stage_id))
    if not filename:
        return ""
    path = _LOOP_1_DIR / filename
    try:
        text = path.read_text(encoding="utf-8").strip()
    except OSError:
        return ""
    # Remove obsolete card-centric markers that are not relevant to field-based execution.
    legacy_markers = (
        "任务卡", "task card", "builder 卡", "auditor 卡", "requirements-auditor",
        "dag-auditor", "execution-join-auditor", "RALPH_TASK_CARD",
    )
    # Remove validation/check requirements that are enforced by the runtime, not by the prompt.
    validation_markers = (
        "## 检查",
        "## 必须遵守",
        "## 分支",
        "## 交付",
    )
    # Filter out validation sections entirely (they are runtime-enforced).
    lines = text.splitlines()
    filtered_lines = []
    skip_section = False
    for line in lines:
        # Check if we're entering a section to skip
        if any(line.strip().startswith(marker) for marker in validation_markers):
            skip_section = True
            continue
        if skip_section:
            # Skip lines until we hit a new top-level section (##) or end of file
            if line.strip().startswith("## "):
                skip_section = False
                filtered_lines.append(line)
            continue
        # Also filter legacy markers
        if not any(marker in line for marker in legacy_markers):
            filtered_lines.append(line)
    text = "\n".join(filtered_lines)
    # Normalize old artifact references to the new field-based paths.
    text = re.sub(
        r"(?:loop-artifacts/)?([0-9]+(?:\.[0-9]+)?)-r([0-9]+)\.(json|md)",
        r"loop-artifacts/stages/\1/r\2/fields.\3",
        text,
    )
    return text


def resolve_template_path() -> Path:
    """Return the field template; the old generic card template is ignored."""

    template_dir = Path(__file__).with_name("templates")
    override = os.environ.get("RALPH_PROMPT_TEMPLATE", "stage_prompt_fieldcentric.md")
    candidate = Path(override)
    if not candidate.is_absolute():
        candidate = template_dir / candidate
    if candidate.name in {"stage_prompt.md", "stage_prompt_cards.md"}:
        return template_dir / "stage_prompt_fieldcentric.md"
    return candidate


class PromptRenderer:
    """Render only bounded state + field instructions, never task-card state."""

    @staticmethod
    def _short_text(value: Any, limit: int) -> str:
        text = str(value or "").replace("\x00", " ").strip()
        if len(text) <= limit:
            return text
        return text[: max(1, limit - 80)] + "\n[… 已截断，完整内容以项目文件为准 …]"

    @staticmethod
    def _candidate_action(raw_output: str | None) -> str | None:
        if not raw_output:
            return None
        match = re.search(r'["\']action["\']\s*:\s*["\']([A-Za-z_]+)["\']', raw_output)
        if not match:
            return None
        action = match.group(1)
        return action if action in {
            "advance", "rollback", "blocked_human", "skip_blocked", "candidate",
            "explore", "dispatch", "join", "clarify", "repair_prompt",
        } else None

    @staticmethod
    def _semantic_action_conflict(error: str) -> bool:
        lowered = str(error or "").lower()
        return any(marker in lowered for marker in (
            "blocking_findings", "rollback or blocked_human", "requires state.status",
            "does not match current stage", "can advance only", "must enter exploration",
            "cannot be executed", "not allowed for",
        ))

    def _field_recovery_prompt(
        self,
        state: Mapping[str, Any],
        *,
        reason: str = "",
        error_kind: str = "continuation",
        compact: bool = False,
    ) -> RenderedPrompt:
        stage = state.get("stage", {}) if isinstance(state.get("stage"), Mapping) else {}
        task = state.get("task", {}) if isinstance(state.get("task"), Mapping) else {}
        stage_id = str(stage.get("id", "01"))
        revision = str(stage.get("revision", "r1"))
        stage_name = str(stage.get("name", ""))
        description = self._short_text(task.get("description", ""), 700)
        success = self._short_text(stage.get("success_condition", ""), 260)
        outputs = [str(item) for item in stage.get("required_outputs", []) if str(item).strip()]
        field_tasks = state.get("field_tasks", []) if isinstance(state.get("field_tasks"), list) else []
        graph_tasks = state.get("graph_tasks", []) if isinstance(state.get("graph_tasks"), list) else []

        spec = state.get("task_spec", {}) if isinstance(state.get("task_spec"), Mapping) else {}
        matrix = spec.get("attribute_matrix", []) if isinstance(spec, Mapping) else []
        missing: list[str] = []
        present: set[str] = set()
        if isinstance(matrix, list):
            for index, field in enumerate(matrix):
                if not isinstance(field, Mapping):
                    continue
                for key in ("concept", "role", "attribute"):
                    value = field.get(key)
                    if isinstance(value, str) and value.strip():
                        present.add(value.strip())
                if field.get("disposition") in (None, "", "pending"):
                    missing.append(str(field.get("concept") or field.get("attribute") or f"#{index}"))
        missing.extend(output for output in outputs if output not in present)
        missing_line = "；".join(dict.fromkeys(missing)) if missing else "（当前无缺失字段，可准备推进）"

        stage_dir = f"loop-artifacts/stages/{stage_id}/{revision}"
        fields_file = f"{stage_dir}/fields.json"
        advance_file = f"{stage_dir}/advance.json"
        next_stage = str(stage.get("on_success") or "")
        ready_tasks = [
            item for item in field_tasks
            if isinstance(item, Mapping) and str(item.get("status", "")) in {"ready", "pending"}
        ]
        agent_ready_tasks = [task for task in ready_tasks if field_task_requires_agent(task)]
        urgent_task = agent_ready_tasks[0] if agent_ready_tasks else None
        advance_json = json.dumps({
            "action": "advance",
            "status": "passed",
            "stage_id": stage_id,
            "revision": revision,
            "next_stage": next_stage,
            "evidence": [f"{stage_dir}/fields.md"],
            "message": f"完成 {stage_name}，推进到 {next_stage}",
        }, ensure_ascii=False, indent=2)

        authoritative_inputs = spec.get("authoritative_inputs", []) if isinstance(spec, Mapping) else []
        canonical_description = str(task.get("description", "")).strip()
        recent_human_inputs = [
            str(item.get("text", "")).strip()
            for item in authoritative_inputs
            if isinstance(item, Mapping)
            and str(item.get("kind", "")) == "human_input"
            and str(item.get("text", "")).strip()
            and str(item.get("text", "")).strip() != canonical_description
        ][-2:]

        # A fresh local-model context must make its first tool call quickly.
        # The durable stage document and CLAUDE.md remain available on disk;
        # replaying the full stage manual before the first action causes an
        # expensive prefill and invites a plan-only response.  Give one safe,
        # idempotent command and the narrow state delta instead.
        if compact:
            next_action = (
                f"下一次工具调用只执行 `ralph field-init .`。该命令不会覆盖已有草稿；"
                f"完成后只修改 `{fields_file}` 并运行 `ralph field-apply . {fields_file}`。"
            )
            if urgent_task is not None:
                urgent_path = str(urgent_task.get("path", ""))
                urgent_concept = str(urgent_task.get("concept", ""))
                next_action = (
                    f"下一次工具调用必须是 Agent，第一行写 `RALPH_FIELD_TASK={urgent_path}`，"
                    f"且只处理 `{urgent_concept}`；不要先读日志、Grep、Glob 或写总报告。"
                )
            compact_lines = [
                f"# RALPH 最小恢复（{stage_id}-{revision} · {stage_name}）",
                f"当前任务：{self._short_text(task.get('description', ''), 420) or '以项目文件为准'}",
                "",
                "若项目存在 `.claude/skills/ralph-stage-executor/SKILL.md`，先调用 `/ralph-stage-executor`；"
                "但以本轮 `ralph` 校验结果为准。",
                "",
                "## 立即动作（不要先总结、规划或重读历史）",
                next_action,
                "",
                f"成功条件：{success or '以节点定义为准'}",
                f"仍需填写：{missing_line}",
                "不要直接修改 `loop-state.json`；普通缺失不能伪装成 blocked_human。",
            ]
            if stage_id in {"02.5", "04.5"}:
                compact_lines.append(
                    "网页 LLM 只有 `ralph web-llm-check` 产生且含两个成功 provider 的回执才可计入；"
                    "项目获人类浏览器授权时，该命令由本地 Agent 用受控 Playwright 实际输入并提交问题；"
                    "LLM 回答不替代两个独立权威来源。"
                )
            if recent_human_inputs:
                compact_lines.extend([
                    "",
                    "## 最近人类补充（先判断是否与当前任务一致；不一致时保留为待整合输入，不要覆盖当前字段）",
                    *[f"- {self._short_text(item, 500)}" for item in recent_human_inputs],
                ])
            if reason:
                compact_lines.extend(["", f"上一轮诊断：{self._short_text(reason, 420)}"])
            text = "\n".join(compact_lines).rstrip() + "\n"
            return RenderedPrompt(text=text, sha256=hashlib.sha256(text.encode("utf-8")).hexdigest())

        lines = [
            f"# RALPH 字段增量提示（{stage_id}-{revision} · {stage_name}）",
            f"当前任务：{description or '以 loop-state.json 为准'}",
            "",
            "若项目存在 `.claude/skills/ralph-stage-executor/SKILL.md`，先调用 `/ralph-stage-executor`；"
            "但以本轮 `ralph` 校验结果为准。",
            "",
        ]
        if flow_only_mode(state):
            lines.extend([
                "## 当前运行模式：flow-only（只验证流程，不做真实网页研究）",
                "本轮仍必须执行字段任务的完整机械链路：一字段一 Agent → Read 一个任务文件 → Write/Edit 同一文件的 field → `ralph field-apply`。",
                "禁止 WebSearch/WebFetch、curl、python 搜索和伪造 evidence_refs；字段可以使用 `disposition=inferred`，在 rationale 标明‘仅用于流程验证’，evidence_refs 保持空数组。",
                "这不是等待人类确认，也不是 research 阻塞；完成字段后继续派发下一个 ready 字段。",
                "",
            ])
        if urgent_task is not None:
            urgent_path = str(urgent_task.get("path", ""))
            urgent_concept = str(urgent_task.get("concept", ""))
            lines.extend([
                "## 现在只做这一件事（最高优先级）",
                f"下一次工具调用必须是 Agent，且只处理字段 `{urgent_concept}`。",
                f"Agent prompt 第一行必须是 `RALPH_FIELD_TASK={urgent_path}`；不要先 Read、Grep、Glob、Bash 或构造总报告。",
                f"子代理读取 `{urgent_path}` 后立即 Write/Edit 同一文件的 `field`，再运行 `ralph field-apply . {urgent_path}`；完成后结束。",
                "不要向人类提问，不要一次派多个字段，不要直接修改 loop-state.json。",
                "",
                "## 当前批次硬顺序",
                "ready 字段必须逐字段派发；当前字段完成或被恢复后，再处理下一个字段。",
            ])
        else:
            lines.extend([
                "## 当前批次硬顺序（必须先执行）",
                "按当前阶段文件增量填写；不要先读取完整事件日志或构造总报告。",
            ])
        lines.extend([
            "",
            "## 当前阶段方法论",
            # The full 1-loop legacy stage document is now injected without truncation.
            # The agent can read the complete methodology; the durable specification
            # remains on disk at the original path for reference.
            _read_stage_prompt_file(stage_id),
            "",
            f"## 阶段成功条件（runtime 校验）\n{success or '以节点定义为准'}",
            f"应交付字段角色：{'、'.join(outputs) or '按当前任务补充'}",
            f"仍需填写：{missing_line}",
            "",
            "## 固定增量流程",
            f"0. 只有 disposition=research_required 的字段必须逐字段派 Agent；pending/assumed_default 的结构化字段由 Commander 自己增量填写。不要先读取完整事件日志或逐个 cat 任务文件。"
            f"本地默认最多同时运行 {max_parallel_fields()} 个字段 Agent；先派这一批，收到回执并 field-apply 后再派下一批。DAG 的 parallel_group 仍保留，不等于无限并发。",
            "1. 若文件不存在，运行 `ralph field-init .`。",
            f"2. 只修改 `{fields_file}`，可多轮填写；同一 `concept` 更新，其他已通过字段保留。",
            f"3. 每次填写后运行 `ralph field-apply . {fields_file}`；只修复命令列出的 JSON/字段问题。",
            "4. 不要直接 Write/Edit `loop-state.json`；不要把普通缺失误报为 blocked_human。",
            "5. research_required 字段应尽可能带 evidence_refs 和 observed_at；搜索或浏览器失败时保持 research_required/uncertain，禁止写成\u201c已验证\u201d。evidence_refs 是软提示，不是硬性阻塞条件。",
            "6. 02.5/04.5 要逐 claim 填 validation_records（两个独立来源、observed_at、verdict）；已配置网页 LLM 时必须引用成功回执。"
            "03 必须提交 role=task_graph 的结构化 DAG，并让每个节点真实写出 node.writes 文件后 graph-apply。",
            "7. 字段和 required_outputs 都完成后写入下面的 advance.json，再运行 `ralph apply`。",
            "",
            f"## advance.json 示例：`{advance_file}`",
            "```json",
            advance_json,
            "```",
            f"运行：`ralph apply . {advance_file}`",
            "",
            "## Hook 规则",
            "普通缺失是软提示，不会因为增量填写而卡死；直接修改状态文件、危险副作用、越界路径和活动人类阻塞仍会硬拒绝。",
            "对 research_required 字段，Agent 是当前阶段的逐字段执行方式；必须一字段一派发，不需要预先批准。"
            "对 pending/assumed_default 字段可由 Commander 自己增量填写。",
            # Web-LLM cross-verification skill is available for stages 02.5 and 04.5.
            # The skill file is at ~/.hermes/skills/web-llm-cross-verify/SKILL.md and
            # contains the complete address list, CSS selectors, and operation flow.
            # Claude Code agents can load it via the skill mechanism or read it directly.
            "网页 LLM 交叉验证 Skill: `~/.hermes/skills/web-llm-cross-verify/SKILL.md` 包含完整地址清单、CSS 选择器、操作流程。02.5/04.5 阶段必须引用此 skill。",
            # Default preferences are already available through the project
            # instructions.  Do not duplicate the full block in every live
            # recovery prompt; this is a major source of needless context.
            *([] if compact else ["使用项目 AGENTS.md 中的默认决策画像；缺少明确偏好时直接采用，不向人类重复追问。"]),
        ])
        if stage_id == "exploration":
            lines.extend([
                "",
                "## 探索尾节点规则（不是普通任务，也不是终止）",
                "先运行 `ralph task-next .` 检查 tasks/TASKS.md 中是否有 ready/pending 任务；人类阻塞项直接跳过，不等待人类。",
                "探索字段仍按 fields.json → `ralph field-apply` 增量填写；preference_brief 必须返回用户偏好、缺口和下一轮分解方向。",
                "候选任务必须包含研究摘要、理由、范围，并显式标记 `status=candidate`。候选只能写入 queue，不得静默执行。",
                "如果本轮只有候选而没有已选 ready 任务，提交 `candidate` 动作，不要提交带 candidate selected_task 的 `advance`；下一轮由主 Agent 分析偏好后再分解。",
                "只有从 tasks/TASKS.md 选定 ready/pending 任务时，才在 `payload.exploration.selected_task` 写完整来源和理由，并用 `selection_mode=task_board` 的 `advance` 返回 01。",
            ])
        if field_tasks:
            ready_tasks = [
                task for task in field_tasks
                if isinstance(task, Mapping) and str(task.get("status", "")) in {"ready", "pending"}
            ]
            active_tasks = [
                task for task in field_tasks
                if isinstance(task, Mapping) and str(task.get("status", "")) in {"dispatching", "dispatched"}
            ]
            deferred_tasks = [
                task for task in field_tasks
                if isinstance(task, Mapping) and str(task.get("status", "")) == "deferred"
            ]
            batch = [task for task in ready_tasks if field_task_requires_agent(task)][:max_parallel_fields()]
            commander_tasks = [task for task in ready_tasks if not field_task_requires_agent(task)]
            lines.extend([
                "",
                "## 当前阶段的独立字段子任务",
                (
                    f"当前共有 {len(field_tasks)} 个字段任务；本轮只处理最多 {max_parallel_fields()} 个 ready 字段。"
                    "不要读取全部任务文件，也不要先构造总报告；完成当前批次后由下一轮提示给出下一批。"
                ),
            ])
            for task in batch:
                if not isinstance(task, Mapping):
                    continue
                task_path = str(task.get("path", ""))
                concept = str(task.get("concept", ""))
                if field_task_requires_agent(task):
                    lines.append(
                        f"- `{task.get('id', '')}`：字段 `{concept}`；任务文件 `{task_path}`。"
                        f"立即调用 Agent（不要先 Read 该文件），prompt 第一行写 `RALPH_FIELD_TASK={task_path}`；"
                        "由子代理读取并把结果写入该任务文件的 field 对象，再运行 `ralph field-apply . <文件>`；"
                        "若无法写文件，才把同一个单字段 JSON 返回给主 Agent。"
                    )
            if commander_tasks:
                lines.append(
                    f"本阶段另有 {len(commander_tasks)} 个 pending/assumed_default 结构字段，"
                    f"Commander 可直接增量填写 `{fields_file}` 并运行 `ralph field-apply`；不要因它们为空而派 research Agent。"
                )
            if active_tasks:
                lines.append(
                    "正在运行的字段任务（不要重复派发）："
                    + "；".join(
                        f"{task.get('concept')}[{task.get('status')}]"
                        for task in active_tasks[:max_parallel_fields()]
                    )
                )
            if len([task for task in ready_tasks if field_task_requires_agent(task)]) > len(batch):
                lines.append(
                    f"其余 {len([task for task in ready_tasks if field_task_requires_agent(task)]) - len(batch)} 个 research_required 字段留到当前批次完成后再派发。"
                )
            if deferred_tasks:
                lines.append(
                    f"另有 {len(deferred_tasks)} 个字段已保存不完整草稿，等待下一次 supervisor 上下文重新开放；"
                    "本轮不要伪造 advance。"
                )
            lines.append(
                "每个字段可多轮填写；field-apply 只合并当前 concept，保留其他已通过字段。"
            )
        if graph_tasks:
            lines.extend([
                "",
                "## 当前执行 DAG 节点",
                "任务图已经由 runtime 校验；不要手改 plan 或 loop-state.json。只按依赖顺序派发 ready 节点，",
                "parallel_group 内节点必须使用不同 orthogonal_key 和 writes；Join 节点必须等待所有依赖。",
            ])
            for task in graph_tasks:
                if not isinstance(task, Mapping):
                    continue
                lines.append(
                    f"- `{task.get('id', '')}` 节点 `{task.get('node_id', '')}`：status={task.get('status', '')}；"
                    f"depends_on={task.get('depends_on', [])}；任务文件 `{task.get('path', '')}`。"
                )
            lines.append("每个节点先写出它 node.writes 声明的实际非空文件，再增量填写自己的节点 JSON 并运行 `ralph graph-apply . <节点文件>`；runtime 校验依赖和交付文件并更新 ready/blocked/Join，再由 Commander 提交 advance。")
        if error_kind in {"memory_guard", "connection", "timeout", "api_error", "runtime"}:
            lines.extend([
                "",
                "这是模型/基础设施中断，不是阶段失败。不要重复读取完整 loop-events.md；保存当前草稿后用 `ralph resume .` 开短上下文。",
            ])
        if compact:
            lines.extend([
                "",
                "这是一个新的 Commander 上下文；以 loop-state.json 和字段任务文件为唯一事实。",
                "不要复述旧 transcript，不要输出 READY 或总报告；执行上面的下一步命令。",
            ])
        if reason:
            lines.extend(["", f"上一轮诊断（只修复此项）：{self._short_text(reason, 900)}"])
        text = "\n".join(lines).rstrip() + "\n"
        return RenderedPrompt(text=text, sha256=hashlib.sha256(text.encode("utf-8")).hexdigest())

    def render(self, state: Mapping[str, Any]) -> RenderedPrompt:
        return self._field_recovery_prompt(state)

    def compact_recovery_prompt(
        self,
        state: Mapping[str, Any],
        *,
        reason: str = "",
        error_kind: str = "continuation",
        action_hint: str | None = None,
        fresh_session: bool = False,
        protocol_template: Mapping[str, Any] | None = None,
        root: str | Path | None = None,
    ) -> RenderedPrompt:
        del action_hint, fresh_session, protocol_template, root
        return self._field_recovery_prompt(state, reason=reason, error_kind=error_kind, compact=True)

    def repair_prompt(
        self,
        state: Mapping[str, Any],
        error: str,
        raw_output: str | None = None,
    ) -> RenderedPrompt:
        action = self._candidate_action(raw_output)
        conflict = self._semantic_action_conflict(error)
        feedback = protocol_feedback(
            error=error,
            action=action,
            preserve_action=not conflict,
            correction=(
                "当前 action 与状态机条件冲突；不要伪造 advance，按错误选择 rollback、blocked_human 或其他分支。"
                if conflict else None
            ),
            expected="使用当前阶段字段增量模板，只修复命令列出的语法、字段或状态机问题。",
        )
        field_tasks = state.get("field_tasks", []) if isinstance(state, Mapping) else []
        if field_tasks:
            if "STAGE_RESULT_INVALID" in feedback or "no valid JSON RALPH action" in feedback:
                feedback = (
                    "上一轮只是 Commander 的中途自然语言汇报，不是结构化字段提交；"
                    "状态和字段任务均保留。不要输出阶段结果，继续当前字段 Agent 流程。"
                )
            feedback += (
                "\n\n这是 Commander 的中途自然语言回报被误当作阶段结果，不代表阶段完成或失败。"
                "当前仍有字段 Agent/任务在执行：不要输出 RALPH_STAGE_RESULT，不要重做阶段，"
                "继续等待当前字段回执；收到回执后直接检查任务文件并运行 ralph field-apply。"
            )
        return self._field_recovery_prompt(state, reason=feedback, error_kind="protocol")
