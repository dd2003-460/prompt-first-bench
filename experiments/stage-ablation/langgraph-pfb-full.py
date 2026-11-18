# -*- coding: utf-8 -*-
"""LangGraph 版 pfb 状态机——按 pfb 检查点逐一对齐。

设计原则（2026-11-18 D 指令）：
1. 复用 pfb 的 DecompStateMachine 实例（不重写 pfb 逻辑），
   把 run() 里每个检查点包成一个 langgraph node。
2. 控制参数用同一个 ObjectiveConfig() 默认值 → 和 pfb 原生跑完全一致。
3. 基础设施：langgraph StateGraph + SqliteSaver（控制流 checkpoint）
   + pfb 的 _save_checkpoint（树形数据 checkpoint，每轮落盘）。
4. 可观测：每轮写 rounds_log + 终盘写 runs-langgraph-pfb-{qid}.json。

检查点映射（pfb run() 行号 → langgraph node）：
  _probe_network (1152)      → probe
  _decompose_l1 (482)        → decompose_l1
  max_nodes/max_depth (1245) → route_after_probe
  DECOMPOSE 阶段 (1257-1491) → decompose
  VERIFY 阶段 (1493-1496)    → verify
  父节点核验 (1498-1501)     → verify（内嵌）
  J_verify→REWORK (1503-1507)→ rework
  D33 矛盾扫描 (1509-1513)   → contradictions
  记录 (1515-1540)           → checkpoint
  CHECKPOINT (1542-1543)     → checkpoint（内嵌 _save_checkpoint）
  J_stop (1545-1554)         → route_after_checkpoint

用法:
  python3 langgraph-pfb-full.py gpu
  python3 langgraph-pfb-full.py nat
  python3 langgraph-pfb-full.py soc
"""
import json
import os
import re
import sys
import time
import operator
from typing import TypedDict, Annotated, Optional

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver

# ── 复用 pfb 状态机（不重写，只包 node）──
from s5_state_machine import (
    DecompStateMachine, ObjectiveConfig, NodeRecord, State, LeakError,
    _ngram_overlap, marginal_gain, judge_necessary_batch,
    classify_edge, classify_edge_var, S_alpha_corrected,
)
from s5_pipeline import gap_check
from s8b_pilot import QUESTIONS
from ablation_harness import call_llm

# ── 全局 SM 实例（langgraph node 间共享；数据在 SM，控制流在 state）──
_SM: Optional[DecompStateMachine] = None


# ═══════════════════════════════════════════════════════════
# LangGraph State（只存控制流；数据在 _SM 实例里）
# ═══════════════════════════════════════════════════════════
class PFBState(TypedDict, total=False):
    # 控制流
    round: int
    stop: bool
    stop_reason: str
    # 每轮分解后待核验的节点 id（verify node 用）
    pending_verify: list
    # 每轮记录（append 语义）
    rounds_log: Annotated[list, operator.add]


# ═══════════════════════════════════════════════════════════
# Node 1: probe — 网络出口探针（pfb _probe_network, 行 1152）
# ═══════════════════════════════════════════════════════════
def probe(state: PFBState) -> dict:
    print("[LG:probe] 网络出口探针...", flush=True)
    _SM._probe_network()
    print(f"[LG:probe] network_degraded={_SM.network_degraded}", flush=True)
    return {}


# ═══════════════════════════════════════════════════════════
# Node 2: decompose_l1 — L1 骨架分解（pfb _decompose_l1, 行 482）
# ═══════════════════════════════════════════════════════════
def decompose_l1(state: PFBState) -> dict:
    print("[LG:decompose_l1] L1 骨架分解...", flush=True)
    _SM.state = State.DECOMPOSE
    _SM._decompose_l1(skip_if_seeded=False)
    print(f"[LG:decompose_l1] L1 完成: {len(_SM.nodes)} 个顶层维度", flush=True)
    return {}


