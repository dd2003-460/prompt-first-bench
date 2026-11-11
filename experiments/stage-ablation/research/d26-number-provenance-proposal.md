# Decision 26: 数字溯源检查（number-provenance check）

> origin: ai (Lead) · 状态: **proposal，未落代码** · 2026-11-12
> 触发源: r14-tree-quality-audit.md §3/§5（靶点 #2 升级）；CC C9 确认通道型 degraded 是另一类问题，本条针对"模型型"幻觉。

## 背景（为什么需要）

r14 审计发现 verify 阶段只查"有没有证据"，不查"数字是否可溯源"——Goodhart 的真正猎物：

| 节点 | 内容 | 问题 |
|---|---|---|
| N143 | "每 6-12 个月 XID 错误概率约 1-2%"、"数据中心卡年故障率 <0.1%" | 无公开来源，纯权重残留 |
| N142 | ROCm "吞吐低 20-30%"、"Triton 重编译 4-8 小时" | 方向可能对，精度编的 |
| N140 | W4 量化 "ΔMMLU<1.5%, PPL<0.2" | 真实值依赖方法+模型，无通用常数 |
| N141 | FP8 "HumanEval/GSM8K 衰减<0.5%" | 同上 |
| N57 | "ΔPPL_W4<0.5 bits/token 且 MMLU 下降≤2% 方可接受" | 阈值拍的，表述得像标准 |

这些节点状态是 degraded（verify 没通过），但仍在树中、仍会被 assemble_report 带进报告正文——DRB judge 的 instruction_following / comprehensiveness 维度会吃到不可溯源的数字。

## 规则（≤3 句，meta-rule，进 verify prompt）

1. claim 含硬数字（统计量/阈值/百分比/速率/时长）时，每个数字必须能在 evidence 的具体出处中找到对应值或可推导的计算链。
2. 找不到的数字：claim 降级为 [待核验] 标注版本，原始数字不进报告正文。
3. 判断"是否有出处"用 structural test（evidence 文本里出现该数字或其明确来源），不用经验比例。

general 自检：不写死任何域特定先验（不写 GPU/XID/MMLU 等词），对任何领域的事实断言同样适用。✅

## 三问（modification-rationale 格式）

**Q1 · general 吗？** 是。任何领域的事实断言都适用；r14 证据全在 GPU 域，但机制（精确数字 + 无出处 = 权重残留）与域无关。

**Q2 · 正交吗（对照 M1-M10）？** 是。contribution filter 管"节点是否推进目标函数"——结构层；本条管"数字是否有出处"——内容层。一个节点可以 contribution 高但数字全是编的（N143 正是这种：推理链完整、结论有用、但统计值是幻觉）。两者独立触发、独立拦截。

**Q3 · Levin 方向？已有实验支撑？** 是。用更短的程序（溯源绑定检查）捕获更多错误行为（编造精确值）。已有实验 = r14 审计逐条列出的 5 个幻觉节点（runs-s5-sm-gpu.json，commit d230a64d 产物）。

## 实施设计（待 drb-1 出分后启动）

- **位置**: s5_state_machine.py verify 阶段，_verify_batch 内，现有 judge 调用之后加一步轻量检查（本地 LLM 单次调用，输入 = claim + evidence，输出 = 数字清单 × 出处命中 bool）。
- **成本**: 每节点 +1 次 LLM 调用（仅含硬数字的 claim 触发，预计 ~30% 节点）；一轮 run 增加 ~5-10min。
- **退出条件**: DRB bench 若显示不可溯源数字并未拖分（judge 不吃这套），则降级为监控项不强制拦截——避免过度工程。
- **验收**: r15（或 drb-1 修复版 run）中，报告正文出现"无出处的硬数字"次数 = 0（assemble_report 侧 grep [待核验] 外泄验证）。

## 与 Decision 25 的关系

Decision 25（URL-pattern junk-detector）已按 CC C9 证据改判 deferred——它修的失败模式（DDG/Bing junk）不是主因（主因 = cn.bing 跨域噪声，unusable 52%）。D26 修的是另一条独立链路（模型生成侧幻觉，非检索侧）。两者不冲突：检索修好后 D26 仍是最后一道闸。