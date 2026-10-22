from pathlib import Path
import json
import subprocess

from ralph_runtime import prompt_first
import ralph_runtime.cli as cli


def reviewer_output(verdict: str, repair_stage: str = "none", finding: str = "测试审阅"):
    return (
        f"## Reviewer findings\n\n{finding}\n\n"
        "<!-- ralph-review\n"
        f"verdict: {verdict}\n"
        f"repair_stage: {repair_stage}\n"
        "-->\n"
    )


def write_current(root: Path, text: str = "# 当前阶段记录\n") -> Path:
    state = prompt_first.load_state(root)
    artifact = root / state["current_artifact"]
    artifact.write_text(text, encoding="utf-8")
    return artifact


def pass_current(root: Path) -> None:
    prompt_first.record_reviewer_result(root, reviewer_output("pass"))
    state = prompt_first.load_state(root)
    artifact = root / state["current_artifact"]
    artifact.write_text(
        artifact.read_text(encoding="utf-8").rstrip()
        + "\n"
        + prompt_first.DONE_MARKER
        + "\n",
        encoding="utf-8",
    )


def fake_reviewer(monkeypatch, outputs):
    """Return deterministic reviewer output without launching Claude."""

    calls = []

    def fake_run(command, **kwargs):
        calls.append((command, kwargs))
        return subprocess.CompletedProcess(command, 0, next(outputs), "")

    monkeypatch.setattr(prompt_first.subprocess, "run", fake_run)
    return calls


def test_initialize_creates_markdown_cursor_and_external_stage_rules(tmp_path: Path):
    state = prompt_first.initialize(tmp_path, "完善一份面向大众的动机社会章节")

    assert state["stage"] == "01"
    assert not (tmp_path / "loop-state.json").exists()
    cursor = (tmp_path / "ralph-loop.md").read_text(encoding="utf-8")
    artifact = tmp_path / state["current_artifact"]
    document = artifact.read_text(encoding="utf-8")
    rules = prompt_first.load_stage_rules(tmp_path, "01")
    assert "ralph-prompt-state" in cursor
    assert "## 原始任务（请勿改写）" in cursor
    assert "## 当前阶段工作记录" in document
    assert "Reviewer 回执" in document
    assert "将任务拆成互相区分" in rules["text"]
    assert prompt_first.DONE_MARKER not in document


def test_default_init_creates_prompt_first_scaffold_then_adopts_first_task(tmp_path: Path):
    project = tmp_path / "new-project"

    assert cli.main(["init", str(project)]) == 0
    assert (project / "ralph-loop.md").exists()
    assert not (project / "loop-state.json").exists()

    adopted = prompt_first.initialize(project, "完整的第一项任务")
    document = (project / adopted["current_artifact"]).read_text(encoding="utf-8")

    assert adopted["task"] == "完整的第一项任务"
    assert "完整的第一项任务" in document


def test_reviewer_pass_allows_done_without_content_quality_gate(tmp_path: Path):
    prompt_first.initialize(tmp_path, "测试 prompt-first")
    write_current(tmp_path, "# 很短但明确的阶段记录\n")

    receipt = prompt_first.record_reviewer_result(
        tmp_path,
        reviewer_output("pass", "none", "Reviewer 认为当前版本可交接"),
    )
    assert receipt["verdict"] == "pass"
    pass_current(tmp_path)

    advanced, changed = prompt_first.advance_if_marked_done(tmp_path)

    assert changed is True
    assert advanced["stage"] == "02"
    assert (tmp_path / advanced["current_artifact"]).is_file()


def test_structured_reviewer_output_is_rendered_to_markdown_receipt(tmp_path: Path):
    prompt_first.initialize(tmp_path, "测试结构化 Reviewer 回执")
    write_current(tmp_path, "# 当前阶段记录\n")
    structured = json.dumps(
        {
            "report": "缺少来源交叉验证。",
            "findings": [
                {
                    "location": "来源表",
                    "impact": "无法判断关键主张是否可靠",
                    "evidence_gap": "只有单一来源",
                    "repair_action": "补充独立来源并记录冲突",
                }
            ],
            "verdict": "revise",
            "repair_stage": "01",
        },
        ensure_ascii=False,
    )

    receipt = prompt_first.record_reviewer_result(tmp_path, structured)

    assert receipt["verdict"] == "revise"
    document = (tmp_path / prompt_first.LATEST_REVIEW).read_text(encoding="utf-8")
    assert "缺少来源交叉验证" in document
    assert "来源表" in document
    assert "verdict: revise" in document


