# 分层规划（L0/L1/L2）— 活文档，动态调整

> origin: ai · 2026-11-22 · D 指令："完整规划你的目标，动态调整，搜集需要的信息，阶段性工作分层压缩"
> 本文件是唯一规划入口。每完成一个阶段 → 压缩成 L2 笔记（结论+证据+下一步），细节沉到子文件。
> 动态调整规则：发现子项偏离 L0 → 删；优先级变 → 重排；新正交子项 → 加。唯一不动的是 L0。

## L0 目标（不动）

**造一个至少有自我认识的 AGI**（D 硬件: 27b + 4×V100, 不改权重）
- AGI 定义: (a) 判断信息充分性 + (b) 获取缺失信息 + (c) 推理到答案
- "至少有自我认识" = (a)+(b) 可测量地被做出来
- 副产物（可发表）: 严格 judge + 预算-质量非单调 + 自我认识测量/改进 + 质疑协议本身

## L1 阶段（按服务链排序，当前在 ②）

| # | 阶段 | 状态 | 压缩笔记（L2 指针） |
|---|---|---|---|
| ① | 测量层：judge + metacog 轴 | ✅ 基本完成 | L2-1 |
| ② | 改进层：断点定位 + 干预 + 重测 | 🔄 断点已定位, 干预 2 待跑 | L2-2 |
| ③ | 题目层：AGI 题面 + gold | 🔄 题面 v0 落盘, 等 D 确认 | L2-3 |
| ④ | 实验层：Idea 2 + 补重复 | 🔄 Idea 2 在跑, 补重复排队 | L2-4 |
| ⑤ | 发表层：workshop 稿 | ⏸ 等 ②④ 数据 | L2-5 |

## L2 压缩笔记（每阶段一段：结论 / 证据 / 下一步）

### L2-1 测量层（2026-11-22 收口）
- **结论**: 三层机械 judge v1.0 冻结（0.5*depth+0.5*cov, COS=0.70）；metacog 轴 v1.1 建成（gap/retrieval/healthy_gap/post_acc）。
- **证据**: judge-v1-cov-calibration.md（15 runs 标定）；metacog-budget-scan-v1.1.json（83 runs）；跨题质询通过（hg 0.90-0.98 三题一致, 排除"gpu 题特殊"替代解释）。
- **新发现（已验证, era-matched）**: gap_rate 随题难度单调升，**限定 sm-* era（同 budget=150 默认）**: nat 0.0281(n=21) < soc 0.0576(n=26) < gpu 0.1469(n=18)，三对 Mann-Whitney 全 p<0.001，KW H=39.2 p<0.0001。= 功能性 monitoring 特征。
- **质询修正（重要）**: 最初 83-run 聚合把 sm-* era（Nov20-21, budget=150）和 budget-* scan（Nov22, 50-719）两个 population 混了，gpu 被稀释到 0.102。era-matched 后 gpu=0.147 梯度更强。budget scan 内部 gap_rate 非单调（50→0.079, 100→0.209, 150→0.147, 300→0.082, 719→0.089）= budget 效应独立于难度，**两 population 不可混算**。
- **混淆边界（诚实标注）**: ① soc 题内 gap_rate 与 n_nodes 正相关（rho=0.488, p=0.010）→ soc 难度效应部分可能是预算效应；② 难度梯度只在 budget=150 单点验证，跨 budget 的梯度需补重复时按 budget 分层重验。claim 限定为"同预算下跨题难度梯度成立"。
- **下一步**: 权重 0.4/0.3/0.3 待补重复后消融；mech 层符号对齐（独立工作项）；难度梯度在补重复时按 budget 分层重验（排除 soc 混淆）。

### L2-2 改进层（进行中）
- **结论**: 断点 = 修复环（rework 46 次 fix rate 0/46, 全烧在 unverifiable 上）。27b monitoring 健康（hg 0.938），缺的是 targeted control。
- **证据**: metacog-loop-design-20261122.md（evidence 正则分类 + rework_count 分布）。
- **下一步**: 干预 2（rework 只对 contradicted 触发）→ 前后各 ≥3 runs → Welch t 检验（ε≈0.1 统计门禁）。

### L2-3 题目层（等 D）
- **结论**: AGI 题面 v0 落盘（q9-agi-question-v0.md），gold 骨架未建。
- **阻塞**: 题面措辞需 D 一句话确认；gold 骨架 arena 外包优先。
- **下一步**: D 确认后 → gold 调研（arena）→ rubric 判定点。

### L2-4 实验层（在跑）
- **结论**: Idea 2（checkpoint-as-cache）A/B 各 3 reps 在跑（22:13 起, ~3h）；补重复（5 budget × 8-12 reps）排队。
- **证据**: idea2_runner.sh（ac6090870）；idea2-run.log。
- **下一步**: Idea 2 完 → 配对统计（judge v1.0 + metacog 轴双评）→ 补重复开跑。

### L2-5 发表层（v0.1 稿已落盘）
- **结论**: workshop 稿 v0.1 写完（workshop-draft-metacog-20261122.md, edacf05b7）。三发现: ①监控在/修复缺（rework 0/46, 断点=修复环）②gap 难度校准（era-matched nat<soc<gpu 全 p<0.001）③预算-质量非单调（150=peak, sd<spread）。限制节前置（单模型/self-judge/n=3/mech 诊断）。
- **证据**: 全数字来自本地已验证 artifact（k7-pareto-15run / metacog-budget-scan-v1.1 / judge-v1-cov-calibration / plan-layered era-matched 重算）。
- **下一步**: Idea 2 + 补重复数据齐后填 §4.3 的 n 和 peak 位置；repair-loop fix 跑完补 §5.1 的实测；heterogeneous re-judge（无 API key, 已知 gap）。

## 质询协议（D 不在时, 质疑替代 D）

**每个阶段性结论出数前, 强制过三问**（落盘到对应 L2 笔记）：
1. **最强替代解释是什么？**（数据错? 方法错? 前提错? 题特殊?）→ 设计一个能排除它的检验, 跑了才算数
2. **独立来源能交叉验证吗？**（≥2 源: 本地数据重算 / 文献 / arena）
3. **这个数字换个口径还成立吗?**（judge 版本 / 聚合方式 / 样本子集）

已执行实例:
- hg_rate 0.938 → 替代解释"gpu 题 claim 本来就查不到" → 跨题检验（nat/soc 也 0.94+）→ 排除 ✅
- K7 150=peak → 替代解释"run 噪声" → sd(0.0445) < tier spread(0.0901) → 排除 ✅
- 撞车调研"未撞车" → 替代解释"关键词太窄" → 换 4 轮关键词 + 全文 0 hits 确认 → 边界=conf 0.7 ✅
