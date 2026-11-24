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
- **结论**: 断点 = 修复环。修正数字: rework 修复率 1.6-2.1%（36/2298 budget-scan, 61/2919 era-matched，runs-s5-sm-*.json 源），非 0/46（旧口径只数了 rework_count>0 的节点子集）。degraded 口径 = search-source: 84% unverifiable / 6% contradicted / 10% ambiguous（hg_rate 0.938 同口径）。
- **失败模式解剖（18 runs, 5812 节点）**: ① 验证率跨层平坦（L2-L4 43-49%），深度不是验证悬崖——深度掉的是 coverage 不是 ver%；② L2-L4 无链断（18/18 runs 每层都有 verified）；③ loop 连续但不累积 = **filter 不是 repair cycle**（树绕开 55% 未验证节点生长）。L1 pending 92% 是 by design（source=given, s5_state_machine.py:494）。
- **下一步**: 干预 2（rework 只对 contradicted 触发）→ 前后各 ≥3 runs → Welch t。可证伪分支点: 省出的预算若没转成 depth，瓶颈在 expansion 不在 repair。

### L2-3 题目层（等 D）
- **结论**: AGI 题面 v0 落盘（q9-agi-question-v0.md），gold 骨架未建。
- **阻塞**: 题面措辞需 D 一句话确认；gold 骨架 arena 外包优先。
- **下一步**: D 确认后 → gold 调研（arena）→ rubric 判定点。

### L2-4 实验层（配对统计完成 11-24）
- **结论**: Idea 2（checkpoint-as-cache）A/B 各 3 reps 跑完（22:13 起）。**口径**: ~~B 臂新预算仅 28 节点~~（勘误: 本批跑于硬钳制 47a8543cd 之前, max_nodes 未硬顶, 见下）；B 臂正确解读 = wall time 节省 + 前缀一致性，质量只作旁证。
- **A-r1 已评**（idea2-scores.json）: wall 2865s, 316 节点, judge 0.5111（depth 0.8 / cov 0.222, 在 K7 budget-150 区间 0.43-0.52 内）, metacog 0.2365（hg 0.930, post 0.400）。
- **证据**: idea2_runner.sh（ac6090870）；idea2-run.log；idea2-scores.json。
- **✅ A/B 配对统计完成 (11-24, 684816ab0, idea2-ab-paired-20261124.md)**: ① wall time B 省 17.4% 但 n=3 不显著 (t=1.121, r1 反慢) + 两臂规模/时序混杂 → 本批不足以支持可靠 wall time 收益；② 前缀一致性: 内容核心 (claim/层级/父子/source) 122/122 逐字一致 ×3 run, 缓存语义内容层成立, evidence/edge_type/status 三 LLM 重生成字段漂移 (标注重算非内容漂移)；③ **预算口径勘误**: 本批跑于硬钳制修复 47a8543cd (11-23 13:44) 之前, "--max-nodes 150/B 臂仅 28 新节点"假设不成立 (realized A 316-435 / B 401-411) → 干净预算轴上重测 wall time 需 47a8543cd 之后代码重跑。
- **收口决策 (11-24 20:09, Lead 拍板)**: 不重跑。① 稿子 idea2 claim = metacog precision tradeoff (coverage↓/gap-marking↑), 从未声称 wall time 省时 → 省时只是旁证; ② vLLM 被 719 队列占用, 6 run 重跑 4.5h+ 排到半夜后; ③ n=3 不显著就如实写"未证实"是可防御口径。**idea2 收口为: 内容层缓存成立 (前缀 122/122 逐字一致) + metacog precision tradeoff 成立 + wall time 收益未证实 (本批 pre-clamp 混杂, 干净重测未做)**。
- **过夜队列已挂**（rep_scan_queue.sh, b8e7d0a13, pid 16572）: idea2 完 → 自动补重复 100/150/300×5 reps（r4-r8 接续 K7, peak 定位优先, 50/719 端点不补）→ 每 run 自动双轴评分 append 到 rep-scan-scores.json。✅ 凌晨 01:43 跑完 15 reps; **唤醒后第一动作已完成 (11-24)**: rep-scan-scores.json 池化 → k7-pareto-newjudge-20261124.md (104 runs, cov ~300 饱和, 拐点≈300) + idea2 配对统计 (684816ab0) + workshop §4.3 已填。