def test_reviewer_revise_keeps_stage_and_returns_findings_to_same_context(tmp_path: Path):
    prompt_first.initialize(tmp_path, "测试同阶段返修")
    write_current(tmp_path, "# 仍不完整\n")
    prompt_first.record_reviewer_result(
        tmp_path,
        reviewer_output("revise", "01", "缺少关键证据，不能交给下一阶段"),
    )

    unchanged, changed = prompt_first.advance_if_marked_done(tmp_path)
    response = prompt_first.handle_stop({"cwd": str(tmp_path)})

    assert changed is False
    assert unchanged["stage"] == "01"
    assert prompt_first.load_state(tmp_path)["stage"] == "01"
    assert response["decision"] == "block"
    assert "独立 Reviewer 上一轮判定 revise" in response["reason"]
    assert "缺少关键证据" in response["reason"]


def test_missing_reviewer_does_not_advance_even_with_done_marker(tmp_path: Path):
    state = prompt_first.initialize(tmp_path, "测试缺少 Reviewer")
    first = tmp_path / state["current_artifact"]
    first.write_text("# 有完成标记但没有 Reviewer\n\n<!-- ralph: done -->\n", encoding="utf-8")

    unchanged, changed = prompt_first.advance_if_marked_done(tmp_path)

    assert changed is False
    assert unchanged["stage"] == "01"


def test_reviewer_after_done_cannot_authorize_advance(tmp_path: Path):
    prompt_first.initialize(tmp_path, "测试 Reviewer 顺序")
    artifact = write_current(tmp_path, "# 先错误写入完成标记\n")
    artifact.write_text(
        artifact.read_text(encoding="utf-8").rstrip()
        + "\n"
        + prompt_first.DONE_MARKER
        + "\n",
        encoding="utf-8",
    )

    receipt = prompt_first.record_reviewer_result(tmp_path, reviewer_output("pass"))
    unchanged, changed = prompt_first.advance_if_marked_done(tmp_path)

    assert receipt["verdict"] == "unknown"
    assert changed is False
    assert unchanged["stage"] == "01"
    assert "reviewed_before_done: false" in (
        tmp_path / prompt_first.LATEST_REVIEW
    ).read_text(encoding="utf-8")


def test_reviewer_receipt_expires_when_main_artifact_changes(tmp_path: Path):
    prompt_first.initialize(tmp_path, "测试过期回执")
    artifact = write_current(tmp_path)
    prompt_first.record_reviewer_result(tmp_path, reviewer_output("pass"))
    artifact.write_text(artifact.read_text(encoding="utf-8") + "\n新增但未复核内容\n", encoding="utf-8")
    artifact.write_text(artifact.read_text(encoding="utf-8") + prompt_first.DONE_MARKER + "\n", encoding="utf-8")

    unchanged, changed = prompt_first.advance_if_marked_done(tmp_path)

    assert changed is False
    assert unchanged["stage"] == "01"


def test_stop_hook_advances_only_after_reviewer_pass_and_done(tmp_path: Path):
    prompt_first.initialize(tmp_path, "测试 Stop Hook")
    write_current(tmp_path, "# 阶段一\n")
    pass_current(tmp_path)

    response = prompt_first.handle_stop({"cwd": str(tmp_path)})

    assert response["decision"] == "block"
    assert "current Claude context" in response["systemMessage"]
    assert prompt_first.load_state(tmp_path)["stage"] == "02"
    assert "资料搜集" in response["reason"]


def test_prompt_uses_external_rules_and_requires_reviewer(tmp_path: Path):
    prompt_first.initialize(tmp_path, "测试首写")
    prompt = prompt_first.render_prompt(tmp_path)

    assert prompt.startswith("这是当前阶段的自动模板；阶段游标、任务、目标路径和规则正文已经由 runtime 注入，")
    assert "初始模板先只调用一次 Read" in prompt
    assert "第一步只调用一次 Read" in prompt
    assert "阶段规则来源：" in prompt
    assert "将任务拆成互相区分" in prompt
    assert "ralph prompt-first review ." in prompt
    assert "Reviewer 未通过时继续当前阶段" in prompt


