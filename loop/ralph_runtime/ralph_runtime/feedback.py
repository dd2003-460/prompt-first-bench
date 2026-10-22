"""Short, actionable feedback messages for Claude Code Hook decisions.

The Hook must not merely say that a tool or result is invalid.  Local models
need a bounded correction loop: what was detected, what to stop doing, and the
one next action that can make progress.  Keeping the framing here makes the
feedback stable, searchable, and easy to test without copying transcripts.
"""

from __future__ import annotations

from typing import Any


def render_feedback(
    code: str,
    *,
    detected: str,
    correction: str,
    next_action: str,
    forbidden: str = "",
    expected: str = "",
) -> str:
    """Render one compact, model-facing correction prompt."""

    lines = [
        f"RALPH_FEEDBACK[{code}]",
        f"已检测到：{detected}",
        f"立即修正：{correction}",
        f"唯一下一步：{next_action}",
    ]
    if forbidden:
        lines.append(f"禁止：{forbidden}")
    if expected:
        lines.append(f"输出要求：{expected}")
    return "\n".join(lines)


def protocol_feedback(
    *,
    error: str,
    action: str | None,
    expected: str,
    correction: str | None = None,
    next_action: str | None = None,
    preserve_action: bool = True,
) -> str:
    """Feedback for a rejected RALPH_STAGE_RESULT."""

    action_hint = (
        f"已识别原输出动作 `{action}`；保留这个真实动作，只补齐缺失字段。"
        if action and preserve_action
        else (
            f"原输出动作 `{action}` 与当前状态/门禁条件冲突；不要强行保留，"
            "根据校验结果选择合法分支。"
            if action
            else "原输出没有可识别动作；根据刚才真实完成情况选择合法动作，不要猜测或伪造通过。"
        )
    )
    return render_feedback(
        "STAGE_RESULT_INVALID",
        detected=f"RALPH_STAGE_RESULT 校验失败：{error}",
        correction=correction or f"{action_hint}只修复协议，不重做当前阶段。",
        next_action=next_action or "停止工具调用，直接返回一次完整的 <RALPH_STAGE_RESULT> JSON。",
        forbidden="READY、自然语言结论、Bash、cat、echo、Write、Edit 和 ralph apply。",
        expected=expected,
    )


def gate_feedback(*, card_id: str, error: str, expected: str) -> str:
    """Feedback for an invalid bounded subagent gate receipt."""

    return render_feedback(
        "GATE_RECEIPT_INVALID",
        detected=f"任务卡 `{card_id}` 的独立门禁回执未通过：{error}",
        correction="只把已有审计结论改写为门禁协议，不新增调研、不读取其他文件。",
        next_action="直接返回一次完整的 <RALPH_GATE_REVIEW> JSON。",
        forbidden="Bash、Write、Edit、继续搜索、重新派发或解释性长文。",
        expected=expected,
    )


def tool_feedback(
    code: str,
    *,
    detected: str,
    correction: str,
    next_action: str,
    forbidden: str = "",
) -> str:
    """Alias used by tool policies to keep their messages uniform."""

    return render_feedback(
        code,
        detected=detected,
        correction=correction,
        next_action=next_action,
        forbidden=forbidden,
    )


def feedback_context(value: Any, limit: int = 400) -> str:
    """Bound arbitrary diagnostic details before inserting them in feedback."""

    text = str(value or "").replace("\x00", " ").strip()
    if len(text) <= limit:
        return text
    return text[: max(1, limit - 40)] + "\n[… 反馈细节已截断 …]"
