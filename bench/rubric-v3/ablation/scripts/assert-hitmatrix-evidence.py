#!/usr/bin/env python3
"""assert-hitmatrix-evidence.py — 冻结 hit-matrix.json evidence verbatim 合规审计（RV3G6-o3-claim-rejudge-evidence-audit）

对 ablation/hit-matrix.json 全部 cell 的 evidence 字段做**形式合规**机判（不判命中语义——
evidence 是否支持对应 claim/node 的命中，属 judge 职责，本脚本零 h 值判定）：

判定语义预注册（与 loop-artifacts/stages/01/RV3G6o3ea-goal-decomposition.md §2 表 byte-stable）：
  C1 非空        h=1 cell evidence 为 null/空串            → FAIL
                 依据 TASK-ablation Step 1「每个 h=1 必须附 evidence」硬约束
  C2 verbatim    evidence ∉ 所属 run 文件全文连续子串       → FAIL
                 依据「必须是 run 文件里真实存在的句子（不许改写）」；原始文本直接比对
                 （F1 实证 8 个 run 文件全 LF-only，无归一化需求；若未来出现 CRLF 变体走
                 current-goal 失败降级条款 1 双轨输出，不在本版本静默放宽）
  C3 长度惯例    len(evidence) > 40 字符                    → SIGNAL（不 FAIL）
                 「≤40字」是 TASK-ablation 输出格式示例中的填写惯例，非验收门禁
  C4 张冠李戴    evidence ∉ 所属 run 但 ∈ 其他某 run        → FAIL（C2 子类，单独报出定位）
                 **触发条件锁定**：仅当 C2 已 FAIL 时检查。不做全局唯一性检查——
                 11 组跨 run 重复字符串（如「3090=350W」各 run 独立写出）是合法现象，
                 C2 PASS 的 cell 即使字符串跨 run 重复也不报（见 02.5 X2）。
  C5 h=0 带值    h=0 cell evidence 非 null                  → SIGNAL（冗余暴露，非违规）

exit code：0 = 无 FAIL（含 SIGNAL）/ 1 = 存在 FAIL。stdout `[SIGNAL]` 前缀义务继承全局约定。
结构损坏（hit-matrix.json 不可解析 / cell 缺字段）→ fail-loud SystemExit（无 exit 2 分支——
本脚本消费的是仓库内冻结数据而非外部投递 schema）。

附加产出（A4）：§3.2 口径声明 4「98 个 h=1 cell 中 27 个 evidence 含 gold-tree 数值 token」
独立复算——只报 V1 口径（gold_numbers_per_node per-line − _noise_exempt，与
assert-o3-claim-list.py 同函数逻辑同源引用，防第三个口径引入双源漂移），并与声明值 27
对照注记 mismatch（02 F3：V1=13 / V2=34 / V3=35 均 ≠ 27，数字失实登记见 04 日志）。

路径解析用 Path(__file__).resolve().parents[4]（任意 cwd 可跑；不继承既有三脚本的
repo-root-only 相对路径限制）。
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / "bench" / "rubric-v3"
HIT_MATRIX = BASE / "ablation" / "hit-matrix.json"
GOLD_TREE = BASE / "ablation" / "gold-tree.md"
RUN_DIR = BASE / "ablation"


def load_run_texts():
    """8 个 run 文件原始文本（LF-only 已实证，不做任何归一化）。"""
    out = {}
    for p in sorted(RUN_DIR.glob("runs-C0-run*.md")):
        out[p.stem.replace("runs-C0-", "")] = p.read_text(encoding="utf-8")
    assert len(out) == 8, f"run 文件数异常：{sorted(out)}"
    return out


def gold_numbers_per_node():
    """gold-tree.md 每节点行的数值 token —— 与 assert-o3-claim-list.py 同名函数同逻辑（V1 口径）。"""
    tree = GOLD_TREE.read_text(encoding="utf-8")
    out = {}
    for line in tree.splitlines():
        ids_in_line = re.findall(r"\bN-\d+(?:\.\d+)*\b", line)
        if not ids_in_line:
            continue
        toks = set(re.findall(r"\d+(?:\.\d+)?", line))
        for nid in ids_in_line:
            out.setdefault(nid, set()).update(toks)
    return out


def noise_exempt(node_id_set):
    """噪声豁免集 —— 与 assert-o3-claim-list.py::_noise_exempt 同逻辑（ID 分段 + 一级前缀 + {0,1,31,4,13}）。"""
    ex = {"0", "1"}
    for nid in node_id_set:
        parts = nid[2:].split(".")
        ex |= set(parts)
        ex.add(".".join(parts[:2]))
    ex |= {"31", "4", "13"}
    return ex


def main():
    hm = json.loads(HIT_MATRIX.read_text(encoding="utf-8"))
    runs = sorted(hm.keys())
    texts = load_run_texts()
    bad_runs = [r for r in runs if r not in texts]
    if bad_runs:
        print(f"[FAIL] hit-matrix 含未知 run：{bad_runs}")
        return 1

    fails, signals = [], []
    n_h1 = n_h0 = 0
    audit_rows = []

    for run in runs:
        for node in sorted(hm[run].keys()):
            cell = hm[run][node]
            if not isinstance(cell, dict) or "h" not in cell:
                print(f"[FAIL] {run}/{node}: cell 结构损坏（非 dict 或缺 h 字段）")
                return 1
            h = cell["h"]
            ev = cell.get("evidence")
            if h == 1:
                n_h1 += 1
                # C1 非空
                if ev is None or (isinstance(ev, str) and ev.strip() == ""):
                    fails.append(f"C1 {run}/{node}: h=1 但 evidence 为空")
                    audit_rows.append((run, node, "FAIL", "C1 空 evidence"))
                    continue
                if not isinstance(ev, str):
                    fails.append(f"C1 {run}/{node}: evidence 非字符串类型 {type(ev).__name__}")
                    audit_rows.append((run, node, "FAIL", "C1 类型异常"))
                    continue
                # C2 verbatim 连续子串
                if ev in texts[run]:
                    audit_rows.append((run, node, "PASS", f"len={len(ev)}"))
                else:
                    # C4 张冠李戴诊断（仅 C2 FAIL 时触发）
                    others = [r for r in runs if r != run and ev in texts[r]]
                    if others:
                        fails.append(f"C4 {run}/{node}: evidence 出自其他 run {others}（张冠李戴）")
                        audit_rows.append((run, node, "FAIL", f"C4 张冠李戴 → {others}"))
                    else:
                        fails.append(f"C2 {run}/{node}: evidence 非所属 run 连续子串（改写/拼接/编造）")
                        audit_rows.append((run, node, "FAIL", "C2 非子串"))
                # C3 长度惯例（独立于 C2 结果，超长且合法也报 SIGNAL）
                if len(ev) > 40:
                    signals.append(f"C3 {run}/{node}: evidence 长 {len(ev)} > 40 字（惯例超界，非门禁）")
            elif h == 0:
                n_h0 += 1
                if ev is not None:
                    signals.append(f"C5 {run}/{node}: h=0 cell 带 evidence（冗余，非违规）")
            else:
                fails.append(f"C? {run}/{node}: h 值非法 {h!r}（应为 0/1）")
                audit_rows.append((run, node, "FAIL", "h 值非法"))

    # 逐格审计表（98 行 h=1）
    print(f"# hit-matrix evidence verbatim 审计 · h=1 {n_h1} cell / h=0 {n_h0} cell")
    for run, node, verdict, note in audit_rows:
        print(f"  [{verdict}] {run}/{node}  {note}")

    # A4：§3.2 声明 4 复算（V1 口径）
    gold_nums = gold_numbers_per_node()
    blacklist = set().union(*gold_nums.values()) - noise_exempt(set(gold_nums.keys()))
    v1_hits = 0
    for run in runs:
        for node in sorted(hm[run].keys()):
            cell = hm[run][node]
            if cell.get("h") == 1 and isinstance(cell.get("evidence"), str):
                toks = set(re.findall(r"\d+(?:\.\d+)?", cell["evidence"]))
                if toks & blacklist:
                    v1_hits += 1
    declared = 27
    print(f"# §3.2 声明 4 复算（V1 口径 = assert-o3-claim-list.py 同源 per-line − 噪声豁免）")
    print(f"  V1 计数 = {v1_hits}/98 vs o3-claim-list §3.2 声明值 = {declared}"
          + ("（一致）" if v1_hits == declared else "（MISMATCH——02 F3：三口径 V1=13/V2=34/V3=35 均≠27，数字失实，勘误候选已导出）"))

    for s in signals:
        print(f"[SIGNAL] {s}")
    for f in fails:
        print(f"[FAIL] {f}")

    ok = not fails
    print(f"VERDICT: {'PASS' if ok else 'FAIL'}（FAIL {len(fails)} / SIGNAL {len(signals)} / 审计 {n_h1} h=1 cell）")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())