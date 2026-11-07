# 新颖性撞车扫描（2026-11-07 · 成璐问"decomp 也有人做了，我们还有啥新的？怎么完整搜索未知？"）

## 背景

成璐的观察：pfb 最终形态 = 正交分解 → 全渠道搜索 → 质询/找矛盾 → 外部校验 → 修正输入 → 内外逻辑校验的 loop。decomp 类工作别人也在做（GPT Researcher、Open Deep Research、STORM 等，见 `competitor-survey.md`）。担心撞车，且 arXiv 关键词命中是否足够覆盖"未知"存疑。

## 本轮扫描方法

arXiv API × 16 组关键词（deep research + self-verification / agentic fact-checking / rubric / harness / goal decomposition / caliber consistency / multi-agent debate factual / confidence cascade search / contradiction detection / prompt benchmark ablation / test-time scaling verification / process evaluation / stage gate / query decomposition loop / external verification / calibration search policy），按提交日期倒序取 top15/组，去重后 **121 篇 unique**，2026-03 ~ 2026-11。原始数据 `/tmp/arxiv-novelty.json`（scratch，非落盘资产）。

## 最接近的 8 篇（逐条比对）

| 论文 | 做什么 | 与 pfb 重叠 | 不重叠（我们的增量） |
|------|--------|------------|---------------------|
| **Rethinking Verification in Agent Harnesses** (2610.34577) | agent harness 里验证机制的系统思考 | "验证属于 harness 层"这个定位 | 我们是**测量**（rubric+ablation 臂），他们是设计；我们没有他们的工程方案，他们有我们的量化证据 |
| **VeriHarness: Scaling Agentic Verification for Long-Horizon Tasks** (2610.00972) | 长程任务的规模化验证 | 验证规模化思想 | 他们面向长程任务执行，我们面向**调研质量评分**；无 rubric 维度设计 |
| **RubricAtlas** (2610.36878) | 从专家报告挖 type-level rubric 评 DRA | rubric 评 deep research | 他们是**自动生成** rubric，我们是**手工精雕 + 信息论权重**（O3 surprisal 公式 w_v=1+min(−log₂p̃, log₂(1/ε))）；未做自动挖掘 |
| **Dr.Credit** (2609.34296) | rubric-grounded process credit assignment | rubric→过程分 | 他们做 RL 信用分配，我们做**诊断性消融**（哪个 prompt 组件贡献多少分） |
| **DEEPRUBRIC** (2606.17029) | evidence-tree rubric 监督 RL | gold 树 + rubric | 同上：RL 训练信号 vs 我们的 pipeline 组件归因 |
| **Incremental Open-Ended Deep Research with Structured Harness** (2610.11566) | 结构化 harness 做增量研究 | "harness 结构化" | 他们管增量更新，我们管**阶段门禁 + 回退**（repair_stage） |
| **Multi-Turn Evaluation of DRA Under Process-Level Feedback** (2606.09748) | 过程级反馈的多轮评测 | 过程评测 | 他们是端到端多轮交互，我们是**单管道内六阶段**的组件消融 |
| **Where Do Deep-Research Agents Go Wrong?** (2606.02060) | span-level 错误定位 | 错误分析 | 他们定位**哪错了**，我们度量**为什么错**（M1-M6 六维 + O5 口径链 + O6 矛盾发现） |

**结论（2026-11-07 晚修正，成璐指出"分解并不是一切"）**：novelty 不是"四件套组合"这个笼统说法，而是**三个正交轴上的位置选择 + 各轴贡献的独立测量**——

1. **分解方式**（怎么拆）：不新（GPT Researcher/TreeFlex/ScaffoldAgent 都做了），只是管道第一环
2. **校验方式**（谁验、怎么验）：我们真正在动的轴。单模型自验（S5）→ 多 persona 质询（S8）→ 异族 judge（B-face），验证独立性是连续变量不是开关
3. **组合贡献的独立性**（各组件增益是否正交可加）：决定论文能否立住的关键。若 S5 增益全来自 R4 终审，则"分解+检索+校验"是伪正交；只有证明各臂 Δ 落在不同维度（M1/M4/O6 归因到不同组件），"组合"才有意义

**空的不是"组合"本身，是"带贡献度测量的组合"**。MetaResearcher 做类似的事但没测各组件独立贡献（RL 训练把贡献混进权重梯度，拆不开）——这是 prompt 层的结构性优势：每个组件可单独开/关，消融天然干净。论文 claim 按三轴结构写，不写"我们做了 X+Y+Z"。

