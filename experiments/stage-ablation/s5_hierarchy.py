# -*- coding: utf-8 -*-
"""v17 层级目录分解（成璐 2026-11-09 设计）：

把整题一次性拆大树的 P1e 换成逐层 INDEX 分解——每个父节点是一个"文件夹"，
它的子节点清单就是该文件夹的 INDEX.md（只列条目+一句话说明，不抄内容），
每层一次 LLM 调用只处理一个父节点的展开，上下文永远小。

结构对齐项目标准：INDEX 递归可达，父→子的拆分即 index。
无限预算：无 max_rounds / budget_nodes / per_layer_cap；停止只靠 R1（所有叶子都停）。
安全阀 MAX_FRONTIER_ROUNDS=30 只是防死循环（模型反复输出同义节点时 R1 判不出来的兜底）。
"""
import json
import math
from collections import Counter

from ablation_harness import call_llm
from s5_pipeline import (
    _extract_json, _perturb, _sa_tree, decompose, gap_check,
    search_node, verify_node, QUESTIONS,
)

MAX_FRONTIER_ROUNDS = 30  # 安全阀，不是目标函数的一部分


def _parents_block(parents):
    return "\n".join(
        f"{p['id']} [{p.get('level','?')}]: {p['claim']}" for p in parents)


def _confirmed_block(confirmed, limit=40):
    if not confirmed:
        return "（前几轮暂无已确认事实）"
    return "\n".join(f"- {i}: {c} [{s}]" for i, c, s in confirmed[-limit:])


def decompose_layer(question, parents, confirmed, start_id):
    """对给定父节点集合做一次 INDEX 分解。返回新子节点列表。"""
    from s5_pipeline import P1H_INDEX
    prompt = P1H_INDEX.format(
        question=question,
        confirmed_block=_confirmed_block(confirmed),
        parents_block=_parents_block(parents),
        start=start_id,
    ) + _perturb()
    out, _ = call_llm(prompt, max_tokens=8000, temperature=0.7, top_p=0.95)
    d = _extract_json(out or "")
    d = d if isinstance(d, dict) else {}
    nodes = [n for n in (d.get("nodes") or []) if isinstance(n, dict) and n.get("claim")]
    # 编号规范化：强制连续且 level = 父层+1
    parent_levels = {int(str(p.get("level", "L1")).lstrip("L")) for p in parents
                     if str(p.get("level", "")).lstrip("L").isdigit()}
    next_lv = max(parent_levels) + 1 if parent_levels else 1
    for k, n in enumerate(nodes):
        n["id"] = f"N{start_id + k}"
        n.setdefault("level", f"L{next_lv}")
        n.setdefault("source", "search")
    return nodes


def decompose_hierarchy(question, qid="gpu"):
    """主循环：frontier BFS，每轮对最深层所有叶子做 INDEX 分解（分组合批控制 token）。

    返回 (nodes_all, rounds_log)。
    停止：R1 = 某轮所有叶子都没有产生新子节点。
    """
    # 第 0 轮：用现有 decompose 出 L1 骨架（它本来就是干这个的）
    l1, _raw = decompose(question, unlimited=True)  # L1 骨架不封顶：无限预算
    if not l1:
        raise RuntimeError("L1 skeleton empty")
    seen_ids = {n["id"] for n in l1}
    nodes_all = list(l1)
    confirmed = []          # [(id, claim, status)]
    facts = []              # full fact-table records (for P4)
    rounds_log = []
    rnd = 0

    while True:
        rnd += 1
        if rnd > MAX_FRONTIER_ROUNDS:
            print("  [hierarchy] safety valve: MAX_FRONTIER_ROUNDS hit", flush=True)
            break
        lv_max = max(int(str(n.get("level", "L0")).lstrip("L") or 0) for n in nodes_all)
        frontier = [n for n in nodes_all
                    if int(str(n.get("level", "L0")).lstrip("L") or 0) == lv_max]
        new_this_round = []
        for batch_start, i in enumerate(range(0, len(frontier), 3)):
            batch = frontier[i:i + 3]   # 每批 3 个父节点，控制单次 prompt 大小
            kids = decompose_layer(question, batch, confirmed,
                                   start_id=len(nodes_all) + len(new_this_round) + 1)
            new_this_round.extend(kids)
        # 广度审查只对新增部分跑
        if new_this_round:
            added_extra, _missing, _rawb = gap_check(question, new_this_round)
            new_this_round = new_this_round + added_extra[:10]
        # 去重（按 id 和 claim 文本近似）
        existing_claims = {n["claim"][:40] for n in nodes_all}
        deduped = []
        for n in new_this_round:
            if n["id"] in seen_ids or n["claim"][:40] in existing_claims:
                continue
            seen_ids.add(n["id"])
            existing_claims.add(n["claim"][:40])
            deduped.append(n)
        nodes_all.extend(deduped)
        sa, per_layer = _sa_tree(nodes_all)
        # 核验新增的 search 节点：无限预算，全部核验（成璐 2026-11-09：别管速度）
        verified_now = []
        for node in deduped:
            base = {"id": node["id"], "claim": node["claim"],
                    "level": node.get("level", "?"),
                    "source": node.get("source", "search"),
                    "search_query": node.get("search_query", "")}
            if node.get("source") != "search":
                base.update(status="verified",
                            evidence="模型先验/题面给定，未触发检索",
                            corrected_claim=node["claim"])
                verified_now.append((node["id"], node["claim"], "verified"))
            else:
                srcs, err = search_node(node, qid=qid)
                if err:
                    base.update(status="degraded", evidence=f"检索失败: {err}",
                                corrected_claim=node["claim"])
                    verified_now.append((node["id"], node["claim"], "degraded"))
                else:
                    status, evidence, corrected, _r = verify_node(node, srcs)
                    base.update(status=status, evidence=evidence,
                                corrected_claim=corrected or node["claim"])
                    verified_now.append((node["id"], corrected or node["claim"], status))
            facts.append(base)
        confirmed.extend(verified_now)
        stop = "R1-saturation" if not deduped else None
        rounds_log.append({
            "round": rnd, "n_new": len(deduped), "n_total": len(nodes_all),
            "S_alpha": sa, "per_layer": per_layer,
            "frontier_size": len(frontier),
            "n_verified_this_round": len(verified_now), "stop": stop,
        })
        print(f"  [hierarchy] r{rnd}: +{len(deduped)} nodes (total {len(nodes_all)}), "
              f"S_α={sa}, frontier={len(frontier)}, verified +{len(verified_now)}, stop={stop}",
              flush=True)
        if stop:
            break
        prev_sa = sa
    return nodes_all, rounds_log, facts