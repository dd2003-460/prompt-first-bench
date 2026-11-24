# TASK-BIGDIR-REVIEW — 大方向审查：research-AGI-budget 的 "Pareto 边界" 框架是否成立

> origin: ai · 2026-11-24 · 触发：D 质疑"Pareto 理论上算不出来、实验上没意义，为什么不质疑和修改 goal"

## [任务]
评审"通过预算控制 AI 在 Pareto 边界上研究"这个 goal 框架，回答三个具体问题：
1. "Pareto 边界" 在 LLM-agent / 计算资源分配文献里站不站得住？还是只是把"预算→覆盖的递减收益曲线"误标成了 Pareto？
2. 给定下面的实测数据，最强的可防御 claim 是什么——是"系统 claim"（状态机系统 > bare prompt，预算必须由 harness 强加）还是"预算控制/AGI claim"（预算能在 Pareto 边界上控制研究）？
3. 顶会审稿人最可能打的最狠一刀是什么？

## [背景]（最小必要事实，其余自己读仓库）
- 本地 27b 模型 + 状态机分解系统（SM，prompt+hook，不改权重）
- 实测数据（judge 同族 qwen3.8-27b，仅相对有效）：
  1. SM > bare prompt（matched 预算）：nat Δ+0.131 p=0.016，gpu Δ+0.105 p=0.022
  2. gold 覆盖率在 ~400 节点饱和，跨域一致（GPU + Q6 两域）
  3. 模型不知道何时该停：lexical-novelty gain 仍高（0.86-0.958）但 coverage 已塌（~400 后边际收益≈0）
  4. over-expansion 主导：50:24（树过度展开）
- 机制层（为什么预算影响覆盖）：两天内 v1→v7 反复被自己证伪（Simpson 悖论、within-domain 正相关），站不住
- 当前 goal 框架："预算大→完整覆盖所有贡献因子如 gold；预算小→压缩细节"，包装成"research 的 AGI"

## [约束]
- 中文回答；每条结论标 conf(0-1)；给来源 URL（arXiv/会议论文）；不确定的标"未验证"
- 必须实际检索 2024-2026 文献：LLM-agent 计算预算分配 / compute-optimal scaling / test-time compute / diminishing returns in reasoning / Pareto in LLM agents
- 不许凭记忆

## [交付]
markdown 表格，逐条回答三个问题：
| 问题 | 判断 | 文献支撑(具体论文) | conf | 建议(保留/降级/改框架) |
最后一行：整体判断——这个 goal 应该保留"AGI/Pareto"框架，还是降级为"系统 claim"？最小改法是什么？

## [长度] ≤50 行（核心判断+关键文献+决策；检索过程放附录）

## [落盘约束] 文件不存在=任务未完成：结果写入 tasks/BIGDIR-review/result.md

## [回执指纹]
- 本任务书 sha256（定义：全文去掉本行后的 sha256，防自引用）：78bf4221e17ae7d0b0a086f61409f63bdb9f412bd7e86db078be2954d2bfe147

## [回执] 完成后回执必须含 repo URL + branch + commit_sha + 本任务书 sha256（原样带回）