# ═══════════════════════════════════════════════════════════
# Node 3: decompose — 每轮分解（pfb run() 1257-1491）
#   包含：边分类、贡献过滤、_decompose_layer、扇出上限、
#         Q2 正交性、Q4 压缩、gap_check、去重、necessary 过滤、
#         J_decomp 增益、停止判据
# ═══════════════════════════════════════════════════════════
def decompose(state: PFBState) -> dict:
    global _SM
    rnd = state.get("round", 0) + 1
    print(f"\n[LG:decompose] r{rnd} 开始分解...", flush=True)
    _SM.state = State.DECOMPOSE

    # ── 计算 frontier（当前最深层）──
    lv_max = max(int(str(n.level).lstrip("L")) for n in _SM.nodes)
    frontier = [n for n in _SM.nodes
                if int(str(n.level).lstrip("L")) == lv_max]

    # ── 三边分类 + 贡献过滤（pfb 1261-1297）──
    l1_frontier = [p for p in frontier if str(p.level) == "L1"]
    low_contrib_nodes = []
    use_var = _SM.cfg.contrib_samples > 1
    for p in l1_frontier:
        if use_var:
            et, reason, contrib_mean, contrib_std, high_var = classify_edge_var(p.claim, [], _SM.cfg)
            optimistic = contrib_mean + _SM.cfg.lambda_uncertainty * contrib_std
            prune_signal = optimistic
            contrib_display = f"{contrib_mean:.2f}±{contrib_std:.2f}"
        else:
            et, reason, contrib, high_var = classify_edge(p.claim, [], _SM.cfg)
            optimistic = contrib
            prune_signal = contrib
            contrib_display = f"{contrib:.2f}"
        if et != "cartesian":
            print(f"  [LG:decompose] edge-classify {p.id}: {et} ({reason[:50]})", flush=True)
            p.edge_type = et
        if prune_signal < _SM.cfg.contribution_threshold and not high_var:
            print(f"  [LG:decompose] contribution-filter {p.id}: {contrib_display} < {_SM.cfg.contribution_threshold} — skip", flush=True)
            p.status = "degraded"
            low_contrib_nodes.append(p)
    if low_contrib_nodes:
        low_ids = {p.id for p in low_contrib_nodes}
        frontier = [p for p in frontier if p.id not in low_ids]

    # ── 分层分解（pfb 1299-1342）──
    new_nodes = []
    for i in range(0, len(frontier), 3):
        batch = frontier[i:i+3]
        try:
            kids = _SM._decompose_layer(batch)
            # 三边复核
            for p in batch:
                p_children = [c.claim for c in kids if p.id in (c.parent_ids or [])]
                if p_children and len(p_children) >= 2:
                    et, reason, contrib, high_var = classify_edge(p.claim, p_children, _SM.cfg)
                    if et != p.edge_type:
                        print(f"  [LG:decompose] edge-reclassify {p.id}: {p.edge_type}→{et} ({reason[:50]})", flush=True)
                        p.edge_type = et
                        for c in kids:
                            if p.id in (c.parent_ids or []):
                                c.edge_type = et
            # 扇出上限
            base_cap = _SM.cfg.max_kids_per_parent
            for p in batch:
                if p.edge_type == "quotient":
                    cap = min(4, base_cap)
                elif p.edge_type == "stochastic":
                    cap = min(5, base_cap)
                else:
                    cap = base_cap
                pk = [k for k in kids if p.id in (k.parent_ids or [])]
                if len(pk) > cap:
                    base = [n.claim for n in _SM.nodes] + [p.claim]
                    def dist(k):
                        return min((_ngram_overlap(k.claim, c) for c in base), default=0.0)
                    pk.sort(key=dist, reverse=True)
                    dropped = pk[cap:]
                    kids = [k for k in kids if k not in dropped]
                    print(f"  [LG:decompose] fanout cap {cap}: parent {p.id} kept {cap}/{len(pk)+len(dropped)}", flush=True)
            new_nodes.extend(kids)
        except LeakError as e:
            print(f"  [LG:decompose] LEAK r{rnd}: {e} — ABORT (AC2 zero-tolerance)", flush=True)
            raise

    # ── Q2 正交性（pfb 1344-1394）──
    n_orthogonal_dropped = 0
    if new_nodes:
        by_parent = {}
        for nn in new_nodes:
            for pid in (nn.parent_ids or []):
                by_parent.setdefault(pid, []).append(nn)
        ortho_drop_ids = set()
        for pid, siblings in by_parent.items():
            if len(siblings) < 2:
                continue
            pairs = []
            for i in range(len(siblings)):
                for j in range(i + 1, len(siblings)):
                    ov = _ngram_overlap(siblings[i].claim, siblings[j].claim)
                    if ov > 0.5:
                        pairs.append((i, j, ov))
            if not pairs:
                continue
            pair_block = "\n".join(
                f"[{k}] A={siblings[pi].claim[:100]} B={siblings[pj].claim[:100]}"
                for k, (pi, pj, _ov) in enumerate(pairs))
            ortho_prompt = (
                "你是严格审稿人。对下面每对研究子节点，判断 B 能否从 A 推出"
                "（即 B 的信息是否已包含在 A 中，或 B 只是 A 的换措辞/特例）。"
                "能推出 → B 是冗余的。\n\n"
                f"{pair_block}\n\n"
                f"对每对输出一行，共 {len(pairs)} 行，紧凑格式：\"pair\":0,\"redundant\":true\n"
                "只输出这些行。")
            try:
                mtok = min(200 * len(pairs) + 200, 4096)
                out, _ = call_llm(ortho_prompt, max_tokens=mtok, temperature=0.0, retries=2)
                for k, (pi, pj, _ov) in enumerate(pairs):
                    line_pat = rf'\"pair\"\s*:\s*{k}\s*,\s*\"redundant\"\s*:\s*(true|false)'
                    m = re.search(line_pat, out or "")
                    if m and m.group(1) == "true":
                        ortho_drop_ids.add(siblings[pj].id)
                        n_orthogonal_dropped += 1
            except Exception as e:
                print(f"  [LG:decompose] Q2 orthogonality LLM error: {e}", flush=True)
        if ortho_drop_ids:
            new_nodes = [nn for nn in new_nodes if nn.id not in ortho_drop_ids]
            print(f"  [LG:decompose] Q2 orthogonality: dropped {n_orthogonal_dropped} redundant", flush=True)

    # ── Q4 压缩（pfb 1396-1419）──
    n_compression_dropped = 0
    if new_nodes:
        by_parent2 = {}
        for nn in new_nodes:
            for pid in (nn.parent_ids or []):
                by_parent2.setdefault(pid, []).append(nn)
        comp_drop_ids = set()
        for pid, siblings in by_parent2.items():
            if not siblings:
                continue
            parent_claim = next((n.claim for n in _SM.nodes if n.id == pid), "")
            if not parent_claim:
                continue
            gain = marginal_gain([s.claim for s in siblings], [parent_claim])
            if gain < 0.3:
                for s in siblings:
                    comp_drop_ids.add(s.id)
                n_compression_dropped += len(siblings)
                print(f"  [LG:decompose] Q4 compression: parent {pid} gain={gain:.3f} < 0.3 — dropped {len(siblings)}", flush=True)
        if comp_drop_ids:
            new_nodes = [nn for nn in new_nodes if nn.id not in comp_drop_ids]

    # ── gap_check 补充（pfb 1421-1432）──
    if new_nodes:
        added_extra, _miss, _rawb = gap_check(
            _SM.question, [
                {"id": n.id, "claim": n.claim, "level": n.level}
                for n in new_nodes])
        for ae in added_extra[:5]:
            _SM._nid += 1
            new_nodes.append(NodeRecord(
                id=f"N{_SM._nid}",
                claim=ae if isinstance(ae, str) else ae.get("claim", ""),
                level=f"L{lv_max+1}", source="search"))

    # ── 去重（pfb 1434-1443）──
    existing_claims = [n.claim for n in _SM.nodes]
    deduped = []
    for nn in new_nodes:
        is_dup = any(
            _ngram_overlap(nn.claim, ec) > 0.7
            for ec in existing_claims[-80:]
        )
        if not is_dup:
            deduped.append(nn)

    # ── J_precision: necessary 过滤（pfb 1445-1461）──
    id2claim = {n.id: n.claim for n in _SM.nodes}
    cand_list = []
    for nn in deduped:
        par_claims = [id2claim[pid] for pid in nn.parent_ids if pid in id2claim]
        cand_list.append((nn.claim, par_claims))
    verdicts = judge_necessary_batch(cand_list, _SM.confirmed, _SM.cfg)
    necessary_nodes = []
    for nn, v in zip(deduped, verdicts):
        if isinstance(v, bool) and v:
            necessary_nodes.append(nn)
        else:
            _SM.dropped_redundant += 1
    deduped = necessary_nodes
    _SM.nodes.extend(deduped)

    # ── J_decomp: 边际信息增益（pfb 1463-1468）──
    gain = marginal_gain(
        [n.claim for n in deduped],
        existing_claims,
    )
    _SM._gain_history.append(gain)

    # ── 停止判据：necessary 通过率（pfb 1470-1491）──
    _dr = _SM.dropped_redundant if isinstance(_SM.dropped_redundant, int) else 0
    n_new_dropped = _dr - (getattr(_SM, '_prev_dropped', 0) if isinstance(getattr(_SM, '_prev_dropped', 0), int) else 0)
    n_candidates = len(deduped) + n_new_dropped
    pass_rate = len(deduped) / max(n_candidates, 1)
    _SM._prev_dropped = _dr
    if pass_rate < 0.3 and deduped:
        _win = _SM._gain_history[-5:]
        _gstd = (sum((g - sum(_win)/len(_win))**2 for g in _win)/len(_win)) ** 0.5 if len(_win) >= 2 else 0.0
        if _gstd <= _SM.cfg.stop_std_max:
            _SM._no_ness_streak += 1
        else:
            _SM._no_ness_streak = 0
            print(f"    [LG:decompose] high-gain-std ({_gstd:.3f} > {_SM.cfg.stop_std_max}): streak reset", flush=True)
    elif not deduped:
        _SM._no_ness_streak += 1
    else:
        _SM._no_ness_streak = 0

    print(f"  [LG:decompose] r{rnd}: +{len(deduped)} (total {len(_SM.nodes)}), "
          f"gain={gain:.3f}, streak={_SM._no_ness_streak}", flush=True)

    # 饱和停止（pfb 1551-1554）
    stop = False
    stop_reason = ""
    if not deduped:
        stop = True
        stop_reason = "saturation: no new nodes"

    return {
        "round": rnd,
        "pending_verify": [n.id for n in deduped],
        "stop": stop,
        "stop_reason": stop_reason,
    }


