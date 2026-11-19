# Novelty 落位决策 — phase4-paper 论文 claim 结构

> origin: ai · 2026-11-19 · 服务 pfb-hardening-v2 phase4-paper
> 来源：`experiments/stage-ablation/novelty-scan-2026-11-07.md`（三轴结论 + 8 篇最接近 + 引文空间）
> + `modules/D-decomp-state-machine/research/2026-11-07-idea-list.md`（#22-#25）
> 用途：phase4-paper 写论文时直接消费本文件，不再重新调研 novelty 定位。

## 1. 论文 claim 结构（三轴）

**核心 claim**：pfb 的贡献不是"做了分解+检索+校验"（单项都有人做），而是**三个正交轴上的位置选择 + 各轴贡献的独立测量**。

| 轴 | 我们做了什么 | 为什么新 | 证据 |
|----|------------|---------|------|
| ① 分解方式（怎么拆） | 正交完备分解状态机（DecompStateMachine） | **不新**——GPT Researcher/TreeFlex/ScaffoldAgent 都做了。只是管道第一环，不单独当 claim。 | 消融：S5 vs S0 的 Δ 不全来自分解 |
| ② 校验方式（谁验、怎么验） | 单模型自验（S5）→ 多 persona 质询（S8）→ 异族 judge（B-face）。验证独立性是连续变量不是开关。 | **新**——"验证独立性是连续变量"这个定位 + 量化测量（O6 矛盾发现维度）没人做。RubricAtlas 做自动 rubric 挖掘，我们做手工精雕 + 信息论权重（O3 surprisal 公式）。 | S5 vs S0: nat +0.017 / soc +0.0185 / gpu +0.301（phase3 报告） |
| ③ 组合贡献的独立性（各组件增益是否正交可加） | 每个组件可单独开/关（prompt 层消融天然干净），测各臂 Δ 落在哪个 metric 维度。 | **最关键的 claim**——决定论文能否立住。若 S5 增益全来自 R4 终审，则"分解+检索+校验"是伪正交；只有证明各臂 Δ 落在不同维度（M1/M4/O6 归因到不同组件），"组合"才有意义。 | T53b 消融数据（r10 在跑，20/62）+ S8 B-face 重打数据 |

**claim 表述（论文 intro 用）**：
> We do not claim that decomposition, retrieval, or verification are novel. We claim that (a) verification independence is a continuous variable measurable per-component, and (b) the contribution of each pipeline component is orthogonal and independently measurable at the prompt layer — a structural advantage over RL-trained systems where contributions are entangled in weight gradients.

## 2. Related Work 引用清单

### 2.1 最接近的 8 篇（必须逐条引用 + 说明差异）

| 论文 | arXiv | 差异表述（论文里怎么写） |
|------|-------|------------------------|
| Rethinking Verification in Agent Harnesses | 2610.34577 | 他们设计验证机制，我们**测量**验证机制（rubric + ablation 臂） |
| VeriHarness | 2610.00972 | 他们面向长程任务执行，我们面向**调研质量评分** |
| RubricAtlas | 2610.36878 | 他们自动生成 rubric，我们手工精雕 + 信息论权重（O3 surprisal） |
| Dr.Credit | 2609.34296 | 他们做 RL 信用分配，我们做**诊断性消融**（哪个 prompt 组件贡献多少分） |
| DEEPRUBRIC | 2606.17029 | 他们做 evidence-tree rubric 监督 RL，我们做 pipeline 组件归因 |
| Incremental Open-Ended Deep Research | 2610.11566 | 他们管增量更新，我们管**阶段门禁 + 回退**（repair_stage） |
| Multi-Turn Evaluation of DRA | 2606.09748 | 他们端到端多轮交互，我们**单管道内六阶段**的组件消融 |
| Where Do Deep-Research Agents Go Wrong? | 2606.02060 | 他们定位**哪错了**，我们度量**为什么错**（M1-M6 六维 + O5 口径链 + O6 矛盾发现） |

