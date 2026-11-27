# -*- coding: utf-8 -*-
"""M1b 纯提取：盘点 s1/prompts.py 的 prompt 结构 → prompt-inventory.json。

零判断：
  - 用 AST 解析 prompts.py 顶层的 prompt 常量（隐式字符串拼接）与模板函数。
  - line_range / char_count / purpose_one_line 全部从源码机械抽取。
  - purpose_one_line = prompt 文本首句（截到第一个 。或换行，≤50 字），不自己总结。
  - injection_point = 在 s5_state_machine.py 里真正调用该 prompt 的函数（AST 抓
    Name/Attribute 用法，天然排除注释与 docstring；import 别名不算调用点）。

运行：python3 inventory_prompts.py   （在 oood-probe/ 下）
"""
import ast
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PROMPTS_PY = os.path.join(BASE, "s1", "prompts.py")
SM_PY = os.path.join(BASE, "s1", "s5_state_machine.py")
OUT_JSON = os.path.join(BASE, "prompt-inventory.json")


def first_sentence(text):
    """取首句：截到第一个 。(含) 或第一个换行(不含)，strip 后 ≤50 字。"""
    t = text.strip()
    cut = len(t)
    for i, ch in enumerate(t):
        if ch == "\n":
            cut = i
            break
        if ch == "。":
            cut = i + 1
            break
    s = t[:cut].strip()
    if len(s) > 50:
        s = s[:50]
    return s


def parse_prompts(path):
    """返回按源码顺序排列的 prompt 条目（常量 + 模板函数）。"""
    with open(path, encoding="utf-8") as f:
        src = f.read()
    tree = ast.parse(src, filename=path)
    entries = []
    for node in tree.body:
        # 顶层常量：NAME = ( "..." "..." ... )  → 隐式拼接成单个 Constant(str)
        if (isinstance(node, ast.Assign) and len(node.targets) == 1
                and isinstance(node.targets[0], ast.Name)):
            nm = node.targets[0].id
            val = node.value
            if isinstance(val, ast.Constant) and isinstance(val.value, str):
                entries.append({
                    "name": nm,
                    "_kind": "constant",
                    "line_range": [node.lineno, node.end_lineno],
                    "char_count": len(val.value),
                    "purpose_one_line": first_sentence(val.value),
                })
            continue
        # 顶层模板函数：def xxx(...): return (拼接/f-string)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            nm = node.name
            stmts = list(node.body)
            # 去掉 docstring（首句若是字符串表达式），避免污染 char_count/首句
            if (stmts and isinstance(stmts[0], ast.Expr)
                    and isinstance(stmts[0].value, ast.Constant)
                    and isinstance(stmts[0].value.value, str)):
                stmts = stmts[1:]
            frags = []
            for st in stmts:
                for sub in ast.walk(st):
                    if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
                        frags.append((sub.lineno, sub.col_offset, sub.value))
            frags.sort(key=lambda x: (x[0], x[1]))
            joined = "".join(fr[2] for fr in frags)
            entries.append({
                "name": nm,
                "_kind": "function",
                "line_range": [node.lineno, node.end_lineno],
                "char_count": len(joined),  # 静态字符串片段长度（不含运行时插值）
                "purpose_one_line": first_sentence(joined),
            })
    return entries


def build_scopes(tree):
    """收集所有函数作用域 (qualname, lineno, end_lineno)，含嵌套函数与方法。"""
    scopes = []

    def walk(node, stack):
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                qual = ".".join(stack + [child.name])
                scopes.append((qual, child.lineno, child.end_lineno))
                walk(child, stack + [child.name])
            elif isinstance(child, ast.ClassDef):
                walk(child, stack + [child.name])
            else:
                walk(child, stack)

    walk(tree, [])
    return scopes


def enclosing_scope(scopes, line):
    best = None
    for (qn, l0, l1) in scopes:
        if l0 <= line <= l1:
            if best is None or (l1 - l0) < (best[2] - best[1]):
                best = (qn, l0, l1)
    return best[0] if best else "<module>"


def caller_functions(sm_tree, scopes, name):
    """s5_state_machine.py 中真正调用 name 的函数集合（AST 用法，排除注释/docstring/import）。"""
    used_lines = set()
    for node in ast.walk(sm_tree):
        if isinstance(node, ast.Name) and node.id == name:
            used_lines.add(node.lineno)
        elif isinstance(node, ast.Attribute) and node.attr == name:
            used_lines.add(node.lineno)
    callers = set()
    for ln in used_lines:
        callers.add(enclosing_scope(scopes, ln))
    return sorted(callers)


def main():
    with open(PROMPTS_PY, encoding="utf-8") as f:
        prompts_src = f.read()
    with open(SM_PY, encoding="utf-8") as f:
        sm_src = f.read()

    prompts_tree = ast.parse(prompts_src, filename=PROMPTS_PY)
    sm_tree = ast.parse(sm_src, filename=SM_PY)
    sm_scopes = build_scopes(sm_tree)

    entries = parse_prompts(PROMPTS_PY)
    prompts_out = []
    for e in entries:
        prompts_out.append({
            "name": e["name"],
            "line_range": e["line_range"],
            "char_count": e["char_count"],
            "purpose_one_line": e["purpose_one_line"],
            "injection_point": caller_functions(sm_tree, sm_scopes, e["name"]),
        })

    result = {"prompts": prompts_out}
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")

    # ---- 汇总 + 交叉核对 ----
    n_const = sum(1 for e in entries if e["_kind"] == "constant")
    n_func = sum(1 for e in entries if e["_kind"] == "function")
    called = [p["name"] for p in prompts_out if p["injection_point"]]
    not_called = [p["name"] for p in prompts_out if not p["injection_point"]]

    print("== prompt-inventory ==")
    print(f"total prompts : {len(prompts_out)}  (constant={n_const}, function={n_func})")
    print(f"called in s5_state_machine.py : {len(called)}")
    print(f"NOT called in s5_state_machine.py : {len(not_called)} -> {not_called}")
    print("-" * 60)
    for p in prompts_out:
        ip = ", ".join(p["injection_point"]) if p["injection_point"] else "(none in SM)"
        print(f"{p['name']:32s} L{p['line_range'][0]:>3}-{p['line_range'][1]:<3} "
              f"{p['char_count']:>5}c  -> {ip}")
    print("-" * 60)
    print(f"wrote: {OUT_JSON}")
    # 供 grep -c 交叉核对：顶层常量定义数 / 顶层函数定义数
    import re
    grep_const = len(re.findall(r"^[A-Z][A-Z0-9_]* = \(", prompts_src, flags=re.M))
    grep_func = len(re.findall(r"^def ", sm_src.replace("", ""), flags=re.M))  # 占位，实际用 prompts
    grep_func = len(re.findall(r"^def ", prompts_src, flags=re.M))
    print(f"[cross-check] grep-style count in prompts.py: constants={grep_const}, functions={grep_func}")
    print(f"[cross-check] JSON entries={len(prompts_out)}  match={grep_const + grep_func == len(prompts_out)}")


if __name__ == "__main__":
    main()