# ═══════════════════════════════════════════════════════════
# Node 4: verify — 核验本轮新节点 + 父节点核验
#   （pfb 1493-1501: _verify_batch + _verify_parent_nodes）
# ═══════════════════════════════════════════════════════════
def verify(state: PFBState) -> dict:
    _SM.state = State.VERIFY
    pending_ids = state.get("pending_verify", [])
    if pending_ids:
        batch = [n for n in _SM.nodes if n.id in pending_ids]
        if batch:
            print(f"[LG:verify] 核验 {len(batch)} 个节点...", flush=True)
            _SM._verify_batch(batch)
            n_ver = sum(1 for n in batch if n.status == "verified")
            print(f"[LG:verify] 完成: {n_ver}/{len(batch)} verified", flush=True)
    # 父节点级核验（pfb 1498-1501）
    _SM._verify_parent_nodes()
    return {}


# ═══════════════════════════════════════════════════════════
# Node 5: rework — 返工未 verified 节点（pfb 1503-1507）
# ═══════════════════════════════════════════════════════════
def rework(state: PFBState) -> dict:
    pending_ids = state.get("pending_verify", [])
    deduped = [n for n in _SM.nodes if n.id in pending_ids]
    unverified = [n for n in deduped if n.status != "verified"]
    if unverified and _SM._should_rework(deduped):
        _SM.state = State.REWORK
        print(f"[LG:rework] 返工 {len(unverified)} 个未 verified 节点...", flush=True)
        _SM._rework(unverified)
        n_ver = sum(1 for n in unverified if n.status == "verified")
        print(f"[LG:rework] 完成: {n_ver}/{len(unverified)} 转 verified", flush=True)
    else:
        print(f"[LG:rework] 跳过（{len(unverified)} 未 verified，不触发返工）", flush=True)
    return {}