### 2.2 最近竞争者（必须盯 + 差异表述）

| 论文 | arXiv | 差异表述 |
|------|-------|---------|
| **MetaResearcher** | 2606.19893 | **最近的竞争者**。它做 RL 训练（改权重），我们做测量 + prompt 层（不动权重）。它的 contradiction resolution 任务和我们的 O6 重叠，source credibility 评估对应我们的 M6。差异本身是卖点：同等能力目标下，prompt/hook 层的可审计性和回滚性优于权重修改。但"矛盾当一等公民"概念不再独占——我们的增量在**度量**（O6 三档判据 + 防泄露协议），不在概念。 |
| PatEx-Gym | 2610.33503 | **直接可用**。它的"final accuracy ≠ process quality"结论和我们 M1-M6 多维评分的动机完全同构，related work 里当外部证据用。 |
| Question's Gambit | 2609.14412 | **相邻但正交**。它优化"第一次搜什么"（retrieval first move），我们 idea-list #22 的 L1/L2 是"按回滚成本决定分解深度和校验强度"。可引用为"first-move 质量重要"的外部佐证，不构成威胁。 |

### 2.3 自适应路由撞车（#24 相关，必须引用说明差异）

| 论文 | arXiv | 共同范式 | 我们的差异 |
|------|-------|---------|-----------|
| Learning When to Think | 2608.20256 | RL 训练按难度自适应 token 预算 | 我们换"行为本身"（指令集分域），不是调"同一行为的剂量" |
| Thinking Hard, Not Smart | 2608.07968 | 推理模型跨题预算分配失败 | 同上 |
| CIRCE | 2610.41089 | 从约束结构预估复杂度 → 路由+预算 | 同上 |
| SuCo | 2606.17687 | 充分性引导的连续 CoT 长度 | 同上 |
| When Should Active RAG Retrieve? | 2607.24010 | 预算感知的检索/不检索决策 | 同上 |
| Claim-Level Reliability | 2608.11994 | 按 claim 可靠性把算力从采样挪到验证 | 同上 |

**#24 的三个差异点**（conf 中高，待四臂实验实证）：
1. 路由对象不同：它们调"同一行为的剂量"；我们换"行为本身"（两套 prompt 内容不同）
2. 触发维度不同：它们按难度/置信度/充分性；我们按任务类型（要准 vs 要新）
3. 无贡献测量：它们报端到端准确率-预算曲线；没人测路由本身的独立贡献

**claim 影响**："自适应"这个词彻底不能当 novelty。#24 的可卖点 = 指令集分域 + 任务类型触发 + 贡献独立性测量，三者叠加。

## 3. 与 MetaResearcher 的差异（论文里怎么表述）

**一句话**：MetaResearcher 用 RL 训练让 agent 学会找矛盾和评估来源可信度；我们用 prompt 层测量 + 消融让每个组件的贡献可独立归因。

**展开（论文 related work 节用）**：
- MetaResearcher (2606.19893) 是最接近的竞争者：它的 contradiction resolution 任务和我们的 O6 维度重叠，source credibility 评估对应我们的 M6/来源分级。
- 关键差异：它是**训练**（RL 改权重，GRPO meta-reward 联合优化），我们是**测量 + prompt 层**（不动权重，五级干预梯度取最低档）。
- 这个差异本身是卖点：同等能力目标下，prompt/hook 层的可审计性（每个组件可单独开/关，消融天然干净）和回滚性（改 prompt 不改权重，回滚 = 改回旧 prompt）优于权重修改。
- 风险：它 2026-06 就提出了 contradiction resolution as task，说明"矛盾当一等公民"概念不再独占。我们的增量在**度量**（O6 三档判据 + 防泄露协议），不在概念。
- 叙事策略：不写"我们第一个做矛盾检测"，写"我们第一个把矛盾检测做成可独立测量的维度（O6），并在 prompt 层证明其贡献与检索/分解正交"。

