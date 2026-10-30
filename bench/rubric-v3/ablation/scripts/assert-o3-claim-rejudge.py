#!/usr/bin/env python3
"""assert-o3-claim-rejudge.py — O3 claim 级独立重判结果消费断言（RV3G6-o3-claim-rejudge-scaffold, r141）

消费 rejudge/rejudge-results.json（judge 批次产出，schema 见 rejudge/judge-protocol-batch1.md §3），
复算 o3-claim-list.md §3.1 M1/M2 实际读数（与 1.0 identity 锚点的偏离量，逐格报告）。

三分支主流程（exit code 约定 byte-stable，同 assert-goldrank-crossdomain.py 先例）：
  ① rejudge-results.json 缺失      → [SIGNAL] blocked-on-external + exit 0
     （中性状态：judge 通道未执行 ≠ 门禁失败；区别于 assert-kappa-receipt.py 的 FAIL 语义——
       receipt 是「评分有效性声明」缺失=负向事实，rejudge 结果是「待生产数据」缺失=条件未触发。
       stdout [SIGNAL] 前缀分流义务继承 batch2-closure queue 项全局约定。）
  ② schema 违例                    → [ERROR] fail-loud + exit 2
     （cells 覆盖不全 / h_claim 非二值 / evidence 非 run 原文连续子串 / h=0 带 evidence /
       固定字段漂移——任一即不可信结果，拒绝计算）
  ③ 数据齐备                       → M1/M2 复算 + flip 偏离表 + exit 0/1
     **verdict 语义预注册**：M1/M2 偏离本身不是 FAIL 条件——FM-2 检验目标就是找 flip，
     偏离是预期产出。FAIL（exit 1）仅限「结果不可信」类错误在 ② 漏网时的兜底
     （当前实现中 ② 已封闭全部可信性检查，故 ③ 常态 exit 0；保留 exit 1 通道防未来扩展）。

M1/M2 口径（照抄 o3-claim-list §3.1 定义式，不发明新口径）：
  M1 全量        = |{(r,v): h_claim(r,v)==h_id(r,v)}| / 248
  M1 gold strict = 同上，限 v ∈ {N-2.1, N-3.2.2, N-2, N-4, N-1.3}（40 cell）
  M2             = |{r: ∀v, h_claim(r,v)==h_id(r,v)}| / 8
  偏离报告 = flip 清单（(run, node, h_id→h_claim)）按 (node, 方向) 切片计数；
  方向记法：0→1 = FM-2 假漏判证据（旧判据漏掉的真命中）；1→0 = FM-1 假命中证据。

κ 边界（U-K1 UNRESOLVED）：本脚本不计算 κ（公式未在冻结件文字化，o3-claim-list §4.3 只给顺序关系）；
kappa_receipt_ref 字段存在性可查、数值不复核。聚合规则（§4.2 ≥2/3）属多判者阶段，
本脚本消费单判者原始结果，不做聚合。

用法：python3 assert-o3-claim-rejudge.py
  路径固定（相对仓库根）：bench/rubric-v3/ablation/{rejudge/rejudge-results.json,
  rejudge/sample-plan.json, hit-matrix.json, runs-C0-run*.md}
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ABL = ROOT / "bench" / "rubric-v3" / "ablation"
RESULTS = ABL / "rejudge" / "rejudge-results.json"
SAMPLE_PLAN = ABL / "rejudge" / "sample-plan.json"
HIT_MATRIX = ABL / "hit-matrix.json"
RUN_DIR = ABL

SCHEMA_VERSION = "rejudge-results/v1"
PROTOCOL_REF = "rejudge/judge-protocol-batch1.md"
GOLD_STRICT = ["N-2.1", "N-3.2.2", "N-2", "N-4", "N-1.3"]


def load_sample_plan():
    if not SAMPLE_PLAN.is_file():
        print(f"[ERROR] sample-plan.json missing: {SAMPLE_PLAN}")
        sys.exit(2)
    plan = json.load(open(SAMPLE_PLAN))
    cells = {(c["run"], c["node"]) for c in plan["cells"]}
    if len(cells) != len(plan["cells"]) or len(cells) != 248:
        print(f"[ERROR] sample-plan cell set inconsistent (unique={len(cells)}, rows={len(plan['cells'])})")
        sys.exit(2)
    return plan, cells


def load_results():
    if not RESULTS.is_file():
        print("[SIGNAL] blocked-on-external: rejudge-results.json absent "
              "(等 fresh-context judge 通道执行 rejudge/judge-protocol-batch1.md 后零改动接入)")
        sys.exit(0)
    try:
        data = json.load(open(RESULTS))
    except Exception as e:
        print(f"[ERROR] rejudge-results.json unreadable: {e}")
        sys.exit(2)
    return data


def check_schema(data, plan_cells):
    """② schema 硬约束（judge-protocol-batch1.md §3 五条，违例即 exit 2）。"""
    errs = []
    if data.get("schema_version") != SCHEMA_VERSION:
        errs.append(f"schema_version drift: {data.get('schema_version')!r} != {SCHEMA_VERSION!r}")
    if data.get("blind_protocol_ref") != PROTOCOL_REF:
        errs.append(f"blind_protocol_ref drift: {data.get('blind_protocol_ref')!r}")
    if not data.get("judge_id"):
        errs.append("judge_id empty")
    cells = data.get("cells")
    if not isinstance(cells, list):
        errs.append("cells not a list")
        cells = []
    seen = {}
    run_texts = {}
    for i, c in enumerate(cells):
        key = f"cells[{i}]"
        r, n = c.get("run"), c.get("node")
        if (r, n) not in plan_cells:
            errs.append(f"{key}: unknown cell ({r!r}, {n!r})")
            continue
        if (r, n) in seen:
            errs.append(f"{key}: duplicate cell ({r}, {n})")
        seen[(r, n)] = True
        h = c.get("h_claim")
        if h not in (0, 1):
            errs.append(f"{key}: h_claim not binary: {h!r}")
            continue
        ev = c.get("evidence", "MISSING_KEY")
        if h == 1:
            if not isinstance(ev, str) or not ev.strip():
                errs.append(f"{key}: h_claim=1 requires non-empty evidence string")
                continue
            if r not in run_texts:
                run_path = RUN_DIR / f"runs-C0-{r}.md"
                if not run_path.is_file():
                    errs.append(f"{key}: run file missing {run_path.name}")
                    continue
                run_texts[r] = run_path.read_text()
            if ev not in run_texts[r]:
                errs.append(f"{key}: evidence is NOT a contiguous substring of runs-C0-{r}.md "
                            f"(first 40 chars: {ev[:40]!r})")
        else:
            if ev is not None:
                errs.append(f"{key}: h_claim=0 must have evidence=null (got {type(ev).__name__})")
    missing = plan_cells - set(seen)
    if missing:
        errs.append(f"coverage gap: {len(missing)} cells missing, e.g. {sorted(missing)[:5]}")
    return errs


def main():
    plan, plan_cells = load_sample_plan()
    data = load_results()
    errs = check_schema(data, plan_cells)
    if errs:
        for e in errs:
            print(f"[ERROR] {e}")
        print(f"\nRESULT: ERROR ({len(errs)} schema violations) — exit 2")
        sys.exit(2)

    hm = json.load(open(HIT_MATRIX))
    runs = sorted(hm.keys())
    nodes = sorted(hm[runs[0]].keys())

    flips = []          # (run, node, h_id, h_claim)
    agree_full = agree_gold = 0
    per_run_all_agree = {r: True for r in runs}
    for c in data["cells"]:
        r, n, hc = c["run"], c["node"], c["h_claim"]
        hid = hm[r][n]["h"]
        if hc == hid:
            agree_full += 1
            if n in GOLD_STRICT:
                agree_gold += 1
        else:
            flips.append((r, n, hid, hc))
            per_run_all_agree[r] = False

    m1_full = agree_full / 248
    m1_gold = agree_gold / 40
    m2 = sum(per_run_all_agree.values()) / 8
    print(f"[PASS] schema OK (248 cells, judge={data['judge_id']!r}, family={data.get('judge_family')!r})")
    print(f"M1 full         = {agree_full}/248 = {m1_full:.4f}  (identity anchor 1.0000, deviation {1 - m1_full:+.4f})")
    print(f"M1 gold strict  = {agree_gold}/40  = {m1_gold:.4f}  (deviation {1 - m1_gold:+.4f})")
    print(f"M2 run-level    = {sum(per_run_all_agree.values())}/8   = {m2:.4f}  (deviation {1 - m2:+.4f})")
    if not flips:
        print("[info] zero flips — h_claim ≡ h_id（与 identity 基线重合，无新信息；仍如实报出）")
    else:
        by_node_dir = {}
        for r, n, hid, hc in flips:
            by_node_dir.setdefault((n, f"{hid}->{hc}"), []).append(r)
        print(f"flip detail ({len(flips)} cells, by (node, direction); 0->1 = FM-2 假漏判证据, 1->0 = FM-1 假命中证据):")
        for (n, d), rs in sorted(by_node_dir.items()):
            tag = "gold-strict" if n in GOLD_STRICT else ""
            print(f"  {n} {d}: {len(rs)} {rs}" + (f" [{tag}]" if tag else ""))
    kr = data.get("kappa_receipt_ref")
    if kr:
        kp = ROOT / kr
        print(f"[{'PASS' if kp.is_file() else 'SIGNAL'}] kappa_receipt_ref={kr} exists={'yes' if kp.is_file() else 'no'} "
              f"(数值不复核 — U-K1 κ 公式 UNRESOLVED)")
    else:
        print("[info] kappa_receipt_ref=null (单判者批次，κ 门禁适用点多判者阶段 — o3-claim-list §4.3)")
    print("\nNOTE: 本批读数为「相对 Lead-gold」度量（o3-claim-list §5.1 S2 限定语叠加生效）；"
          "M1/M2 偏离是预期产出（FM-2/FM-1 检验目标），非 FAIL 条件。")
    print("RESULT: PASS (data complete, metrics recomputed)")
    sys.exit(0)


if __name__ == "__main__":
    main()