# ═══════════════════════════════════════════════════════════
# Node 6: contradictions — 全局矛盾扫描（pfb 1509-1513）
# ═══════════════════════════════════════════════════════════
def contradictions(state: PFBState) -> dict:
    rnd = state.get("round", 0)
    print(f"[LG:contradictions] r{rnd} 全局矛盾扫描...", flush=True)
    _SM._scan_contradictions(rnd)
    n_new = sum(1 for c in _SM.contradiction_events if c.get("round") == rnd)
    print(f"[LG:contradictions] 发现 {n_new} 个矛盾", flush=True)
    return {}


# ═══════════════════════════════════════════════════════════
# Node 7: checkpoint — 记录 + 落盘 + 停止判据
#   （pfb 1515-1554: 记录 + _save_checkpoint + J_stop）
# ═══════════════════════════════════════════════════════════
def checkpoint(state: PFBState) -> dict:
    global _SM
    rnd = state.get("round", 0)
    pending_ids = state.get("pending_verify", [])
    deduped = [n for n in _SM.nodes if n.id in pending_ids]

    # ── 记录（pfb 1515-1540）──
    sa = S_alpha_corrected(
        [{"level": n.level, "claim": n.claim} for n in _SM.nodes],
        _SM.cfg)
    from collections import Counter as _C
    edge_counts = dict(_C(n.edge_type for n in _SM.nodes))
    n_orth = 0  # 本轮正交丢弃数（decompose node 里算的，这里简化为 0）
    n_comp = 0  # 本轮压缩丢弃数
    round_entry = {
        "round": rnd,
        "n_new": len(deduped),
        "n_total": len(_SM.nodes),
        "gain": round(_SM._gain_history[-1], 3) if _SM._gain_history else 0.0,
        "S_alpha_corr": round(sa, 2),
        "frontier": 0,  # 简化：不重复算 frontier
        "verified": sum(1 for n in deduped if n.status == "verified"),
        "reworked": sum(1 for n in deduped if n.rework_count > 0),
        "dropped_redundant": _SM.dropped_redundant,
        "low_gain_streak": _SM._no_ness_streak,
        "edge_types": edge_counts,
        "contradictions_found": sum(1 for c in _SM.contradiction_events if c.get("round") == rnd),
        "n_orthogonal_dropped": n_orth,
        "n_compression_dropped": n_comp,
    }
    _SM.rounds_log.append(round_entry)
    print(f"  [LG:checkpoint] r{rnd}: +{len(deduped)} (total {len(_SM.nodes)}), "
          f"S_α'={sa:.1f}, ver={round_entry['verified']}/{len(deduped)}, "
          f"streak={_SM._no_ness_streak}", flush=True)

    # ── CHECKPOINT 落盘（pfb 1542-1543）──
    _SM._save_checkpoint(rnd)

    # ── J_stop（pfb 1545-1554）──
    stop = state.get("stop", False)
    stop_reason = state.get("stop_reason", "")
    if not stop and _SM._no_ness_streak >= _SM.cfg.stop_rounds:
        stop = True
        stop_reason = f"stop_rounds: {_SM._no_ness_streak} consecutive low-gain rounds"
        print(f"  [LG:checkpoint] STOP: {stop_reason}", flush=True)
    if not stop and not deduped:
        stop = True
        stop_reason = "saturation: no new nodes"
        print(f"  [LG:checkpoint] STOP: {stop_reason}", flush=True)

    return {
        "rounds_log": [round_entry],
        "stop": stop,
        "stop_reason": stop_reason,
    }


