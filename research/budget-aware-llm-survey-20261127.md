# origin: ai
# Budget-Aware LLM 调研（Q9E-BA 臂立项依据）· 2026-11-27 · arXiv API 速查

## 触发
D 2026-11-27 13:55 指出：当前 Q9E-Scan 的"预算"没传给 LLM（harness 外部截断），
测的是容量不是优化。新臂 Q9E-BA：预算+目标层次写进 prompt，观察 hack 行为。
立项前查：有没有人做过"预算感知 + 目标函数 hack"的组合。

## 查询（arXiv API，2026-11-27 13:58，https + 重试）
1. all:"test-time compute" AND all:budget
2. all:"reward hacking" AND all:large / language
3. all:"compute budget" AND all:reasoning AND cat:cs.CL

## 最近邻（按相关度）
| 论文 | arXiv | 日期 | 测什么 | 与 Q9E-BA 的差异 |
|---|---|---|---|---|
| Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs | 2507.02534（survey） | 2025-07 | 预算约束下推理质量的自适应/可控性综述 | y 轴=答案正确率；本臂 y 轴=覆盖结构+hack 类型（分解行为变形） |
| Reasoning in Token Economies: Budget-Aware Evaluation of LLM Reasoning Strategies | 2406.06487 | 2024-06 | 不同 token 预算下推理策略的评测 | 同上；且对象是单题推理非因子树分解 |
| Inference-Time Reward Hacking in Large Language Models | 2506.19163 | 2025-06 | 推理时优化 reward model 导致的 proxy 失败 | 机制同源（Goodhart：优化 proxy 被 hack）但场景=RL 优化循环；本臂=单次 prompt 约束下的自发行为 |
| Spontaneous Reward Hacking in Iterative Self-Refinement | 2407.04559 | 2024-07 | 自迭代精化中自发 reward hacking | 最接近的"自发"证据；但无预算维度 |
| Optimizing Test-Time Compute via Meta RL Fine-Tuning | 2503.07448 | 2025-03 | meta-RL 学 test-time compute 分配 | 训练路线；本臂不训权重（D 约束） |
| CodeMonkeys: Scaling Test-Time Compute for SE | 2501.13566 | 2025-01 | SE 任务 test-time compute scaling | 域不同 |

## 本地覆盖核查（local-first）
- `pfb-thinkmech/research/autoresearch-landscape-nontraining-20261124.md` L29 已核：
  6 家 research-agent 系统（Agent Laboratory/Co-Scientist 等）无预算轴，
  "Q9 的预算轴仍是独有"——该结论覆盖 research-agent 语境，
  **未覆盖** budget-aware prompting / reward hacking 这条线（本次补齐）。

## 结论（conf 0.8，速查级：标题+摘要未逐篇精读）
1. "预算约束下推理质量衰减"已被测过（Token Economies 等），y 轴=答案正确率。
2. "推理时 reward hacking"已被测过（Inference-Time RH 等），机制=Goodhart/proxy 失败。
3. **组合 gap 未被占**：无人把"预算感知 prompt + 因子树分解 + 目标函数 hack 类型学"
   放在一起测。Q9E-BA 的三型 hack（凑数/层次理解/无视预算）是对 reward hacking
   在"预算约束+层次目标"条件下的具体化，且带对照臂（无感知 baseline）。
4. 风险：2507.02534 survey 若已含"controllable budget"的行为分析章节，
   novelty 收窄为"分解行为 hack 类型学 + research-agent 语境"——
   精读该 survey 后再定 claim 强度（Q9E-BA 设计阶段做，不阻塞立项）。

## 待办
- [ ] Q9E-BA 设计阶段精读 2507.02534（survey 全文）+ 2506.19163（方法节），确认 gap 表述
- [ ] hack 类型学借鉴 2506.19163 的分类框架（若其分类可迁移）
