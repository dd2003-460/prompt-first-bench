# 元认知 / ICL 再校准 / 探针 — 前沿调研（2026-11-07）

origin: ai | 触发：成璐问"元认知是不是校准？ICL 能重新校准 RL 污染的部分吗？有探针可做吗？有前沿研究吗？"
方法：arXiv API 直查（本轮工具输出，来源①），6+5 组查询共 ~70 条命中，人工筛出相关子集。未做网页 LLM 交叉验证（conf 相应降档）。

## 结论速览

1. **元认知 ≠ 纯校准**，但两者共享测量基础设施。学界主流把 metacognition 定义为"监控 + 调节"双组件（monitoring = 知道自己知道什么/不知道什么；regulation = 据此调整行为）。校准只是 monitoring 的一个可测切片（置信度 vs 实际正确率）。所以"元认知要求模型理解自己的特性"对了一半——它还需要"根据这个理解改变行为"，后者才是 pfb M3/M4 测的东西。
2. **RLHF 确实系统性破坏校准**，且方向是过度自信。这不是猜测，有多篇直接证据（见 §2）。所以"RL 污染了置信度通道"这个前提成立。
3. **ICL 能部分修复，但有硬边界**。few-shot 演示可以拉回 verbalized confidence 的校准（§3），但 2026-09 的 Mirage 论文证明 verbalized confidence 在 VLM 上 trajectory-independent——即模型反复自我纠错、最后答错、仍然报高置信。这说明**语言层面的校准声明和内部状态是脱钩的**，ICL 改的是"嘴上说的"，不一定改"心里想的"。
4. **探针路线活跃且比想象中成熟**（§4）。三条线：(a) hidden-state 线性探针读置信度/幻觉风险，(b) learned readout tokens，(c) 内部回路定位失败预测。关键发现：内部信号通常比 verbalized 更准——这正好支持我们之前"logprob/探针只做优先级排序不做触发"的设计判断。
5. **最贴合我们方向的单篇**：`2512.20578 Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits`（2025-12）——用内部回路而非外部 judge 预测自身失败，与 pfb 的 harness 层设计直接对话。

## §1 元认知定义（metacognition 线）

| arXiv | 标题 | 要点 |
|---|---|---|
| 2504.14045 | Metacognition and Uncertainty Communication in Humans and LLMs (2025-04) | 人类 vs LLM 的 metacognition + 不确定性沟通对比框架 |
| 2608.15400 | Metacognition Framework for Self-Awareness and Self-Regulation in Ensembles of LLMs (2026-08) | 显式承认 LLM 三大短板：评估自身不确定性 / 检测知识冲突 / 识别超出专长的问题——ensemble 层面补 |
| 2605.08942 | Decomposing and Steering Functional Metacognition in LLMs (2026-05) | 把"功能性元认知"分解成可 steering 的表征——**元认知可以被表征工程干预**，与我们问的 ICL/steering 直接相关 |
| 2510.05126 | Generalization of Fine-Tuned Uncertainty Communication and Metacognition (2025-09) | 微调出来的不确定性沟通能不能泛化——答案有限，域内好、跨域掉 |
| 2602.18806 | Think²: Grounded Metacognitive Reasoning (2026-02) | 按 Ann Brown 调节循环（plan-monitor-evaluate）实现 grounded metacognition |
| 2308.05342 | Metacognitive Prompting Improves Understanding (2023-08) | 最早的 metacognitive prompting 之一——prompt 层就能提升，harness 可行的早期证据 |

## §2 RLHF 污染校准的证据链