def test_repair_prompt_writes_directly_without_reopening_same_artifact(tmp_path: Path):
    prompt_first.initialize(tmp_path, "测试修订轮次不重复读取")
    write_current(tmp_path, "# 第一版\n")
    prompt_first.record_reviewer_result(
        tmp_path,
        reviewer_output("revise", "01", "补充缺失的时间线与证据"),
    )

    prompt = prompt_first.render_prompt(tmp_path, reason="独立 Reviewer 判定 revise")

    assert prompt.startswith("这是同一 Claude 会话中的修订轮次；当前工件已经在本会话读取过。")
    assert "下一条 assistant 消息必须直接发出唯一的 Write tool call" in prompt
    assert "用 Write 完整重写当前 Markdown" in prompt
    assert "只有 Write 被 Claude 拒绝时才允许补一次 Read" in prompt


def test_research_rules_are_loaded_at_stage_two(tmp_path: Path):
    prompt_first.initialize(tmp_path, "测试浏览器范围")
    write_current(tmp_path, "# 阶段一\n")
    pass_current(tmp_path)
    prompt_first.advance_if_marked_done(tmp_path)

    stage_two_prompt = prompt_first.render_prompt(tmp_path)

    assert "最近 7 天" in stage_two_prompt
    assert "至少寻找两个相互独立的来源" in stage_two_prompt
    assert "ralph prompt-first web-llm ." in stage_two_prompt
    assert "必须 revise" in stage_two_prompt


def test_reviewer_can_route_back_to_an_earlier_stage(tmp_path: Path):
    prompt_first.initialize(tmp_path, "测试回退阶段")
    write_current(tmp_path, "# 阶段一\n")
    pass_current(tmp_path)
    prompt_first.advance_if_marked_done(tmp_path)
    assert prompt_first.load_state(tmp_path)["stage"] == "02"

    write_current(tmp_path, "# 阶段二有问题\n")
    prompt_first.record_reviewer_result(
        tmp_path,
        reviewer_output("revise", "01", "阶段二发现阶段一分解遗漏，必须回补"),
    )
    prompt_first.handle_stop({"cwd": str(tmp_path)})

    assert prompt_first.load_state(tmp_path)["stage"] == "01"
    assert "阶段二发现阶段一分解遗漏" in prompt_first.render_prompt(tmp_path)


def test_reviewer_pass_completes_all_stages(tmp_path: Path):
    prompt_first.initialize(tmp_path, "完成测试")
    for _ in prompt_first.STAGES:
        write_current(tmp_path, "# 当前阶段的最小记录\n")
        pass_current(tmp_path)
        prompt_first.advance_if_marked_done(tmp_path)

    assert prompt_first.load_state(tmp_path)["status"] == "completed"


def test_final_stage_prompt_uses_external_final_review_rules(tmp_path: Path):
    prompt_first.initialize(tmp_path, "最终复核测试")
    for _ in ("01", "02", "02.5", "03", "04"):
        write_current(tmp_path, "# 当前阶段记录\n")
        pass_current(tmp_path)
        prompt_first.advance_if_marked_done(tmp_path)

    prompt = prompt_first.render_prompt(tmp_path)

    assert "阶段 04.5" in prompt
    assert "原始任务是否全部得到回应" in prompt
    assert "ralph prompt-first review ." in prompt


def test_prompt_first_review_command_persists_independent_receipt(tmp_path: Path, monkeypatch, capsys):
    prompt_first.initialize(tmp_path, "测试 reviewer 命令")
    write_current(tmp_path, "# 可审阅的阶段记录\n")
    monkeypatch.setenv("RALPH_PROMPT_FIRST_REVIEW_TRANSPORT", "claude")

    def fake_run(command, **kwargs):
        assert "-p" in command
        assert "--tools" in command
        assert command[command.index("--tools") + 1] == ""
        assert "当前 Markdown 工件快照" in command[-1]
        return subprocess.CompletedProcess(command, 0, reviewer_output("revise", "01", "发现缺口"), "")

    monkeypatch.setattr(cli, "_claude_executable", lambda: "claude")
    monkeypatch.setattr(cli.subprocess, "run", fake_run)

    assert cli.prompt_first_review_project(tmp_path) == 0
    output = capsys.readouterr().out
    assert '"verdict": "revise"' in output
    assert (tmp_path / prompt_first.LATEST_REVIEW).is_file()
    assert "发现缺口" in (tmp_path / prompt_first.LATEST_REVIEW).read_text(encoding="utf-8")


