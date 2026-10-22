"""Stage contracts and controlled field/task documents.

The state machine owns the workflow.  This module turns a stage into two
concrete, inspectable documents:

* a stage contract for the Commander; and
* a small field or DAG task file for each permitted subagent.

It intentionally decomposes *decision semantics*, not arbitrary words.  A
leaf is complete when it can be confirmed, inferred from evidence, asked of
the human, made an explicit assumption, or assigned as a verifiable research
task.
"""

from __future__ import annotations

import copy
import json
import os
import re
from pathlib import Path, PurePosixPath
from typing import Any, Mapping

from .dag import DAGValidationError, ready_tasks
from .runtime_config import field_mode_enabled


CONTRACT_DIR = "loop-artifacts/contracts"
CARD_DIR = "loop-artifacts/task-cards"
CARD_MARKER_RE = re.compile(r"^\s*RALPH_TASK_CARD\s*[:=]\s*(?P<ref>[^\s`]+)\s*$")


SEMANTIC_ROLES = (
    "background",
    "decision_object",
    "objective",
    "comparison_set",
    "constraints",
    "deliverable",
    "uncertainty",
)

# Split the seven semantic roles into independent field-groups so each builder
# subagent only authors a small slice (short output -> far less likely to stall
# on the local 35B backend).  Each group is its own dispatched agent writing its
# own partial file; the runtime merges the partials into the canonical slice
# before the gate audits it.
# 写死的常量已废弃，改为因素驱动：见 factor_groups()。保留名仅作兼容别名。
SEMANTIC_ROLE_GROUPS = None  # type: ignore[assignment]

# 默认 7 个语义角色（与历史一致）：context / options / output 三张命名卡。
DEFAULT_SEMANTIC_ROLES = list(SEMANTIC_ROLES)

_DEFAULT_ROLE_GROUPS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("context", ("background", "decision_object", "objective")),
    ("options", ("comparison_set", "constraints")),
    ("output", ("deliverable", "uncertainty")),
)


def factor_groups(
    state: Mapping[str, Any] | None = None,
    stage_id: str = "01",
    key: str = "task_spec",
    max_per_card: int = 3,
) -> tuple[tuple[str, tuple[str, ...]], ...]:
    """因素驱动的分桶：卡数由因素个数推导。

    默认 7 个语义角色仍映射到 ``context`` / ``options`` / ``output`` 三张命名卡
    （与历史行为一致，保证既有回归测试不破）。当任务在 ``task_spec.factor_roles``
    中声明自定义因素列表时，按 ``ceil(N / max_per_card)`` 动态生成卡数——因素多则
    卡多、因素少则卡少，每卡仍只填 ≤ ``max_per_card`` 个独立字段，主 agent 只派发
    并 ``assemble`` 合并，使子代理在本地小模型下稳定不卡。
    """

    if stage_id not in PARTIAL_BUILDER_STAGES:
        return ()
    factors: list[str] = list(DEFAULT_SEMANTIC_ROLES)
    spec = (state or {}).get("task_spec", {}) or {}
    if isinstance(spec, Mapping):
        custom = spec.get("factor_roles")
        if isinstance(custom, (list, tuple)) and custom:
            factors = [str(item) for item in custom if str(item).strip()]
    if not factors:
        factors = list(DEFAULT_SEMANTIC_ROLES)
    # 默认七个角色保持历史命名分组，避免破坏既有 artifact 路径与测试。
    if factors == DEFAULT_SEMANTIC_ROLES:
        return _DEFAULT_ROLE_GROUPS
    step = max(1, int(max_per_card))
    buckets: list[tuple[str, tuple[str, ...]]] = []
    for idx in range(0, len(factors), step):
        chunk = tuple(factors[idx : idx + step])
        group = chunk[0] if len(chunk) == 1 else f"g{idx // step + 1}"
        buckets.append((group, chunk))
    return tuple(buckets)

# Stages whose task_spec is filled by multiple field-group builders (not one).
PARTIAL_BUILDER_STAGES = ("01",)


# Methodology requirements mirrored from `loop/1-loop/<stage>`.  These are
# appended (never replacing) to the generated task cards so subagents follow
# the project's character-prompt methodology.  They do not change any
# state-machine-owned instruction (gate isolation, input refs, submission
# shape).  Keep this block in sync with loop/1-loop when those prompts evolve.
LOOP_METHODOLOGY: dict[str, list[str]] = {
    "01": [
        "本阶段 = 目标 / 背景 / 约束 + 初步分解：把「要做什么」整理成 task_spec。",
        "搜索优先、不问可搜：派发前先搜索所有可搜索信息（项目结构、依赖、代码、文档、"
        "数据、工具、外部论文/GitHub），搜索齐全后才允许问用户。",
        "问题必须一次性完整、必须是选择题且带推荐项；禁止逐个追问、禁止“你觉得呢”式开放提问。",
        "约束按分类标记：已确认 / 可推断(记录证据+置信度+可逆性) / 假设(默认策略+置信度) / "
        "待研究 / 必须追问。",
        "提问闸门（先推断后提问）：仅当同时满足“用户/项目/环境均无答案、不能推断或研究、"
        "会改变硬可行性/硬预算/验收标准/价值授权、不能用场景覆盖”四项，才生成用户问题。",
        "置信度门槛：所有 MUST 类约束已确认、整体置信度 ≥ 0.7 才继续；< 0.5 回退重新澄清。",
        "分解项先记为 concept，其需要的事实标 research_required，供 02 调研。当前价格、在售性、最新规格/兼容性、"
        "基准数据绝不能在 01 仅凭训练记忆标 confirmed；最多记录为“待调研的未知项”。",
    ],
    "02": [
        "本阶段 = 调研分解结果：对 01 的每个 research_required 字段派窄调研 subagent，带回 evidence_refs。",
        "调研完成字段处置变为 confirmed / assumed_default；引出新未知项作为 pending 字段增殖，直到无 pending。"
        "外部事实必须引用具体 HTTPS 页面，不能只写网站首页；当前市场/价格字段还必须带 observed_at（ISO 日期）。"
        "抓取失败或没有结果时维持 research_required/uncertain，绝不能改写成“已验证”。",
        "若同一字段的 WebSearch/WebFetch 已失败，且项目已配置两个获人类授权网页 LLM，可在 02 运行 `ralph web-llm-check`"
        "向它们索取可复核的来源线索；回执仅是线索/反驳信号，仍须用具体权威页面独立验证，不能直接作为事实证据。",
        "同时为每个分解项整理「后续执行需要什么」雏形，供 03 细化。",
        "每个任务必须有输入 AND 输出、继续条件 AND 回退条件；任务 ID 唯一；DAG 无环。",
        "每个 MUST 类约束必须被至少一个任务覆盖。",
        "单个任务文档 + 执行上下文 ≤ 8K token（作为 subagent prompt 时）；过长需进一步拆分。",
        "并行节点必须显式标注 execution_mode 与 parallel_group_id，同一并行组具有不同正交维度键，"
        "且写入路径无冲突。",
        "跨层依赖必须声明 input_refs、output_schema 与依赖条件；Join 节点必须声明 join_policy。",
        "本阶段只做调研与分解确认，不做交叉验证（交叉验证在 02.5）。",
    ],
    "02.5": [
        "本阶段 = 调研后交叉验证：对 02 的每个关键调研字段，逐字段拿去问各种网页 LLM + 权威数据，检查矛盾与冲突。",
        "Commander 只派发 subagent，不直接去问；每张 builder 卡内嵌该字段的当前内容"
        "（concept/attribute/disposition/evidence/rationale）作为参数。",
        "网页 LLM 清单与具体做法见 loop/1-loop/02.5-交叉验证.md"
        "（网页来源可含 arena.ai/agent、bigmodel、aistudio、perplexity、poe、chatgpt、claude、gemini、grok、copilot；"
        "当前受控 Playwright 提问只支持经人类授权的 perplexity/chatgpt/gemini）。",
        "仅在项目已获人类浏览器授权或已配置 API 时，才通过 `ralph web-llm-check` 向 ≥2 个不同网页 LLM 提同一验证问题；"
        "必须保留回执。无回执不得声称已询问 LLM。无论是否配置，都须 WebSearch 查独立权威来源"
        "（论文/官方规格/基准/厂商文档）交叉印证。",
        "比较不同 LLM / 来源答案，更新字段 confidence / disposition / evidence_refs / rationale，并产出交叉验证摘要。"
        "摘要必须有 validation_records：每个 claim_ref 对应两个不同域名的具体来源、observed_at、"
        "supported/contradicted/uncertain 裁决；一段概述不能替代逐 claim 记录。",
    ],
    "03": [
        "本阶段 = 执行任务分解（含调研 + 后续行动）：把已调研、已交叉验证的分解项细化为可执行子任务图并执行。",
        "子任务图正交、可验证、DAG 无环；并行节点显式标注 execution_mode / parallel_group_id；Join 声明 join_policy。",
        "含调研子任务（继续填 attribute_matrix，产出 evidence_refs）与后续行动子任务（实现/计算/实验/写作）。",
        "只派发当前 ready 任务的已批准任务卡；不得裸派 Agent，也不得跨任务代替决策。",
        "所有 DAG 节点完成后才出现 execution-join-auditor；该门禁完成前禁止进入 04。"
        "每个节点必须实际写出 node.writes 声明的非空项目内文件，再运行 ralph graph-apply；"
        "仅在任务 JSON 写“完成”或把 completed ID 填进状态不算执行。",
        "阶段结束必须产生可验证 artifact 与结构化动作；失败 rollback 或新 revision；无任务 explore。",
    ],
    "04": [
        "本阶段 = 验证与交叉验证：把 03 产物整理成事实账本（claim ledger）并核验一致性。",
        "每个关键 claim 必须有数值/上下文、来源链接、来源类型、日期、适用条件、复核者和状态。",
        "无来源或无法复核的断言必须标 uncertain / rejected，不能进入最终推荐。",
        "检查输出是否覆盖任务定义、证据是否可复现、是否产生未声明副作用、并行结果是否冲突、Join 输入是否完整。",
        "本阶段做「验证」（事实账本 + 一致性核验）；逐源交叉验证在 04.5。",
    ],
    "04.5": [
        "本阶段 = 产出后交叉验证：对 04 的每条关键 claim，逐条拿去问各种网页 LLM + 权威数据，检查矛盾与冲突，给出最终置信度。",
        "Commander 只派发 subagent，不直接去问；每张 builder 卡内嵌该 claim 的当前内容"
        "（claim/source_url/source_type/status/rationale）作为参数。",
        "网页 LLM 清单与具体做法见 loop/1-loop/04.5-交叉验证.md（与 02.5 同一清单）。",
        "仅在项目已获人类浏览器授权或已配置 API 时，才通过 `ralph web-llm-check` 向 ≥2 个不同网页 LLM 提同一验证问题，并保留回执；"
        "无回执不得声称已询问 LLM。WebSearch 的独立权威来源仍是事实核验依据。",
        "比较不同 LLM / 来源答案，更新 claim 的 status / checked_by，并产出最终交叉验证摘要。"
        "若网页 LLM 已获授权，交叉验证字段必须引用 web-llm-check 的成功回执；否则只能明确写未授权/失败，"
        "不能把普通网页来源伪称为 LLM 询问。",
    ],
    "05": [
        "（新管线已弃用 05/06：决策在 03/04 内联完成，交接由 explore 承担。本条目仅兼容旧任务。）",
        "决策必须写明依据、证据、影响范围和下一步动作，不以“已完成”代替验证。",
        "输出仅限：继续执行 / 回滚重新分解 / 标记人类阻塞并跳过 / 生成候选任务。",
    ],
    "06": [
        "（新管线已弃用 05/06：决策在 03/04 内联完成，交接由 explore 承担。本条目仅兼容旧任务。）",
        "验证通过 → 生成交接摘要 → 更新 loop-state → 扫描 ready / blocked_human / candidate 队列 → "
        "自动继续唯一明确任务，或展示候选，或进入 exploration。",
        "blocked_human 不阻塞队列。",
        "candidate 必须包含调研、理由、范围和建议分解；多个实质不同任务同时存在时输出最多三个候选并给出推荐。",
        "没有 ready 任务时进入 exploration，不输出循环终点。",
    ],
}