# ═══════════════════════════════════════════════════════════
# Node 8: stop — 终止
# ═══════════════════════════════════════════════════════════
def stop(state: PFBState) -> dict:
    _SM.state = State.STOP
    print(f"\n[LG:stop] 状态机终止: {state.get('stop_reason', 'unknown')}", flush=True)
    return {}


# ═══════════════════════════════════════════════════════════
# 条件路由
# ═══════════════════════════════════════════════════════════
def route_after_probe(state: PFBState) -> str:
    """probe 之后：检查 max_nodes/max_depth（pfb 1245-1252）。"""
    if len(_SM.nodes) >= _SM.cfg.max_nodes:
        print(f"[LG:route] max_nodes={_SM.cfg.max_nodes} hit → stop", flush=True)
        return "stop"
    if _SM.nodes:
        lv_max = max(int(str(n.level).lstrip("L")) for n in _SM.nodes)
        if lv_max >= _SM.cfg.max_depth:
            print(f"[LG:route] max_depth={_SM.cfg.max_depth} hit → stop", flush=True)
            return "stop"
    return "decompose"


def route_after_checkpoint(state: PFBState) -> str:
    """checkpoint 之后：stop? → stop : decompose（下一轮）"""
    if state.get("stop", False):
        return "stop"
    return "decompose"


