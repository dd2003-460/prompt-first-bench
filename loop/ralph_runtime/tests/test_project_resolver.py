from pathlib import Path

from ralph_runtime.project_resolver import rank_projects, resolve_project


def _marked_project(root: Path, name: str, text: str) -> Path:
    project = root / "projects" / name
    (project / ".claude").mkdir(parents=True)
    (project / ".claude" / "ralph-loop.local.md").write_text(text, encoding="utf-8")
    return project


def test_resolver_reuses_clear_existing_project(tmp_path: Path):
    workspace = tmp_path / "workspace"
    (workspace / "projects").mkdir(parents=True)
    existing = _marked_project(
        workspace,
        "D1-ai-agent-hardware",
        "GPU 显卡 本地 AI 性价比调研",
    )

    resolution = resolve_project("帮我调研性价比最高的 GPU", start=workspace, fallback_workspace=workspace)

    assert resolution.created is False
    assert resolution.project == existing
    assert "已有项目" in resolution.reason


def test_resolver_creates_deterministic_project_when_no_match(tmp_path: Path):
    workspace = tmp_path / "workspace"
    (workspace / "projects").mkdir(parents=True)
    first = resolve_project("做一个独立的天气数据分析", start=workspace, fallback_workspace=workspace)
    second = resolve_project("做一个独立的天气数据分析", start=workspace, fallback_workspace=workspace)

    assert first.created is True
    assert first.project == second.project
    assert first.project.parent == workspace / "projects"


def test_task_only_run_uses_user_project_local_setting_sources(tmp_path: Path, monkeypatch):
    import ralph_runtime.cli as cli

    observed = {}

    def fake_call(command, cwd, env=None):
        observed["command"] = command
        observed["cwd"] = cwd
        observed["env"] = env
        return 0

    monkeypatch.setattr(cli.subprocess, "call", fake_call)
    monkeypatch.setattr(cli, "_claude_executable", lambda: "claude")
    assert cli.run_project("研究本地 GPU", mode="shadow", workspace=tmp_path) == 0
    assert observed["command"][observed["command"].index("--setting-sources") + 1] == "user,project,local"
    assert observed["cwd"].parent == tmp_path / "projects"