# The exploration tail node autonomously discovers new tasks and enqueues them.
LOOP_METHODOLOGY["exploration"] = [
    "探索节点不是终止节点：先读项目 tasks/TASKS.md，运行只读命令 ralph task-next . 看是否有依赖已满足的 ready/pending 任务。",
    "有可接取任务时，在 payload.exploration.selected_task 完整记录 task_id/title/source/source_path/priority/reason，以 selection_mode=task_board 重新进入 01。",
    "没有可接取任务时，必须自主发现新任务：围绕用户目标 / 项目缺口 / 已有研究，做一轮轻量调研（WebSearch、读 memory/），生成 1~3 个候选方向。",
    "候选必须包含研究摘要、理由和范围，并显式标记 status=candidate；候选只进入 queue，不能被静默执行，也不能用带 candidate selected_task 的 advance 绕过批准。",
    "候选探索先返回 preference_brief 给主 Agent 分析；只有后续从 tasks/TASKS.md 选出 ready/pending 任务，才以 selection_mode=task_board 进入 01 澄清背景与目标。",
    "候选如需持久进入任务板，写成 tasks/TASKS.md 的新表格行（列：ID、任务(目标)、状态=pending、优先级、依赖、背景）；这仍是入队，不代表自动执行。",
]


def card_ref(card_id: str) -> str:
    """Return the project-relative, path-safe location for one task card."""

    safe = re.sub(r"[^A-Za-z0-9._-]+", "-", card_id).strip("-")
    return f"{CARD_DIR}/{safe}.md"


def stage_input_package_ref(stage_id: str, revision: str) -> str:
    """Return the deliberately bounded context package for stage reviewers."""

    return f"{CONTRACT_DIR}/{stage_id}-{revision}-stage-input-package.json"


def stage_submission_template_ref(stage_id: str, revision: str) -> str:
    """Return the Commander-owned, copy-and-fill stage result template."""

    return f"{CONTRACT_DIR}/{stage_id}-{revision}-submission-template.json"


def stage_contract_ref(stage_id: str, revision: str) -> str:
    """Return the materialized stage contract (methodology + gate criteria)."""

    return f"{CONTRACT_DIR}/{stage_id}-{revision}-stage-contract.md"


def stage_result_ref(stage_id: str, revision: str) -> str:
    """Return the assembled, machine-checked stage result artifact path."""

    return f"loop-artifacts/stages/{stage_id}-{revision}-result.json"


def stage_slice_ref(stage_id: str, revision: str, key: str) -> str:
    """Return the builder-owned slice file path for one payload key."""

    safe = re.sub(r"[^A-Za-z0-9._-]+", "-", key).strip("-")
    return f"loop-artifacts/stages/{stage_id}/{revision}/{safe}.json"


def normalize_card_ref(value: str | None) -> str | None:
    if not value:
        return None
    candidate = PurePosixPath(str(value).replace("\\", "/"))
    if candidate.is_absolute() or ".." in candidate.parts:
        return None
    normalized = str(candidate)
    return normalized if normalized.startswith(f"{CARD_DIR}/") else None


def task_card_marker(tool_input: Mapping[str, Any]) -> str | None:
    """Read the explicit task-card reference embedded in an Agent prompt."""

    prompt = tool_input.get("prompt")
    if not isinstance(prompt, str):
        return None
    first_content_line = next((line for line in prompt.splitlines() if line.strip()), "")
    match = CARD_MARKER_RE.match(first_content_line)
    return normalize_card_ref(match.group("ref")) if match else None


def agent_prompt_for_card(card: Mapping[str, Any]) -> str:
    return (
        f"RALPH_TASK_CARD={card['card_ref']}\n"
        "先读取该任务卡与其中列出的文件；只在其边界内执行。"
        "不要后台运行；完成后把结构化结果返回给 Commander。"
    )


def _base_card(
    *,
    stage_id: str,
    revision: str,
    suffix: str,
    role: str,
    title: str,
    objective: str,
    instructions: list[str],
    allowed_tools: list[str],
    required_for_advance: bool = True,
    task_id: str | None = None,
    input_refs: list[str] | None = None,
    output_schema: Mapping[str, Any] | None = None,
    is_stage_gate: bool = False,
    bounded_context: bool = False,
    methodology: list[str] | None = None,
) -> dict[str, Any]:
    card_id = f"{stage_id}-{revision}-{suffix}"
    if bounded_context:
        # A gate reviewer must not inherit the Commander conversation or a
        # mutable full-state dump.  It receives only the frozen stage package,
        # the contract and the result template it is meant to audit against.
        refs = [
            stage_input_package_ref(stage_id, revision),
            f"{CONTRACT_DIR}/{stage_id}-{revision}-stage-contract.md",
            stage_submission_template_ref(stage_id, revision),
        ]
    else:
        refs = [
            "loop-state.json",
            "loop-artifacts/contracts/task-spec.json",
            f"{CONTRACT_DIR}/{stage_id}-{revision}-stage-contract.md",
            stage_submission_template_ref(stage_id, revision),
        ]
    for ref in input_refs or []:
        if ref not in refs:
            refs.append(ref)
    merged_instructions = list(instructions)
    if methodology:
        merged_instructions.append(
            "参考阶段方法论（源自 loop/1-loop，补充要求，不覆盖上方门禁/边界规则）："
        )
        merged_instructions.extend(methodology)
    return {
        "id": card_id,
        "stage_id": stage_id,
        "revision": revision,
        "task_id": task_id,
        "role": role,
        "title": title,
        "objective": objective,
        "instructions": merged_instructions,
        "allowed_tools": allowed_tools,
        "document_refs": refs,
        "input_refs": list(input_refs or []),
        "output_schema": dict(output_schema or {}),
        "required_for_advance": required_for_advance,
        "is_stage_gate": is_stage_gate,
        "context_mode": "bounded_artifacts" if bounded_context else "task_card",
        "card_ref": card_ref(card_id),
        "status": "pending",
    }


def _slice_schema(state: Mapping[str, Any], key: str) -> dict[str, Any]:
    """Return the example object a builder must write for one payload key."""

    payload = stage_submission_template(state).get("payload", {})
    return copy.deepcopy(payload.get(key, {}))


def _builder_card(
    state: Mapping[str, Any],
    *,
    stage_id: str,
    revision: str,
    key: str,
    role: str,
    title: str,
    objective: str,
    instructions: list[str],
    allowed_tools: list[str],
) -> dict[str, Any]:
    """A non-gate construction card that writes one payload slice file.

    The Commander only dispatches this card and later runs ``ralph assemble``;
    it never has to author the large payload inline, which keeps the small
    local-model context from overflowing. The builder owns the heavy content.
    """

    slice_ref = stage_slice_ref(stage_id, revision, key)
    card = _base_card(
        stage_id=stage_id,
        revision=revision,
        methodology=LOOP_METHODOLOGY.get(stage_id, []),
        suffix=f"builder-{key}",
        role=role,
        title=title,
        objective=objective,
        instructions=instructions
        + [
            f"用 **Write** 工具把完整填充后的切片写入 `{slice_ref}`（该文件顶层对象即 `payload.{key}` 完整内容；运行时已预生成骨架，直接整体覆盖为填充版）。",
            "禁止再派发任何子代理（不得调用 Agent）；你必须自己用 Write 完成切片写入，嵌套子代理只会额外增加断流风险。",
            "不要写入 loop-state.json 或其他受控文件；不要替 Commander 做独立门禁审计（那是 gate 子代理的职责）。",
            "完成后只把结构化结论简短返回给 Commander，并确认切片文件已写好。",
        ],
        allowed_tools=allowed_tools,
        required_for_advance=True,
        input_refs=[slice_ref],
        output_schema=_slice_schema(state, key),
        is_stage_gate=False,
        bounded_context=False,
    )
    card["document_refs"] = [
        f"{CONTRACT_DIR}/{stage_id}-{revision}-stage-contract.md",
        stage_submission_template_ref(stage_id, revision),
        slice_ref,
    ]
    return card


def _partial_slice_ref(stage_id: str, revision: str, key: str, group: str) -> str:
    return f"loop-artifacts/stages/{stage_id}/{revision}/{key}.partial.{group}.json"