def test_stop_hook_automatically_launches_real_reviewer_and_records_pending(tmp_path: Path, monkeypatch):
    prompt_first.initialize(tmp_path, "测试 Stop Hook 自动 Reviewer")
    write_current(tmp_path, "# 尚未完整的阶段记录\n")
    calls = []

    calls = fake_reviewer(
        monkeypatch,
        iter([reviewer_output("revise", "01", "自动 Reviewer 发现证据缺口")]),
    )
    response = prompt_first.handle_stop({"cwd": str(tmp_path)})

    assert response["decision"] == "block"
    assert len(calls) == 1
    assert calls[0][0][1:5] == ["-m", "ralph_runtime.cli", "prompt-first", "review"]
    state = prompt_first.load_state(tmp_path)
    review = prompt_first.latest_reviewer_review(tmp_path)
    assert state["review_status"] == "complete"
    assert state["review_attempt"] == "1"
    assert review is not None
    assert review["verdict"] == "revise"
    assert review["reviewer_exit_code"] == "0"
    assert state["stage"] == "01"
    events = (tmp_path / "loop-events.md").read_text(encoding="utf-8")
    assert "prompt_first_reviewer_pending" in events
    assert "prompt_first_reviewer_finished" in events
    assert "自动 Reviewer 发现证据缺口" in response["reason"]


def test_invalid_reviewer_output_is_retried_without_advancing(tmp_path: Path, monkeypatch):
    prompt_first.initialize(tmp_path, "测试无效 Reviewer 自动重试")
    write_current(tmp_path, "# 尚未完整的阶段记录\n")
    calls = fake_reviewer(
        monkeypatch,
        iter([
            "Let me first read the current artifact.",
            reviewer_output("revise", "01", "第二次返回了可路由问题"),
        ]),
    )

    response = prompt_first.handle_stop({"cwd": str(tmp_path)})

    assert len(calls) == 2
    assert prompt_first.load_state(tmp_path)["stage"] == "01"
    assert prompt_first.load_state(tmp_path)["review_status"] == "complete"
    assert prompt_first.latest_reviewer_review(tmp_path)["verdict"] == "revise"
    assert "第二次返回了可路由问题" in response["reason"]
    events = (tmp_path / "loop-events.md").read_text(encoding="utf-8")
    assert '"attempt": "1"' in events
    assert '"attempt": "2"' in events


def test_stop_hook_passes_configured_reviewer_model_and_records_it(tmp_path: Path, monkeypatch):
    prompt_first.initialize(tmp_path, "测试 Reviewer 模型隔离")
    write_current(tmp_path, "# 阶段记录\n")
    monkeypatch.setenv("RALPH_PROMPT_FIRST_REVIEW_MODEL", "Qwen2.5-3B-Instruct-4bit")
    calls = fake_reviewer(monkeypatch, iter([reviewer_output("revise", "01")]))
    prompt_first.handle_stop({"cwd": str(tmp_path)})

    command, _ = calls[0]
    assert command[-2:] == ["--model", "Qwen2.5-3B-Instruct-4bit"]
    events = (tmp_path / "loop-events.md").read_text(encoding="utf-8")
    assert '"reviewer_model": "Qwen2.5-3B-Instruct-4bit"' in events


def test_stop_hook_passes_configured_reviewer_effort(tmp_path: Path, monkeypatch):
    prompt_first.initialize(tmp_path, "测试 Reviewer effort")
    write_current(tmp_path, "# 阶段记录\n")
    monkeypatch.setenv("RALPH_PROMPT_FIRST_REVIEW_EFFORT", "low")
    calls = fake_reviewer(monkeypatch, iter([reviewer_output("revise", "01")]))
    prompt_first.handle_stop({"cwd": str(tmp_path)})

    command, _ = calls[0]
    assert command[-2:] == ["--effort", "low"]
    events = (tmp_path / "loop-events.md").read_text(encoding="utf-8")
    assert '"reviewer_effort": "low"' in events