# ═══════════════════════════════════════════════════════════
# 构建图
# ═══════════════════════════════════════════════════════════
def build_graph():
    g = StateGraph(PFBState)
    g.add_node("probe", probe)
    g.add_node("decompose_l1", decompose_l1)
    g.add_node("decompose", decompose)
    g.add_node("verify", verify)
    g.add_node("rework", rework)
    g.add_node("contradictions", contradictions)
    g.add_node("checkpoint", checkpoint)
    g.add_node("stop", stop)

    # 入口：probe
    g.set_entry_point("probe")
    # probe → decompose_l1（首次）或 decompose（resume）
    g.add_edge("probe", "decompose_l1")
    # decompose_l1 → 条件路由（max_nodes/max_depth 检查）
    g.add_conditional_edges("decompose_l1", route_after_probe,
                            {"decompose": "decompose", "stop": "stop"})
    # decompose → verify → rework → contradictions → checkpoint
    g.add_edge("decompose", "verify")
    g.add_edge("verify", "rework")
    g.add_edge("rework", "contradictions")
    g.add_edge("contradictions", "checkpoint")
    # checkpoint → 条件路由（stop? → stop : decompose 下一轮）
    g.add_conditional_edges("checkpoint", route_after_checkpoint,
                            {"stop": "stop", "decompose": "decompose"})
    # stop → END
    g.add_edge("stop", END)

    return g


