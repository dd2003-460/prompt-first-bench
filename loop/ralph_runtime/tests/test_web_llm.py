import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from ralph_runtime import cli
from ralph_runtime.web_llm import (
    WebLLMConfigurationError,
    authorize_browser_providers,
    browser_authorization_path,
    browser_profile_dir,
    configured_browser_providers,
    global_browser_authorization_path,
    open_browser_login,
    run_prompt_first_web_llm_cross_check,
    run_web_llm_cross_check,
)


class _Response:
    def __init__(self, payload):
        self._payload = payload

    def read(self):
        return json.dumps(self._payload).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False


def _providers():
    return json.dumps([
        {
            "id": "reviewer-a",
            "endpoint": "https://reviewer-a.example/v1/chat/completions",
            "model": "reviewer-a-model",
            "api_key_env": "RALPH_TEST_KEY_A",
        },
        {
            "id": "reviewer-b",
            "endpoint": "https://reviewer-b.example/v1/chat/completions",
            "model": "reviewer-b-model",
            "api_key_env": "RALPH_TEST_KEY_B",
        },
    ])


def test_web_llm_cross_check_persists_two_provider_receipt(tmp_path: Path, monkeypatch):
    project = tmp_path / "web-llm-project"
    cli.prepare_project(project, task="验证一个写作主张")
    stage_dir = project / "loop-artifacts" / "stages" / "01" / "r1"
    request = stage_dir / "cross-check.json"
    request.write_text(
        json.dumps({"claim": "清楚区分隐喻和因果主张会提高科普可核验性。", "context": "写作审计"}, ensure_ascii=False),
        encoding="utf-8",
    )
    monkeypatch.setenv("RALPH_WEB_LLM_PROVIDERS_JSON", _providers())
    monkeypatch.setenv("RALPH_TEST_KEY_A", "test-a")
    monkeypatch.setenv("RALPH_TEST_KEY_B", "test-b")

    def fake_urlopen(request_obj, timeout):
        assert timeout > 0
        assert request_obj.get_header("Authorization") in {"Bearer test-a", "Bearer test-b"}
        return _Response({"choices": [{"message": {"content": "uncertain: need authoritative sources"}}]})

    monkeypatch.setattr("ralph_runtime.web_llm.urlopen", fake_urlopen)
    report = run_web_llm_cross_check(project, request.relative_to(project))

    assert report["ok"] is True
    assert report["successful_provider_ids"] == ["reviewer-a", "reviewer-b"]
    receipt = json.loads((project / report["receipt"]).read_text(encoding="utf-8"))
    assert receipt["note"].startswith("LLM replies are adversarial")
    assert {item["endpoint_host"] for item in receipt["responses"]} == {
        "reviewer-a.example",
        "reviewer-b.example",
    }


def test_web_llm_cross_check_refuses_unconfigured_or_single_provider(tmp_path: Path, monkeypatch):
    project = tmp_path / "no-web-llm-project"
    cli.prepare_project(project, task="验证一个主张")
    request = project / "loop-artifacts" / "stages" / "01" / "r1" / "cross-check.json"
    request.write_text('{"claim":"需要核验"}\n', encoding="utf-8")
    monkeypatch.delenv("RALPH_WEB_LLM_PROVIDERS_JSON", raising=False)

    with pytest.raises(WebLLMConfigurationError, match="至少配置两个"):
        run_web_llm_cross_check(project, request.relative_to(project))


def test_web_llm_cross_check_accepts_playwright_browser_receipts(tmp_path: Path, monkeypatch):
    project = tmp_path / "browser-web-llm-project"
    cli.prepare_project(project, task="验证一个主张")
    request = project / "loop-artifacts" / "stages" / "01" / "r1" / "cross-check.json"
    request.write_text('{"claim":"需要核验"}\n', encoding="utf-8")
    monkeypatch.setenv("RALPH_WEB_LLM_BROWSER_PROVIDERS_JSON", json.dumps([
        {"id": "perplexity-review", "site": "perplexity"},
        {"id": "chatgpt-review", "site": "chatgpt"},
    ]))
    monkeypatch.delenv("RALPH_WEB_LLM_PROVIDERS_JSON", raising=False)

    def fake_run(command, **kwargs):
        payload = json.loads(kwargs["input"])
        assert command[0] == "node"
        assert payload["headless"] is False
        return SimpleNamespace(returncode=0, stdout=json.dumps({
            "response": f"uncertain from {payload['site']}",
            "page_url": payload["url"],
        }), stderr="")

    monkeypatch.setattr("ralph_runtime.web_llm.subprocess.run", fake_run)
    report = run_web_llm_cross_check(project, request.relative_to(project))

    assert report["successful_provider_ids"] == ["perplexity-review", "chatgpt-review"]
    receipt = json.loads((project / report["receipt"]).read_text(encoding="utf-8"))
    assert {item["transport"] for item in receipt["responses"]} == {"browser_playwright"}


