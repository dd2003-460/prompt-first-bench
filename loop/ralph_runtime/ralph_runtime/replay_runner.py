"""Deterministic Prompt/action fixture runner."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .prompt_renderer import PromptRenderer
from .protocol import ActionResult, parse_action
from .state import apply_action


def run_fixture(fixture: dict[str, Any]) -> tuple[dict[str, Any], str, ActionResult]:
    state = fixture["state"]
    rendered = PromptRenderer(fixture.get("template_path")).render(state) if fixture.get("template_path") else PromptRenderer().render(state)
    action = parse_action(fixture["agent_output"])
    # Fixtures may predate task-card enforcement.  Their purpose is stable
    # state-transition replay; live Hook application remains contract-gated.
    updated = apply_action(state, action, enforce_contracts=False)
    return updated, rendered.sha256, action


def run_fixture_file(path: str | Path) -> tuple[dict[str, Any], str, ActionResult]:
    fixture = json.loads(Path(path).read_text(encoding="utf-8"))
    return run_fixture(fixture)