# ═══════════════════════════════════════════════════════════
# 主函数
# ═══════════════════════════════════════════════════════════
def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("qid", nargs="?", default="gpu", help="题目 id (nat/soc/gpu)")
    ap.add_argument("--dry-run", action="store_true", help="只 build+compile 不跑 LLM")
    ap.add_argument("--max-nodes", type=int, default=None, help="覆盖 max_nodes（快速验证用）")
    ap.add_argument("--max-depth", type=int, default=None, help="覆盖 max_depth")
    args = ap.parse_args()
    qid = args.qid
    question = QUESTIONS[qid]

    # 控制参数：默认 = pfb 原生 ObjectiveConfig()；--max-nodes/--max-depth 可覆盖
    cfg = ObjectiveConfig()
    if args.max_nodes is not None:
        cfg.max_nodes = args.max_nodes
    if args.max_depth is not None:
        cfg.max_depth = args.max_depth

    print(f"=== LangGraph PFB 完整版: {qid} ===", flush=True)
    print(f"题目: {question[:100]}...", flush=True)
    print(f"配置: max_nodes={cfg.max_nodes}, max_depth={cfg.max_depth}, "
          f"verify_threshold={cfg.verify_threshold}, max_rework={cfg.max_rework}", flush=True)

    # dry-run: 只 build+compile 不跑 LLM
    if args.dry_run:
        g = build_graph()
        from langgraph.checkpoint.memory import MemorySaver
        c = g.compile(checkpointer=MemorySaver())
        gd = c.get_graph()
        print(f"dry-run OK: nodes={list(gd.nodes)}, edges={len(list(gd.edges))}", flush=True)
        return

    # 初始化 SM 实例（控制参数 = pfb 默认 ObjectiveConfig()）
    global _SM
    _SM = DecompStateMachine(question, qid=qid, cfg=cfg)

    # 构建图 + SqliteSaver（控制流 checkpoint）
    g = build_graph()
    ckpt_file = f"/tmp/langgraph-pfb-full-{qid}.sqlite"
    if os.path.exists(ckpt_file):
        os.unlink(ckpt_file)
    print(f"checkpoint 文件: {ckpt_file}", flush=True)

    graph = None
    with SqliteSaver.from_conn_string(ckpt_file) as saver:
        graph = g.compile(checkpointer=saver)

        t0 = time.time()
        try:
            # recursion_limit：默认 25 不够（nat 跑到 N254 超限挂了，2026-11-19）。
            # 图拓扑是 expand/verify/rework 循环，一个图步处理一批 SM 节点，
            # 25 步 ≈ N250。设 300 留足余量（防死循环靠图内 stop 条件，不靠这个上限）。
            final_state = graph.invoke(
                {"round": 0, "stop": False, "stop_reason": "",
                 "pending_verify": [], "rounds_log": []},
                config={"configurable": {"thread_id": f"pfb-full-{qid}"},
                        "recursion_limit": 300}
            )
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(f"\n[LG] 异常终止: {e}", flush=True)
            return
        elapsed = time.time() - t0

    # ── 终盘 ──
    n_total = len(_SM.nodes)
    n_verified = sum(1 for n in _SM.nodes if n.status == "verified")
    n_degraded = sum(1 for n in _SM.nodes if n.status == "degraded")
    verified_rate = n_verified / max(n_total, 1)
    sa = S_alpha_corrected(
        [{"level": n.level, "claim": n.claim} for n in _SM.nodes],
        _SM.cfg)

    print(f"\n=== 结果 ===", flush=True)
    print(f"总节点: {n_total}", flush=True)
    print(f"verified: {n_verified} ({verified_rate:.3f})", flush=True)
    print(f"degraded: {n_degraded}", flush=True)
    print(f"S_α': {sa:.1f}", flush=True)
    print(f"轮数: {len(_SM.rounds_log)}", flush=True)
    print(f"耗时: {elapsed:.1f}s", flush=True)
    print(f"停止原因: {final_state.get('stop_reason', 'unknown')}", flush=True)

    # 写终盘 JSON
    out_file = f"runs-langgraph-pfb-{qid}.json"
    result = {
        "qid": qid,
        "question": question,
        "total_nodes": n_total,
        "verified": n_verified,
        "degraded": n_degraded,
        "verified_rate": round(verified_rate, 4),
        "S_alpha_corr": round(sa, 2),
        "rounds": len(_SM.rounds_log),
        "elapsed_s": round(elapsed, 1),
        "stop_reason": final_state.get("stop_reason", ""),
        "leak_hits_total": _SM.leak_hits_total,
        "rework_events": _SM.rework_events,
        "contradiction_events": _SM.contradiction_events,
        "objective": _SM.objective,
        "rounds_log": _SM.rounds_log,
        "nodes": [
            {
                "id": n.id, "claim": n.claim, "level": n.level,
                "source": n.source, "status": n.status,
                "evidence": n.evidence[:200], "rework_count": n.rework_count,
                "parent_ids": n.parent_ids, "edge_type": n.edge_type,
            }
            for n in _SM.nodes
        ],
    }
    with open(out_file, "w") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"终盘: {out_file}", flush=True)


if __name__ == "__main__":
    main()
