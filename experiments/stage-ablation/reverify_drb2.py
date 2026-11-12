#!/usr/bin/env python3
"""E2/自愈脚本: drb-2 51 个 degraded search 节点用修复后的 research_hook 重跑 verify。

背景: runs-s5-sm-drb-2.json 里 51 个 degraded 节点的 evidence 全是
"检索失败: no sources from any channel (all 5 failed)" —— 根因是 research_hook.py
_JUNK_PATTERNS 正则尾部多一个 | 造成空分支匹配所有输入, 把所有源全杀了 (L12)。
resume 救不回它们 (主循环只 verify 新拆出的节点), 所以独立重跑。

逻辑: 读 runs json → 挑 status=degraded & source=search → 逐个 search_node + verify_node
→ 回写新 status/evidence/corrected_claim → 落盘 runs-s5-sm-drb-2-reverified.json
+ 打印 before/after 对比 (healed / still-degraded / 状态迁移表)。

用法: python3 reverify_drb2.py [--limit N]   # --limit 先跑前 N 个做 smoke
"""
import sys, os, json, time, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s5_pipeline import search_node, verify_node

RUNS = "runs-s5-sm-drb-2.json"
OUT = "runs-s5-sm-drb-2-reverified.json"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="只跑前 N 个 (0=全部)")
    args = ap.parse_args()

    d = json.load(open(RUNS))
    nodes = d["nodes"]
    qid = d.get("qid", "drb-2")
    targets = [n for n in nodes if n.get("status") == "degraded" and n.get("source") == "search"]
    if args.limit:
        targets = targets[:args.limit]
    print(f"[reverify] qid={qid} total_nodes={len(nodes)} degraded_search={len(targets)} (running {len(targets)})", flush=True)

    healed, still_deg, other = [], [], []
    t0 = time.time()
    for i, n in enumerate(targets, 1):
        nid = n["id"]
        # search_node 期望 node dict (含 id/claim/source); 传入副本避免污染原对象中途态
        nd = dict(n)
        try:
            res = search_node(nd, qid=qid)
            # search_node 返回 (srcs, err) 二元组
            if isinstance(res, tuple):
                srcs, serr = res[0], res[1]
            else:
                srcs, serr = res, None
            srcs = srcs or []
        except Exception as e:
            srcs, serr = [], str(e)
        n_src = len(srcs)
        tag = f" err={str(serr)[:60]}" if (serr and not srcs) else ""
        print(f"  [{i}/{len(targets)}] {nid}: srcs={n_src}{tag}", flush=True)
        try:
            vres = verify_node(nd, srcs)
            # verify_node 实际返回 4 元组 (status, evidence, corrected_claim, raw_out)
            status = vres[0] if len(vres) > 0 else "degraded"
            evidence = vres[1] if len(vres) > 1 else ""
            corrected = vres[2] if len(vres) > 2 else ""
        except Exception as e:
            status, evidence, corrected = "degraded", f"verify ERR: {str(e)[:120]}", n.get("corrected_claim") or n["claim"]
        # 回写
        n["status"] = status
        n["evidence"] = evidence
        if corrected:
            n["corrected_claim"] = corrected
        n["rework_count"] = n.get("rework_count", 0) + 1
        n["reverified_at"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        bucket = healed if status == "verified" else (still_deg if status == "degraded" else other)
        bucket.append(nid)
        elen = len(evidence or "")
        print(f"  [{i}/{len(targets)}] {nid}: srcs={n_src} -> {status} (evidence {elen}c)", flush=True)
        # 每 5 个落一次中间盘, 防中途死掉丢进度
        if i % 5 == 0:
            json.dump(d, open(OUT, "w"), ensure_ascii=False, indent=1)

    json.dump(d, open(OUT, "w"), ensure_ascii=False, indent=1)
    dt = time.time() - t0
    print("\n=== REVERIFY SUMMARY ===", flush=True)
    print(f"elapsed: {dt/60:.1f} min", flush=True)
    print(f"healed (verified): {len(healed)}/{len(targets)}", flush=True)
    print(f"still degraded:    {len(still_deg)}", flush=True)
    print(f"other status:      {len(other)}", flush=True)
    if still_deg:
        print(f"still-degraded ids: {still_deg}", flush=True)
    print(f"output: {OUT}", flush=True)

if __name__ == "__main__":
    main()