## 引文空间扫描（Semantic Scholar API，同日追加）

对 8 篇最接近论文爬 references + citations（S2 免费 tier 限流严重，429 反复出现；成功拿到 2606.17029/2606.02060/2609.14412/2610.33503 的引用边，其余受限）。另对 3 个新发现的邻域论文拉了 arXiv 摘要全文比对：

| 论文 | 实际做什么（读摘要后） | 与 pfb 关系修正 |
|------|----------------------|----------------|
| **Question's Gambit** (2609.14412, 2026-09) | "第一步检索"模块：把问题拆成 clues → 改写互补搜索 → 合并重排，给 agent 一个开局上下文。BrowseComp-Plus 上 gpt-5.5 答案准确率 83.1%→90.5% | **不是 cascade 分层撞车**。它优化的是"第一次搜什么"（retrieval first move），我们 idea-list #22 的 L1/L2 是"按回滚成本决定分解深度和校验强度"。相邻但正交：它是 loop 前的预处理，我们是 loop 内的资源分配。可引用为"first-move 质量重要"的外部佐证，不构成威胁 |
| **PatEx-Gym** (2610.33503, 2026-10) | 专利审查 agent benchmark：1M 专利 + 52K 论文语料，迭代搜索+文档访问+新颖性评估；核心发现"最终决策准确率不能反映审查质量"，prior-art discovery 对 frontier 模型仍很难 | **直接可用**。它的"final accuracy ≠ process quality"结论和我们 M1-M6 多维评分的动机完全同构，related work 里当外部证据用；它的 PASS 轨迹合成法（document visit 当隐式相关信号）对我们的 B-face 真实泛化题构造有借鉴价值 |
| **MetaResearcher** (2606.19893, 2026-06) | deep research agent 的 RL 训练框架：对抗虚拟环境（注入时间动态+虚假信息）→ 逼出 source credibility 评估能力；任务含 hypothesis generation 和 **contradiction resolution**；GRPO meta-reward 联合优化正确率/搜索效率/反思深度/工具多样性；Scout/Filter/Synthesizer 异构多智能体 | **最近的竞争者，要盯**。它的 contradiction resolution 任务和我们的 O6 重叠，source credibility 评估对应我们的 M6/来源分级。差异：它是**训练**（RL 改权重），我们是**测量+prompt 层**（不动权重，五级干预梯度取最低档）。这个差异本身可以写成卖点：同等能力目标下，prompt/hook 层的可审计性和回滚性优于权重修改。但它 2026-06 就提出了 contradiction resolution as task，说明"矛盾当一等公民"这个概念不再独占——我们的增量在**度量**（O6 三档判据+防泄露协议），不在概念 |

**引文空间结论**：关键词空间的"四件套组合空位"判断在引文空间依然成立——没有任何一篇同时覆盖 prompt 消融 + 信息论 rubric + 口径链 + 矛盾度量。但 MetaResearcher 提示风险升级：概念层面（矛盾解决、来源可信度）已有强工作在训，我们的叙事必须钉死在**测量学**（怎么定义、怎么打分、怎么防 judge 泄露）而不是**能力主张**（agent 能找矛盾）。

## 真正的风险点（诚实说）

1. **RubricAtlas 方向最近**。如果他们在 ACL 之后把自动 rubric 挖掘做到 expert-level 精度，我们手工 rubric 的差异化就只剩"信息论权重 + 域特化判据"（O5/O6 这类）。应对：rubric-v3 的价值主张要押在**可解释的维度设计**（每个 O 对应一个可证伪机制），不是"我们有 rubric"。
2. **"验证属于 harness"的定位正在变拥挤**。2610.34577 / 2610.00972 / GenMem (2609.34633) 都在同一句话附近。这句话本身不再 novel——novelty 必须下沉到**具体机制 + 量化证据**。
3. **decomp 本身确实不新**。GPT Researcher 的子查询递归、TreeFlex (2610.20334)、ScaffoldAgent (2606.20122) 都做了分解。我们的差异在**分解后的校验回路**，不在分解本身。论文叙事要把 claim 放在回路上。

## "怎么完整搜索未知"——方法回答

