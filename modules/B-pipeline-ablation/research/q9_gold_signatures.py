#!/usr/bin/env python3
"""Q9 gold 共享签名表 (2026-11-27, T3b 逐级机械 judge 的地基)

来源: experiments/stage-ablation/gold/Q9-v2.md (37 节点/深度 5/21 叶 J1-J21)。
本模块是 gold 派生数据, 供 q9_formula_instantiation_probe.py 与
q9_hierarchical_judge.py 共同 import — 单一事实源, 不复制。

SIG: 21 个定义式签名 (jid, 概念正则, 实例化附加正则)。
  mention (L1)   = 概念正则在 run 文本中出现
  instantiated   = 同一行内 概念 且 实例化附加 同现 (公式右侧有具体内容)
DIM: 5 个顶层维度 → 叶 J 映射 (gold 树 N-1..N-5)。
TRACE: 输入溯源签名 (第三因子, v1 概念级近似: 行内含来源引用)。

局限 (v1): 正则=概念级近似, 不判公式算得对不对; TRACE 不含 R 编号
(噪声太高), 漏掉"据 R4"类引用 — 溯源因子偏严, 解释结果时注意。
"""
import re

# (jid, 概念正则, 实例化附加正则) — 与 gold Q9-v2.md 21 叶一一对应
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

# 5 顶层维度 → 叶 J (gold 树 N-1..N-5, 决策变量层 N-5 不参与加权, 此处仅分组)
DIM = {
    "N-1_capability": ["J1", "J2", "J3", "J4", "J5"],
    "N-2_cost":       ["J6", "J7", "J8"],
    "N-3_reliability": ["J9", "J10", "J11", "J12", "J13", "J14"],
    "N-4_time":       ["J15", "J16", "J17"],
    "N-5_levers":     ["J18", "J19", "J20", "J21"],
}

# 输入溯源 (第三因子): 实例化所在行含来源引用
TRACE = re.compile(r"https?://|arxiv\.org|github\.com|来源|引自|reference", re.I)

assert len(SIG) == 21, "gold Q9-v2.md 有 21 叶"
assert sum(len(v) for v in DIM.values()) == 21, "5 维度应覆盖全部 21 叶"
