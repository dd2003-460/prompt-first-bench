# TASK-IDEA-REVIEW-ROUND6 — 最终闭式 paper 碰撞核查 + venue 匹配

> origin: ai · 2026-11-25 · 触发：D 微信 08:53 三连催"其余 idea 问一遍" + 20:25 预印本/venue 诉求
> 背景：IDEA-review 前 5 轮查的是 #53 转向前的旧 claim（GPU run 树 + 交叉梯度 MI）。D 17:39 转向闭式数学路线（eb1b0598c），最终 paper 18:15 定稿（9pp）。前 5 轮对最终 paper 零覆盖。Lead 已做 arXiv 初判（6 组，未见直接撞车，4 最近邻可切割，conf 0.6，单源）。本轮 = 对最终 paper 的独立碰撞核查 + venue 匹配。

## [任务]
对最终闭式 paper 做三件事：
1. **独立碰撞核查**：2024-2026 arXiv / IEEE / ACM / 顶会 / GitHub / 工业白皮书里，有没有人做过（或做了近邻）"闭式数学测量深层判断对 GPU 瓶颈诊断的增量贡献"？必须实际检索，给具体论文 URL + 标题 + 版本/日期。
2. **非 arXiv 源覆盖**：重点查 IEEE TC/TCAD、ACM TOS、工业白皮书（NVIDIA/AMD 性能建模）、专利——Lead 初判只覆盖 arXiv。
3. **venue 匹配**：基于最终 paper 性质（闭式数学测量文，无 GPU 实验、无 eval/dataset 交付物），判断投哪个 venue（NeurIPS E&D / ICML workshop / MLSys / ACL Findings / arXiv 兜底），给排序 + 理由 + 接收概率（标 conf）。

## [最终 paper 自包含描述]
- 标题：How Much Does Microarchitecture Matter? A Closed-Form, Pre-Registered Measure of the Incremental Contribution of Deep Judgments in GPU Bottleneck Diagnosis
- 核心 claim：GPU 瓶颈诊断中，深层微架构级判断对瓶颈判定的增量信息贡献 > 浅层枚举，且该增量可从 hardware spec + workload prior 闭式计算（不跑 GPU）。
- 方法：闭式数学（4 硬件 spec + workload 先验），含 resist 电阻瓶颈模型；预注册（held-out 先锁）。
- novelty（Lead 初判）：闭式 × 增量贡献测量 × 预注册 三元组合。
- 性质：纯闭式数学测量文，无 GPU 实验、无 eval/dataset 交付物。
- paper 全文：本分支 tasks/idea53-goal/submission/paper.tex（9pp）。

## [Lead 初判（供交叉核验，不代替独立检索）]
- 4 最近邻（可切割）：2610.10924 TME 闭式阈值 / 2402.08964 spec 回归 / 2607.13184 Microflow / 2512.01644 LLM 刻画
- conf 0.6（单源 arXiv，非穷尽）

## [约束]
- 中文；每条结论标 conf(0-1)；给来源 URL；不确定标"未验证"
- 必须实际检索（arXiv API / Google Scholar / IEEE Xplore / ACM DL / GitHub）；检索片段而非全文的定量条目标"未验证"+强度
- 不许凭记忆；不许直接复用 Lead 初判的 4 个最近邻当结论（要独立检索验证 + 补充）

## [交付]
markdown 表格：
| 检索源 | 撞车/近邻(URL) | 与最终 paper 距离 | 是否撞车(是/否/近邻) | conf |
最后：① 碰撞核验总判断（撞车/未撞车/窄空白）+ conf ② venue 排序（含接收概率，标 conf）③ 最难一击

## [长度] ≤60 行（核心判断+关键文献+venue 排序；检索过程放附录）

## [落盘约束] 文件不存在=任务未完成：结果追加到 tasks/IDEA-review/result.md（第六轮节）

## [回执指纹]
- 本任务书 sha256（定义：全文去掉本行后的 sha256，防自引用）：8c5158db02b7e328ed261d9547a9775da8127a2ada881a6f874ad8d629801951

## [回执] 完成后回执必须含 repo URL + branch + commit_sha + 本任务书 sha256（原样带回）