| arXiv | 标题 | 要点 |
|---|---|---|
| 2410.09724 | Taming Overconfidence in LLMs: Reward Calibration in RLHF (2024-10) | 直接点题：RLHF 导致 overconfidence，解法是在 reward 里加校准项 |
| 2604.10585 | Calibration Collapse Under Sycophancy Fine-Tuning (2026-04) | **最强证据**：谄媚型 reward hacking 会直接打崩 UQ（uncertainty quantification）——reward 信号污染 → 校准崩溃 |
| 2502.11028 | Mind the Confidence Gap: Overconfidence, Calibration, Distractor Effects (2025-02) | 系统分析 overconfidence 的来源，distractor 效应单独量化 |
| 2305.14975 | Just Ask for Calibration: Eliciting Calibrated Confidence from HF-Fine-Tuned LMs (2023-05) | 早期工作：HF 微调后校准变差，但特定 prompt 策略能 eliciting 回来——**prompt/harness 层修复的先例** |
| 2409.19817 | Calibrating LMs with Adaptive Temperature Scaling (2024-09) | 后训练破坏温度校准，自适应 scaling 修复——logit 层修复路线 |
| 2509.01564 | Enhancing Uncertainty Estimation with Expectation of Aggregated Internal Belief (2025-09) | 点名 RLHF 后模型的 overconfidence，用内部信念聚合估计不确定性 |

## §3 ICL 再校准（直接回答"ICL 能修 RL 污染吗"）

| arXiv | 标题 | 要点 |
|---|---|---|
| 2312.04021 | A Study on the Calibration of In-context Learning (2023-12) | ICL 本身引入新的 miscalibration（prior bias + context 偏差）——ICL 既是药也是毒 |
| 2506.12796 | Surprise Calibration for Better ICL (2025-06) | 用 surprise 信号校准 ICL 中的 prior/context 冲突——**思路和我们 idea-list #22 的级联阈值同源** |
| 2309.17249 | Batch Calibration for ICL and Prompt Engineering (2023-09) | batch 层面重校 ICL 输出分布 |
| 2310.10266 | Generative Calibration for ICL (2023-10) | 生成式校准，缓解 prompt 敏感性 |
| 2401.12406 | Enhancing ICL via Linear Probe Calibration (2024-01) | **ICL × 探针交叉点**：用 linear probe 校准 ICL——证明两条线可以合并 |
| 2402.05515 | NoisyICL: Noise in Parameters Calibrates ICL (2024-02) | 参数加噪反而改善 ICL 校准（去 prior 依赖）——反直觉结果 |
| 2410.02210 | Calibrate to Discriminate: Label-Free Comparative Inference (2024-10) | "indiscriminate confidence"：对错都报同样置信——比较推理打破 |
| 2609.18453 | The Mirage of Calibrated Confidence (VLM, 2026-09) | **边界条件**：verbalized confidence trajectory-independent，自纠错不降低口头置信——ICL/prompt 修的只是语言层 |
| 2609.10996 | Rethinking Verbalized Confidence for LLM-as-a-Judge (2026-09) | 反转：2025 后的顶级闭源模型上 verbalized confidence 反而成了更稳的 soft-scoring 机制——**污染程度随模型代际下降** |

## §4 探针路线（"有探针可做吗"）

| arXiv | 标题 | 要点 |
|---|---|---|
| 2407.03282 | LLM Internal States Reveal Hallucination Risk Faced With a Query (2024-07) | 经典：query 阶段内部状态即可预测幻觉风险——**生成前可读**，支持"触发在生成时不在事后" |
| 2512.20949 | Neural Probe-Based Hallucination Detection (2025-12) | 探针检测幻觉，对比 uncertainty/self-critique 基线 |
| 2512.20578 | Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits (2025-12) | **最相关**：内部回路预测自身失败，不需要外部 judge/multi-sample——harness 友好的探针 |
| 2610.27566 | Learned Readout Tokens for Extracting LLM Confidence (2026-10) | 学出来的读出 token 提取置信度——比固定层探针更灵活 |
| 2605.31220 | Shared Doubt: Zero-Shot Cross-Lingual Confidence Estimation (2026-05) | 跨语言零样本置信估计——探针的可迁移性 |
| 2405.16282 | Confidence Under the Hood: Confidence-Probability Alignment (2024-05) | 口头置信 vs 内部概率的对齐度系统调查——量化"嘴和心脱钩"有多严重 |
| 2610.25846 | Measurement Validity and Representation Dynamics of Confidence Signals (2026-10) | **方法论警示**：verbalized / linear probe / semantic ensemble 三个通道测的不是同一个东西——选探针前先定测量效度 |
| 2607.07626 | Future Confidence Distillation (2026-07) | 把未来 token 的置信蒸馏到当前——面向 retrieval/tool-use 路由的置信估计，**直接服务我们的 cascade 路由** |
| 2601.18901 | Self-Aware Knowledge Probing via Confidence Calibration (2026-01) | 关系知识探测 + 校准联合评估 |