关键词命中有结构性盲区：**没人给新东西起过名字的东西搜不到**（它只能用旧词描述自己，或根本没用文字描述）。三层补法，按性价比排：

1. **引文滚雪球（最有效，本轮没做）**：从上面 8 篇最接近论文的引用列表双向爬——它们引用的前人（避免撞已发表的）+ 引用它们的人（发现同期竞争者）。arXiv API 不支持反向引用，走 Semantic Scholar API（免费 tier 100 req/5min）或 Google Scholar 手动。这一步能把"关键词空间"换成"引文空间"，覆盖那些用不同术语描述同一系统的论文。
2. **非 arXiv 渠道**：GitHub trending（agent/harness/research 标签）、HuggingFace papers 周榜、ACL/NeurIPS/ICLR 2026 accepted list（很多系统论文不进 arXiv 关键词索引但进会议目录）。competitor-survey.md 已经覆盖了 GitHub 侧，会议目录还没扫。
3. **LLM 交叉询问**：把"这 8 篇 + 我们的四件套组合"喂给 ≥2 个独立 LLM 问"你知道还有谁在做完全一样的事吗"——它们训练语料里的长尾知识能补关键词漏网。按红线走 ego-browser 通道。

**关于"增加大量搜索预算"**：我的判断是**不加量，换维度**。121 篇已经覆盖了关键词空间的头部；再加 10 组同构关键词的边际收益很低（会看到更多 CascadeFilter/手眼标定这类噪声）。真正缺的是引文空间 + 会议目录这两个正交维度，不是关键词数量。

## 自适应路由撞车扫描（2026-11-07 晚追加 · 成璐问"这种自适应是不是也有很多人做"）

**结论：是，"自适应分配 test-time compute/检索预算"已非常拥挤，但 #24（长短prompt按任务类型分域）不在它们的层面上。**

最接近的 6 篇（arXiv API 本轮查询，原始数据 `/tmp/arxiv-adaptive.json`，33→87 unique）：

| 论文 | 做什么 | 共同范式 |
|------|--------|---------|
| Learning When to Think (2608.20256) | RL 训练按难度自适应 token 预算 | 同一行为调剂量 |
| Thinking Hard, Not Smart (2608.07968) | 推理模型跨题预算分配失败（难题没多算） | 同上，且证明这是开放问题 |
| CIRCE (2610.41089) | 从约束结构预估复杂度 → 路由+预算 | 难度信号→标量预算 |
| SuCo (2606.17687) | 充分性引导的连续 CoT 长度 | 充分性信号→长度 |
| When Should Active RAG Retrieve? (2607.24010) | 预算感知的检索/不检索决策 | 效用信号→检索开关 |
| Claim-Level Reliability (2608.11994) | 按 claim 可靠性把算力从采样挪到验证 | 可靠性信号→算力再分配 |

**#24 的三个差异点**（conf 中高，待四臂实验实证）：
1. **路由对象不同**：它们调"同一行为的剂量"（token 数/采样数/检索与否）；我们换"行为本身"——事实断言型挂纪律指令集（短prompt+hook），启发型挂探索指令集（长prompt+质询）。两套 prompt 内容不同，不是调参。
2. **触发维度不同**：它们按难度/置信度/充分性路由；我们按任务类型路由（要准 vs 要新）。两轴不正交——简单题可能要新（反例搜索），复杂题可能只要一个数字。
3. **无贡献测量**：它们报端到端准确率-预算曲线；没人测路由本身的独立贡献、各指令集增益是否正交可加（= 三轴 novelty 第 3 轴）。

**对 claim 的影响**："自适应"这个词彻底不能当 novelty（2608.07968 连"模型不会省着用"都发了）。#24 的可卖点 = 指令集分域 + 任务类型触发 + 贡献独立性测量，三者叠加，不是"会自适应"。idea-list #24 的"可证伪实验"（四臂交叉对比）正好能产出第 3 轴的证据。

## 建议的下一步（按优先级）

1. 对 8 篇最接近论文跑 Semantic Scholar 引文滚雪球（~1h，外包 arena 或本地脚本）→ 更新本文件的"最接近"表
2. 扫 NeurIPS/ICLR/ACL 2026 accepted list 的 agent track → 补会议渠道
3. 论文 related work 节按"单项有人碰、组合空"的结构写，claim 押在回路机制 + 量化证据上（呼应 competitor-survey.md §L1/L2/L3 分层）