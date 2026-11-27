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

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "q9-budget-scan")
RUNS = sorted(glob.glob(os.path.join(DATA, "q9-*-r*.json")))
JUDGE = json.load(open(os.path.join(DATA, "llm-judge-coverage-20261127.json")))

# 21 个定义式签名: (jid, 概念正则, 实例化附加正则)
# instantiated = 概念命中 且 (同行/同节点出现 = 带右侧内容, 或具体数字)
SIG = [
    ("J1",  r"fit|显存(适配|占用|够|装)|内存(墙|占用)|W.{0,6}KV.{0,6}(A|R)", r"16\s*(GiB|GB)|≤\s*16|W\s*[+＋]\s*KV"),
    ("J2",  r"吞吐|throughput|tokens?/?sec|tok/s",                        r"\d+(\.\d+)?\s*(tok|token)s?/?s|tokens?/?sec\s*[=≈]|/秒"),
    ("J3",  r"可观测上限|观测上限|NCU|kernel.{0,6}(上限|计数器)|SM.{0,6}占用", r"max\s*\{|max\(.*\)|上限\s*[=≈]"),
    ("J4",  r"Q_target|目标.{0,4}(质量|能力)|发表级",                       r"Σ|/6|I\s*\("),
    ("J5",  r"G_cap|能力(缺口|差距)|Q_now",                                  r"max\s*\(\s*0|max\(0"),
    ("J6",  r"kWh|电耗|能耗|电费|P_avg",                                     r"kWh\s*[=≈]|P\s*[·×x]\s*t|kW\s*[·×x]"),
    ("J7",  r"折旧|残值|摊销|C_hw|硬件(成本|价格)",                          r"[−-]\s*残值|/可用|服务小时|摊销"),
    ("J8",  r"C_API|API.{0,4}(成本|费用)|token.{0,4}(单价|价格)",            r"T_in|p_in|输入.{0,4}(token|价格)|输出.{0,4}(token|价格)"),
    ("J9",  r"claim.{0,4}precision|主张.{0,4}(精度|准确)|判真",              r"precision\s*[=≈]|/已裁决|/裁决"),
    ("J10", r"unsupported|无证据|与证据冲突",                                 r"rate\s*[=≈]|/已审|冲突.{0,4}比"),
    ("J11", r"experiment.{0,4}pass|实验(通过|通过率)|验收测试",               r"pass\s*[=≈]|/有效测试|/有效"),
    ("J12", r"κ|kappa|一致性|双评审",                                         r"p_o|p_e|\(1\s*[−-]\s*p_e\)"),
    ("J13", r"source.{0,4}coverage|来源(覆盖|可追溯)|溯源",                   r"coverage\s*[=≈]|/全部|可追溯.{0,4}数"),
    ("J14", r"repeatability|可复现|复现.{0,4}(率|run)",                       r"复现.{0,4}run|Wilson|/n\b"),
    ("J15", r"T_serial|串行(时间|耗时)|阶段(计时|耗时)",                       r"t_decompose|Σ\s*\(|decompose.{0,10}research"),
    ("J16", r"makespan|DAG|关键路径|并行(时间|耗时)",                          r"max_{path}|max\(.*DAG|DAG.{0,10}Σ|关键路径"),
    ("J17", r"speedup|加速比|等待率|T_wall",                                  r"T_serial\s*/\s*T_wall|T_blocked|加速比\s*[=≈]"),
    ("J18", r"ΔQ|干预.{0,4}(对照|基线)|因果效应",                              r"Q\s*\(.{0,8}\)\s*[−-]|ΔQ\s*[=≈]"),
    ("J19", r"tool.{0,4}success|工具(成功率|调用)|调用.{0,4}成功",             r"success\s*[=≈]|/计划调用|/计划"),
    ("J20", r"gate.{0,4}pass|阶段(验收|门)|验收门",                            r"gate\s*pass|/计划门|门数"),
    ("J21", r"B\*|边际(收益|成本)|Pareto|预算(拐点|最优)",                     r"ΔQ\s*/\s*ΔB|min\s*B|0\.01\s*/\s*节点"),
]

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
