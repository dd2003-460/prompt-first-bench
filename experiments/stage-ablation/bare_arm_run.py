#!/usr/bin/env python3
"""bare arm: 裸跑臂（2026-11-21, D 定义）。v2: 纯文本协议（27b 扛不住每轮 JSON）。

与 SM 臂（formula/text）的唯一区别 = 过程控制权：
  - SM 臂：机器控制循环（状态机 + 冗余惩罚 + S_alpha + 强制核验 + 迭代返工 + 强制收尾）
  - bare 臂：模型自己控制循环（自己决定拆什么、搜什么、何时停），
    机器只提供搜索工具（research_hook）+ 记录树，不介入过程。

同目标语义（递归分解树 + 正交/完备/压缩 + 性价比）、同树格式要求、同搜索工具。
测的是"过程本身值多少"——模型为了目标，在树格式下自己如何逼近。

协议（纯文本，27b 友好）：
  每轮模型输出可含：
    SEARCH: <查询语句>   （可选，机器执行搜索并返回结果）
    TREE:                （当前树状态，缩进列表，机器记录最后一版）
    DONE                 （模型自判完备，停止）
  搜索预算耗尽后机器强制停止（不催不罚），然后一次合成调用写最终答案
  （与 SM 臂的 synthesize_answer 对等——两臂都有合成步骤）。

用法:
  python3 bare_arm_run.py nat r01
输出:
  <cwd>/modules/B-pipeline-ablation/data/t53b/runs/{qid}_bare_{round}.json
  <cwd>/modules/B-pipeline-ablation/data/t53b/runs/{qid}_bare_{round}_judge.json
"""
import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ablation_harness import call_llm
from s8b_pilot import QUESTIONS
from s5_pipeline import research_hook
from judge_v2_depth import score_run

# 输出目录：相对 pfb 根（脚本在 experiments/stage-ablation/ 下）
PFB_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RUNS_DIR = os.path.join(PFB_ROOT, "modules/B-pipeline-ablation/data/t53b/runs")

BARE_PROMPT = (
    "你是严谨的研究员。下面是一道待解问题。你的任务：为这道题构建一棵递归分解树，"
    "使最终答案能够『完整、详尽、准确』地回答这道题，且性价比最优（信息密度最高、"
    "不冗余、不遗漏）。\n\n"
    "【树的要求】\n"
    "1. 递归分解：从顶层维度开始逐层下钻，直到叶子节点是可核验的具体断言"
    "（带数字/来源/推导，不是抽象目录名）。\n"
    "2. 正交性：同层兄弟节点必须正交——A 的取值不影响 B 需要查什么 → 可并列；"
    "A 是 B 的父级或子集 → 不得并列，只保留更上层。\n"
    "3. 完备性：题目显式列出的每个子问必须被某节点覆盖；影响决策的关键维度不得遗漏。\n"
    "4. 压缩：同义变体不得重复；能合并的合并；每节点必须携带新增信息，否则删掉。\n"
    "5. 性价比：优先展开对最终答案影响最大的分支；影响小的可以浅一些。"
    "当你判断继续展开的边际信息增益低于成本时，停止——不需要无限展开。\n\n"
    "【每轮输出格式】（纯文本，按以下标记）\n"
    "SEARCH: <查询语句>      （可选。需要查资料时写这一行，机器会执行搜索并返回结果，"
    "你下一轮继续。每轮最多一条 SEARCH。）\n"
    "TREE:                  （你当前维护的完整树，缩进列表，每行一个节点，"
    "格式：- [N1] 断言内容 (来源: given/记忆/已查[1])。每次输出都要给完整树，"
    "机器只记录你最后一版。）\n"
    "DONE                   （你判断树已完备、可以写最终答案时，在末尾写这一行。）\n\n"
    "【流程】你自己控制：先拆顶层维度，逐层下钻，需要查资料就 SEARCH，"
    "判断完备了就写 DONE。机器不控制你的过程、不催你、不罚你——但搜索次数有限"
    "（{max_search} 次），用完后机器会强制你基于已有树写最终答案。\n\n"
    "【问题】\n{question}\n"
)

SEARCH_RESULT_FMT = (
    "\n\n【搜索结果】（你上一条 SEARCH 的结果，引用时标 [已查n]）\n"
    "{results}\n\n继续。"
)

SYNTH_PROMPT = (
    "基于你刚才构建的分解树和搜索到的资料，写这道题的最终完整答案。"
    "要求：覆盖树中每个关键分支的结论；凭记忆的数字标 [凭记忆]，查到的标 [已查]；"
    "不确定的标 [待核验]；给出推导链。直接写答案，不要复述树。\n\n"
    "【问题】\n{question}\n\n"
    "【你的分解树（最后一版）】\n{tree}\n\n"
    "【搜索资料汇总】\n{sources}\n"
)


