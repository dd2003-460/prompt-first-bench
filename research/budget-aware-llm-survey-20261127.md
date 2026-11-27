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

## 第二轮查询（2026-11-27 14:05，prompt 层预算专项，D 追问"除训练关联外 prompt 传递预算的效果"）
query: token-budget+CoT / thinking-budget / length-control+reasoning / budget+instruction-follow / effort-allocation+prompt

| 论文 | arXiv | 层级 | 与 Q9E-BA 关系 |
|---|---|---|---|
| Token-Budget-Aware LLM Reasoning | 2412.18547 | **prompt 层**（"including a reasonable token budget in the prompt"） | **最直接的先例**：prompt 里写预算→推理确实被压缩，且预算取值对压缩效果影响很大（"choice of token budget plays a crucial role"）。证据=prompt 传递预算 work，但效果对预算值敏感 |
| ReasonIF: LRMs Fail to Follow Instructions During Reasoning | 2510.15211 | prompt 层（评测） | **测量框架直接可用**：系统评测 LRM 在推理过程中是否遵循指令，明确把"undesirable shortcuts, hallucinations, or reward hacking within reasoning traces"列为风险维度。我们的 H1/H2/H3 三型 hack 可挂进它的 6 类指令分类做对照 |
| Steering LLM Thinking with Budget Guidance | 2506.13752 | harness 层（轻量 predictor 建模剩余长度 Gamma 分布，无微调） | 非 prompt 传递，是生成中注入信号——与我们的"prompt 一次性告知"形成方法论对照（一次性 vs 持续引导） |
| Increasing the Thinking Budget is Not All You Need | 2512.19585 | harness 层（预算 × self-consistency/reflection 交互） | 系统研究 thinking budget 作为参数的交互效应；支持"预算不是单一旋钮"的判断 |
| Token Budget Saturation & Early Detection of Non-Convergence | 2607.21433 | harness 层（token 预算耗尽=不收敛，probe 早期检测） | 提供"预算耗尽 vs 自然收敛"的二分法——我们 scan 的 n_nodes 贴满 cap 的 run 应按此区分 |

## 结论修正（conf 0.85，两轮速查+摘要级）
1. **D 的问题答案：有**。prompt 层预算传递有直接证据（2412.18547）：写进 prompt 的 token 预算确实改变行为（压缩推理），且效果对预算取值敏感。
2. **但那是"压缩"方向**（少花 token 保住答案质量），y 轴=答案正确率/压缩比。
3. **本臂 gap 收窄但仍成立**：无人测"prompt 预算 + 层次目标（gate 优先）+ 分解行为变形（hack 类型学）"。
   2510.15211 测"推理中指令遵循"但未做预算×目标的交互；2412.18547 做预算但未做层次目标。
   Q9E-BA = 两者的交叉点 + 分解树语境（research-agent 独有，本地 landscape L29 已核 6 家无预算轴）。
4. **设计启示（来自 2412.18547）**：预算取值敏感 → 我们的 5 档（50/100/150/300/719）跨度合理，
   但 BA 臂 prompt 里预算表述要统一口径（"最多 N 个节点" vs "约 N 个节点"），避免措辞引入第二变量。
5. **ReasonIF 的 reward-hacking-in-traces 维度**支持我们的预判：推理过程中的 hack 是已知风险类别，
   我们做的是把它具体化到"预算约束下的分解行为"。

## 待办
- [ ] Q9E-BA 设计阶段精读 2507.02534（survey 全文）+ 2412.18547（方法节：预算怎么写的 prompt）+ 2510.15211（6 类指令分类）
- [ ] hack 类型学对照 2510.15211 的分类框架（若可迁移则引用，不可迁移则自建三型）
