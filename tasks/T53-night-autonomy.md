# T53 夜间自治任务书（2026-11-12 · D 睡前指令）

> origin: human (D 指令) + ai (执行细化)
> 状态：r14 运行中（proc_9f36253dab6c, pid 69056），本文件是夜间自主推进的完整授权与边界。

## 授权范围（D 原话拆解）

1. **打赢开源 SOTA**（"虽然很可能是幻想"）— 继续调状态机，目标 ≥5 道 deepresearch 题上 judge 分 ≥ CellCog Max 对标基线（DRB 56.72 作为分数锚点）。
2. **打赢之后**：继续实现 D 的其他 idea（IDEA-INDEX.md 里未 ✅ 的条目）。
3. **调研纪律（硬约束）**：真的开始研究某个 idea 前必须滚雪球调研——注意最新进展和"可直接做的组"，避免撞车。落盘 lit-survey/ + IDEA-INDEX 更新完成度标记。
4. **邮件准备**：调研完成后起草给相关领域教授组的通信邮件（只起草，不发送——外发留痕等 D 醒来确认）。

## 硬约束（继承 tasks/T53-decomp-state-machine.md，此处只索引不重复）

- **严禁泄漏**：状态机任何位置不得泄漏题目本身（T53 文件 §硬约束 + research/sm-leak-sop.md）
- **general 原则**：prompt 规则必须是 meta-rule，不得写死某道题的统计量或域特定先验。判定用 structural test（可检验结构特征），不用经验比例。
- **无 train/test 污染**：bench 题特征不得进入 prompt 规则（ICL-as-training，Decision 23）。
- **过去版本可复现**：每次改 s5_state_machine.py 前 git commit；每轮 run 记录 rN + commit SHA；checkpoint JSON 保留全部历史版本不覆盖。
- **目标函数公式**：U(T) = C·A·S − λ·cost(T)（机器侧验收，不进 prompt）；S_α' 只做过程监控（proxy cone），不进 prompt。

## 当前状态（交接快照）

| 项 | 值 |
|---|---|
| r14 | 运行中，commit d230a64d（structural test + 信息量语义），baseline = sm-gpu-r11-crash-303.json |
| r13 教训 | 63/70 节点判 quotient = 例子诱导偏置 → 已修（cartesian 默认 + 运算结构才判 quotient） |
| r14 观察点 | edge_types 应回到 cartesian 主导（quotient ≤20%）；节点数预期 100-150；contribution filter 首次生效（阈值 0.10） |
| 本地 LLM | 127.0.0.1:8787 (qwen3.8-27b) |
| 网络 | ego-browser 可用但慢（WEBLLM-SKIP 属降级非故障） |

## 夜间工作序列（遇阻跳过做下一个，不停摆）

### Phase 1: r14 监控与校准（~1h）
1. 盯 proc_9f36253dab6c 跑完（预计 30-60min）。
2. 提取 stats：节点数 / edge_types 分布 / contribution-filter 触发次数 / leaks / degraded 率。
3. 判定：quotient >30% → 再修 prompt 跑 r15；节点 <80 且 verified <30% → 放宽 fanout cap；正常区间（quotient ≤20%, 节点 100-150）→ 进 Phase 2。
4. 结果落盘 experiments/stage-ablation/r14-results.md（含 r12/r13 对比表）。

### Phase 2: DRB pilot + 迭代优化循环（D 04:05 授权升级：校准合理即开跑，不用等 Lead 确认；打不赢→诊断弱项→改机制→重跑，循环到收敛）
1. 选 5 道 deepresearch 类题（HotpotQA hard / 2WikiMultihop / DRB 公开题集；多跳+事实检索混合，避开 GPU 域）。
2. 每题跑状态机，记录节点数/轮数/核验率/答案质量。
3. 评分口径：异族 judge（数字正确 0.5 + 对比/单位正确 0.5，n=3 median）。
4. 对照：CellCog Max 56.72（overall）+ 子项（comprehensiveness 57.06 / insight 57.67 / instruction following 56.58 / readability 53.81）。
5. 汇总 experiments/stage-ablation/s5-sm-bench-report.md。
6. 打不赢 → 诊断弱项子项 → 回 Phase 1 修机制（不是加题）。