def _search(query, qid, max_results=8):
    try:
        srcs = research_hook("bare", query, max_results=max_results,
                             enable_local=(qid == "gpu"))
        lines = []
        for i, s in enumerate(srcs or [], 1):
            lines.append(f"[{i}] {s.get('title','')}\n    {s.get('url','')}\n    "
                         f"{s.get('snippet','')[:300]}")
        return "\n".join(lines) if lines else "（无结果）"
    except Exception as e:
        return f"（搜索失败: {e}）"


def _extract_tree(text):
    """从输出里提取 TREE: 之后到 DONE/SEARCH 之前的缩进列表。"""
    m = re.search(r"TREE:\s*\n((?:\s*[-*].*\n?)+)", text)
    if not m:
        return None
    lines = [l.strip() for l in m.group(1).strip().splitlines() if l.strip().startswith(("-", "*"))]
    return lines if lines else None


def run_one(qid, round_id, max_search=8, max_tokens=4096):
    question = QUESTIONS[qid]
    prompt = BARE_PROMPT.format(question=question, max_search=max_search)
    all_sources = []
    last_tree = []
    n_search = 0
    done_by_model = False
    t0 = time.time()

    for step in range(max_search + 3):
        content, _ = call_llm(prompt, max_tokens=max_tokens, temperature=0.7,
                              enable_thinking=False)
        tree = _extract_tree(content)
        if tree:
            last_tree = tree
        if "DONE" in content.upper():
            done_by_model = True
            break
        m = re.search(r"SEARCH:\s*(.+)", content)
        if m and n_search < max_search:
            n_search += 1
            q = m.group(1).strip()
            res = _search(q, qid)
            all_sources.append(f"### SEARCH #{n_search}: {q}\n{res}")
            prompt = prompt + SEARCH_RESULT_FMT.format(results=res)
            print(f"[bare] {qid} {round_id} step{step}: search {n_search}/{max_search} "
                  f"tree={len(last_tree)}", flush=True)
            continue
        # 既没 SEARCH 也没 DONE：再给一次机会（不罚，只提醒格式）
        if step < max_search:
            prompt = prompt + ("\n\n【格式提醒】每轮输出需含 TREE:（完整树）和/或 "
                               "SEARCH:（查询）；完备了就在末尾写 DONE。")
            continue
        break  # 预算耗尽

    elapsed = time.time() - t0
    # 合成最终答案（与 SM 臂 synthesize_answer 对等）
    tree_text = "\n".join(last_tree) if last_tree else "（树为空）"
    sources_text = "\n\n".join(all_sources) if all_sources else "（未搜索）"
    synth = SYNTH_PROMPT.format(question=question, tree=tree_text, sources=sources_text)
    answer, _ = call_llm(synth, max_tokens=max_tokens, temperature=0.7,
                         enable_thinking=False)
    answer = (answer or "").strip()
    elapsed = time.time() - t0

    # 树深度：优先用节点 ID 层级（N2.1.1 → 3），无 ID 时按缩进估
    max_depth = 0
    for l in last_tree:
        m = re.search(r"\[(N[\d.]+)\]", l)
        if m:
            depth = m.group(1).count(".") + 1
        else:
            indent = len(l) - len(l.lstrip())
            depth = indent // 2 + 1
        max_depth = max(max_depth, depth)

    out = {
        "qid": qid,
        "arm": "bare",
        "round": round_id,
        "n_nodes": len(last_tree),
        "max_depth": max_depth,
        "n_search": n_search,
        "done_by_model": done_by_model,
        "elapsed_s": round(elapsed, 1),
        "answer": answer,
        "tree": last_tree,
        "observed_at": datetime.now(timezone.utc).isoformat(),
    }
    os.makedirs(RUNS_DIR, exist_ok=True)
    path = os.path.join(RUNS_DIR, f"{qid}_bare_{round_id}.json")
    with open(path, "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"[bare] {qid} {round_id}: nodes={len(last_tree)} depth={max_depth} "
          f"search={n_search} done_by_model={done_by_model} "
          f"elapsed={elapsed:.0f}s answer_len={len(answer)}", flush=True)
    if answer:
        try:
            j = score_run(qid, answer)
            jpath = os.path.join(RUNS_DIR, f"{qid}_bare_{round_id}_judge.json")
            with open(jpath, "w") as f:
                json.dump(j, f, ensure_ascii=False, indent=2)
            print(f"[bare] {qid} {round_id} judge: overall={j.get('overall')}", flush=True)
        except Exception as e:
            print(f"[bare] {qid} {round_id} judge FAILED: {e}", flush=True)
    else:
        print(f"[bare] {qid} {round_id} NO ANSWER (skip judge)", flush=True)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("qid", choices=["nat", "soc", "gpu"])
    ap.add_argument("round_id", help="e.g. r01")
    ap.add_argument("--max-search", type=int, default=8)
    ap.add_argument("--max-tokens", type=int, default=4096)
    a = ap.parse_args()
    run_one(a.qid, a.round_id, a.max_search, a.max_tokens)