## §5 activation steering（ICL 之外的第三类干预，顺带覆盖）

| arXiv | 标题 | 要点 |
|---|---|---|
| 2512.07667 | Depth-Wise Activation Steering for Honest LMs (2025-12) | 诚实性 steering：模型内部知道正确答案但说错——按深度分层干预，不改权重 |
| 2605.10664 | Prompt-Activation Duality (2026-05) | **重要坑**：residual-stream steering 在有状态对话中因 KV-cache 污染失效——steering 向量被存进 cache 反复复用。我们若做本地 27b steering 必须注意 |
| 2604.24693 | Contextual Linear Activation Steering (2026-04) | 固定强度 steering 不够，要 context-dependent 强度 |
| 2410.12877 | Improving Instruction-Following via Activation Steering (2024-10) | instruction 向量的提取与应用先例 |

## 对我们（pfb / autoresearch 系统）的含义

1. **harness 三层图需要修正**：之前说"harness 已收敛、信源置信层可做、元认知是硬骨头"。这批文献说明元认知层内部又分三档：
   - 语言层校准（verbalized confidence）→ prompt/ICL 可修，但有 Mirage 边界（嘴心脱钩）
   - 内部信号读取（probe/readout token/internal circuits）→ **不动权重、推理时读取**，本质仍是 harness，且证据显示比语言层更准
   - 内部状态改写（activation steering）→ 介于 harness 和训练之间，KV-cache 坑要注意
   所以"硬骨头"其实只属于第三档的边缘情况；第二档（探针）是已经可用的工程件。
2. **"logprob 探针只做优先级排序不做触发"的设计得到外部支持**：2407.03282（query 阶段内部状态预测幻觉）+ 2607.07626（future confidence distillation 服务路由）都指向同一架构：探针输出喂给路由器，不直接改生成。
3. **ICL 再校准的正确姿势**：不是"往上下文塞校准示例"（2312.04021 证明这本身引入新偏差），而是 surprise-calibration（2506.12796）或 comparative inference（2410.02210）这类**结构化用法**——例子教的是"怎么比"，不是"答案是什么"。这和我们 rubric O5 的 judge-only anchor 设计同构。
4. **RL 污染是事实，但代际在收敛**（2609.10996）：越新的模型 verbalized confidence 越可用。含义：我们针对本地 27b（LM Studio/vLLM 部署的 qwen3.8-27b）做的校准 harness，换底座后要重新标定，不能假设永久有效。

## 缺口 / 待核验

- [待核验] 2609.18453 (Mirage) 的 trajectory-independence 是否在纯文本 LLM 上也成立（原文是 VLM）——需读全文确认
- [待核验] 2512.20578 的内部回路方法是否开源、能否在 27b 规模复现
- [待核验] 2605.08942 "steering functional metacognition" 的具体 steering 方向和效果量
- 未做 ego-browser 网页 LLM 交叉验证（本轮时间预算内优先 arXiv 一手源）；以上 conf 按"刚查到的 arXiv 摘要"= ①类，但摘要≠全文，具体数字/方法细节引用前需读 PDF