### Phase 3: idea 逐个推进
按 IDEA-INDEX.md 未完成条目产投比排序：
1. 开工前滚雪球调研：arXiv 近 6 月 + GitHub 已有实现 + 谁在做做到哪了。
2. 撞车 → 标 📦 吸收记差异，换下一个。
3. 找"方法已发表但工程未落地"窗口（优势 = 本地 27b + hook 不改权重）。
4. 产出落盘 lit-survey/，IDEA-INDEX 更新状态。

### Phase 4: 教授通信邮件（Phase 3 后）
1. 定目标教授组（领域匹配 + 近期活跃 + 合作意愿信号）。
2. 起草邮件（介绍 autoresearch 方向 + 具体技术问题 + 合作切入点）。
3. **只起草不发送**。存 个人/outbox-drafts/，APPROVALS.md 留痕，等 D 醒来审阅。

## 唤醒与汇报

- cron/heartbeat 周期唤醒（loop-station-keepalive 30min，需确认 enabled）。
- 每次唤醒读此文件 → 看当前 Phase → 推进 → 更新「执行日志」。
- 关键节点（r14 完成 / bench 出分 / 撞车 / 需 D 决策）QQ 汇报，其余静默。

## 红线（夜间也有效）

- 不发任何对外消息（邮件/社交/发布）——只起草。
- 不动 AGENTS.md 非临时内容。不花钱。
- 删工作区外文件前写 APPROVALS。
- 拿不准的事 → 标 [待D醒] 跳过做别的。

## 执行日志

- 2026-11-12 ~02:00 任务书创建，r14 启动（proc_9f36253dab6c, commit d230a64d）。- 2026-11-12 ~04:05 D 指令升级：① 迭代优化循环授权（不止 r14，确认有优化空间就继续改/跑）；② DRB 感觉差不多时直接跑（HF muset-ai/DeepResearch-Bench-Dataset + 官方 judge 口径对齐 56.72，先 2-3 题试水再扩 5 题）；③ gold 答案降级为回归测试集（保留，不进主验收），主验收 = DRB 公开题。bus L2 已通知 teamer。
- 2026-11-12 ~03:40 Lead 唤醒：r14 已于 02:44 DONE（137 records/40 unique，quotient 12.4%✅，leaks=0，degraded 56.9%⚠️，contribution-filter 零触发❌）。CC 期间已完成 C1/C2/C3（校准分析 + DDG 取证 + id 撞号 fix @7cf91694），卡在内存；现 free RAM ~40GB 已释放。Lead 落盘 experiments/stage-ablation/r14-results.md（含 r11/r13/r14 对比表 + Phase 1 判定：不进 r15，进 Phase 2 DRB pilot）。下一步等 CC 启动 drb-1（新 qid 顺带验证 id fix）→ 组装器 → 四维判分。
- 2026-11-12 ~04:15 Lead 唤醒：drb-1 健康运行中（pid 4308, round-1 VERIFY, log 04:12 仍在写；_nid fix 生效无撞号，fanout cap N1 kept 8/24，edge-reclassify 3 次 cartesian→quotient 符合预期）。处理 inbox：采纳 CC C9 live census（unusable 52%，主因 = cn.bing 跨域噪声非 URL junk）→ Decision 25 改判 deferred（sm-thinking-sop.md 已更新）；审计靶点 #2 升级为 Decision 26 数字溯源提案（research/d26-number-provenance-proposal.md，三问过，未落代码，drb-1 出分后实施）；lead-to-cc L5 回写。commit ac0f0883。下一步：等 drb-1 出树（预计 1-2h）→ assemble → judge → bench report §3；drb-2/drb-16 已就位排队第二题。
