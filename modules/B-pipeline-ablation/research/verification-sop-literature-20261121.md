# 验证流程 SOP 文献对标（跑/记录/分析/稳定性/客观性）

# origin: ai
# 生成: 2026-11-21 · 触发: D 问"前沿论文有展示这些验证流程吗 / 要学其 SOP 吗 / 还是师门隐性课程不披露"
# 方法: local-first（lit-survey+research 查 reproducibility/预注册 → 真缺口）→ arXiv https 查证（来源①）
# 结论: **不是隐性课程，是公开 SOP**。且有一篇几乎逐字对口。

## 0. 一句话

我们刚建的"跑/记录/分析/稳定性/客观性"五环节验证，**不是自创，是独立收敛到了公开方法论**。
前沿公开披露，甚至有论文标题就叫 "Towards Reproducible LLM Evaluation"。
真正空白的是"私有小规模 bench 的过程/深度细粒度验证"——公开 SOP 都针对大 benchmark。

## 1. 五环节 → 公开文献映射（arXiv ID 均 https 查证，来源①）

| 环节 | 公开对应物 | 论文 | 对口度 |
|---|---|---|---|
| 跑（run 可复现） | 重复实验 + temperature=0/seed 仍不确定 | 2410.03492 "Towards Reproducible LLM Evaluation" | 逐字对口 |
| 记录（record 账本） | experimental protocol / data availability | 通用工程卫生，非前沿 | 低（我们已做 1:1 对账） |
| 分析（p 值/CI） | 量化 benchmark 分数不确定性 + 预测区间 | 2410.03492 | 高 |
| 稳定性（sensitivity） | 不确定性量化（重复实验的预测区间） | 2410.03492 | 高（我们 ad-hoc trim 可升级） |
| 客观性（judge 有效性） | LLM-as-a-Judge 可靠性一整个分支 | 见下 | 高 |

### 客观性（judge 有效性）分支
- 2411.15594 "A Survey on LLM-as-a-Judge" — 可靠性/一致性/偏差的系统综述
- 2504.19076 "LLM-Evaluation Tropes" — LLM 评估何时会假阳性（self-reinforcing）
- 2602.00521 "Diagnosing Reliability of LLM-as-a-Judge via Item Response Theory" — 用 IRT 形式化诊断 judge 可靠性
- 2412.12509 "Can You Trust LLM Judgments?" — judge 可靠性
- 2610.14029 "Instance-Level Reliability of LLM-as-a-Judge" — 实例级（非聚合）可靠性

## 1b. 2410.03492 的稳定性验证在什么量级（ar5iv 全文查证，来源①）

| 维度 | 他们的量级 | 我们的量级 | 差距 |
|---|---|---|---|
| 题目数 q | Small=100 题 / Large=5760 题 | 3 题 | 33~1920× |
| 重复次数 n | 1→30 次扫描 | 10 轮/arm（固定） | 上限 3× |
| 模型数 | 6（GPT-3.5T/GPT-4o/Llama-3 70B+7B/Gemini-1.5P/Claude 3） | 1（qwen3.8-27b） | 6× |
| 收敛判据 | 预测区间宽度 <0.01 需 n=30 | 无（ad-hoc trim） | — |

