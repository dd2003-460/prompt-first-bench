"""Auditable cross-checks through configured web-LLM APIs or browser UIs.

Claude Code's WebSearch can find public evidence, but it cannot submit a
question to an authenticated ChatGPT/Claude/Gemini web page.  This module
provides the missing, explicit boundary: configured OpenAI-compatible HTTPS
endpoints and configured Playwright browser profiles both produce durable
receipts.  Browser profiles type the same bounded question into a real web UI;
they never read browser cookies or credentials.  A model answer remains a
*review signal*, never primary factual evidence; callers still need independent
authoritative sources.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from .result_artifacts import state_stage_artifact_dir
from .state import load_state


class WebLLMConfigurationError(ValueError):
    """The project requested a web-LLM check without usable provider config."""


_BROWSER_SITES = {
    "perplexity": "https://www.perplexity.ai/",
    "chatgpt": "https://chatgpt.com/",
    "gemini": "https://gemini.google.com/app",
}
_BROWSER_AUTHORIZATION_RELATIVE_PATH = Path(
    "loop-artifacts/contracts/web-llm-browser-authorization.json"
)
_BROWSER_AUTHORIZATION_KIND = "ralph_web_llm_browser_authorization"
_GLOBAL_BROWSER_AUTHORIZATION_KIND = "ralph_web_llm_browser_global_authorization"


def _bounded_text(value: Any, limit: int) -> str:
    text = str(value or "").replace("\x00", " ").strip()
    if len(text) <= limit:
        return text
    return text[: max(1, limit - 80)] + "\n[… truncated by RALPH web-LLM boundary …]"


def configured_providers(raw: str | None = None) -> list[dict[str, str]]:
    """Read sanitized OpenAI-compatible provider settings from the environment.

    ``RALPH_WEB_LLM_PROVIDERS_JSON`` is a JSON array.  Each item requires
    ``id``, ``endpoint``, ``model`` and ``api_key_env``.  API values themselves
    are never placed in the JSON, events or receipts.
    """

    payload = raw if raw is not None else os.environ.get("RALPH_WEB_LLM_PROVIDERS_JSON", "")
    if not payload.strip():
        return []
    try:
        items = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise WebLLMConfigurationError("RALPH_WEB_LLM_PROVIDERS_JSON 必须是 JSON 数组") from exc
    if not isinstance(items, list):
        raise WebLLMConfigurationError("RALPH_WEB_LLM_PROVIDERS_JSON 必须是 JSON 数组")

    providers: list[dict[str, str]] = []
    seen: set[str] = set()
    for index, raw_item in enumerate(items):
        if not isinstance(raw_item, Mapping):
            raise WebLLMConfigurationError(f"provider[{index}] 必须是对象")
        provider_id = str(raw_item.get("id", "")).strip()
        endpoint = str(raw_item.get("endpoint", "")).strip()
        model = str(raw_item.get("model", "")).strip()
        api_key_env = str(raw_item.get("api_key_env", "")).strip()
        parsed = urlparse(endpoint)
        if not provider_id or not model or not api_key_env:
            raise WebLLMConfigurationError(
                f"provider[{index}] 需要 id、model 和 api_key_env"
            )
        if provider_id in seen:
            raise WebLLMConfigurationError(f"provider id 重复：{provider_id}")
        if parsed.scheme != "https" or not parsed.netloc:
            raise WebLLMConfigurationError(
                f"provider[{index}] endpoint 必须是 HTTPS URL；拒绝本地/明文端点"
            )
        seen.add(provider_id)
        providers.append(
            {
                "id": provider_id,
                "endpoint": endpoint,
                "model": model,
                "api_key_env": api_key_env,
                "endpoint_host": parsed.netloc,
            }
        )
    return providers


def _parse_browser_providers(payload: str | list[Any], *, source: str) -> list[dict[str, str]]:
    """Validate browser providers from an environment value or authorization file."""

    if isinstance(payload, str):
        if not payload.strip():
            return []
        try:
            items = json.loads(payload)
        except json.JSONDecodeError as exc:
            raise WebLLMConfigurationError(f"{source} 必须是 JSON 数组") from exc
    else:
        items = payload
    if not isinstance(items, list):
        raise WebLLMConfigurationError(f"{source} 必须是 JSON 数组")

    providers: list[dict[str, str]] = []
    seen: set[str] = set()
    for index, raw_item in enumerate(items):
        if not isinstance(raw_item, Mapping):
            raise WebLLMConfigurationError(f"browser provider[{index}] 必须是对象")
        provider_id = str(raw_item.get("id", "")).strip()
        site = str(raw_item.get("site", "")).strip().lower()
        if not provider_id or not site:
            raise WebLLMConfigurationError(f"browser provider[{index}] 需要 id 和 site")
        if site not in _BROWSER_SITES:
            raise WebLLMConfigurationError(
                f"browser provider[{index}] site 必须是：{', '.join(sorted(_BROWSER_SITES))}"
            )
        if provider_id in seen:
            raise WebLLMConfigurationError(f"browser provider id 重复：{provider_id}")
        url = str(raw_item.get("url") or _BROWSER_SITES[site]).strip()
        parsed = urlparse(url)
        if parsed.scheme != "https" or not parsed.netloc:
            raise WebLLMConfigurationError(
                f"browser provider[{index}] url 必须是 HTTPS URL；拒绝本地/明文端点"
            )
        seen.add(provider_id)
        providers.append(
            {
                "id": provider_id,
                "site": site,
                "url": url,
                "endpoint_host": parsed.netloc,
                "model": f"{site} web UI",
            }
        )
    return providers


def browser_authorization_path(project: str | Path) -> Path:
    """Return the durable project-local browser authorization path."""

    return Path(project).expanduser().resolve() / _BROWSER_AUTHORIZATION_RELATIVE_PATH


def global_browser_authorization_path() -> Path:
    """Return the user-owned, cross-project browser authorization path."""

    config_home = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config"))
    return config_home.expanduser().resolve() / "ralph-runtime" / "web-llm-browser.json"


def _project_browser_providers(project: str | Path) -> list[dict[str, str]]:
    path = browser_authorization_path(project)
    if not path.is_file():
        return []
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise WebLLMConfigurationError(
            f"项目浏览器授权文件 JSON 语法错误：{path.relative_to(Path(project).expanduser().resolve())}"
        ) from exc
    if not isinstance(document, Mapping):
        raise WebLLMConfigurationError("项目浏览器授权文件必须是对象")
    if document.get("kind") != _BROWSER_AUTHORIZATION_KIND or document.get("authorized_by") != "human":
        raise WebLLMConfigurationError(
            "项目浏览器授权文件缺少人类授权标记；请由人类运行 `ralph web-llm-authorize`。"
        )
    return _parse_browser_providers(
        document.get("providers", []),
        source="项目浏览器授权文件 providers",
    )


def _global_browser_authorization() -> Mapping[str, Any] | None:
    path = global_browser_authorization_path()
    if not path.is_file():
        return None
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise WebLLMConfigurationError(f"全局浏览器授权文件 JSON 语法错误：{path}") from exc
    if not isinstance(document, Mapping):
        raise WebLLMConfigurationError("全局浏览器授权文件必须是对象")
    if document.get("kind") != _GLOBAL_BROWSER_AUTHORIZATION_KIND or document.get("authorized_by") != "human":
        raise WebLLMConfigurationError(
            "全局浏览器授权文件缺少人类授权标记；请由人类运行 `ralph web-llm-authorize --global`。"
        )
    return document


def browser_profile_dir() -> str | None:
    """Return an explicitly configured dedicated persistent browser profile.

    The path is never stored in receipts.  It is deliberately separate from
    the user's regular browser profile so RALPH never reads or imports existing
    cookies, passwords, or session stores.  An environment override is useful
    for ephemeral test environments; normal users set it once in the global
    human authorization file.
    """

    candidate = os.environ.get("RALPH_WEB_LLM_BROWSER_PROFILE_DIR", "").strip()
    if not candidate:
        document = _global_browser_authorization()
        candidate = str(document.get("browser_profile_dir", "")).strip() if document else ""
    if not candidate:
        return None
    return str(Path(candidate).expanduser().resolve())


def _global_browser_providers() -> list[dict[str, str]]:
    document = _global_browser_authorization()
    if document is None:
        return []
    return _parse_browser_providers(
        document.get("providers", []),
        source="全局浏览器授权文件 providers",
    )


def configured_browser_providers(
    raw: str | None = None,
    *,
    project: str | Path | None = None,
) -> list[dict[str, str]]:
    """Read browser-UI providers that the local Playwright runner may use.

    ``RALPH_WEB_LLM_BROWSER_PROVIDERS_JSON`` is a JSON array containing
    ``id`` and ``site``.  ``site`` is deliberately a small allowlist of public
    LLM web applications, with an optional HTTPS ``url`` override for a
    user-authorized compatible deployment.  Credentials and browser storage
    are never part of this configuration or a persisted receipt.
    """

    payload = raw if raw is not None else os.environ.get("RALPH_WEB_LLM_BROWSER_PROVIDERS_JSON", "")
    if payload.strip():
        return _parse_browser_providers(payload, source="RALPH_WEB_LLM_BROWSER_PROVIDERS_JSON")
    if project is not None:
        project_providers = _project_browser_providers(project)
        if project_providers:
            return project_providers
    return _global_browser_providers()


def authorize_browser_providers(
    project: str | Path,
    sites: list[str] | tuple[str, ...] | None = None,
    *,
    global_scope: bool = False,
    browser_profile: str | Path | None = None,
) -> dict[str, Any]:
    """Persist an explicit human authorization for supported browser sites.

    This is intentionally a control-plane operation: stage agents may use the
    resulting authorization through ``web-llm-check`` but StagePolicy never
    permits them to execute this command themselves.  The file contains only
    public URLs and no browser profile, cookies, passwords or API keys.
    """

    root = Path(project).expanduser().resolve()
    requested = [str(site).strip().lower() for site in (sites or tuple(_BROWSER_SITES))]
    if not requested:
        raise WebLLMConfigurationError("至少选择一个受支持的 browser provider")
    invalid = sorted({site for site in requested if site not in _BROWSER_SITES})
    if invalid:
        raise WebLLMConfigurationError(
            f"不支持的 browser provider：{', '.join(invalid)}；可选：{', '.join(sorted(_BROWSER_SITES))}"
        )
    selected = list(dict.fromkeys(requested))
    providers = [
        {"id": f"{site}-review", "site": site, "url": _BROWSER_SITES[site]}
        for site in selected
    ]
    output = global_browser_authorization_path() if global_scope else browser_authorization_path(root)
    document = {
        "schema_version": 1,
        "kind": _GLOBAL_BROWSER_AUTHORIZATION_KIND if global_scope else _BROWSER_AUTHORIZATION_KIND,
        "authorized_by": "human",
        "authorized_at": datetime.now(timezone.utc).isoformat(),
        "scope": "global" if global_scope else "project",
        "source": "loop/1-loop/02.5-交叉验证.md and loop/1-loop/04.5-交叉验证.md URL allowlist",
        "providers": providers,
        "privacy": "Fresh Playwright contexts only; no cookie, credential, or browser-profile access.",
    }
    if browser_profile is not None:
        profile = str(Path(browser_profile).expanduser().resolve())
        document["browser_profile_dir"] = profile
        document["privacy"] = (
            "Dedicated persistent Playwright profile only; do not point at a regular browser profile. "
            "No cookie, credential, or password extraction."
        )
    output.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(document, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    fd, temporary = tempfile.mkstemp(prefix=f".{output.name}.", suffix=".tmp", dir=output.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, output)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    return {
        "ok": True,
        "authorization": str(output) if global_scope else str(output.relative_to(root)),
        "provider_ids": [provider["id"] for provider in _parse_browser_providers(providers, source="authorization")],
        "scope": "global" if global_scope else "project",
        "persistent_profile": bool(browser_profile is not None),
        "requires_two_providers": True,
    }


def _all_providers(project: str | Path | None = None) -> list[dict[str, str]]:
    providers = [*configured_providers(), *configured_browser_providers(project=project)]
    ids = [provider["id"] for provider in providers]
    if len(set(ids)) != len(ids):
        raise WebLLMConfigurationError("API provider 与 browser provider 的 id 不能重复")
    return providers


def web_llm_crosscheck_enabled(project: str | Path | None = None) -> bool:
    """Whether the runtime can honestly require actual web-LLM receipts."""

    try:
        return len(_all_providers(project)) >= 2
    except WebLLMConfigurationError:
        return False


def _response_text(payload: Mapping[str, Any]) -> str:
    choices = payload.get("choices")
    if not isinstance(choices, list) or not choices or not isinstance(choices[0], Mapping):
        raise ValueError("provider response has no choices[0]")
    message = choices[0].get("message")
    if not isinstance(message, Mapping):
        raise ValueError("provider response has no choices[0].message")
    content = message.get("content")
    if not isinstance(content, str) or not content.strip():
        raise ValueError("provider response has empty choices[0].message.content")
    return _bounded_text(content, 8000)


def _review_prompt(claim: str, context: str) -> str:
    return (
        "Independently review the following claim. Give one verdict: supported, contradicted, or uncertain. "
        "State the decisive reason, distinguish factual evidence from inference, and do not invent citations. "
        "Your answer is an adversarial review signal, not an authoritative source.\n\n"
        f"Claim:\n{claim}\n\nContext:\n{context or '(none)'}"
    )


def _ask_provider(provider: Mapping[str, str], claim: str, context: str, timeout: float) -> dict[str, Any]:
    key = os.environ.get(provider["api_key_env"], "").strip()
    receipt = {
        "provider_id": provider["id"],
        "model": provider["model"],
        "endpoint_host": provider["endpoint_host"],
        "status": "error",
    }
    if not key:
        receipt["error"] = f"missing credential environment variable: {provider['api_key_env']}"
        return receipt
    prompt = _review_prompt(claim, context)
    body = json.dumps(
        {
            "model": provider["model"],
            "messages": [
                {
                    "role": "system",
                    "content": "You are a careful cross-validation reviewer. Never fabricate evidence or URLs.",
                },
                {"role": "user", "content": prompt},
            ],
            "temperature": 0,
        },
        ensure_ascii=False,
    ).encode("utf-8")
    request = Request(
        provider["endpoint"],
        data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(request, timeout=timeout) as response:  # nosec B310 - endpoint is HTTPS-validated config
            raw = response.read().decode("utf-8")
        text = _response_text(json.loads(raw))
    except (HTTPError, URLError, TimeoutError, ValueError, json.JSONDecodeError) as exc:
        receipt["error"] = _bounded_text(exc, 500)
        return receipt
    receipt.update(
        {
            "status": "ok",
            "response": text,
            "response_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        }
    )
    return receipt


def _browser_runner_path() -> Path:
    return Path(__file__).with_name("web_llm_browser_runner.mjs")


def _ask_browser_provider(provider: Mapping[str, str], claim: str, context: str, timeout: float) -> dict[str, Any]:
    """Ask a browser-UI provider through the local Playwright runner.

    The runner receives only the bounded review prompt and provider URL.  It
    starts a fresh context, which intentionally prevents silent reuse or
    extraction of a user's authenticated browser profile.
    """

    receipt: dict[str, Any] = {
        "provider_id": provider["id"],
        "model": provider["model"],
        "endpoint_host": provider["endpoint_host"],
        "transport": "browser_playwright",
        "status": "error",
    }
    runner = _browser_runner_path()
    if not runner.is_file():
        receipt["error"] = f"browser runner missing: {runner.name}"
        return receipt
    payload = {
        "site": provider["site"],
        "url": provider["url"],
        "prompt": _review_prompt(claim, context),
        "headless": os.environ.get("RALPH_WEB_LLM_BROWSER_HEADLESS", "0").strip().lower()
        in {"1", "true", "yes"},
        "timeout_ms": int(timeout * 1000),
    }
    profile_dir = browser_profile_dir()
    if profile_dir:
        payload["profile_dir"] = profile_dir
    channel = os.environ.get("RALPH_WEB_LLM_BROWSER_CHANNEL", "").strip()
    if channel:
        payload["channel"] = channel
    try:
        completed = subprocess.run(
            ["node", str(runner)],
            input=json.dumps(payload, ensure_ascii=False),
            text=True,
            capture_output=True,
            timeout=timeout + 15,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        receipt["error"] = _bounded_text(exc, 500)
        return receipt
    if completed.returncode != 0:
        receipt["error"] = _bounded_text(completed.stderr or completed.stdout or "browser runner failed", 500)
        return receipt
    try:
        result = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        receipt["error"] = _bounded_text(f"browser runner returned invalid JSON: {exc}", 500)
        return receipt
    if not isinstance(result, Mapping) or not isinstance(result.get("response"), str) or not result["response"].strip():
        receipt["error"] = _bounded_text(
            result.get("error") if isinstance(result, Mapping) else "browser runner returned no response",
            500,
        )
        return receipt
    text = _bounded_text(result["response"], 8000)
    receipt.update(
        {
            "status": "ok",
            "response": text,
            "response_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "page_url": _bounded_text(result.get("page_url"), 500),
        }
    )
    return receipt


def open_browser_login(site: str, *, wait_seconds: int = 900) -> dict[str, Any]:
    """Open a dedicated persistent profile for one-time human sign-in.

    This command sends no prompt.  It only keeps a visible browser open long
    enough for the human to complete the provider's normal login flow.  The
    resulting session stays in the dedicated RALPH profile for later local
    Agent browser checks.
    """

    normalized_site = str(site).strip().lower()
    if normalized_site not in _BROWSER_SITES:
        raise WebLLMConfigurationError(
            f"不支持的 browser provider：{normalized_site}；可选：{', '.join(sorted(_BROWSER_SITES))}"
        )
    profile_dir = browser_profile_dir()
    if not profile_dir:
        raise WebLLMConfigurationError(
            "未配置专用持久浏览器 profile；先由人类运行 `ralph web-llm-authorize --global --profile-dir <目录>`。"
        )
    runner = _browser_runner_path()
    if not runner.is_file():
        raise OSError(f"browser runner missing: {runner.name}")
    wait_seconds = max(30, min(int(wait_seconds), 3600))
    payload = {
        "mode": "login",
        "site": normalized_site,
        "url": _BROWSER_SITES[normalized_site],
        "profile_dir": profile_dir,
        "headless": False,
        "timeout_ms": wait_seconds * 1000,
    }
    completed = subprocess.run(
        ["node", str(runner)],
        input=json.dumps(payload, ensure_ascii=False),
        text=True,
        capture_output=True,
        timeout=wait_seconds + 20,
        check=False,
    )
    if completed.returncode != 0:
        raise WebLLMConfigurationError(
            _bounded_text(completed.stderr or completed.stdout or "browser login runner failed", 500)
        )
    return {
        "ok": True,
        "site": normalized_site,
        "profile_dir": profile_dir,
        "message": "可见浏览器会话已结束；后续 RALPH 项目将复用此专用 profile。",
    }


def _timeout_seconds() -> float:
    try:
        return min(120.0, max(5.0, float(os.environ.get("RALPH_WEB_LLM_TIMEOUT_SECONDS", "45"))))
    except ValueError:
        return 45.0


def _write_markdown_receipt(path: Path, claim: str, context: str, responses: list[Mapping[str, Any]]) -> None:
    """Persist browser/API review evidence as Markdown for prompt-first projects."""

    lines = [
        "# 网页 AI 交叉询问回执",
        "",
        f"- 时间：{datetime.now(timezone.utc).isoformat()}",
        "- 性质：网页 AI 回答仅是审阅线索，不是权威事实来源。",
        "",
        "## 询问主张",
        "",
        claim,
        "",
        "## 上下文",
        "",
        context or "（无额外上下文）",
        "",
        "## 回执",
        "",
    ]
    for item in responses:
        lines.extend([
            f"### {item.get('provider_id', 'unknown provider')}",
            "",
            f"- 传输：{item.get('transport', 'api')}",
            f"- 状态：{item.get('status', 'error')}",
        ])
        if item.get("page_url"):
            lines.append(f"- 页面：{item['page_url']}")
        if item.get("error"):
            lines.append(f"- 错误：{item['error']}")
        response = str(item.get("response") or "").strip()
        if response:
            lines.extend(["", "回答：", "", *[f"    {line}" for line in response.splitlines()]])
        lines.append("")
    lines.extend([
        "## 使用限制",
        "",
        "将上述回答与独立来源分开记录；不得把网页 AI 的未引证说法写成已验证事实。",
        "",
    ])
    encoded = "\n".join(lines)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def run_prompt_first_web_llm_cross_check(
    project: str | Path,
    claim: str,
    context: str = "",
) -> dict[str, Any]:
    """Use configured local browser/API reviewers without field/DAG state.

    The sole durable result is a Markdown receipt under the prompt-first
    artifacts.  This is an execution helper, not a stage-quality gate.
    """

    root = Path(project).expanduser().resolve()
    bounded_claim = _bounded_text(claim, 4000)
    bounded_context = _bounded_text(context, 6000)
    if not bounded_claim:
        raise ValueError("prompt-first 网页 AI 询问需要非空问题或主张")
    providers = _all_providers(root)
    if len(providers) < 2:
        raise WebLLMConfigurationError(
            "至少配置两个独立 web-LLM provider 才能执行交叉询问；"
            "可由人类预先运行 `ralph web-llm-authorize --global`。"
        )
    responses = [
        (
            _ask_browser_provider(provider, bounded_claim, bounded_context, _timeout_seconds())
            if provider.get("site")
            else _ask_provider(provider, bounded_claim, bounded_context, _timeout_seconds())
        )
        for provider in providers
    ]
    output = root / "loop-artifacts" / "prompt-first" / "02-web-llm-cross-check.md"
    _write_markdown_receipt(output, bounded_claim, bounded_context, responses)
    return {
        "ok": True,
        "receipt": str(output.relative_to(root)),
        "successful_provider_ids": [item["provider_id"] for item in responses if item.get("status") == "ok"],
        "failed_provider_ids": [item["provider_id"] for item in responses if item.get("status") != "ok"],
    }


def run_web_llm_cross_check(project: str | Path, request_file: str | Path) -> dict[str, Any]:
    """Ask configured independent providers and persist a durable receipt."""

    root = Path(project).expanduser().resolve()
    state = load_state(root / "loop-state.json")
    stage_dir = state_stage_artifact_dir(root, state).resolve()
    path = Path(request_file).expanduser()
    if not path.is_absolute():
        path = root / path
    path = path.resolve()
    if stage_dir not in path.parents:
        raise ValueError(
            f"web-LLM 请求必须位于当前阶段目录 `{stage_dir.relative_to(root)}` 中"
        )
    try:
        request_data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"web-LLM 请求 JSON 语法错误：{exc.msg}") from exc
    if not isinstance(request_data, Mapping):
        raise ValueError("web-LLM 请求必须是对象")
    field = request_data.get("field") if isinstance(request_data.get("field"), Mapping) else {}
    # A field worker is only permitted to mutate its single task JSON.  Accept
    # that task file directly so it does not need to create a second writable
    # request artifact before asking the configured reviewers.
    claim = _bounded_text(request_data.get("claim") or field.get("attribute") or field.get("concept"), 4000)
    context = _bounded_text(request_data.get("context") or field.get("rationale"), 6000)
    if not claim:
        raise ValueError("web-LLM 请求需要非空 claim")
    providers = _all_providers(root)
    requested = request_data.get("providers")
    if requested is not None:
        if not isinstance(requested, list) or not all(isinstance(item, str) and item.strip() for item in requested):
            raise ValueError("providers 必须是 provider id 数组")
        wanted = {item.strip() for item in requested}
        providers = [provider for provider in providers if provider["id"] in wanted]
    if len(providers) < 2:
        raise WebLLMConfigurationError(
            "至少配置两个独立 web-LLM provider 才能执行交叉核验；"
            "设置 RALPH_WEB_LLM_PROVIDERS_JSON（API）、"
            "RALPH_WEB_LLM_BROWSER_PROVIDERS_JSON（受控 Playwright 网页 UI），"
            "或由人类运行 `ralph web-llm-authorize <project>`。"
        )

    responses = [
        (
            _ask_browser_provider(provider, claim, context, _timeout_seconds())
            if provider.get("site")
            else _ask_provider(provider, claim, context, _timeout_seconds())
        )
        for provider in providers
    ]
    now = datetime.now(timezone.utc).isoformat()
    receipt = {
        "schema_version": 1,
        "kind": "ralph_web_llm_cross_check",
        "created_at": now,
        "request_ref": str(path.relative_to(root)),
        "claim": claim,
        "claim_sha256": hashlib.sha256(claim.encode("utf-8")).hexdigest(),
        "context_sha256": hashlib.sha256(context.encode("utf-8")).hexdigest(),
        "responses": responses,
        "successful_provider_ids": [item["provider_id"] for item in responses if item.get("status") == "ok"],
        "note": "LLM replies are adversarial review signals, not authoritative factual sources.",
    }
    output_dir = stage_dir / "web-llm"
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / f"{receipt['claim_sha256'][:16]}.json"
    encoded = json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    fd, temporary = tempfile.mkstemp(prefix=f".{output.name}.", suffix=".tmp", dir=output_dir)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, output)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    return {
        "ok": True,
        "receipt": str(output.relative_to(root)),
        "successful_provider_ids": receipt["successful_provider_ids"],
        "failed_provider_ids": [item["provider_id"] for item in responses if item.get("status") != "ok"],
        "requires_authoritative_sources": True,
    }