def test_stop_hook_revises_same_stage_then_re_reviews_before_advancing(tmp_path: Path, monkeypatch):
    prompt_first.initialize(tmp_path, "测试自动 Reviewer 同阶段闭环")
    artifact = write_current(tmp_path, "# 第一版\n")
    outputs = iter(
        [
            reviewer_output("revise", "01", "补充 RTX 50 系列时间线"),
            reviewer_output("pass", "none", "当前版本可以交接"),
        ]
    )
    calls = fake_reviewer(monkeypatch, outputs)
    first = prompt_first.handle_stop({"cwd": str(tmp_path)})
    assert prompt_first.load_state(tmp_path)["stage"] == "01"
    assert "补充 RTX 50 系列时间线" in first["reason"]

    artifact.write_text("# 第一版\n\n## 修复\n已补充 RTX 50 系列时间线。\n", encoding="utf-8")
    second = prompt_first.handle_stop({"cwd": str(tmp_path)})
    assert prompt_first.load_state(tmp_path)["stage"] == "01"
    assert prompt_first.latest_reviewer_review(tmp_path)["verdict"] == "pass"
    assert "现在才可以把" in second["reason"]
    assert len(calls) == 2

    artifact.write_text(artifact.read_text(encoding="utf-8").rstrip() + "\n" + prompt_first.DONE_MARKER + "\n", encoding="utf-8")
    fifth = prompt_first.handle_stop({"cwd": str(tmp_path)})
    assert prompt_first.load_state(tmp_path)["stage"] == "02"
    assert "资料搜集" in fifth["reason"]
    assert len(calls) == 2


def test_stop_hook_repairs_premature_done_before_running_reviewer(tmp_path: Path, monkeypatch):
    prompt_first.initialize(tmp_path, "测试完成标记顺序")
    artifact = write_current(tmp_path, "# 内容已写入\n\n" + prompt_first.DONE_MARKER + "\n")

    fake_reviewer(monkeypatch, iter([reviewer_output("pass")]))
    response = prompt_first.handle_stop({"cwd": str(tmp_path)})

    assert prompt_first.load_state(tmp_path)["stage"] == "01"
    assert prompt_first.DONE_MARKER not in artifact.read_text(encoding="utf-8")
    review = prompt_first.latest_reviewer_review(tmp_path)
    assert review["verdict"] == "pass"
    assert review["reviewed_before_done"] == "true"
    assert "现在才可以把" in response["reason"]

    artifact.write_text(artifact.read_text(encoding="utf-8").rstrip() + "\n" + prompt_first.DONE_MARKER + "\n", encoding="utf-8")
    prompt_first.handle_stop({"cwd": str(tmp_path)})
    assert prompt_first.load_state(tmp_path)["stage"] == "02"


def test_prompt_first_settings_only_install_markdown_stop_hook(tmp_path: Path):
    settings_path = cli.install_prompt_first_hooks(tmp_path)
    settings = json.loads(settings_path.read_text(encoding="utf-8"))

    assert settings["env"]["CLAUDE_CODE_AUTO_COMPACT_WINDOW"] == str(cli.DEFAULT_AUTO_COMPACT_WINDOW)
    assert settings["env"]["CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"] == str(cli.DEFAULT_AUTOCOMPACT_PERCENT)
    assert set(settings["hooks"]) == {"PreToolUse", "PostToolUse", "PreCompact", "PostCompact", "Stop"}
    assert "prompt-first-pre-tool" in settings["hooks"]["PreToolUse"][0]["hooks"][0]["command"]
    assert [item["matcher"] for item in settings["hooks"]["PostToolUse"]] == [".*"]
    assert settings["hooks"]["PostToolUse"][0]["continueOnBlock"] is False
    assert all("prompt-first-post-tool" in item["hooks"][0]["command"] for item in settings["hooks"]["PostToolUse"])
    assert "prompt-first-precompact" in settings["hooks"]["PreCompact"][0]["hooks"][0]["command"]
    assert "prompt-first-postcompact" in settings["hooks"]["PostCompact"][0]["hooks"][0]["command"]
    assert "prompt-first-stop" in settings["hooks"]["Stop"][0]["hooks"][0]["command"]


def test_prompt_first_compaction_hooks_persist_and_reconnect(tmp_path: Path):
    prompt_first.initialize(tmp_path, "测试上下文压缩续接")

    assert prompt_first.handle_precompact(
        {"cwd": str(tmp_path), "trigger": "auto"}
    ) == {}
    response = prompt_first.handle_postcompact(
        {
            "cwd": str(tmp_path),
            "trigger": "auto",
            "compact_summary": "old transcript summary",
        }
    )

    context = response["hookSpecificOutput"]["additionalContext"]
    assert "已完成上下文压缩" in context
    assert "不要重放旧对话" in context
    assert "01" in context
    events = (tmp_path / "loop-events.md").read_text(encoding="utf-8")
    assert "prompt_first_context_compaction_started" in events
    assert "prompt_first_context_compaction_completed" in events