def test_prompt_first_web_llm_writes_markdown_receipt_without_field_state(tmp_path: Path, monkeypatch):
    project = tmp_path / "prompt-first-browser-project"
    monkeypatch.setenv("RALPH_WEB_LLM_BROWSER_PROVIDERS_JSON", json.dumps([
        {"id": "perplexity-review", "site": "perplexity"},
        {"id": "chatgpt-review", "site": "chatgpt"},
    ]))
    monkeypatch.delenv("RALPH_WEB_LLM_PROVIDERS_JSON", raising=False)

    def fake_run(command, **kwargs):
        payload = json.loads(kwargs["input"])
        return SimpleNamespace(returncode=0, stdout=json.dumps({
            "response": f"review from {payload['site']}",
            "page_url": payload["url"],
        }), stderr="")

    monkeypatch.setattr("ralph_runtime.web_llm.subprocess.run", fake_run)
    report = run_prompt_first_web_llm_cross_check(project, "检查科普写作主张", "普通读者")

    receipt = project / report["receipt"]
    assert report["successful_provider_ids"] == ["perplexity-review", "chatgpt-review"]
    assert receipt.suffix == ".md"
    assert "网页 AI 交叉询问回执" in receipt.read_text(encoding="utf-8")


def test_prompt_first_web_llm_cli_generates_question_from_markdown_task(tmp_path: Path, monkeypatch, capsys):
    from ralph_runtime import prompt_first

    prompt_first.initialize(tmp_path, "检查一个写作主张")
    captured = {}

    def fake_prompt_first_check(project, question, context):
        captured.update({"project": Path(project), "question": question, "context": context})
        return {"ok": True, "receipt": "loop-artifacts/prompt-first/02-web-llm-cross-check.md"}

    monkeypatch.setattr(cli, "run_prompt_first_web_llm_cross_check", fake_prompt_first_check)

    assert cli.main(["prompt-first", "web-llm", str(tmp_path)]) == 0
    assert "检查一个写作主张" in captured["question"]
    assert captured["context"].startswith("当前阶段：01")
    assert json.loads(capsys.readouterr().out)["ok"] is True


def test_human_project_browser_authorization_enables_local_agent_runner(tmp_path: Path, monkeypatch):
    project = tmp_path / "authorized-browser-project"
    cli.prepare_project(project, task="验证一个主张")
    request = project / "loop-artifacts" / "stages" / "01" / "r1" / "cross-check.json"
    request.write_text('{"claim":"需要核验"}\n', encoding="utf-8")
    authorization = authorize_browser_providers(project, ["perplexity", "gemini"])
    document = json.loads(browser_authorization_path(project).read_text(encoding="utf-8"))
    assert authorization["provider_ids"] == ["perplexity-review", "gemini-review"]
    assert document["authorized_by"] == "human"
    assert document["providers"][0]["url"] == "https://www.perplexity.ai/"
    monkeypatch.delenv("RALPH_WEB_LLM_PROVIDERS_JSON", raising=False)
    monkeypatch.delenv("RALPH_WEB_LLM_BROWSER_PROVIDERS_JSON", raising=False)

    def fake_run(command, **kwargs):
        payload = json.loads(kwargs["input"])
        assert command[0] == "node"
        return SimpleNamespace(returncode=0, stdout=json.dumps({
            "response": f"uncertain from {payload['site']}",
            "page_url": payload["url"],
        }), stderr="")

    monkeypatch.setattr("ralph_runtime.web_llm.subprocess.run", fake_run)
    report = run_web_llm_cross_check(project, request.relative_to(project))

    assert report["successful_provider_ids"] == ["perplexity-review", "gemini-review"]


def test_web_llm_authorize_cli_writes_human_scoped_configuration(tmp_path: Path, capsys):
    project = tmp_path / "cli-authorized-browser-project"
    cli.prepare_project(project, task="验证一个主张")

    assert cli.main([
        "web-llm-authorize", str(project), "--providers", "perplexity", "chatgpt",
    ]) == 0

    result = json.loads(capsys.readouterr().out)
    assert result["provider_ids"] == ["perplexity-review", "chatgpt-review"]
    assert browser_authorization_path(project).is_file()


def test_global_browser_authorization_reuses_dedicated_profile_across_projects(tmp_path: Path, monkeypatch):
    config_home = tmp_path / "config"
    profile = tmp_path / "dedicated-ralph-profile"
    monkeypatch.setenv("XDG_CONFIG_HOME", str(config_home))
    monkeypatch.delenv("RALPH_WEB_LLM_BROWSER_PROVIDERS_JSON", raising=False)
    monkeypatch.delenv("RALPH_WEB_LLM_BROWSER_PROFILE_DIR", raising=False)

    authorization = authorize_browser_providers(
        tmp_path / "ignored-project",
        ["perplexity", "gemini"],
        global_scope=True,
        browser_profile=profile,
    )

    assert authorization["scope"] == "global"
    assert authorization["persistent_profile"] is True
    assert global_browser_authorization_path().is_file()
    assert browser_profile_dir() == str(profile.resolve())
    assert [item["id"] for item in configured_browser_providers(project=tmp_path / "another-project")] == [
        "perplexity-review", "gemini-review",
    ]


def test_browser_login_uses_dedicated_profile_without_sending_a_prompt(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path / "config"))
    profile = tmp_path / "dedicated-ralph-profile"
    authorize_browser_providers(
        tmp_path / "ignored-project",
        ["perplexity", "chatgpt"],
        global_scope=True,
        browser_profile=profile,
    )

    def fake_run(command, **kwargs):
        payload = json.loads(kwargs["input"])
        assert command[0] == "node"
        assert payload["mode"] == "login"
        assert payload["site"] == "perplexity"
        assert payload["profile_dir"] == str(profile.resolve())
        assert "prompt" not in payload
        return SimpleNamespace(returncode=0, stdout='{"login_completed":true}', stderr="")

    monkeypatch.setattr("ralph_runtime.web_llm.subprocess.run", fake_run)
    result = open_browser_login("perplexity", wait_seconds=30)

    assert result["ok"] is True
    assert result["profile_dir"] == str(profile.resolve())