- 方法本身（t 分布预测区间 x̄ ± t·s·√(1/n+1/n')，α=0.05）**与量级无关**，n=10 可直接套，
  只是 PI 宽度约为 n=30 的 √3≈1.7 倍（~0.02 量级）。
- 他们的核心发现：temperature=0+固定 seed 下 LLM 输出仍不确定，重复实验的分数均值有真实方差。
  → 直接支撑我们"10 轮/arm 不是浪费，是必要的稳定性证据"。
- 我们的 ad-hoc trim 可以升级为他们的 PI 公式（stats.py 已有 t 分布 CDF，加 ~10 行），
  但 n=10 的 PI 较宽，结论只能到"Δ 显著 > PI 宽度"级别，不能到 0.01 精度。

## 2. 要不要学其 SOP — 选择性学（性价比判断）

**学（直接对口、成本低）：**
1. **2410.03492 的不确定性量化**：用少量重复实验估计分数的**预测区间**，而非 ad-hoc trim。
   我们的敏感性分析现在是"去极端轮次看 Δ 不变"（启发式），可升级为 bootstrap CI / 重复实验预测区间。
   对口理由：它明确针对"不想跑很多次（cost）但要量化不确定性"——正是我们小样本场景。
2. **judge 可靠性设计**（2411.15594 survey）：解我们 [残留]1（judge 单族 non-IRR）。
   学它怎么把 judge 设计成 reliable（多族/IRT/实例级），而不是单族 temperature=0 就完事。

**不学（不适用）：**
- 大 benchmark 的"重复实验 N 次"成本方案——我们 3题×2臂×10轮，样本太小，重跑不经济。
  这正是 gap 所在（见 §3）。

## 3. 真正的空白（我们的差异化点）

公开 SOP 覆盖"**大 benchmark 的分数可复现性**"（2410.03492 等）。
但"**私有小规模 bench 的过程/深度细粒度评估 + 验证**"是空白：
- 公开论文评估的是"最终答案分数"，我们评估的是"推理树的过程/深度"（细粒度 rubric）。
- 公开论文样本量大（可重跑量化不确定性），我们样本小（n=10/arm，重跑不经济）→ 不确定性量化方法要降维。
- 这与我们 process-depth-eval-survey-20261121.md 的 gap 结论一致（rubric bench 与 PRM 之间的空档）。

**推论**：我们不是要"学一套现成 SOP 照搬"，而是要"把公开的不确定性量化/judge 可靠性方法，
降维适配到私有小规模过程/深度 bench"——这个适配本身可能是可发表的贡献（撞车也落盘，可套磁）。

## 4. 对当前 verification.md 的修正建议（可执行）

1. 稳定性环节：把 ad-hoc trim 补一句"对标 2410.03492 的预测区间方法，trim 是小样本下的启发式近似"。
2. 客观性环节 [残留]1：从"待异族 judge"细化为"对标 2411.15594 的 judge 可靠性设计（多族/IRT）"。
3. 新增 [gap]：私有小规模过程/深度 bench 的验证 SOP 无现成文献 → 我们的差异化贡献点。

## 5. 来源与置信度

- arXiv ID/摘要: 来源①（本轮 https 查证），conf 0.95
- "2410.03492 逐字对口"判断: 来源①摘要 + 我们场景比对，conf 0.8
- "私有小规模 bench 验证是空白": 来源②（lit-survey 缺口确认 + 本轮 arXiv 未命中小样本过程评估），conf 0.6（未穷尽全部文献，可能有个别小样本研究未查到）

## 1c. 关键实测：我们的方差来源 ≠ 2410 的方差来源（2026-11-21 实测，来源①）

**场景差异**：2410 测云端 API 模型的**采样随机性**（temp=0+seed 仍有方差）。
我们场景 = 本地 NVFP4 量化模型（Qwen3.8-27B-NVFP4）走 vLLM，多一层**推理引擎非确定性**。

**实测**（8787 端点，qwen3.8-27b-mtp，temp=0）：

| 测试 | 结果 |
|---|---|
| 短 prompt 串行 ×2 | MATCH（逐字符一致） |
| 长 prompt 串行 ×2（~2000 字符，max_tokens=2000） | MATCH |
| 长 prompt **并发 ×4**（4 线程同 prompt 同时打） | **4 个全不同**，且都 ≠ 串行 |
| 并发 ×4 重复 2 次 | 两次产生**相同的 4 输出集合**（仅顺序不同） |

**结论**：
1. 单请求 temp=0 在 vLLM 下**确定性**（串行 MATCH）——2410 的"temp=0 仍不确定"在
   我们单请求场景**不成立**。
2. **并发负载下非确定性**：continuous batching + MTP 投机解码 + NVFP4 的组合，
   使同一 prompt 在不同 batch 组合下产生不同输出。且是**确定性的一组**（batch 组合决定输出，
   非随机采样）——两次并发产生相同输出集合。
3. **T53b 轮次间方差的真正来源** = 推理引擎并发非确定性 + 基础设施故障（rc=137/143、
   watchdog 误杀、502 burst、回滚重跑）+ checkpoint resume 分叉，**不是 LLM 采样随机性**。
   证据：nat_formula 10 轮 n_nodes 51~204、final_state 混合（rework/verify/stop），
   r05/r07 是 stop 早停（树没拆完，n_nodes 仅 51/70）。

**对稳定性结论的影响**：
- 我们之前"10 轮稳定性"测的**不是** 2410 的 LLM 采样方差，而是**基础设施/并发扰动下的结论稳健性**。
- 这其实**更贴近真实部署**（本地 vLLM 必然并发），比 2410 的纯采样方差更有实践意义。
- 主结论（nat depth Δ=0.113、soc cov Δ=0.186 显著）在去极端轮次后不变 → 对这类扰动稳健。
- **但** r05/r07 等 stop 早停轮的分数被"树没拆完"污染，应视为下界而非真实能力。
  → [残留] 新增：nat_formula r05/r07（stop）分数受早停污染，Δ 若剔除后需重算。

**对 2410 量级对标的修正**：
- 2410 的"重复实验量化不确定性"在我们场景要改测**并发扰动**而非采样重复。
- 单请求确定 → 不需要 2410 那种 n=30 重复；需要的是**并发负载下的输出分布**（batch 组合空间）。
- 这本身是个 gap：公开 SOP 没覆盖"本地量化模型 + vLLM 并发非确定性"的评估方法。

## 1d. 更新文献与量化模型维度（2026-11-21 二次查证，ID 均经 abs 页面核实）

D 指出 2410 太老（2024-10）+ 我们是本地量化模型。核实结果：

| 论文 | 日期 | 对口点 |
|---|---|---|
| 2609.37294 SafeLLM4SE | 2026-09 | **2410 的直接升级**：统计评估报告规范，反对单输出/平均分/best-of-N 掩盖方差与估计不确定性 |
| 2609.07664 "Accuracy is Not Enough" | 2026-09 | **量化模型保真度**：zero-shot accuracy 对量化不敏感（argmax 不变≠分布不变），需分布敏感指标（divergence）对比 BF16 基模 |
| 2609.19524 Unified Trustworthy Eval | 2026-09 | 输出级/轨迹级/跨模态三层评估，8 维可信度 |

**量化模型维度——已关闭（2026-11-21，D 指令：不需保真度实验，文献背书即可）**：

关闭论证（两条独立证据）：
1. **共同因素抵消**（设计层面）：T53b 是同一量化模型（NVFP4）上的双臂消融（formula vs text prompt）。
   量化分布偏移同时打在两个臂上，Δ 中被抵消。唯一残余风险 = 量化×臂类型交互
   （量化对 formula 和 text 影响不同）——无先验理由认为存在，且若存在应表现为两臂都变差而非方向性偏移。
2. **文献背书**（2610.27913 ACE-Compression，2026-10-20，ar5iv 全文核实）：35+ 压缩 checkpoint × 6 开源 LLM，
   四能力维度之一即 **procedural reasoning and constraint execution**（= 我们测的推理树过程/深度）：
   - "4-bit quantization stays close to the FP16 parent on both prompt-level and instruction-level views"
   - "Quantization is generally more resilient to ability degradation than pruning"
   - Qwen2.5-7B BnB-4bit 甚至略超 FP16（0.7209 vs 0.7172 prompt-level strict）
   → 4-bit 量化在程序性推理维度上 ≈ FP16，不构成 T53b 的方差来源。

诚实 caveat（写入 verification.md 局限节，不阻塞）：
- ACE 测的是 INT4（BnB/AWQ/GPTQ），我们是 NVFP4（4-bit 浮点，块级浮点 scale，通常保真度 ≥ INT4）——
  同属 4-bit 类，方向一致，非逐字匹配。
- ACE 发现压缩"redistributes ability profile"（非均匀）+ 细粒度能力更不稳定——我们的 rubric 打分
  属细粒度维度，残余风险存在但被共同因素抵消论证覆盖。
- 2609.07664 "Accuracy is Not Enough" 提醒 accuracy 类指标对量化不敏感——我们 coverage/depth 是
  rubric 打分非 argmax accuracy，对该问题部分免疫。

结论：T53b 方差来源清单 = 并发非确定性（实测）+ 基础设施故障（实测）+ checkpoint resume 分叉（实测）。
**量化保真度从清单移除**（文献+设计双重关闭）。

**ID 核实教训**：arXiv API 的 entry 解析（非贪婪 regex 跨 entry）会错位——本轮 2610.01058/2610.00656 两个 ID
均错位（实际分别是 MOMAT 越狱防御 / Lingtai）。所有 ID 必须经 arxiv.org/abs/<id> 页面标题核实后才可引用。