def test_hard_context_error_detector_only_matches_overflow():
    assert "Prompt too long" in cli._context_error_excerpt(
        "API Error: 400 Prompt too long: 121391 tokens exceeds max context window of 120000"
    )
    assert cli._context_error_excerpt("普通的 context 说明，没有超限") is None


def test_prompt_first_post_tool_nudges_after_current_artifact_read(tmp_path: Path):
    prompt_first.initialize(tmp_path, "测试 Read 后继续")
    state = prompt_first.load_state(tmp_path)
    artifact = prompt_first.ensure_stage_document(tmp_path, state)
    result = prompt_first.handle_post_tool(
        {
            "cwd": str(tmp_path),
            "tool_name": "Read",
            "tool_input": {"file_path": str(artifact)},
        }
    )

    context = result["hookSpecificOutput"]["additionalContext"]
    assert "下一条 assistant 消息必须直接发出唯一的 Write" in context

    assert prompt_first.handle_post_tool(
        {
            "cwd": str(tmp_path),
            "tool_name": "Read",
            "tool_input": {"file_path": str(tmp_path / "ralph-loop.md")},
        }
    ) == {}


def test_prompt_first_post_tool_nudges_after_web_llm_receipt_read(tmp_path: Path):
    prompt_first.initialize(tmp_path, "测试网页回执后收束")
    pass_current(tmp_path)
    prompt_first.handle_stop({"cwd": str(tmp_path)})
    receipt = tmp_path / prompt_first.ARTIFACT_DIR / "02-web-llm-cross-check.md"
    receipt.write_text("# 网页回执\n- 状态：未授权\n", encoding="utf-8")

    result = prompt_first.handle_post_tool(
        {
            "cwd": str(tmp_path),
            "tool_name": "Read",
            "tool_input": {"file_path": str(receipt)},
        }
    )

    context = result["hookSpecificOutput"]["additionalContext"]
    assert "网页 LLM 回执已读完" in context
    assert "不要重复运行 web-llm" in context
    assert "Write" in context


def test_prompt_first_bounds_repeated_research_tools_before_write(tmp_path: Path):
    prompt_first.initialize(tmp_path, "测试研究工具重试上限")
    pass_current(tmp_path)
    prompt_first.handle_stop({"cwd": str(tmp_path)})

    results = [
        prompt_first.handle_post_tool(
            {
                "cwd": str(tmp_path),
                "tool_name": "WebSearch",
                "tool_input": {"query": f"gpu query {index}"},
            }
        )
        for index in range(4)
    ]

    assert all("只记录真实结果" in item["hookSpecificOutput"]["additionalContext"] for item in results)
    assert "已达到上限" in results[-1]["hookSpecificOutput"]["additionalContext"]
    assert results[-1]["decision"] == "block"
    assert "prompt_first_research_tool" in (tmp_path / "loop-events.md").read_text(encoding="utf-8")


def test_prompt_first_pre_tool_denies_only_redundant_research_calls(tmp_path: Path):
    prompt_first.initialize(tmp_path, "测试研究工具 PreToolUse 上限")
    pass_current(tmp_path)
    prompt_first.handle_stop({"cwd": str(tmp_path)})
    for index in range(4):
        prompt_first.handle_post_tool(
            {
                "cwd": str(tmp_path),
                "tool_name": "WebFetch",
                "tool_input": {"url": f"https://example.com/{index}"},
            }
        )

    denied = prompt_first.handle_pre_tool(
        {
            "cwd": str(tmp_path),
            "tool_name": "WebFetch",
            "tool_input": {"url": "https://example.com/extra"},
        }
    )
    ordinary = prompt_first.handle_pre_tool(
        {
            "cwd": str(tmp_path),
            "tool_name": "Bash",
            "tool_input": {"command": "echo still allowed"},
        }
    )

    assert denied["hookSpecificOutput"]["permissionDecision"] == "deny"
    assert "拒绝继续 Fetch" in denied["hookSpecificOutput"]["additionalContext"]
    assert ordinary == {}


