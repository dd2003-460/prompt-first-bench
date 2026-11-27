#!/usr/bin/env python3
"""
verify_gate.py — 自动验收器

输入：subagent 产出（文件路径/指标）+ gate 标准
输出：PASS/FAIL + 具体差距

约束：
- 只认证据（文件存在/指标达标），不认"完成了"三个字
- FAIL 时返回具体差距描述（不是"不达标"三个字）
- 支持多种 gate 类型：文件存在/JSON 有效/指标 ≥ 阈值/矛盾检测

用法：
    python3 verify_gate.py --gate "文件存在且 JSON 有效" --output checkpoints/sm-soc-r0.json
    python3 verify_gate.py --gate "soc cov ≥ 0.898" --metric-file checkpoints/sm-soc-r0.json --metric-key soc_cov
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


def check_file_exists(path: str) -> tuple[bool, str]:
    """检查文件是否存在"""
    p = Path(path)
    if p.exists():
        return True, f"文件存在: {p}"
    return False, f"文件不存在: {p}"


def check_json_valid(path: str) -> tuple[bool, str]:
    """检查 JSON 是否有效"""
    p = Path(path)
    if not p.exists():
        return False, f"文件不存在: {p}"
    try:
        with open(p) as f:
            json.load(f)
        return True, f"JSON 有效: {p}"
    except json.JSONDecodeError as e:
        return False, f"JSON 无效: {p} ({e})"


def check_metric_threshold(path: str, key: str, threshold: float, 
                           operator: str = ">=") -> tuple[bool, str]:
    """检查指标是否达到阈值"""
    p = Path(path)
    if not p.exists():
        return False, f"文件不存在: {p}"
    
    try:
        with open(p) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return False, f"JSON 无效: {p} ({e})"
    
    # 提取指标
    if key in data:
        value = data[key]
    else:
        # 尝试嵌套查找
        value = None
        for k in data:
            if isinstance(data[k], dict) and key in data[k]:
                value = data[k][key]
                break
    
    if value is None:
        return False, f"指标 '{key}' 不存在于 {p}（可用键: {list(data.keys())[:10]}）"
    
    # 比较
    try:
        value = float(value)
    except (ValueError, TypeError):
        return False, f"指标 '{key}' 不是数字: {value}"
    
    if operator == ">=":
        passed = value >= threshold
    elif operator == "<=":
        passed = value <= threshold
    elif operator == "==":
        passed = value == threshold
    else:
        return False, f"未知操作符: {operator}"
    
    status = "PASS" if passed else "FAIL"
    return passed, f"{status}: {key} = {value} (阈值: {operator} {threshold})"


def check_contradiction(path: str) -> tuple[bool, str]:
    """检查是否有矛盾（简化版：检查 JSON 中是否有 'contradiction' 字段）"""
    p = Path(path)
    if not p.exists():
        return False, f"文件不存在: {p}"
    
    try:
        with open(p) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return False, f"JSON 无效: {p} ({e})"
    
    if "contradiction" in data:
        if data["contradiction"]:
            return False, f"发现矛盾: {data['contradiction']}"
        else:
            return True, "无矛盾"
    
    # 没有 contradiction 字段，假设无矛盾
    return True, "未检测到矛盾（无 contradiction 字段）"


def verify(gate: str, output: str | None = None, metric_file: str | None = None, 
           metric_key: str | None = None, threshold: float | None = None, 
           operator: str = ">=") -> dict:
    """
    验证 gate 是否达标。
    
    Args:
        gate: gate 标准描述（自然语言）
        output: 产出文件路径
        metric_file: 指标文件路径
        metric_key: 指标键名
        threshold: 阈值
        operator: 比较操作符（>=/<=/==）
    
    Returns:
        dict: {
            "passed": bool,
            "evidence": str,
            "gap": str (if failed),
            "verified_at": "..."
        }
    """
    results = []
    
    # 解析 gate 类型
    gate_lower = gate.lower()
    
    if "文件存在" in gate or "file exists" in gate_lower:
        if output:
            passed, evidence = check_file_exists(output)
            results.append((passed, evidence))
    
    if "json 有效" in gate or "json valid" in gate_lower:
        if output:
            passed, evidence = check_json_valid(output)
            results.append((passed, evidence))
    
    if "≥" in gate or ">=" in gate or "<=" in gate or "==" in gate:
        if metric_file and metric_key and threshold is not None:
            passed, evidence = check_metric_threshold(
                metric_file, metric_key, threshold, operator
            )
            results.append((passed, evidence))
    
    if "矛盾" in gate or "contradiction" in gate_lower:
        if output:
            passed, evidence = check_contradiction(output)
            results.append((passed, evidence))
    
    # 汇总
    if not results:
        return {
            "passed": False,
            "evidence": "无法解析 gate 标准",
            "gap": f"gate '{gate}' 无法解析为可检查项（支持：文件存在/JSON 有效/指标 ≥ 阈值/矛盾检测）",
            "verified_at": datetime.now(timezone.utc).isoformat(),
        }
    
    all_passed = all(p for p, _ in results)
    evidence = "; ".join(e for _, e in results)
    gap = "" if all_passed else "; ".join(e for p, e in results if not p)
    
    return {
        "passed": all_passed,
        "evidence": evidence,
        "gap": gap,
        "verified_at": datetime.now(timezone.utc).isoformat(),
    }


def main():
    ap = argparse.ArgumentParser(description="Verify gate: check if output meets gate standard")
    ap.add_argument("--gate", required=True, help="Gate standard (natural language)")
    ap.add_argument("--output", help="Output file path")
    ap.add_argument("--metric-file", help="Metric file path (JSON)")
    ap.add_argument("--metric-key", help="Metric key name")
    ap.add_argument("--threshold", type=float, help="Threshold value")
    ap.add_argument("--operator", default=">=", help="Comparison operator (>=/<=/==)")
    ap.add_argument("--json", action="store_true", help="Output as JSON")
    args = ap.parse_args()
    
    result = verify(
        args.gate,
        args.output,
        args.metric_file,
        args.metric_key,
        args.threshold,
        args.operator,
    )
    
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        status = "PASS" if result["passed"] else "FAIL"
        print(f"{status}: {result['evidence']}")
        if result["gap"]:
            print(f"Gap: {result['gap']}")
    
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