### L2-5 发表层（v0.1 稿已落盘）
- **结论**: workshop 稿 v0.1 写完（workshop-draft-metacog-20261122.md, edacf05b7+8c266fc8e+f501166f9）。四发现: ①监控在/修复缺（rework 修复率 1.6-2.1%, loop=filter 非 repair cycle）②gap 难度校准（era-matched nat<soc<gpu 全 p<0.001）③预算-质量非单调（150=peak, sd<spread）④loop 连续但不累积（验证率跨层平坦, 无链断, 树绕开未验证节点生长）。限制节前置（单模型/self-judge/n=3/mech 诊断/执行者连续性 meta）。
- **证据**: 全数字来自本地已验证 artifact（k7-pareto-15run / metacog-budget-scan-v1.1 / judge-v1-cov-calibration / plan-layered era-matched 重算）。
- **下一步**: Idea 2 + 补重复数据齐后填 §4.3 的 n 和 peak 位置；repair-loop fix 跑完补 §5.1 的实测；heterogeneous re-judge（无 API key, 已知 gap）。

## 连续性策略（执行者层 · 2026-11-22 D 指出最大瓶颈）

**问题**: goal 状态机只记录"醒来后做什么"，不驱动"什么时候醒来"。执行者（我）的行动是被动触发的。
**架构内可达上限（四件套，全部已就位）**:
1. **同步推进**: 单次会话内把不依赖 GPU 的工作全做完（测量/分析/写稿/质询），不留半截。
2. **异步覆盖**: GPU 等待期挂后台进程（Idea 2 / 补重复），完成时自动唤醒续接统计——等待期不空转，唤醒后无缝接。
3. **无缝续接粒度**: 本文件 L2 笔记 + "下一步"写到"任何一次唤醒不用重新推理就能动手"的程度（具体到文件/命令/参数）。
4. **会话死后唤醒（2026-11-22 23:40 修复, memory/stop-hook-fix-20261122.md）**: stop_hook 只管会话内别停；会话彻底停掉后由 keepalive-wake cron（10min, no_agent, 03f4afb0ea3b）检查"空闲>10min + 有活跃 goal + 30min 去重"→ 投递唤醒消息。HALT 加 6h TTL 防瞬时会话压死主会话（今早 config-sync cron 写 HALT 没删, 压死一整天, 已修）。
**架构外（做不到，诚实标注）**: 唤醒后干得对不对仍靠规划质量；gateway 挂时无解（heartbeat 可查）。已写进 workshop §6 meta-limitation。

## 质询协议（D 不在时, 质疑替代 D）

**每个阶段性结论出数前, 强制过三问**（落盘到对应 L2 笔记）：
1. **最强替代解释是什么？**（数据错? 方法错? 前提错? 题特殊?）→ 设计一个能排除它的检验, 跑了才算数
2. **独立来源能交叉验证吗？**（≥2 源: 本地数据重算 / 文献 / arena）
3. **这个数字换个口径还成立吗?**（judge 版本 / 聚合方式 / 样本子集）

已执行实例:
- hg_rate 0.938 → 替代解释"gpu 题 claim 本来就查不到" → 跨题检验（nat/soc 也 0.94+）→ 排除 ✅
- K7 150=peak → 替代解释"run 噪声" → sd(0.0445) < tier spread(0.0901) → 排除 ✅
- 撞车调研"未撞车" → 替代解释"关键词太窄" → 换 4 轮关键词 + 全文 0 hits 确认 → 边界=conf 0.7 ✅