def test_prompt_first_post_tool_asks_commander_to_stop_after_artifact_write(tmp_path: Path, monkeypatch):
    prompt_first.initialize(tmp_path, "测试 Write 后收束")
    state = prompt_first.load_state(tmp_path)
    artifact = prompt_first.ensure_stage_document(tmp_path, state)
    calls = fake_reviewer(monkeypatch, iter([reviewer_output("revise", "01", "测试 fallback 回执")]))
    result = prompt_first.handle_post_tool(
        {
            "cwd": str(tmp_path),
            "tool_name": "Write",
            "tool_input": {"file_path": str(artifact)},
        }
    )

    context = result["hookSpecificOutput"]["additionalContext"]
    assert "PostToolUse fallback" in context
    assert "下一条 assistant 消息必须直接发出唯一的 Write" in context
    assert "不要 Read、不要 Edit" in context
    assert "测试 fallback 回执" in context
    assert result["decision"] == "block"
    assert len(calls) == 1


def test_prompt_first_post_tool_still_reviews_when_done_marker_is_premature(tmp_path: Path, monkeypatch):
    prompt_first.initialize(tmp_path, "测试提前完成标记")
    state = prompt_first.load_state(tmp_path)
    artifact = prompt_first.ensure_stage_document(tmp_path, state)
    artifact.write_text(artifact.read_text(encoding="utf-8") + prompt_first.DONE_MARKER + "\n", encoding="utf-8")
    fake_reviewer(monkeypatch, iter([reviewer_output("revise", "01", "提前完成标记无效")]))

    result = prompt_first.handle_post_tool(
        {
            "cwd": str(tmp_path),
            "tool_name": "Write",
            "tool_input": {"file_path": str(artifact)},
        }
    )

    assert "PostToolUse fallback" in result["hookSpecificOutput"]["additionalContext"]


def test_post_tool_write_runs_reviewer_fallback_in_same_context(tmp_path: Path, monkeypatch):
    prompt_first.initialize(tmp_path, "测试 PostToolUse Reviewer 兜底")
    state = prompt_first.load_state(tmp_path)
    artifact = prompt_first.ensure_stage_document(tmp_path, state)
    artifact.write_text("# 当前阶段记录\n", encoding="utf-8")
    calls = fake_reviewer(
        monkeypatch,
        iter([reviewer_output("revise", "01", "自动兜底发现证据缺口")]),
    )

    result = prompt_first.handle_post_tool(
        {
            "cwd": str(tmp_path),
            "tool_name": "Write",
            "tool_input": {"file_path": str(artifact)},
        }
    )

    assert len(calls) == 1
    context = result["hookSpecificOutput"]["additionalContext"]
    assert "PostToolUse fallback" in context
    assert "自动兜底发现证据缺口" in context
    assert result["decision"] == "block"
    assert prompt_first.load_state(tmp_path)["review_status"] == "complete"


def test_new_explicit_loop_defaults_to_prompt_first(tmp_path: Path, monkeypatch):
    captured = {}

    def fake_loop(project, task, **kwargs):
        captured.update({"project": Path(project), "task": task, **kwargs})
        return 0

    monkeypatch.setattr(cli, "prompt_first_loop_project", fake_loop)
    assert cli.main(["loop", str(tmp_path / "new-project"), "写一份高质量调研"]) == 0
    assert captured["project"] == (tmp_path / "new-project").resolve()
    assert captured["task"] == "写一份高质量调研"


def test_prompt_first_loop_injects_external_rules_and_no_tool_gates(tmp_path: Path, monkeypatch):
    launched = {}

    def fake_run(command, **kwargs):
        launched["command"] = command
        launched["kwargs"] = kwargs
        return 0, False

    monkeypatch.setattr(cli, "_claude_executable", lambda: "claude")
    monkeypatch.setattr(cli, "_run_prompt_first_supervised", fake_run)
    assert cli.prompt_first_loop_project(tmp_path, "完成一个最小 Markdown 流程", max_cycles=1) == 0

    command = launched["command"]
    settings = json.loads((tmp_path / ".claude" / "settings.ralph-prompt-first.json").read_text(encoding="utf-8"))
    assert "--append-system-prompt" in command
    assert "ralph prompt-first review ." in command[-1]
    assert "当前阶段操作与质检标准" in command[-1]
    assert set(settings["hooks"]) == {"PreToolUse", "PostToolUse", "PreCompact", "PostCompact", "Stop"}
    assert not (tmp_path / "loop-state.json").exists()
