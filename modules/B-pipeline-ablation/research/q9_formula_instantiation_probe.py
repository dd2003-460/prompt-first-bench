#!/usr/bin/env python3
"""Q9 公式实例化探针 (2026-11-27 21:41, D 提议"逐级概念-公式标志"的最便宜探针)

问题: judge 伪影 claim 在 §11 被降级为定性假设。本探针给决定性重测:
gold Q9-v2.md 有 21 个定义式 (关系锚), 逐式判 run 里
  - mention (L1): 概念出现
  - instantiated (L2): 概念 + "=" 右侧有具体表达式/数字 (公式被实例化)
预算轴上: 实例化率随预算升 = 预算真买能力; 平 = judge 伪影成立。

与 L1/L2 审计同构 (话题 vs 推导), 但锚在 gold 的 21 个定义式上,
不是自由关键词 — 这是"关系锚"判法的第一个机械实现。

局限: 正则签名是概念级近似, 不判公式对不对 (那是逐级 judge 的活,
本探针只判"实例化没"); S-c 类 (J4/J5/J12/J18/J21 开放阈值) 的
instantiated 判据放宽为"给出符号式/区间"也算。
"""
import json, glob, re, os, statistics
from q9_gold_signatures import SIG  # 单一事实源 (T3b 共享模块)

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "q9-budget-scan")
RUNS = sorted(glob.glob(os.path.join(DATA, "q9-*-r*.json")))
JUDGE = json.load(open(os.path.join(DATA, "llm-judge-coverage-20261127.json")))

def probe_run(f):
    r = json.load(open(f))
    name = os.path.basename(f)
    bud = int(name.split("-")[1].split("r")[0])
    nodes = r.get("nodes", [])
    text = "\n".join((n.get("claim") or "") for n in nodes)
    per_j = {}
    for jid, cp, ip in SIG:
        c = re.compile(cp, re.I)
        i = re.compile(ip, re.I)
        ment = len(c.findall(text))
        inst = 0
        for line in text.split("\n"):
            if c.search(line) and i.search(line):
                inst += 1
        per_j[jid] = dict(mention=ment > 0, instantiated=inst > 0, n_inst=inst)
    return dict(file=name, bud=bud, n=len(nodes), per_j=per_j,
                n_ment=sum(1 for v in per_j.values() if v["mention"]),
                n_inst=sum(1 for v in per_j.values() if v["instantiated"]))

rows = [probe_run(f) for f in RUNS]
for row in rows:
    m = re.match(r"q9-(\d+)-r(\d)", row["file"])
    det = JUDGE["detail"].get(m.group(1), {}).get(f"r{m.group(2)}")
    row["judge"] = det["n_gates_hit"] if det else None

print(f"{'run':36} {'bud':>4} {'n':>4} {'judge':>5} {'mention':>8} {'inst':>5}")
for row in rows:
    print(f"{row['file']:36} {row['bud']:>4} {row['n']:>4} "
          f"{row['judge'] if row['judge'] is not None else '-':>5} "
          f"{row['n_ment']:>7}/21 {row['n_inst']:>4}/21")

# 预算轴
print("\n预算轴 (21 式中 mention / instantiated 均值):")
axis = {}
for r in rows:
    axis.setdefault(r["bud"], []).append(r)
for b in sorted(axis):
    g = axis[b]
    mm = statistics.mean([x["n_ment"] for x in g])
    ii = statistics.mean([x["n_inst"] for x in g])
    jm = statistics.mean([x["judge"] for x in g if x["judge"] is not None])
    print(f"  bud {b:>4}: judge={jm:.2f}  mention={mm:.1f}/21  instantiated={ii:.1f}/21")

# 逐式: 哪些公式几乎无人实例化
print("\n逐式实例化 (10 run 合计):")
tot = {jid: [0, 0] for jid, _, _ in SIG}
for row in rows:
    for jid, v in row["per_j"].items():
        tot[jid][0] += v["mention"]
        tot[jid][1] += v["instantiated"]
for jid, _, _ in SIG:
    m, i = tot[jid]
    bar = "#" * i + "." * (10 - i)
    print(f"  {jid:<4} mention {m:>2}/10  inst {i:>2}/10  {bar}")

out = dict(per_run=rows, per_jid_total={k: v for k, v in tot.items()})
dst = os.path.join(DATA, "formula-instantiation-probe-20261127.json")
json.dump(out, open(dst, "w"), ensure_ascii=False, indent=2)
print(f"\n落盘 {os.path.relpath(dst, DATA)}")
