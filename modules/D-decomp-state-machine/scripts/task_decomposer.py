#!/usr/bin/env python3
"""
task_decomposer.py — 任务分解器

输入：goal 描述 + 当前状态（checkpoint/loop-state.json）
输出：子任务列表（JSON），每个子任务带：目标/输入/输出/gate 标准

约束：
- 正交（子任务之间不重叠）
- 完备（子任务合起来覆盖全部目标）
- 原子（每个子任务一步可做完可检查）
- ≤5 个并行子任务

用法：
    python3 task_decomposer.py --goal "跑完 soc 119 节点 verify" --state checkpoints/sm-soc-r0.json
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# LLM 调用（复用 s5_pipeline 的 call_llm）
sys.path.insert(0, str(Path(__file__).parent))
try:
    from s5_pipeline import call_llm
except ImportError:
    print("ERROR: cannot import call_llm from s5_pipeline", file=sys.stderr)
    sys.exit(1)


DECOMPOSE_PROMPT = """你是任务分解专家。给定一个目标和当前状态，把它分解成 ≤5 个并行子任务。

要求：
1. **正交**：子任务之间不重叠（一个事只归一个子任务）
2. **完备**：子任务合起来覆盖全部目标，无遗漏
3. **原子**：每个子任务一步可做完可检查（不是"研究 X"这种大词，是"跑 X 脚本并验证输出"这种具体动作）
4. **≤5 个**：超过 5 个说明拆得太细，合并

每个子任务必须包含：
- id: T1, T2, ...
- goal: 1 句话描述这个子任务要做什么
- input: 需要什么输入（文件路径/数据/参数）
- output: 产出什么（文件路径/指标/结论）
- gate: 怎么判断这个子任务做完了（可机器检查的标准，如"文件存在且 JSON 有效"、"指标 ≥ 0.8"）
- priority: P1（核心链路）/ P2（增强鲁棒性）

当前状态（JSON）：
{state}

目标：
{goal}

输出格式（纯 JSON，不要 markdown）：
{{
  "tasks": [
    {{"id": "T1", "goal": "...", "input": "...", "output": "...", "gate": "...", "priority": "P1"}},
    ...
  ],
  "reasoning": "为什么这样拆（1-2 句）"
}}
"""


def decompose(goal: str, state: dict, max_tasks: int = 5) -> dict:
    """
    调用 LLM 分解目标为子任务列表。
    
    Args:
        goal: 目标描述（1-2 句）
        state: 当前状态（dict，来自 checkpoint/loop-state.json）
        max_tasks: 最大子任务数（默认 5）
    
    Returns:
        dict: {"tasks": [...], "reasoning": "..."}
    """
    prompt = DECOMPOSE_PROMPT.format(
        goal=goal,
        state=json.dumps(state, ensure_ascii=False, indent=2)[:4000]  # 截断防超 token
    )
    
    response, usage = call_llm(
        prompt,
        max_tokens=2000,
        temperature=0.3,  # 低温度，稳定输出
        top_p=0.9
    )
    
    if not response:
        raise RuntimeError("LLM returned empty response")
    
    # 提取 JSON
    try:
        # 尝试直接解析
        result = json.loads(response)
    except json.JSONDecodeError:
        # 尝试从 markdown code block 提取
        import re
        match = re.search(r'```json\s*(\{.*?\})\s*```', response, re.DOTALL)
        if match:
            result = json.loads(match.group(1))
        else:
            # 尝试找第一个 { 到最后一个 }
            start = response.find('{')
            end = response.rfind('}')
            if start != -1 and end != -1:
                result = json.loads(response[start:end+1])
            else:
                raise RuntimeError(f"Cannot extract JSON from LLM response: {response[:200]}")
    
    # 验证结构
    if "tasks" not in result or not isinstance(result["tasks"], list):
        raise RuntimeError(f"LLM response missing 'tasks' field or not a list: {list(result.keys()) if isinstance(result, dict) else type(result)}")
    
    tasks = result["tasks"]
    
    # 检查 ≤ max_tasks
    if len(tasks) > max_tasks:
        print(f"WARNING: LLM returned {len(tasks)} tasks, truncating to {max_tasks}", file=sys.stderr)
        tasks = tasks[:max_tasks]
    
    # 验证每个 task 有必需字段
    for i, task in enumerate(tasks):
        for field in ["id", "goal", "input", "output", "gate"]:
            if field not in task:
                raise RuntimeError(f"Task {i} missing field '{field}': {task}")
    
    result["tasks"] = tasks
    result["decomposed_at"] = datetime.now(timezone.utc).isoformat()
    result["n_tasks"] = len(tasks)
    
    return result


def main():
    ap = argparse.ArgumentParser(description="Task decomposer: goal → ≤5 parallel subtasks")
    ap.add_argument("--goal", required=True, help="Goal description (1-2 sentences)")
    ap.add_argument("--state", help="Path to state JSON (checkpoint/loop-state.json)")
    ap.add_argument("--max-tasks", type=int, default=5, help="Max number of subtasks (default 5)")
    ap.add_argument("--output", help="Output JSON path (default: stdout)")
    args = ap.parse_args()
    
    # 加载状态
    state = {}
    if args.state:
        state_path = Path(args.state)
        if state_path.exists():
            with open(state_path) as f:
                state = json.load(f)
        else:
            print(f"WARNING: state file not found: {args.state}", file=sys.stderr)
    
    # 分解
    result = decompose(args.goal, state, args.max_tasks)
    
    # 输出
    output_json = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        with open(args.output, "w") as f:
            f.write(output_json)
        print(f"Decomposed into {result['n_tasks']} tasks → {args.output}", file=sys.stderr)
    else:
        print(output_json)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
