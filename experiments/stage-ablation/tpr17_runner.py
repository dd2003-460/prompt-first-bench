#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T-PR-17 prompt 序列消融 runner（一期 3 臂）。

臂定义（见 tasks/T-PR-17-decomp.md F3）:
  canonical    : decompose->verify->rework->contradiction（现状基线）
  verify-off   : patch _verify_batch 直接标 verified（不核验直接接受，rework 不触发）
  null-control : canonical 序列 + ShuffledList 包装 self.confirmed（state 块乱序，纯位置扰动）

实现 = monkey-patch（不改 s5_state_machine.py 本体，K7 进程已加载旧代码）。
F2b 约束 1/2/3 硬性记录: 每 call token 数 + tool calls 次数 + evidence delta（verify 前后节点/证据变化）。
多指标: depth / 节点覆盖 / precision / parent-link 正确率 / verified 比例 / 重复缺失 / 失败率。

用法:
  python3 tpr17_runner.py --mode preflight --checkpoints r1,r2,r3
  python3 tpr17_runner.py --mode smoke --arm verify-off --checkpoint r1
  python3 tpr17_runner.py --arm canonical --checkpoint r1 --rep 5 --budget 719
"""
import argparse
import copy
import datetime
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

DATA_ROOT = "/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/tpr17"
CKPT_BASE = os.path.join(HERE, "checkpoints/archive/budget-719-r1-20261122-143216")
ARMS = ["canonical", "verify-off", "null-control"]


class ShuffledList:
    """包装 self.confirmed：切片返回 shuffle 副本（state 块乱序），append 透传。
    纯位置扰动——_decompose_layer 与 judge_necessary_batch 都看到乱序 state 块。"""
    def __init__(self, inner, rng):
        self._inner = inner
        self._rng = rng
    def __getitem__(self, idx):
        if isinstance(idx, slice):
            seg = self._inner[idx]
            sh = list(seg)
            self._rng.shuffle(sh)
            return sh
        return self._inner[idx]
    def __iter__(self):
        sh = list(self._inner)
        self._rng.shuffle(sh)
        return iter(sh)
    def __len__(self):
        return len(self._inner)
    def append(self, item):
        self._inner.append(item)


class CallLog:
    """F2b 约束 1/2: 每 call 的 token 数 + tool calls 次数 + evidence delta。"""
    def __init__(self):
        self.calls = []
        self.tool_calls = 0
        self._snapshots = []

    def log_call(self, kind, tin, tout):
        self.calls.append({"kind": kind, "in": tin, "out": tout})

    def snapshot(self, nodes):
        self._snapshots.append({
            "n_nodes": len(nodes),
            "evidence_chars": sum(len(n.evidence or "") for n in nodes),
            "verified": sum(1 for n in nodes if n.status == "verified"),
        })


def _wrap_call_llm(sm_mod, log):
    """包 s5_state_machine.call_llm：记录每 call 的 token（F2b 约束 1）。"""
    orig = sm_mod.call_llm

    def wrapped(prompt, *a, **k):
        content, usage = orig(prompt, *a, **k)
        log.log_call("llm", usage.get("in", 0), usage.get("out", 0))
        return content, usage

    sm_mod.call_llm = wrapped
    return orig


def _wrap_save_checkpoint(sm, log):
    """包 _save_checkpoint：每次落盘前抓 evidence 快照（F2b 约束 3: evidence delta）。"""
    orig = sm._save_checkpoint

    def wrapped(rnd):
        log.snapshot(sm.nodes)
        return orig(rnd)

    sm._save_checkpoint = wrapped
    return orig


def _patch_verify_off(sm):
    """verify-off 臂：patch _verify_batch 直接标 verified，不核验直接接受。
    语义干净：无 search/verify LLM 调用 → rework 不触发（无 degraded 节点）。"""
    def fake_verify(batch):
        for n in batch:
            n.status = "verified"
            if not n.evidence:
                n.evidence = "[verify-off] 未核验直接接受（monkey-patch）"
            sm.confirmed.append((n.id, n.claim, "verified"))
        return batch

    sm._verify_batch = fake_verify


def _patch_null_control(sm, rng):
    """null-control 臂：ShuffledList 包装 self.confirmed（state 块乱序，纯位置扰动）。"""
    sm.confirmed = ShuffledList(sm.confirmed, rng)


def _count_tool_calls(sm):
    """tool calls 次数：verify 阶段每个 search=source 节点触发联网检索（search_node）。
    用 retrieval_sources 非空的节点数近似（联网检索成功留下来源）。"""
    return sum(1 for n in sm.nodes if n.retrieval_sources)


def _resolve_ckpt(spec):
    """checkpoint spec -> 绝对路径。支持 'r1'/'r2'/'r3' 或完整路径。"""
    if os.path.isdir(spec):
        return spec
    if spec in ("r1", "r2", "r3"):
        p = os.path.join(CKPT_BASE, f"sm-gpu-{spec}")
        if os.path.isdir(p):
            return p
    return spec


def _seed_nodes(sm, sm_mod, meta, nodes):
    """从 checkpoint 种子 self.nodes / self.confirmed / self._nid / self.ckpt_round。
    镜像 s5_state_machine.main 的 resume 逻辑（L1 跳过 decompose）。"""
    id2rec = {}
    for nd in nodes:
        rec = sm_mod.NodeRecord(
            id=nd["id"], claim=nd["claim"], level=nd.get("level", "L1"),
            source=nd.get("source", "search"), status=nd.get("status", "pending"),
            evidence=nd.get("evidence", ""), corrected_claim=nd.get("corrected_claim", ""),
            rework_count=nd.get("rework_count", 0), parent_ids=list(nd.get("parent_ids") or []),
            objective=nd.get("objective"), edge_type=nd.get("edge_type", "cartesian"),
            search_query=nd.get("search_query", ""), retrieval_sources=list(nd.get("retrieval_sources") or []),
        )
        sm.nodes.append(rec)
        id2rec[rec.id] = rec
    # _nid: 续编号（镜像 main: max(N{num})）
    mx = 0
    for nid in id2rec:
        if nid.startswith("N"):
            try:
                mx = max(mx, int(nid[1:]))
            except ValueError:
                pass
    sm._nid = mx
    sm.ckpt_round = int(meta.get("round", 0) or 0)
    # confirmed: 非 pending 节点（镜像 main resume）
    for rec in sm.nodes:
        if rec.status != "pending":
            sm.confirmed.append((rec.id, rec.claim, rec.status))
    return id2rec


def build_sm(arm, ckpt_spec, budget, seed, qid="gpu", question=None):
    """构造已种子 checkpoint + 应用臂 patch 的 SM。返回 (sm, sm_mod, log, meta, id2rec)。
    question 优先取 checkpoint meta['question']（权威，与生产一致），其次参数。"""
    import s5_state_machine as sm_mod

    ckpt = _resolve_ckpt(ckpt_spec)
    # 先读 meta 拿 question（checkpoint 自带，与生产一致；qid 不在 QUESTIONS 也不会跑错题）
    meta_pre = json.load(open(os.path.join(ckpt, "meta.json")))
    q = question or meta_pre.get("question") or ""
    sm = sm_mod.DecompStateMachine(q, qid=qid,
                                   cfg=sm_mod.ObjectiveConfig(max_nodes=budget, max_depth=5))
    log = CallLog()
    _wrap_call_llm(sm_mod, log)
    meta, nodes = sm._load_checkpoint(ckpt)
    id2rec = _seed_nodes(sm, sm_mod, meta, nodes)
    _wrap_save_checkpoint(sm, log)
    rng = random.Random(seed)
    if arm == "verify-off":
        _patch_verify_off(sm)
    elif arm == "null-control":
        _patch_null_control(sm, rng)
    # canonical: 无 patch
    return sm, sm_mod, log, meta, id2rec


def compute_metrics(sm, log, id2rec):
    """F2b 约束 3: 多指标判分（depth 单独会奖励浅树/节点膨胀，必须并列报）。
    返回 dict: depth / 节点覆盖 / precision / parent-link 正确率 / verified 比例 /
    重复缺失 / 失败率 + F2b 1/2 (token, tool calls, evidence delta)。"""
    nodes = sm.nodes
    n = len(nodes)
    ids = {x.id for x in nodes}
    # depth: 最长 parent 链（root=1）
    depth_of = {}
    def _depth(nid, seen=None):
        if seen is None:
            seen = set()
        if nid in depth_of:
            return depth_of[nid]
        if nid in seen:
            return 0
        seen.add(nid)
        rec = id2rec.get(nid)
        if rec is None or not rec.parent_ids:
            depth_of[nid] = 1
            return 1
        d = 1 + max(_depth(pid, seen) for pid in rec.parent_ids if pid in id2rec)
        depth_of[nid] = d
        return d
    depth = max((_depth(x.id) for x in nodes), default=0)
    # parent-link 正确率: 非根节点 parent_ids 非空且全部指向存在节点
    nonroot = [x for x in nodes if str(x.level) != "L1"]
    ok_link = 0
    for x in nonroot:
        pids = x.parent_ids or []
        if pids and all(p in ids for p in pids):
            ok_link += 1
    link_acc = (ok_link / len(nonroot)) if nonroot else 1.0
    # verified 比例
    n_ver = sum(1 for x in nodes if x.status == "verified")
    # 重复/缺失: 同 claim 归一化后重复计数；缺失=非根节点 parent 链断（link 失败）
    norm = {}
    dup = 0
    for x in nodes:
        key = "".join((x.claim or "").split())[:40]
        if key in norm:
            dup += 1
        norm[key] = x.id
    missing_link = len(nonroot) - ok_link
    # 失败率: rework 后仍非 verified / 总（degraded+pending 视为未成功核验）
    n_fail = sum(1 for x in nodes if x.status in ("degraded", "pending"))
    fail_rate = (n_fail / n) if n else 0.0
    # F2b 1/2: token + tool calls + evidence delta
    tot_in = sum(c["in"] for c in log.calls)
    tot_out = sum(c["out"] for c in log.calls)
    snaps = log._snapshots
    ev_delta = (snaps[-1]["evidence_chars"] - snaps[0]["evidence_chars"]) if snaps else 0
    return {
        "n_nodes": n, "depth": depth,
        "coverage_nonroot": len(nonroot), "precision_dup": dup,
        "parent_link_accuracy": round(link_acc, 4),
        "verified_ratio": round(n_ver / n, 4) if n else 0.0,
        "duplicate_nodes": dup, "missing_link_nodes": missing_link,
        "failure_rate": round(fail_rate, 4),
        "tokens_in": tot_in, "tokens_out": tot_out, "tokens_total": tot_in + tot_out,
        "n_llm_calls": len(log.calls), "tool_calls": _count_tool_calls(sm),
        "evidence_delta_chars": ev_delta,
        "evidence_snapshots": snaps,
    }


REQ_FIELDS = ["id", "claim", "level", "source", "status", "evidence",
              "corrected_claim", "rework_count", "parent_ids", "objective",
              "edge_type", "search_query", "retrieval_sources"]


def _read_tree(root):
    """递归读树形 checkpoint 的所有 node.json。"""
    nodes = []
    def rec(d):
        for fn in sorted(os.listdir(d)):
            fp = os.path.join(d, fn)
            if os.path.isdir(fp) and fn[0].isdigit():
                nj = os.path.join(fp, "node.json")
                if os.path.exists(nj):
                    nodes.append(json.load(open(nj)))
                rec(fp)
    rec(root)
    return nodes


def preflight(specs):
    """T1: 3 checkpoint preflight——JSON schema 完整性 + parent-link 完整性 + T5 bug 核验。
    preflight 失败 = 记录为结果，不静默剔除。返回 (report_dict, ok_bool)。"""
    report = {"checkpoints": {}, "overall_ok": True}
    for spec in specs:
        path = _resolve_ckpt(spec)
        entry = {"path": path, "exists": os.path.isdir(path)}
        if not entry["exists"]:
            report["checkpoints"][spec] = entry
            report["overall_ok"] = False
            continue
        meta = json.load(open(os.path.join(path, "meta.json")))
        nodes = _read_tree(path)
        ids = {n["id"] for n in nodes}
        entry["n_nodes_meta"] = meta.get("n_nodes")
        entry["n_nodes_actual"] = len(nodes)
        entry["unique_ids"] = len(ids)
        entry["round"] = meta.get("round")
        entry["levels"] = {}
        for n in nodes:
            entry["levels"][n.get("level")] = entry["levels"].get(n.get("level"), 0) + 1
        # schema 完整性
        bad_schema = [(n.get("id"), [f for f in REQ_FIELDS if f not in n])
                      for n in nodes if any(f not in n for f in REQ_FIELDS)]
        entry["schema_missing_count"] = len(bad_schema)
        entry["schema_missing_examples"] = bad_schema[:5]
        # parent-link 完整性
        dangling = [(n["id"], pid) for n in nodes for pid in (n.get("parent_ids") or [])
                    if pid not in ids]
        entry["dangling_parent_count"] = len(dangling)
        entry["dangling_examples"] = dangling[:5]
        # T5 bug: 非 L1 节点 parent_ids 为空（持久化丢失签名）
        t5 = [n["id"] for n in nodes
              if str(n.get("level")) != "L1" and not (n.get("parent_ids") or [])]
        entry["t5_empty_parent_nonroot"] = t5
        entry["t5_hit"] = len(t5) > 0
        # 单轮 gap_check 补充签名：空 parent 的非 L1 节点 ≤5/轮（added_extra[:5]）
        entry["t5_is_gapcheck_supplement"] = (len(t5) <= 5)
        entry["pass"] = (entry["schema_missing_count"] == 0
                         and entry["dangling_parent_count"] == 0
                         and entry["n_nodes_meta"] == entry["n_nodes_actual"])
        if not entry["pass"]:
            report["overall_ok"] = False
        report["checkpoints"][spec] = entry
    # T5 bug 累积说明：gap_check 补充节点每轮新增 ≤5，且跨轮持久化（r1 的 5 个在 r2/r3 仍在）。
    # 按 spec 顺序算每轮净增，标注"累积"而非单轮。
    seq = [report["checkpoints"][s] for s in specs if s in report["checkpoints"]]
    prev = 0
    for e in seq:
        cur = len(e.get("t5_empty_parent_nonroot", []))
        e["t5_net_new_this_round"] = cur - prev
        e["t5_cumulative"] = cur
        prev = cur
    report["t5_bug_summary"] = {
        "hit": all(e.get("t5_hit") for e in seq),
        "note": ("T5 parent_ids 持久化丢失 bug 命中全部 3 checkpoint：gap_check 补充节点"
                 "（added_extra[:5]）创建时未设 parent_ids，跨轮累积持久化。"
                 "非 L1 节点 parent 链断裂 → depth/parent-link 指标受影响，但 JSON schema 完整、"
                 "无 dangling parent（已存在的节点 parent 都在）。resume 续跑时这些节点会被当 root 处理。"),
    }
    return report, report["overall_ok"]


def smoke_test(arm, ckpt_spec, budget, seed):
    """T3 冒烟（dry-run）：patch 能加载 + checkpoint 能加载 + 首个 prompt 能构造。
    绝不发 LLM 调用（vLLM 被 719 队列占用）。返回 (ok_bool, info_dict)。"""
    import s5_state_machine as sm_mod
    info = {"arm": arm, "checkpoint": _resolve_ckpt(ckpt_spec)}
    try:
        sm, sm_mod, log, meta, id2rec = build_sm(arm, ckpt_spec, budget, seed)
    except Exception as e:
        info["error"] = f"build_sm failed: {type(e).__name__}: {e}"
        return False, info
    info["n_nodes_seeded"] = len(sm.nodes)
    info["n_confirmed"] = len(sm.confirmed)
    info["_nid_next"] = sm._nid + 1
    info["ckpt_round"] = sm.ckpt_round
    # patch 加载核验
    if arm == "verify-off":
        info["patch_loaded"] = sm._verify_batch.__name__ == "fake_verify"
    elif arm == "null-control":
        info["patch_loaded"] = isinstance(sm.confirmed, ShuffledList)
    else:
        info["patch_loaded"] = True  # canonical 无 patch
    # 首个 prompt 能构造：镜像 run() 首轮——frontier=最深层节点，_decompose_layer 构造 prompt。
    # 不调 call_llm：手工复刻 prompt 拼装（与 _decompose_layer 同源），验证可构造 + 无 KeyError。
    try:
        lv_max = max(int(str(n.level).lstrip("L")) for n in sm.nodes)
        frontier = [n for n in sm.nodes if int(str(n.level).lstrip("L")) == lv_max][:3]
        parents_block = "\n".join(
            f"{p.id} [{p.level}] (edge={p.edge_type}): {p.claim}" for p in frontier)
        cb = sm.confirmed[-40:] if sm.confirmed else []
        confirmed_block = "\n".join(f"- {i}: {c} [{s}]" for i, c, s in cb) or "（暂无）"
        from s5_pipeline import P1H_INDEX
        prompt = sm._safe_prompt(P1H_INDEX, question=sm.question,
                                 confirmed_block=confirmed_block,
                                 parents_block=parents_block,
                                 start=len(sm.nodes) + 1)
        info["first_prompt_constructed"] = True
        info["first_prompt_len"] = len(prompt)
        info["first_frontier"] = [p.id for p in frontier]
        info["first_prompt_head"] = prompt[:200]
    except Exception as e:
        info["first_prompt_constructed"] = False
        info["prompt_error"] = f"{type(e).__name__}: {e}"
    ok = info.get("patch_loaded") and info.get("first_prompt_constructed")
    return ok, info


def run_arm(arm, ckpt_spec, rep, budget, seed, qid="gpu", out_root=DATA_ROOT):
    """跑一个 cell（arm × checkpoint × rep）。发真实 LLM 调用。返回 metrics dict。"""
    os.makedirs(out_root, exist_ok=True)
    sm, sm_mod, log, meta, id2rec = build_sm(arm, ckpt_spec, budget, seed, qid=qid)
    # checkpoint 输出隔离到本 cell 子目录（防跨 cell 串档）
    cell_ckpt = os.path.join(out_root, f"{arm}_{ckpt_spec}_r{rep}_ckpt")
    os.makedirs(cell_ckpt, exist_ok=True)
    os.environ["SM_CKPT_DIR"] = cell_ckpt
    result = sm.run(skip_l1=True)
    metrics = compute_metrics(sm, log, id2rec)
    metrics.update({
        "arm": arm, "checkpoint": ckpt_spec, "rep": rep, "budget": budget,
        "seed": seed, "qid": qid, "final_state": result.final_state,
        "n_rework_events": len(result.rework_events),
        "leak_hits_total": result.leak_hits_total,
        "ts": datetime.datetime.now().isoformat(timespec="seconds"),
    })
    out_path = os.path.join(out_root, f"{arm}_{ckpt_spec}_r{rep}.json")
    json.dump(metrics, open(out_path, "w"), ensure_ascii=False, indent=1)
    return metrics


def main(argv=None):
    ap = argparse.ArgumentParser(description="T-PR-17 prompt 序列消融 runner（3 臂）")
    ap.add_argument("--mode", choices=["preflight", "smoke", "run"], default="run")
    ap.add_argument("--arm", choices=ARMS, default="canonical")
    ap.add_argument("--checkpoint", default="r1", help="r1/r2/r3 或完整路径")
    ap.add_argument("--checkpoints", default="r1,r2,r3", help="preflight: 逗号分隔列表")
    ap.add_argument("--rep", type=int, default=1)
    ap.add_argument("--budget", type=int, default=719, help="max_nodes")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--qid", default="gpu")
    ap.add_argument("--out", default=DATA_ROOT)
    a = ap.parse_args(argv)

    if a.mode == "preflight":
        specs = [s.strip() for s in a.checkpoints.split(",") if s.strip()]
        report, ok = preflight(specs)
        out_path = os.path.join(a.out, "preflight.json")
        os.makedirs(a.out, exist_ok=True)
        report["ts"] = datetime.datetime.now().isoformat(timespec="seconds")
        json.dump(report, open(out_path, "w"), ensure_ascii=False, indent=1)
        print(json.dumps(report, ensure_ascii=False, indent=1))
        print(f"\n[preflight] overall_ok={ok} → {out_path}")
        return 0 if ok else 2

    if a.mode == "smoke":
        ok, info = smoke_test(a.arm, a.checkpoint, a.budget, a.seed)
        print(json.dumps(info, ensure_ascii=False, indent=1))
        print(f"\n[smoke] arm={a.arm} ok={ok}")
        return 0 if ok else 2

    # run mode（正式 run，T4 用；vLLM 释放后）
    m = run_arm(a.arm, a.checkpoint, a.rep, a.budget, a.seed, qid=a.qid, out_root=a.out)
    print(json.dumps(m, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