def _partial_builder_card(
    state: Mapping[str, Any],
    *,
    stage_id: str,
    revision: str,
    key: str,
    group: str,
    roles: tuple[str, ...],
    allowed_tools: list[str],
) -> dict[str, Any]:
    """A builder that owns only one semantic-role group of a slice.

    It writes a small partial file (only its roles) instead of the whole slice,
    so the local model's single output is short and stall-resistant.  The runtime
    merges all group partials into the canonical slice before the gate runs.
    """

    slice_ref = _partial_slice_ref(stage_id, revision, key, group)
    card = _base_card(
        stage_id=stage_id,
        revision=revision,
        methodology=LOOP_METHODOLOGY.get(stage_id, []),
        suffix=f"builder-{key}-{group}",
        role=f"{key}-writer-{group}",
        title=f"任务规格构造·{group}",
        objective=f"只填写 task_spec 的语义角色：{', '.join(roles)}。",
        instructions=[
            f"你**只负责** task_spec 的这几个语义角色：{', '.join(roles)}；不要写其他角色。",
            f"用 **Write** 工具把你的部分写入 `{slice_ref}`。文件顶层对象只需包含："
            "`semantic_map`（只列你负责的角色，每条给 2-4 个真实条目）、"
            "`attribute_matrix`（只列这些角色的叶节点，含 concept/role/attribute/disposition/rationale，"
            "disposition ∈ {confirmed,inferred,assume,research}）、以及可选的 `assumptions`/`scenarios`/`requirements_audit`。",
            "其他角色一律不要出现在文件里（不要留空数组占位），避免与同阶段其他 builder 的输出冲突。",
            "禁止再派发任何子代理（不得调用 Agent）；你自己用 Write 完成，嵌套子代理只会增加断流风险。",
            "不要写入 loop-state.json 或其他受控文件；不要替 Commander 做独立门禁审计（那是 gate 的职责）。",
            "完成后只把结构化结论简短返回给 Commander，并确认文件已写好。",
        ],
        allowed_tools=allowed_tools,
        required_for_advance=True,
        input_refs=[slice_ref],
        output_schema=_slice_schema(state, key),
        is_stage_gate=False,
        bounded_context=False,
    )
    card["slice_roles"] = list(roles)
    card["document_refs"] = [
        f"{CONTRACT_DIR}/{stage_id}-{revision}-stage-contract.md",
        stage_submission_template_ref(stage_id, revision),
        slice_ref,
    ]
    return card


def _stage_review_schema(stage_id: str) -> dict[str, Any]:
    """The common review receipt every independent stage gate must return."""

    return {
        "type": "object",
        "required": [
            "reviewer_card_id",
            "verdict",
            "recommended_action",
            "checked_input_refs",
            "checked_output_refs",
            "checks",
            "blocking_findings",
            "summary",
        ],
        "stage": stage_id,
        "verdict_values": ["pass", "rollback", "blocked_human"],
        "check_status_values": ["pass", "fail", "uncertain"],
    }


