#!/usr/bin/env python3
"""
dispatch_template.py — 并行派发器

输入：task_decomposer.py 的输出（子任务列表 JSON）
输出：delegate_task 调用参数（每个子任务一个 subagent）

约束：
- 每个子任务一个 subagent（独立上下文）
- context 字段：goal-template §1-§5 全文 + 子任务描述 + 相关数据路径
- 并发上限：3（避免资源竞争）
- 派发后前台持续干活（不结束 turn，防静默黑洞）

用法：
    python3 dispatch_template.py --tasks tasks.json --output dispatch_params.json
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# goal-template 路径
GOAL_TEMPLATE_PATH = Path.home() / "Desktop/workspace/agents/goal-template.md"


def load_goal_template() -> str:
    """加载 goal-template.md 全文（§1-§5）"""
    if not GOAL_TEMPLATE_PATH.exists():
        raise FileNotFoundError(f"goal-template not found: {GOAL_TEMPLATE_PATH}")
    with open(GOAL_TEMPLATE_PATH) as f:
        content = f.read()
    # 提取 §1-§5（到 §6 之前）
    start = content.find("## §1")
    end = content.find("## §6")
    if start == -1:
        return content  # 找不到就返回全文
    if end == -1:
        return content[start:]
    return content[start:end]


def build_context(task: dict, goal_template: str, 
                  data_paths: list[str] | None = None) -> str:
    """
    构建 subagent 的 context 字段。
    
    Args:
        task: 子任务 dict（id/goal/input/output/gate/priority）
        goal_template: goal-template.md §1-§5 全文
        data_paths: 相关数据路径列表（可选）
    
    Returns:
        str: context 字段内容
    """
    context_parts = [
        "## Goal 模板（必读）",
        goal_template,
        "",
        "## 你的子任务",
        f"- **ID**: {task['id']}",
        f"- **目标**: {task['goal']}",
        f"- **输入**: {task['input']}",
        f"- **输出**: {task['output']}",
        f"- **Gate 标准**: {task['gate']}",
        f"- **优先级**: {task['priority']}",
    ]
    
    if data_paths:
        context_parts.append("")
        context_parts.append("## 相关数据路径")
        for p in data_paths:
            context_parts.append(f"- {p}")
    
    context_parts.append("")
    context_parts.append("## 执行要求")
    context_parts.append("1. 按 gate 标准执行，产出可验证（指标/文件/分数）")
    context_parts.append("2. 完成后返回：产出文件路径 + 关键指标 + 是否达标")
    context_parts.append("3. 如果 gate 不达标，返回具体差距描述（不是'完成了'三个字）")
    
    return "\n".join(context_parts)


def build_dispatch_params(tasks: list[dict], goal_template: str, 
                          data_paths: list[str] | None = None, 
                          max_concurrent: int = 3) -> dict:
    """
    构建 delegate_task 调用参数。
    
    Args:
        tasks: 子任务列表
        goal_template: goal-template.md §1-§5 全文
        data_paths: 相关数据路径列表（可选，所有子任务共享）
        max_concurrent: 并发上限（默认 3）
    
    Returns:
        dict: {
            "tasks": [
                {"goal": "...", "context": "...", "priority": "..."},
                ...
            ],
            "max_concurrent": 3,
            "dispatched_at": "..."
        }
    """
    # 按优先级排序（P1 优先）
    tasks_sorted = sorted(tasks, key=lambda t: (t.get("priority", "P2"), t.get("id", "")))
    
    # 构建每个子任务的 dispatch 参数
    dispatch_tasks = []
    for task in tasks_sorted[:max_concurrent]:  # 只取前 max_concurrent 个
        context = build_context(task, goal_template, data_paths)
        dispatch_tasks.append({
            "goal": task["goal"],
            "context": context,
            "priority": task.get("priority", "P2"),
            "task_id": task["id"],
            "gate": task["gate"],
            "output": task["output"],
        })
    
    return {
        "tasks": dispatch_tasks,
        "max_concurrent": max_concurrent,
        "dispatched_at": datetime.now(timezone.utc).isoformat(),
        "n_tasks": len(dispatch_tasks),
        "remaining_tasks": [t["id"] for t in tasks_sorted[max_concurrent:]],
    }


def main():
    ap = argparse.ArgumentParser(description="Dispatch template: tasks → delegate_task params")
    ap.add_argument("--tasks", required=True, help="Path to tasks JSON (from task_decomposer.py)")
    ap.add_argument("--output", help="Output JSON path (default: stdout)")
    ap.add_argument("--data-paths", nargs="*", help="Data paths for all subtasks")
    ap.add_argument("--max-concurrent", type=int, default=3, help="Max concurrent subagents (default 3)")
    args = ap.parse_args()
    
    # 加载任务
    tasks_path = Path(args.tasks)
    if not tasks_path.exists():
        print(f"ERROR: tasks file not found: {args.tasks}", file=sys.stderr)
        return 1
    with open(tasks_path) as f:
        tasks_data = json.load(f)
    
    tasks = tasks_data.get("tasks", [])
    if not tasks:
        print("ERROR: no tasks in input", file=sys.stderr)
        return 1
    
    # 加载 goal-template
    goal_template = load_goal_template()
    
    # 构建 dispatch 参数
    params = build_dispatch_params(
        tasks,
        goal_template,
        args.data_paths,
        args.max_concurrent
    )
    
    # 输出
    output_json = json.dumps(params, ensure_ascii=False, indent=2)
    if args.output:
        with open(args.output, "w") as f:
            f.write(output_json)
        print(f"Built dispatch params for {params['n_tasks']} tasks → {args.output}", file=sys.stderr)
        if params["remaining_tasks"]:
            print(f"Remaining (not dispatched): {params['remaining_tasks']}", file=sys.stderr)
    else:
        print(output_json)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