## 4. Idea 落位表（idea-list → 论文哪一节）

| Idea | 落位 | 论文里怎么用 |
|------|------|------------|
| #22 矛盾检测三级级联（L1 先验 → L2 ICL → L3 构造） | Method 节（S5 管线的检索路由机制） | 作为 S5 的"查不查"路由机制描述。可证伪实验（S5-cascade vs S5-full vs D1）列入 B-face 候选。 |
| #23 S8-discuss 多模型讨论校验臂 | Method 节（校验方式轴）+ Experiment 节（S8 vs S5 vs D1 消融） | 三轴 novelty 第 2 轴的实证。O6 维度是 S8 的主指标。B-face 重打数据已落盘。 |
| #24 长短 prompt 按任务类型分域 | Method 节（指令集分域机制）+ Experiment 节（四臂交叉对比） | 三轴 novelty 第 3 轴（贡献独立性）的实证。四臂实验设计已落盘 idea-list #24。 |
| #25 理论定位（机制假设 H1/H2 + 可证伪预测 P1-P4） | Discussion 节（Mechanism & Predictions） | 把论文从"纯消融报告"升级到"有机制解释的系统研究"。H1: M1 由外部锚点密度驱动；H2: O6/M4 由指令结构驱动。 |
| #30-#33 目标函数 hack + MDL 路线 | Method 节（S_α 目标函数设计）+ Limitations 节（reward hacking 风险） | S_α' 保留为过程监控指标（非验收标准），Goodhart 防线：两个代理都不进 prompt。 |
| #34 压缩项连续性 + 外生离散信息豁免 | Method 节（redundancy_score 设计） | 外生离散信息（显卡规格、市场价格）豁免压缩惩罚——这正好和本文件 T2（硬件知识库）呼应。 |

## 5. 论文结构（phase4-paper gate 要求的正式结构）

| 节 | 内容 | 数据来源 |
|----|------|---------|
| Abstract | 三轴 claim + 三题面 S5 > S0 结果（nat +0.017 / soc +0.0185 / gpu +0.301） | phase3-comparison-report |
| Intro | 问题（deep research agent 质量怎么测）→ 现有工作（8 篇 + MetaResearcher）→ 我们的三轴 claim | 本文件 §1-§3 |
| Method | S5 管线机制（分解状态机 + 核验 + 综合 + 判分）+ 三轴设计 + O3/O5/O6 维度定义 | s5-sm-bench-report + rubric-v3 |
| Experiment | 三题面对比（nat/soc/gpu）+ S5 vs S0 消融 + S8 B-face 重打 + T53b 消融数据 | phase3 报告 + T53b runs |
| Discussion | 机制假设 H1/H2 + 可证伪预测 P1-P4 + 与 MetaResearcher 的差异 | 本文件 §3 + idea-list #25 |
| Limitations | ① 绝对分待异源复核（T8-C3-v3 blocked）② 跨题面口径不一致（verified rate vs judge coverage mean）③ nat 未跑 10-run mean ④ webllm 三通道全挂（reworks 91 个全是来源缺失非树质量） | phase3 报告 §2.2 + §4 |
| Related Work | 8 篇最接近 + MetaResearcher + PatEx-Gym + 自适应路由 6 篇 | 本文件 §2 |

## 6. 待办（phase4-paper 推进前必须完成）

- [ ] T53b 消融数据跑完（当前 r10，20/62）→ 补全 Experiment 节
- [ ] 异源 judge 复核（T8-C3-v3 blocked_human：无非 Qwen 端点）→ 解除 Limitations ①
- [ ] nat 补跑 10-run mean → 解除 Limitations ③
- [ ] 跨题面口径统一（可选，取决于论文定位）→ 解除 Limitations ②
- [ ] 本文件 commit + push（pfb repo）