def _fixed_stage_cards(state: Mapping[str, Any], stage_id: str, revision: str) -> list[dict[str, Any]]:
    builders: list[dict[str, Any]] = []
    if stage_id == "01":
        builders = [
            _partial_builder_card(
                state,
                stage_id=stage_id,
                revision=revision,
                key="task_spec",
                group=group,
                roles=roles,
                allowed_tools=["Read", "Glob", "Grep", "Write"],
            )
            for group, roles in factor_groups(state, stage_id, "task_spec")
        ]
    elif stage_id == "02":
        builders = [
            _builder_card(
                state,
                stage_id=stage_id,
                revision=revision,
                key="plan",
                role="plan-decomposer",
                title="任务 DAG 构造",
                objective="把已澄清需求分解为正交、可验证、可并行/合并的任务图切片。",
                instructions=[
                    "每个节点必须有 title、objective、evidence_plan、acceptance_criteria、输入输出、依赖与写入路径。",
                    "并行节点显式标注 execution_mode 与 parallel_group_id；Join 节点声明 join_policy。",
                    "每个 MUST 类约束必须被至少一个节点覆盖；DAG 无环。",
                ],
                allowed_tools=["Read", "Glob", "Grep", "Write"],
            )
        ]
    elif stage_id == "02.5":
        builders = [
            _builder_card(
                state,
                stage_id=stage_id,
                revision=revision,
                key="cross_validation",
                role="cross-validation-writer",
                title="调研后交叉验证构造",
                objective="对 02 的每个关键调研字段，向各种网页 LLM + 权威数据核验矛盾与冲突。",
                instructions=[
                    "逐字段读取 attribute_matrix 中的调研字段（concept/attribute/disposition/evidence/rationale）。",
                    "对每个字段向 ≥2~3 个不同网页 LLM 提同一验证问题（清单见 loop/1-loop/02.5-交叉验证.md），并 WebSearch 查权威来源。",
                    "比较不同 LLM / 来源答案，更新字段 confidence/disposition/evidence_refs/rationale，并记录矛盾。",
                    "产出 cross_validation 切片：validated_fields、contradictions、summary。",
                ],
                allowed_tools=["Read", "Glob", "Grep", "WebSearch", "WebFetch", "Write"],
            )
        ]
    elif stage_id == "04":
        builders = [
            _builder_card(
                state,
                stage_id=stage_id,
                revision=revision,
                key="verification",
                role="verification-writer",
                title="事实账本构造",
                objective="把研究/核验结果整理成逐条可溯源的 claim ledger 切片。",
                instructions=[
                    "每条 claim 必须含 claim、source_url、source_type、checked_by、status(verified/rejected/uncertain)。",
                    "无来源或无法复核的断言标 uncertain/rejected，不能进入最终推荐。",
                    "summary 总结核验结论与残余不确定性。",
                ],
                allowed_tools=["Read", "Glob", "Grep", "WebSearch", "WebFetch", "Write"],
            )
        ]
    elif stage_id == "04.5":
        builders = [
            _builder_card(
                state,
                stage_id=stage_id,
                revision=revision,
                key="cross_validation_out",
                role="cross-validation-writer",
                title="产出后交叉验证构造",
                objective="对 04 的每条关键 claim，向各种网页 LLM + 权威数据核验矛盾与冲突，给出最终置信度。",
                instructions=[
                    "逐条读取 verification claim ledger 中的关键 claim（claim/source_url/source_type/status/rationale）。",
                    "对每条 claim 向 ≥2~3 个不同网页 LLM 提同一验证问题（清单见 loop/1-loop/04.5-交叉验证.md），并 WebSearch 查权威来源。",
                    "比较不同 LLM / 来源答案，更新 claim 的 status/checked_by，并记录矛盾。",
                    "产出 cross_validation_out 切片：validated_claims、contradictions、summary。",
                ],
                allowed_tools=["Read", "Glob", "Grep", "WebSearch", "WebFetch", "Write"],
            )
        ]
    elif stage_id == "05":
        builders = [
            _builder_card(
                state,
                stage_id=stage_id,
                revision=revision,
                key="decision",
                role="decision-writer",
                title="决策构造",
                objective="把候选方案、证据与风险整理成可追溯的决策切片。",
                instructions=[
                    "selected_option 与 decision_rationale 必填，并追溯到已验证事实与偏好。",
                    "evidence_refs 非空；rejected_options、risks 至少列出；human_approval_needed 明确 true/false。",
                ],
                allowed_tools=["Read", "Glob", "Grep", "Write"],
            )
        ]
    elif stage_id == "06":
        builders = [
            _builder_card(
                state,
                stage_id=stage_id,
                revision=revision,
                key="handoff",
                role="handoff-writer",
                title="交接构造",
                objective="把交付物、遗留项与候选队列整理成交接切片。",
                instructions=[
                    "deliverables 非空；decision_ref 引用 05 的决策；remaining_tasks/blocked_human/candidates 为数组。",
                    "resume_instruction 给出下一轮或恢复入口。",
                ],
                allowed_tools=["Read", "Glob", "Grep", "Write"],
            )
        ]

    gate = None
    if stage_id == "01":
        gate = _base_card(
            stage_id=stage_id,
            revision=revision,
            methodology=LOOP_METHODOLOGY.get(stage_id, []),
            suffix="requirements-auditor",
            role="requirements-auditor",
            title="需求、遗漏和假设审计",
            objective="独立检查 Commander 对用户意图的语义分解，找出会改变决策的遗漏属性与隐含假设。",
            instructions=[
                "你是独立阶段门禁，不继承 Commander 主对话；只读取任务卡中的阶段输入包、契约和提交模板。",
                "只分析已给输入与项目内已有资料；不得开始外部调研或给出最终推荐。",
                "按背景、决策对象、目标、比较集合、约束、交付物、不确定性逐项审计。",
                "先执行需求分流闸门：显式输入或项目证据标记 confirmed；由多条证据高置信推导出的结论标记 inferred；可用默认策略推进的标记 assume；可以通过本地/网页证据解决的标记 research；只有不可自行解析且会改变可行性、硬预算、验收标准或价值授权的才标记 ask_human。",
                "每个叶节点必须记录 disposition、rationale、evidence_refs、confidence、impact 和 reversible；不要把‘字段没有单独出现’当成必须追问。",
                "返回一次性问题包：仅包含同时满足‘未被输入或环境确定、不能推断/研究、会改变关键分支、不能用场景覆盖’四条件的问题，并为每题给推荐选项。",
                "如果模型档位未明确，先读取已有模型/配置；仍未知时建立 30-35B 与更大模型档位的场景并把内存需求列为 research，不因模型名未知而阻塞。",
                "如果用户明确要购买本地 GPU/硬件，标记本地硬件采购为 confirmed 或 inferred；候选集合已经包含云服务时，不再追问云服务是否比较，而是按‘主方案/补充基线’记录假设或场景。",
                "返回 requirements_audit：覆盖缺口、冲突、默认假设风险和建议场景分支。",
            ],
            allowed_tools=["Read", "Glob", "Grep"],
            output_schema=_stage_review_schema(stage_id),
            is_stage_gate=True,
            bounded_context=True,
            input_refs=[stage_result_ref(stage_id, revision)],
        )
    elif stage_id == "02":
        gate = _base_card(
            stage_id=stage_id,
            revision=revision,
            methodology=LOOP_METHODOLOGY.get(stage_id, []),
            suffix="dag-auditor",
            role="dag-auditor",
            title="任务 DAG 正交性与可执行性审计",
            objective="审计 Commander 的任务分解是否覆盖需求、相互正交、可并行、可验证且没有写冲突。",
            instructions=[
                "你是独立阶段门禁，不继承 Commander 主对话；只读取任务卡中的阶段输入包、契约和提交模板。",
                "不做实际领域调研；只检查任务图和任务卡草案。",
                "检查每个节点的输入、输出、前置条件、后置条件、证据计划和写入路径。",
                "检查并行组的 orthogonal_key、依赖、Join 和潜在写冲突。",
                "指出漏项、重复项、错误粒度和不可验证节点，并给出可执行的修改建议。",
            ],
            allowed_tools=["Read", "Glob", "Grep"],
            output_schema=_stage_review_schema(stage_id),
            is_stage_gate=True,
            bounded_context=True,
            input_refs=[stage_result_ref(stage_id, revision)],
        )
    elif stage_id == "02.5":
        gate = _base_card(
            stage_id=stage_id,
            revision=revision,
            methodology=LOOP_METHODOLOGY.get(stage_id, []),
            suffix="cross-validation-auditor",
            role="cross-validation-auditor",
            title="调研后交叉验证门禁审计",
            objective="独立检查每个关键调研字段是否经过 ≥2 个独立来源核验，矛盾冲突是否已被记录与处置。",
            instructions=[
                "你是独立阶段门禁，不继承 Commander 主对话；只读取任务卡中的阶段输入包、契约和提交模板。",
                "检查 attribute_matrix 中每个调研字段是否带 evidence_refs，且 evidence 来自不同网页 LLM / 权威来源。",
                "检查矛盾/冲突字段是否已在 rationale 标注，且 disposition 已相应更新（必要时标 research_required 或降 confidence）。",
                "输出 pass、rollback 或 blocked_human；矛盾未消解不得 pass。",
            ],
            allowed_tools=["Read", "Glob", "Grep", "WebSearch", "WebFetch"],
            output_schema=_stage_review_schema(stage_id),
            is_stage_gate=True,
            bounded_context=True,
            input_refs=[stage_result_ref(stage_id, revision)],
        )
    elif stage_id == "04":
        gate = _base_card(
            stage_id=stage_id,
            revision=revision,
            methodology=LOOP_METHODOLOGY.get(stage_id, []),
            suffix="evidence-verifier",
            role="evidence-verifier",
            title="关键事实与证据账本核验",
            objective="逐条核验会影响决策的外部事实，拒绝没有可追溯证据、日期或适用条件的断言。",
            instructions=[
                "你是独立阶段门禁，不继承 Commander 主对话；只读取任务卡中的阶段输入包、契约和提交模板。",
                "只审计候选 claim ledger；不要重写整份研究报告。",
                "规格优先官方资料；价格必须带地区、币种、日期和新旧状态；性能必须带工作负载与方法。",
                "每条事实标记 verified、rejected 或 uncertain；不能核实就不能进入最终推荐。",
                "对每条 rejected/uncertain claim 给出缺什么证据、应回到哪个研究任务。",
            ],
            allowed_tools=["Read", "Glob", "Grep", "WebSearch", "WebFetch"],
            output_schema=_stage_review_schema(stage_id),
            is_stage_gate=True,
            bounded_context=True,
            input_refs=[stage_result_ref(stage_id, revision)],
        )
    elif stage_id == "04.5":
        gate = _base_card(
            stage_id=stage_id,
            revision=revision,
            methodology=LOOP_METHODOLOGY.get(stage_id, []),
            suffix="cross-validation-auditor",
            role="cross-validation-auditor",
            title="产出后交叉验证门禁审计",
            objective="独立检查每条关键 claim 是否经过 ≥2 个独立来源核验，矛盾冲突是否已被记录与处置，最终置信度是否合理。",
            instructions=[
                "你是独立阶段门禁，不继承 Commander 主对话；只读取任务卡中的阶段输入包、契约和提交模板。",
                "检查 verification claim ledger 中每条关键 claim 的 status/checked_by 是否来自不同网页 LLM / 权威来源。",
                "检查矛盾/冲突 claim 是否已标 uncertain/rejected，且未进入最终推荐。",
                "输出 pass、rollback 或 blocked_human；矛盾未消解不得 pass。",
            ],
            allowed_tools=["Read", "Glob", "Grep", "WebSearch", "WebFetch"],
            output_schema=_stage_review_schema(stage_id),
            is_stage_gate=True,
            bounded_context=True,
            input_refs=[stage_result_ref(stage_id, revision)],
        )
    elif stage_id == "05":
        gate = _base_card(
            stage_id=stage_id,
            revision=revision,
            methodology=LOOP_METHODOLOGY.get(stage_id, []),
            suffix="decision-auditor",
            role="decision-auditor",
            title="决策输入与结论门禁审计",
            objective="独立检查候选方案、验证账本与决策规则是否足以支持当前选择，避免把偏好、事实和推断混为一谈。",
            instructions=[
                "你是独立阶段门禁，不继承 Commander 主对话；只读取任务卡中的阶段输入包、契约和提交模板。",
                "检查推荐是否能追溯到已验证事实、明确偏好与适用场景。",
                "检查被拒方案、残余风险和需要人类确认的价值判断是否被清楚保留。",
                "输出 pass、rollback 或 blocked_human；不要替 Commander 作最终选择。",
            ],
            allowed_tools=["Read", "Glob", "Grep"],
            output_schema=_stage_review_schema(stage_id),
            is_stage_gate=True,
            bounded_context=True,
            input_refs=[stage_result_ref(stage_id, revision)],
        )
    elif stage_id == "06":
        gate = _base_card(
            stage_id=stage_id,
            revision=revision,
            methodology=LOOP_METHODOLOGY.get(stage_id, []),
            suffix="handoff-auditor",
            role="handoff-auditor",
            title="交接、遗留项与候选队列门禁审计",
            objective="独立检查最终产物是否可复用、未决风险是否显式、以及下一任务与候选任务是否没有被静默执行。",
            instructions=[
                "你是独立阶段门禁，不继承 Commander 主对话；只读取任务卡中的阶段输入包、契约和提交模板。",
                "检查交付物、决策引用、遗留任务、人类阻塞项与候选任务是否完整可恢复。",
                "检查是否把候选任务误当作已执行任务，或遗漏恢复入口。",
                "输出 pass、rollback 或 blocked_human；不要自行结束或开启新任务。",
            ],
            allowed_tools=["Read", "Glob", "Grep"],
            output_schema=_stage_review_schema(stage_id),
            is_stage_gate=True,
            bounded_context=True,
            input_refs=[stage_result_ref(stage_id, revision)],
        )
    elif stage_id == "exploration":
        gate = _base_card(
            stage_id=stage_id,
            revision=revision,
            methodology=LOOP_METHODOLOGY.get(stage_id, []),
            suffix="exploration-auditor",
            role="exploration-auditor",
            title="任务板接续与新任务审计",
            objective="独立检查尾部节点是否先扫描项目 tasks/，是否选择了依赖满足的任务，以及无任务时是否自主发现并把候选写成任务板新行（入队）而非静默执行。",
            instructions=[
                "你是独立阶段门禁，不继承 Commander 主对话；只读取任务卡中的阶段输入包、契约和提交模板。",
                "检查 scanned_sources 是否包含实际读取的项目任务板（tasks/TASKS.md）或队列证据。",
                "有 ready/pending 且依赖满足的现有任务时，优先检查 selected_task 是否来自 tasks/，而不是先创造新候选。",
                "当没有可接取任务时，检查 Commander 是否自主发现了 1~3 个候选方向，并直接在 tasks/TASKS.md 写入了带背景/目标的新行（入队）；不应只在内存返回 candidate。",
                "检查 preference_brief 是否把用户偏好、缺口和下一轮分解方向返回给主 Agent。",
                "输出 pass、rollback 或 blocked_human；不要自行执行候选任务。",
            ],
            allowed_tools=["Read", "Glob", "Grep", "Bash"],
            output_schema=_stage_review_schema(stage_id),
            is_stage_gate=True,
            bounded_context=True,
        )
    if gate is None:
        return builders
    return builders + [gate]


def _plan_cards(state: Mapping[str, Any]) -> list[dict[str, Any]]:
    stage = state.get("stage", {})
    if str(stage.get("id")) != "03":
        return []
    plan = state.get("plan", {})
    if not isinstance(plan, Mapping):
        return []
    raw_nodes = plan.get("nodes", [])
    if not isinstance(raw_nodes, list) or not raw_nodes:
        return []
    try:
        ready = set(ready_tasks(plan, plan.get("completed", ())))
    except (DAGValidationError, TypeError, ValueError):
        return []
    revision = str(stage.get("revision", "r1"))
    cards: list[dict[str, Any]] = []
    for raw in raw_nodes:
        if not isinstance(raw, Mapping) or str(raw.get("id", "")) not in ready:
            continue
        task_id = str(raw["id"])
        cards.append(
            _base_card(
                stage_id="03",
                revision=revision,
                methodology=LOOP_METHODOLOGY.get("03", []),
                suffix=task_id,
                role=str(raw.get("role", "research-worker")),
                title=str(raw.get("title", task_id)),
                objective=str(raw.get("objective", "完成任务卡定义的可验证子任务。")),
                instructions=[
                    "仅处理本任务卡的范围；不得替其他任务作结论。",
                    "遵守输入、输出、前置/后置条件与证据计划。",
                    "所有外部事实必须附可追溯来源、日期与适用条件；不确定事实明确标 uncertain。",
                    "把结果返回给 Commander，不要修改 loop-state.json。",
                ],
                allowed_tools=["Read", "Glob", "Grep", "WebSearch", "WebFetch", "Skill"],
                task_id=task_id,
                input_refs=[str(item) for item in raw.get("input_refs", ())],
                output_schema=raw.get("output_schema", {}),
            )
        )
    all_task_ids = {
        str(raw.get("id", ""))
        for raw in raw_nodes
        if isinstance(raw, Mapping) and str(raw.get("id", ""))
    }
    completed = {str(item) for item in plan.get("completed", ())}
    if all_task_ids and all_task_ids.issubset(completed):
        output_refs = [
            str(path)
            for raw in raw_nodes
            if isinstance(raw, Mapping)
            for path in raw.get("writes", ())
        ]
        cards.append(
            _builder_card(
                state,
                stage_id="03",
                revision=revision,
                key="execution_summary",
                role="execution-assembler",
                title="执行汇总构造",
                objective="在所有 DAG 节点完成后，把各节点产物汇成满足任务卡的 execution_summary 切片。",
                instructions=[
                    "汇总每个 DAG 节点的 completed_task_ids、artifact_refs 与未证实 claim。",
                    "completed_task_ids 必须精确覆盖当前 DAG 的全部节点（与 loop-state.json 的 plan.nodes 一致）。",
                    "artifact_refs 列出各节点实际写入的产物路径；未证实内容保留为 unresolved_claims。",
                ],
                allowed_tools=["Read", "Glob", "Grep", "Write"],
            )
        )
        cards.append(
            _base_card(
                stage_id="03",
                revision=revision,
                methodology=LOOP_METHODOLOGY.get("03", []),
                suffix="execution-join-auditor",
                role="execution-join-auditor",
                title="执行产物输入输出与 Join 门禁审计",
                objective="在所有 DAG 节点完成后，独立检查产物是否满足任务卡、Join 输入是否完整、以及未证实内容是否被正确标记。",
                instructions=[
                    "你是独立阶段门禁，不继承 Commander 主对话；只读取任务卡中的阶段输入包、契约和提交模板。",
                    "核对每个 DAG 节点的前置/后置条件、输出接口、证据计划及写入路径。",
                    "核对 Join 的输入是否全部就绪，且并行任务没有覆盖或互相替代。",
                    "未验证的事实必须保留为候选 claim，不能提升为结论。",
                    "输出 pass、rollback 或 blocked_human，并列出任何需要回到的任务节点。",
                ],
                allowed_tools=["Read", "Glob", "Grep"],
                input_refs=output_refs,
                output_schema=_stage_review_schema("03"),
                is_stage_gate=True,
                bounded_context=True,
            )
        )
    return cards


