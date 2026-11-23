# decomp: 主会论文骨架（ICML 2027, 9 页 + 附录, 截止 2027-01-14 abstract / 01-22 paper, 60 天）
# origin: ai · 2026-11-23
# 对象: metacog workshop 稿 (experiments/stage-ablation/workshop-draft-metacog-20261122.md) 的主会扩展版
# 注意: 这是 metacog 轨（27B research agent 两轴测量），不是 T-PUB-1 formula_judge 轨（机械验证器论文，在 projects/AI-计算科学/D1-generalization/）——两条轨各自成文
# 窗口修正 (2026-11-23): ICLR 2027 已过期 66 天, ICML 2027 (1/14 abstract 还有52天/1/22 paper 还有60天) 为主会目标
# 数据源: workshop 稿 experiments/stage-ablation/workshop-draft-metacog-20261122.md (10158 词, 8 节)
# 目标: 9 页 ICML 格式 ≈ 7000-8000 词正文 + 附录 (数据/代码/完整统计)

## 字数预算 (9 页 ≈ 7500 词正文)

| 节 | workshop 现状 | 主会目标 | 动作 |
|----|--------------|---------|------|
| Abstract | 1003 词 | 150-200 词 | **压缩 80%** — workshop 把 4 findings 全塞进 abstract, 主会只留 1 句 hook + 1 句方法 + 1 句核心 finding |
| 1. Introduction | 418 词 | 900-1000 词 | **扩 2×** — 加: ①research agent 评测现状 (端到端混淆 model/harness) ②为什么 compute constraint 是关键变量 ③contribution 列表 (3 条) ④与 RSI 验证器赛道 (TRUST 等) 的差异化定位 |
| 2. Setup & Method | 760 词 | 1500-1800 词 | **扩 2×** — 加: ①两轴测量框架的完整定义 (metacog 轴公式 + quality 轴 4 层 rubric) ②harness 架构 (状态机/预算/工具) ③3 域题集构造 (gold 树如何冻结) ④27B 部署细节 (4×V100, 无权重更新) |
| 3. Related work | 270 词 | 800-1000 词 | **扩 3×** — 从 condensed 展开: ①RSI 验证器 (TRUST/RuHarness/Phantom/Agent-as-a-Judge) ②metacognition in LLMs (knowing-what-you-don't-know 线) ③budget/compute scaling ④harness vs model 分离测量 (本文核心定位) |
| 4. Findings | 5207 词 | 3000-3500 词 | **压缩 40% + 重组** — 4 findings 各留核心数字, 细节移附录: ①monitoring/repair 分离 (gap rate + rework 1.6-2.1%) ②difficulty-calibrated gap marking (era-matched 3 域) ③budget curve (L4 0/21 + bare-arm 0/6 + verbosity bias 控制臂) ④checkpoint reuse 权衡 |
| 5. Implications | 354 词 | 500-600 词 | 扩 1.5× — 对 agent 设计的实操含义 (harness 价值=让断裂可测量, 不是防断裂) |
| 6. Limitations | 1217 词 | 400-500 词 | **压缩 60%** — 移附录, 正文只留 3 条最关键的 (same-model judge bias / n 规模 / era-scoping) |
| 7. Future work | 614 词 | 删 (并入 §5 或附录) | 主会 9 页通常无独立 future work 节 |
| 8. Data & code | 239 词 | 200 词 | 保留, 移附录或脚注 |
| **附录** | — | 3000-4000 词 | 新增: 完整统计表 / 逐 run 数据 / rubric 全文 / bare-arm 6 run 明细 / degeneration detector 算法 / 跨域 detector bias 清洗细节 |

## 缺口清单 (主会 vs workshop 差什么)

1. **Related work 深度不够** (270→1000 词): 需补 RSI 验证器赛道最新 (TRUST 2611.10787 在审 ICLR 2027, 同方向 3 篇 RSI 在审) + metacognition-in-LLM 线 (knowing-what-you-don't-know) 的系统调研 → 走 arena-outsource
2. **理论节缺失**: publication-strategy 原排期有"理论"节, 但 workshop 稿没有。主会 9 页可加 1 节 (500-800 词): 两轴框架的形式化定义 (metacog 轴 = 信息状态监控, 可形式化为节点字段上的确定性函数; quality 轴 = gold 条件覆盖, 可形式化为树编辑距离) — 这是"可发表"的差异化 (纯实证 vs 实证+形式化)
3. **图/表缺失**: workshop 稿纯文字, 主会需 3-5 个图 (budget curve 折线 / gap rate by domain 柱状 / rework yield 分布 / verbosity bias 散点) + 2-3 个表 (4 findings 汇总 / 3 域对比 / 控制臂结果)
4. **统计严谨性**: 主会需完整 CI + effect size + 多重比较校正 (workshop 只标 p 值) → 走 stats-protocol
5. **匿名化**: ICML 双盲, 需去作者名/机构/致谢 → 提交前 checklist

## 60 天排期 (2026-11-23 → 2027-01-22)

| 周 | 日期 | 任务 | 依赖 |
|----|------|------|------|
| W1 | 11/23-11/29 | ①B' 臂 n=10 完成 (后台跑) ②c3 双口径重判 ③related work arena 调研 | B' 批 |
| W2 | 11/30-12/06 | ①§1 Intro 扩写 ②§2 Setup 扩写 ③理论节初稿 | W1 |
| W3 | 12/07-12/13 | ①§3 Related work 扩写 (用 W1 arena 结果) ②§4 Findings 压缩重组 ③图 1-2 (budget curve + gap rate) | W2 |
| W4 | 12/14-12/20 | ①§4 剩余 findings ②§5 Implications ③图 3-4 (rework + verbosity) ④表 1-2 | W3 |
| W5 | 12/21-12/27 | ①附录 (完整统计 + 逐 run) ②统计严谨性 (CI + effect size + 多重比较) ③Limitations 压缩 | W4 |
| W6 | 12/28-01/03 | ①全文通读 + 字数控制 (≤8000 词正文) ②图 5 + 表 3 ③匿名化 checklist | W5 |
| W7 | 01/04-01/10 | ①内部 review (arena 交叉验证) ②修订 ③abstract 压缩到 200 词 | W6 |
| W8 | 01/11-01/14 | **ICML 2027 abstract 提交 (01/14 AoE)** | W7 |
| W9 | 01/15-01/22 | ①full paper 终稿 ②**ICML 2027 paper 提交 (01/22 AoE)** | W8 |

## 风险

- 60 天比原 12 周 (84 天) 紧 24 天 → W1 的 B' 臂 + related work 是关键路径, 必须 W1 内完成
- 理论节是新增工作量 (workshop 没有), 若 W2 卡住可降级为"方法的形式化描述" (不加独立理论节)
- 统计严谨性 (W5) 若发现多重比较后 p 值不显著 → 需改 claim 强度 (workshop 已标 "suggestive" 的 finding 主会需更谨慎措辞)