def required_card_specs(state: Mapping[str, Any]) -> list[dict[str, Any]]:
    stage = state.get("stage", {})
    stage_id = str(stage.get("id", "01"))
    revision = str(stage.get("revision", "r1"))
    return _fixed_stage_cards(state, stage_id, revision) + _plan_cards(state)


# Structural fields are regenerated from the contract each time; runtime
# evidence fields must survive prompt re-rendering and interruption recovery.
_STAGE_CARD_STRUCTURAL = (
    "id",
    "stage_id",
    "revision",
    "task_id",
    "is_stage_gate",
    "role",
    "title",
    "objective",
    "instructions",
    "allowed_tools",
    "input_refs",
    "output_schema",
    "required_for_advance",
    "card_ref",
    "context_mode",
    "bounded_context",
    "document_refs",
)
_STAGE_CARD_EVIDENCE = (
    "status",
    "agent_id",
    "dispatch_count",
    "last_agent_message",
    "gate_verdict",
    "gate_review_ref",
    "completed_at",
    "verdict",
    "audit_artifact_ref",
    "error",
)


def ensure_stage_cards(state: Mapping[str, Any]) -> dict[str, Any]:
    """Seed deterministic, approved cards for the current stage.

    Structural fields (input_refs, instructions, schemas, …) are refreshed from
    the contract on every load so older persisted states keep working with new
    runtime logic; runtime evidence (dispatch/completion status) is preserved.

    In field-centric mode (``RALPH_FIELD_GATE`` set) no cards are seeded: the
    Commander works directly off the field table and dispatches narrow
    single-field subagents, so the heavy builder/gate cards are intentionally
    absent.
    """

    updated = copy.deepcopy(dict(state))
    if field_mode_enabled():
        # Field-centric mode: drop any orphaned builder/gate cards left by a
        # previous enforce run so the Commander is not forced to dispatch them and
        # so render() / the field gate see a clean field table.
        updated.pop("subagent_cards", None)
        return updated
    cards = updated.setdefault("subagent_cards", {})
    if not isinstance(cards, dict):
        cards = {}
        updated["subagent_cards"] = cards
    for spec in required_card_specs(updated):
        existing = cards.get(spec["id"])
        if existing is None:
            cards[spec["id"]] = copy.deepcopy(spec)
            continue
        for key in _STAGE_CARD_STRUCTURAL:
            if key in spec:
                existing[key] = spec[key]
    return updated


def cards_for_current_stage(state: Mapping[str, Any]) -> list[dict[str, Any]]:
    stage = state.get("stage", {})
    stage_id = str(stage.get("id", ""))
    revision = str(stage.get("revision", "r1"))
    values = state.get("subagent_cards", {})
    if not isinstance(values, Mapping):
        return []
    cards = [
        dict(card)
        for card in values.values()
        if isinstance(card, Mapping)
        and str(card.get("stage_id")) == stage_id
        and str(card.get("revision")) == revision
    ]
    return sorted(cards, key=lambda card: str(card.get("id", "")))


def required_cards_for_current_stage(state: Mapping[str, Any]) -> list[dict[str, Any]]:
    return [card for card in cards_for_current_stage(state) if card.get("required_for_advance")]


def card_by_ref(state: Mapping[str, Any], ref: str | None) -> dict[str, Any] | None:
    normalized = normalize_card_ref(ref)
    if normalized is None:
        return None
    values = state.get("subagent_cards", {})
    if not isinstance(values, Mapping):
        return None
    for raw in values.values():
        if isinstance(raw, Mapping) and raw.get("card_ref") == normalized:
            return dict(raw)
    return None


def _semantic_contract() -> str:
    roles = "、".join(SEMANTIC_ROLES)
    return (
        "先按决策语义而非字面词语拆解：" + roles + "。\n\n"
        "对每个语义角色展开会改变决策的隐藏属性；当属性已能被确认、合理推断、"
        "向人类追问、明确假设或变成可验证研究任务时，停止继续拆分。禁止无穷拆词、"
        "把未单独命名的字段自动变成问题，或无证据静默假设。\n\n"
        "需求分流闸门：用户明确输入/历史补充 > 项目状态与文档 > 本地环境与配置 > 工具研究 > 高置信推断 > 默认假设/场景。"
        "只有当信息无法确认、推断或研究，会改变硬可行性/硬预算/验收标准/价值授权，且不能用场景覆盖时，"
        "才使用 ask_human。模型档位未知时先检查本地配置，仍未知就建立 30-35B 与更大模型场景并研究内存；"
        "用户已明确购买本地硬件或候选集合已包含云服务时，不得重复追问这些事实。"
    )


def _stage_gate_card_id(state: Mapping[str, Any]) -> str:
    """Find the current independent gate card, including the delayed 03 gate."""

    gates = [card for card in cards_for_current_stage(state) if card.get("is_stage_gate")]
    if gates:
        return str(gates[0]["id"])
    stage = state.get("stage", {})
    stage_id = str(stage.get("id", "01"))
    revision = str(stage.get("revision", "r1"))
    suffix = {
        "01": "requirements-auditor",
        "02": "dag-auditor",
        "02.5": "cross-validation-auditor",
        "03": "execution-join-auditor",
        "04": "evidence-verifier",
        "04.5": "cross-validation-auditor",
        "05": "decision-auditor",
        "06": "handoff-auditor",
        "exploration": "exploration-auditor",
    }.get(stage_id, "stage-auditor")
    return f"{stage_id}-{revision}-{suffix}"


def _stage_review_template(state: Mapping[str, Any]) -> dict[str, Any]:
    stage = state.get("stage", {})
    stage_id = str(stage.get("id", "01"))
    revision = str(stage.get("revision", "r1"))
    return {
        "reviewer_card_id": _stage_gate_card_id(state),
        "context_mode": "bounded_artifacts",
        "verdict": "pass",
        "recommended_action": "advance",
        "checked_input_refs": [stage_input_package_ref(stage_id, revision)],
        "checked_output_refs": [],
        "checks": [
            {
                "criterion": "填写本阶段契约中的一项可验证验收条件",
                "status": "pass",
                "evidence_refs": [],
                "note": "填写独立审计依据；不确定或失败不能写 pass。",
            }
        ],
        "blocking_findings": [],
        "summary": "填写独立审计的结论与边界。",
    }


def _stage_payload_template(state: Mapping[str, Any]) -> dict[str, Any]:
    stage_id = str(state.get("stage", {}).get("id", "01"))
    payload: dict[str, Any] = {"stage_review": _stage_review_template(state)}
    if stage_id == "01":
        payload["task_spec"] = {
            "semantic_map": {role: [] for role in SEMANTIC_ROLES},
            "attribute_matrix": [
                {
                    "concept": "",
                    "role": "",
                    "attribute": "",
                    "disposition": "confirmed",
                    "rationale": "",
                    "evidence_refs": [],
                    "confidence": 0.0,
                    "impact": "material",
                    "reversible": True,
                    "alternative_scenario": "",
                }
            ],
            "constraints": [],
            "assumptions": [],
            "open_questions": [],
            "scenarios": [{"id": "S1", "name": ""}],
            "success_criteria": [],
            "requirements_audit": {
                "card_id": _stage_gate_card_id(state),
                "artifact_ref": "",
                "summary": "",
            },
        }
    elif stage_id == "02":
        payload["plan"] = {
            "revision": str(state.get("stage", {}).get("revision", "r1")),
            "decomposition_rationale": [],
            "coverage_proof": [],
            "risk_notes": [],
            "nodes": [],
            "parallel_groups": [],
            "joins": [],
        }
    elif stage_id == "02.5":
        payload["cross_validation"] = {
            "revision": str(state.get("stage", {}).get("revision", "r1")),
            "validated_fields": [],
            "contradictions": [],
            "summary": {},
        }
    elif stage_id == "03":
        payload["execution_summary"] = {
            "completed_task_ids": [],
            "artifact_refs": [],
            "unresolved_claims": [],
        }
    elif stage_id == "04":
        payload["verification"] = {
            "claim_ledger": [
                {
                    "claim": "",
                    "source_url": "",
                    "source_type": "",
                    "checked_by": "",
                    "status": "verified",
                }
            ],
            "summary": {},
        }
    elif stage_id == "04.5":
        payload["cross_validation_out"] = {
            "revision": str(state.get("stage", {}).get("revision", "r1")),
            "validated_claims": [],
            "contradictions": [],
            "summary": {},
        }
    elif stage_id == "05":
        payload["decision"] = {
            "selected_option": "",
            "decision_rationale": "",
            "evidence_refs": [],
            "rejected_options": [],
            "risks": [],
            "human_approval_needed": False,
        }
    elif stage_id == "06":
        payload["handoff"] = {
            "deliverables": [],
            "decision_ref": "",
            "remaining_tasks": [],
            "blocked_human": [],
            "candidates": [],
            "resume_instruction": "",
        }
    elif stage_id == "exploration":
        payload["exploration"] = {
            "preference_brief": "",
            "scanned_sources": ["tasks/TASKS.md"],
            "selection_mode": "task_board",
            "selected_task": {
                "task_id": "",
                "title": "",
                "source": "task_board",
                "source_path": "tasks/TASKS.md",
                "priority": "P1",
                "reason": "",
            },
            "candidate_tasks": [],
        }
    return payload


def stage_submission_template(state: Mapping[str, Any]) -> dict[str, Any]:
    """Return the one canonical, copy-and-fill ActionResult skeleton."""

    stage = state.get("stage", {})
    return {
        "action": "advance",
        "status": "passed",
        "stage_id": str(stage.get("id", "")),
        "revision": str(stage.get("revision", "r1")),
        "next_stage": str(stage.get("on_success") or ""),
        "rollback_to": None,
        "evidence": [],
        "artifact_refs": [],
        "message": "填写本阶段为何满足成功条件，以及仍然不成立的边界。",
        "payload": _stage_payload_template(state),
    }


def ensure_builder_skeletons(state: Mapping[str, Any], root: Path) -> list[str]:
    """Pre-generate an editable skeleton slice for every pending builder card.

    The builder no longer authors the whole payload slice from scratch: the
    runtime writes a skeleton (the submission template's ``payload[task_id]``
    with its placeholder values intact) before dispatch, so the subagent only
    has to Edit the empty/placeholder fields.  This is what keeps a small local
    model from stalling on a large open-ended authoring task.

    Idempotent: a slice that already exists is left untouched.
    Returns the list of skeleton paths written this call.
    """

    stage = state.get("stage", {})
    stage_id = str(stage.get("id", ""))
    revision = str(stage.get("revision", "r1"))
    template = stage_submission_template(state)
    payload = template.get("payload", {})

    written: list[str] = []
    for card in state.get("subagent_cards", {}).values():
        if card.get("is_stage_gate"):
            continue
        if str(card.get("stage_id", "")) != stage_id or str(card.get("revision", "")) != revision:
            continue
        refs = card.get("input_refs") or []
        if not refs:
            continue
        slice_path = Path(root) / refs[0]
        if slice_path.exists():
            continue
        task_id = slice_path.stem
        if card.get("slice_roles"):
            skeleton = {
                "semantic_map": {role: [] for role in card["slice_roles"]},
                "attribute_matrix": [],
                "assumptions": [],
                "scenarios": [],
                "requirements_audit": {},
            }
        else:
            skeleton = copy.deepcopy(payload.get(task_id, {}))
        skeleton_path = slice_path
        skeleton_path.parent.mkdir(parents=True, exist_ok=True)
        skeleton_path.write_text(
            json.dumps(skeleton, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        written.append(str(skeleton_path))
    return written


def merge_task_spec_partials(root: Path, stage_id: str, revision: str, state: Mapping[str, Any] | None = None) -> str | None:
    """Combine the field-group partial files into the canonical task_spec slice.

    Returns the canonical slice ref, or ``None`` when any partial is missing or
    unparseable (caller must ensure all group builders completed first).
    """

    canonical_ref = stage_slice_ref(stage_id, revision, "task_spec")
    canonical_path = Path(root) / canonical_ref
    merged: dict[str, Any] = {
        "semantic_map": {},
        "attribute_matrix": [],
        "assumptions": [],
        "scenarios": [],
        "requirements_audit": {},
    }
    groups = factor_groups(state, stage_id, "task_spec")
    for group, roles in groups:
        pref = Path(root) / _partial_slice_ref(stage_id, revision, "task_spec", group)
        if not pref.exists():
            return None
        try:
            data = json.loads(pref.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return None
        if not isinstance(data, Mapping):
            return None
        semantic_map = data.get("semantic_map", {})
        if isinstance(semantic_map, Mapping):
            for role in roles:
                if role in semantic_map:
                    merged["semantic_map"][role] = semantic_map[role]
        attribute_matrix = data.get("attribute_matrix", [])
        if isinstance(attribute_matrix, list):
            merged["attribute_matrix"].extend(attribute_matrix)
        for key in ("assumptions", "scenarios"):
            value = data.get(key)
            if isinstance(value, list):
                merged[key].extend(value)
        requirements_audit = data.get("requirements_audit")
        if isinstance(requirements_audit, Mapping) and requirements_audit:
            merged["requirements_audit"] = requirements_audit
    canonical_path.parent.mkdir(parents=True, exist_ok=True)
    canonical_path.write_text(
        json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return canonical_ref


def reconcile_partial_merges(root: Path, state: Mapping[str, Any]) -> str | None:
    """Merge field-group partials into the canonical slice when all are done.

    Called once per supervisor cycle, before the Commander session starts, so the
    gate always reads a fully merged slice.  Returns the merged ref or ``None``.

    In addition to writing the canonical ``task_spec.json`` file, the merged
    fields are written back into the in-state ``task_spec`` (which the gate
    reads via ``stage_input_package``).  Without this write-back the gate only
    ever saw an empty spec and rolled back indefinitely.
    """

    stage = state.get("stage", {})
    stage_id = str(stage.get("id", ""))
    revision = str(stage.get("revision", "r1"))
    if stage_id not in PARTIAL_BUILDER_STAGES:
        return None
    groups = factor_groups(state, stage_id, "task_spec")
    partial_ids = [
        f"{stage_id}-{revision}-builder-task_spec-{group}" for group, _ in groups
    ]
    cards = state.get("subagent_cards", {})
    if not all(cards.get(pid, {}).get("status") == "completed" for pid in partial_ids):
        return None
    ref = merge_task_spec_partials(root, stage_id, revision, state)
    if ref is None:
        return None
    from .state import load_state, save_state

    try:
        merged = json.loads((Path(root) / ref).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return ref
    state_path = Path(root) / "loop-state.json"
    live = load_state(state_path)
    task_spec = dict(live.get("task_spec", {})) if isinstance(live.get("task_spec"), Mapping) else {}
    for key in ("semantic_map", "attribute_matrix", "assumptions", "scenarios", "requirements_audit"):
        if key in merged:
            task_spec[key] = merged[key]
    if str(task_spec.get("status", "")) in ("", "unclarified") and any(
        merged.get(k) for k in ("semantic_map", "attribute_matrix")
    ):
        task_spec["status"] = "structured_pending_audit"
    live["task_spec"] = task_spec
    save_state(state_path, live)
    # Keep the caller's in-memory state object in sync so the rest of the
    # cycle (status checks, recovery prompt) sees the populated spec.
    if isinstance(state, dict):
        state["task_spec"] = task_spec
    return ref


def stage_input_package(state: Mapping[str, Any]) -> dict[str, Any]:
    """Create the small immutable evidence package given to a gate reviewer.

    It deliberately excludes the Commander conversation, hidden reasoning,
    prior Stop prompts and unrelated run history.  An auditor has enough
    information to judge the stage contract, but not enough context to merely
    mirror the Commander narrative.
    """

    stage = state.get("stage", {})
    stage_id = str(stage.get("id", "01"))
    revision = str(stage.get("revision", "r1"))
    task_spec = state.get("task_spec", {})
    cards = [
        {
            "id": card.get("id"),
            "task_id": card.get("task_id"),
            "title": card.get("title"),
            "status": card.get("status"),
            "card_ref": card.get("card_ref"),
        }
        for card in cards_for_current_stage(state)
    ]
    return {
        "context_mode": "bounded_artifacts",
        "purpose": "供独立阶段门禁审计；不包含 Commander 主对话或隐藏推理。",
        "stage": {
            "id": stage_id,
            "revision": revision,
            "name": stage.get("name"),
            "input_description": stage.get("input_description"),
            "required_outputs": stage.get("required_outputs", []),
            "success_condition": stage.get("success_condition"),
            "failure_condition": stage.get("failure_condition"),
            "on_success": stage.get("on_success"),
            "on_failure": stage.get("on_failure"),
        },
        "task": state.get("task", {}),
        "authoritative_inputs": task_spec.get("authoritative_inputs", []) if isinstance(task_spec, Mapping) else [],
        "structured_inputs": {
            "task_spec": state.get("task_spec", {}),
            "plan": state.get("plan", {}),
            "verification": state.get("verification", {}),
            "decision": state.get("decision", {}),
            "handoff": state.get("handoff", {}),
            "queue": state.get("queue", {}),
            "task_intake": state.get("task_intake"),
            "last_exploration": state.get("last_exploration"),
        },
        "current_stage_cards": cards,
        "submission_template_ref": stage_submission_template_ref(stage_id, revision),
    }


def _field_contract_text(state: Mapping[str, Any], *, stage_id: str, revision: str) -> str:
    """Field-table contract used in ``RALPH_FIELD_GATE`` mode."""

    contract_ref = stage_contract_ref(stage_id, revision)
    submission_ref = stage_submission_template_ref(stage_id, revision)
    lines = [
        "# RALPH 字段中心 · 阶段契约",
        "",
        f"阶段：{stage_id}-{revision}",
        "",
        "## 你只维护一张字段表（不强制固定任务文件）",
        "",
        f"- 权威输入：`loop-state.json`、`{contract_ref}`、`{submission_ref}`。",
        "- 用 `ralph field-apply` 把字段原子写入字段表（**禁止直接 Write/Edit `loop-state.json`**，运行时只读它）。",
        "- 每条字段形如：concept / role / attribute / disposition / rationale / evidence_refs / confidence / impact / reversible。",
        "- disposition 取英文枚举值之一：confirmed / assumed_default / research_required / pending；直接照抄。",
        '- 例：{"concept": "字段名", "role": "背景", "attribute": "具体属性", "disposition": "confirmed", "rationale": "...", "evidence_refs": [], "confidence": 1.0, "impact": "material", "reversible": true}。',
        "- `confirmed`=已知背景或已有可复核证据的事实；`assumed_default`=不确定偏好（默认全范围，无人类输入）；",
        "`research_required`=未知事实（派单字段调研 subagent 带回 evidence_refs）；`pending`=尚未处理。"
        "当前价格/在售性/最新兼容性/基准等外部事实在查到具体来源前不得标 confirmed。",
        "- 对每个 `research_required` 字段，用 Agent 派**只填这一个字段**的窄调研 subagent；它把该字段 JSON 交回，你合并进表。",
        "- 每回填一个字段，若引出新的未知项，作为新的 `pending` 字段加进同一张表（差集=新字段，自动增殖）。",
        "- **只回传空缺**：系统只告诉你还差哪些 `pending` 字段；你照着补，不会因为没一次交齐而失败。",
        "- `loop-artifacts/` 下的长文档（契约/输入包/提交模板）由子代理读取；Commander 自身直接维护字段表，不要再派发任务卡。",
        "",
        "## 提交（用命令，不要输出 token）",
        "",
        "字段 + 本阶段 required_outputs 齐全后，**用命令显式推进**——运行时不会解析聊天里的 `<RALPH_STAGE_RESULT>` token（只有 stage 01 字段齐全会**自动**推进）。",
        "正确动作：",
        "1. 若本阶段字段有更新，先落盘：`ralph field-apply . loop-artifacts/stages/%s/%s/fields.json`（或写入同目录字段增量文件）。" % (stage_id, revision),
        "2. 写 advance 动作文件 `loop-artifacts/stages/%s/%s/advance.json`：" % (stage_id, revision),
        "```json",
        "{",
        '  "action": "advance",',
        '  "status": "passed",',
        f'  "stage_id": "{stage_id}",',
        f'  "revision": "{revision}",',
        '  "next_stage": "<节点图上本阶段的后继 id>",',
        '  "payload": { "stage_review": "<简述已满足的字段条件与依据>", ',
        '                "task_spec": "<即 loop-state.json 里的 task_spec（含完整 attribute_matrix）>" }',
        "}",
        "```",
        "3. 运行 **`ralph apply . loop-artifacts/stages/%s/%s/advance.json`**（等效 `ralph validate --result ... --apply`）即完成推进；运行时自动校验、原子落盘。" % (stage_id, revision),
        "",
        "只有「用户/项目/环境都无答案、不能推断或研究、且会改变硬可行性/硬预算/验收」的字段，",
        "才在 `payload.questions` 一次性提问；否则不要用 `blocked_human` 卡住。",
    ]
    if stage_id == "01":
        lines.extend(
            [
                "",
                "## 01：目标 / 背景 / 约束 + 分解（字段化）",
                "",
                "把目标、范围、约束、已知背景整理为字段写入 `attribute_matrix`；",
                "不确定偏好用 `assumed_default`（默认全范围），未知事实用 `research_required` 派调研；"
                "01 只记录“哪些事实未知”，不把训练记忆中的当前价格、基准或最新规格写成已证实事实。",
                "同时把目标拆成分解项记为 concept，其需要的事实标 research_required，供 02 调研。",
                "读 `loop-artifacts/contracts/01-r1-stage-contract.md` 与输入包确认验收标准所需的字段集合。",
            ]
        )
    elif stage_id == "02":
        lines.extend(
            [
                "",
                "## 02：调研分解结果（字段化）",
                "",
                "对 01 的每个 `research_required` 字段派窄调研 subagent，把结果写回 `attribute_matrix`（带具体 evidence_refs）。"
                "站点首页无效；当前市场事实须额外填 observed_at（ISO 日期）。",
                "若同一字段的 WebSearch/WebFetch 连续失败、且已配置两个网页 LLM，可运行 `ralph web-llm-check` 询问具体来源线索；"
                "LLM 回执不是一手证据，必须据此再验证实际页面，做不到就保留 research_required/uncertain。",
                "调研完成字段置 `confirmed` / `assumed_default`；引出新未知项作为 `pending` 字段增殖，直到无 `pending`。",
                "同时为每个分解项整理「后续执行需要什么」雏形，供 03 细化。本阶段不做交叉验证（在 02.5）。",
            ]
        )
    elif stage_id == "02.5":
        lines.extend(
            [
                "",
                "## 02.5：调研后交叉验证（字段化）",
                "",
                "对 02 的每个关键调研字段，逐字段派 subagent 去问各种网页 LLM + 权威数据，检查矛盾与冲突。",
                "每张派发卡内嵌该字段的当前内容（concept/attribute/disposition/evidence/rationale）作为参数；subagent 不读无关文档。",
                "网页 LLM 清单与做法见 `loop/1-loop/02.5-交叉验证.md`。比较不同 LLM / 来源答案，更新字段 confidence/disposition/evidence_refs/rationale，并产出交叉验证摘要。"
                "交付必须有 validation_records（每条 claim_ref 的两个独立来源、observed_at、verdict），不能用一段“已验证”摘要过关。",
            ]
        )
    elif stage_id == "03":
        lines.extend(
            [
                "",
                "## 03：执行任务分解（含调研 + 后续行动）（字段化）",
                "",
                "把已调研、已交叉验证的分解项细化为 role=task_graph 的结构化 DAG 并执行；含调研子任务与后续行动子任务。"
                "attribute 中的自然语言节点列表无效。",
                "每个节点必须先写出 node.writes 声明的实际非空文件，再运行 `ralph graph-apply`；调研子任务继续填 `attribute_matrix` 并产出 `evidence_refs`。",
            ]
        )
    elif stage_id == "04":
        lines.extend(
            [
                "",
                "## 04：验证与交叉验证（字段化）",
                "",
                "把 03 产物整理成事实账本（claim ledger）写入 `attribute_matrix` / verification；每条 claim 带来源与状态。",
                "无来源或无法复核的标 uncertain / rejected。本阶段做「验证」，逐源交叉验证在 04.5。",
            ]
        )
    elif stage_id == "04.5":
        lines.extend(
            [
                "",
                "## 04.5：产出后交叉验证（字段化）",
                "",
                "对 04 的每条关键 claim，逐条派 subagent 去问各种网页 LLM + 权威数据，检查矛盾与冲突，给出最终置信度。",
                "每张派发卡内嵌该 claim 的当前内容（claim/source_url/source_type/status/rationale）作为参数。",
                "网页 LLM 清单与做法见 `loop/1-loop/04.5-交叉验证.md`。更新 claim 的 status/checked_by，并产出最终交叉验证摘要。",
            ]
        )
    elif stage_id == "exploration":
        lines.extend(
            [
                "",
                "## 探索：自主发现新任务并写回任务板（字段化）",
                "",
                "先读 `tasks/TASKS.md` 并跑 `ralph task-next .`；有 ready 任务则 selected_task + selection_mode=task_board 进入 01。",
                "无 ready 任务时，自主做轻量调研发现 1~3 个候选方向，并直接把每个候选写成 `tasks/TASKS.md` 的新表格行（ID / 任务(目标) / 状态 / 优先级 / 依赖 / 背景），即入队。",
                "写完后重跑 `ralph task-next .` 选最高优先级 ready 任务进入 01；其「背景」列作为 01 输入。",
            ]
        )
    return "\n".join(lines) + "\n"



def stage_contract_text(state: Mapping[str, Any]) -> str:
    stage = state.get("stage", {})
    stage_id = str(stage.get("id", "01"))
    revision = str(stage.get("revision", "r1"))
    cards = cards_for_current_stage(state)
    submission_ref = stage_submission_template_ref(stage_id, revision)
    # Field-centric mode: the Commander maintains a single field table and commits
    # it via the <RALPH_STAGE_RESULT> action; the assemble/validate card flow
    # is intentionally absent.  Emit a field-table contract instead so a freshly
    # materialized contract file does not re-teach the old card workflow.
    if field_mode_enabled():
        return _field_contract_text(state, stage_id=stage_id, revision=revision)
    lines = [
        "# RALPH 阶段契约",
        "",
        f"阶段：{stage_id}-{revision}",
        "",
        "## 固定提交接口",
        "",
        "本阶段推进采用「builder 构造 + gate 审计 + assemble 合成」的填空式流程；Commander 只做编排，不内联大段 payload：",
        "1. 若有 builder 构造卡（角色含 `-writer`/`-assembler`），先逐个派发；它在 `loop-artifacts/stages/<stage>/<rev>/<key>.json` 写好一个 payload 切片后返回。",
        "2. 待所有 builder 完成，再派发独立阶段门禁（auditor）卡；它读取合成结果并只返回 `<RALPH_GATE_REVIEW>`。",
        "3. 门禁完成后运行 `ralph assemble` 把切片合成为 `loop-artifacts/stages/<stage>-<rev>-result.json`，并自动注入门禁回执。",
        "4. 运行 `ralph validate --result <结果路径>` 机械复核；若有字段问题，让对应 builder 改切片后重跑 assemble，不要手工改大 JSON。",
        "5. 复核通过后运行 `ralph validate --result <结果路径> --apply` 提交；或在最后直接输出一个 `<RALPH_STAGE_RESULT>`（其内部即该结果文件内容）。",
        "exploration 尾节点无 builder，直接按下方契约输出 exploration payload 即可。",
        "任务卡、阶段契约、输入包和提交模板由运行时物化；Commander 不得用 Agent、Write 或 Edit 创建/修复它们（builder 写切片是运行时批准的例外）。",
        "任务卡为 `dispatched` 时表示内部子代理正在运行，不是 `blocked_human`；不得重派或循环读取 `loop-events.md`，等待 `SubagentStop`。",
        "",
        "## 通用语义分解规则",
        "",
        _semantic_contract(),
        "",
    ]
    if stage_id == "01":
        lines.extend(
            [
                "## 01：主动澄清与遗漏分析",
                "",
                "必须形成 `task_spec`：semantic_map、attribute_matrix、约束、假设、一次性问题包、场景分支和成功标准。",
                "先读取项目内上下文；对会改变任务图或结论的未知项执行需求分流闸门，只有无法确认、推断、研究且不能场景化的事项才主动追问。",
                "完成前必须派发 requirements-auditor；本阶段禁止 deep-research、Skill、WebSearch、WebFetch 和最终推荐。",
            ]
        )
    elif stage_id == "02":
        lines.extend(
            [
                "## 02：调研分解结果",
                "",
                "对 01 的每个 research_required 字段派窄调研 subagent，把结果写回 attribute_matrix（带 evidence_refs）。",
                "调研完成字段置 confirmed / assumed_default；引出新未知项作为 pending 字段增殖。",
                "同时为每个分解项整理「后续执行需要什么」雏形，供 03 细化。本阶段不做交叉验证（在 02.5）。",
                "完成前必须派发 dag-auditor。",
            ]
        )
    elif stage_id == "02.5":
        lines.extend(
            [
                "## 02.5：调研后交叉验证",
                "",
                "对 02 的每个关键调研字段，逐字段派 subagent 去问各种网页 LLM + 权威数据，检查矛盾与冲突。",
                "每张派发卡内嵌该字段的当前内容（concept/attribute/disposition/evidence/rationale）作为参数。",
                "网页 LLM 清单与做法见 loop/1-loop/02.5-交叉验证.md；比较答案后更新字段置信度并产出交叉验证摘要。",
                "完成前必须派发 cross-validation-auditor。",
            ]
        )
    elif stage_id == "03":
        lines.extend(
            [
                "## 03：执行任务分解（含调研 + 后续行动）",
                "",
                "把已调研、已交叉验证的分解项细化为可执行子任务图并执行；含调研子任务与后续行动子任务。",
                "只能派发当前 ready 任务的已批准任务卡；不得裸派 Agent，也不得跨任务代替决策。",
                "所有 DAG 节点完成后才会出现 execution-join-auditor；该独立门禁完成前禁止进入 04。",
            ]
        )
    elif stage_id == "04":
        lines.extend(
            [
                "## 04：验证与交叉验证",
                "",
                "把 03 产物整理成事实账本（claim ledger）；每条 claim 带来源链接、来源类型、复核者和状态。",
                "无来源或无法复核的断言必须标 uncertain/rejected，不能进入最终推荐。",
                "本阶段做「验证」（事实账本 + 一致性核验）；逐源交叉验证在 04.5。",
                "完成前必须派发 evidence-verifier。",
            ]
        )
    elif stage_id == "04.5":
        lines.extend(
            [
                "## 04.5：产出后交叉验证",
                "",
                "对 04 的每条关键 claim，逐条派 subagent 去问各种网页 LLM + 权威数据，检查矛盾与冲突，给出最终置信度。",
                "每张派发卡内嵌该 claim 的当前内容（claim/source_url/source_type/status/rationale）作为参数。",
                "网页 LLM 清单与做法见 loop/1-loop/04.5-交叉验证.md（与 02.5 同一清单）。",
                "完成前必须派发 cross-validation-auditor。",
            ]
        )
    elif stage_id == "05":
        lines.extend(
            [
                "## 05：可追溯决策（新管线已弃用，仅兼容旧任务）",
                "",
                "必须把选择、拒绝选项、证据引用、残余风险与需要人类确认的价值判断分开写清。",
                "完成前必须派发 decision-auditor；事实不足时回到 03 或 04，而不是用语言掩盖。",
            ]
        )
    elif stage_id == "06":
        lines.extend(
            [
                "## 06：交接与队列（新管线已弃用，仅兼容旧任务）",
                "",
                "必须留下可恢复的交付物、决策引用、遗留事项、人类阻塞项、候选队列和恢复指令。",
                "完成前必须派发 handoff-auditor；候选任务只能入队，不能被静默执行。",
            ]
        )
    elif stage_id == "exploration":
        lines.extend(
            [
                "## 探索：自主发现新任务并写回任务板（尾节点，非终止）",
                "",
                "先读取项目 `tasks/TASKS.md`，必要时运行只读命令 `ralph task-next .`，看是否有依赖已满足的 ready/pending 任务。",
                "有可接取任务时，必须在 `payload.exploration.selected_task` 完整记录 task_id、title、source、source_path、priority 和 reason，并以 `selection_mode=task_board` 重新进入 01。",
                "没有可接取任务时，必须**自主发现新任务**：围绕用户目标 / 项目缺口 / 已有研究，做一轮轻量调研（WebSearch、读 memory/），生成 1~3 个候选方向。",
                "对每个候选方向，**直接把它写成 `tasks/TASKS.md` 的新表格行**（列：ID、任务(目标)、状态=pending/ready、优先级、依赖、背景）——即「入队」，不是只在内存返回 candidate，也不是静默执行。",
                "写完后再次运行 `ralph task-next .` 选出最高优先级 ready 任务，以 `selection_mode=task_board` 进入 01，用其「背景」列作为 01 的输入澄清背景与目标。",
                "候选必须包含研究摘要、理由和范围；写进任务板的条目才是可接取任务。完成前必须派发 exploration-auditor（审计任务板扫描、发现依据、写入的任务条目）。",
            ]
        )
    else:
        lines.extend(["## 当前阶段", "", "按节点输入、输出、条件和批准的任务卡执行；不得跳过验证。"])

        if cards:
            lines.extend(["", "## 已批准的子代理任务卡", ""])
            for card in cards:
                status = str(card.get("status", "pending"))
                kind = "builder 构造" if not card.get("is_stage_gate") else "gate 审计"
                lines.append(f"- `{card['id']}`：{card['title']}（{kind}；{status}）— `{card['card_ref']}`")
    return "\n".join(lines).rstrip() + "\n"


def task_card_text(state: Mapping[str, Any], card: Mapping[str, Any]) -> str:
    task = state.get("task", {}) if isinstance(state.get("task"), Mapping) else {}
    lines = [
        "# RALPH 子代理任务卡",
        "",
        f"- **Card ID**: `{card['id']}`",
        f"- **阶段**: `{card['stage_id']}-{card['revision']}`",
        f"- **角色**: `{card['role']}`",
        f"- **标题**: {card['title']}",
        f"- **任务目标**: {card['objective']}",
        f"- **原始任务**: {task.get('description', '')}",
        "",
        "## 必读文件",
        "",
    ]
    lines.extend(f"- `{ref}`" for ref in card.get("document_refs", []))
    if card.get("context_mode") == "bounded_artifacts":
        lines.extend(
            [
                "",
                "## 上下文隔离",
                "",
                "你是独立门禁审计代理：不得依赖 Commander 主对话、隐藏推理或未列出的历史资料。",
                "只以本卡列出的阶段输入包、阶段契约和提交模板作判断；输入不足时应给出 rollback 或 blocked_human，而不是猜测。",
            ]
        )
    lines.extend(["", "## 执行边界", ""])
    lines.extend(f"{index}. {item}" for index, item in enumerate(card.get("instructions", []), start=1))
    if not card.get("is_stage_gate"):
        slice_ref = (card.get("input_refs") or ["loop-artifacts/stages/<stage>/<rev>/<key>.json"])[0]
        lines.extend(
            [
                "",
                f"**切片填写方式（关键）**：`{slice_ref}` 已由运行时预生成为骨架（结构完整、含占位/示例值）。",
                f"你**必须用 Write 工具把整个填充后的切片写入 `{slice_ref}`**（直接整体覆盖骨架），不要只返回 JSON 文本。",
                "**严禁把 JSON 作为纯文本返回**：只有写入了 `{slice_ref}` 文件才算完成；只回自然语言会被判定为未提交并退回重做。",
                "**增量填写**：`semantic_map` 中仍为空数组的语义角色才需要补充；已填角色不要重写，只针对空角色补真实条目，"
                "并补上对应 `attribute_matrix` 叶节点（concept/role/attribute/disposition/rationale，disposition∈{confirmed,inferred,assume,research}）。"
                "七类角色（background/decision_object/objective/comparison_set/constraints/deliverable/uncertainty）都非空后才算完成。",
                "若 Commander 派发时附带门禁回执（`<RALPH_GATE_REVIEW>`），只修正回执中 `status:\"fail\"` 的 check 对应的字段，其余保持不变。",
            ]
        )
    lines.extend(["", "## 允许工具", "", ", ".join(f"`{tool}`" for tool in card.get("allowed_tools", [])) or "- 无", ""])
    if card.get("output_schema"):
        lines.extend(["## 输出接口", "", "```json", json.dumps(card["output_schema"], ensure_ascii=False, indent=2, sort_keys=True), "```", ""])
    if card.get("is_stage_gate"):
        review_template = _stage_review_template(state)
        review_template["reviewer_card_id"] = str(card["id"])
        lines.extend(
            [
                "## 必填门禁回执模板",
                "",
                "完成时必须填写下列 JSON，并用 `<RALPH_GATE_REVIEW>` 标记返回给 Commander。",
                "如果任何检查失败、不确定或需要人类输入，填写 `rollback` 或 `blocked_human`，不要伪造 `pass`。",
                "",
                "```json",
                json.dumps(review_template, ensure_ascii=False, indent=2, sort_keys=True),
                "```",
                "",
            ]
        )
    lines.extend(
        [
            "## 返回给 Commander 的格式",
            "",
            "- 已确认事实 / 来源 / 适用条件",
            "- 不确定或冲突项",
            "- 对应任务卡的结构化结论",
            "- 不要修改 `loop-state.json`，不要替 Commander 决定后续阶段。",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def _write_if_changed(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return
    path.write_text(content, encoding="utf-8")


def materialize_contract_documents(root: str | Path, state: Mapping[str, Any]) -> list[str]:
    """Write deterministic, project-local stage contract documents.

    Field mode never materializes the historical card directory.  The active
    dispatch surface is ``stages/<stage>/<revision>/tasks/*.json``.
    """

    root = Path(root)
    stage = state.get("stage", {})
    stage_id = str(stage.get("id", "01"))
    revision = str(stage.get("revision", "r1"))
    task_spec_path = root / CONTRACT_DIR / "task-spec.json"
    task_spec = {
        "task": state.get("task", {}),
        "task_spec": state.get("task_spec", {}),
        "stage": {"id": stage_id, "revision": revision},
    }
    _write_if_changed(task_spec_path, json.dumps(task_spec, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    input_package_ref = stage_input_package_ref(stage_id, revision)
    _write_if_changed(
        root / input_package_ref,
        json.dumps(stage_input_package(state), ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    )
    submission_ref = stage_submission_template_ref(stage_id, revision)
    _write_if_changed(
        root / submission_ref,
        json.dumps(stage_submission_template(state), ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    )
    contract_ref = f"{CONTRACT_DIR}/{stage_id}-{revision}-stage-contract.md"
    _write_if_changed(root / contract_ref, stage_contract_text(state))
    written = [str(task_spec_path.relative_to(root)), input_package_ref, submission_ref, contract_ref]
    if not field_mode_enabled():
        for card in cards_for_current_stage(state):
            ref = normalize_card_ref(str(card.get("card_ref", "")))
            if ref is None:
                continue
            _write_if_changed(root / ref, task_card_text(state, card))
            written.append(ref)
    return written
