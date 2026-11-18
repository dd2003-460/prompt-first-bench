# 消融矩阵 × 前人工作重合映射（2026-11-18 夜）

> origin: ai · D 指令「这些矩阵和哪些前人工作重合（重合也索引前人论文，方便交流套磁，然后方便标记复现和创新）」
> 一句话：pfb 的分解树/falsification/rework 跟 Arbor、FALCA 高度同构（要复现+引用），但质检门/交叉验证置信度/缺口标注/S_α 目标函数/judge-dependence 实证是 pfb 独有创新（前人没有）。套磁首选 FALCA 团队（BAAI+THU+CASIA）和 Arbor 团队（RUC-NLPIR）。
> 来源标注：所有前人工作来自 `competitor-survey.md`（②类来源，工作区历史文件，2026-11-03/11-17 观察）。arXiv 编号是该文件记录的，**未在本轮独立核验**，高风险的保留 [待核验] 标记。

## 0. 怎么用这份文件（套磁 + 标记）

- **套磁**：找「做过最相关工作的人」，因为他们的 lab 最可能理解你的工作、最可能合作/引用/接收。按 §3 优先级排，先联系重合度最高的。
- **标记复现 vs 创新**：写论文 related work 时，§2 的「复现前人」组件要引用对应论文（说明你站在他们肩上），「pfb 独有创新」组件要强调差异化（说明你的贡献）。
- **诚实条款**：competitor-survey.md 是②类来源，arXiv 编号未独立核验。套磁前建议用 ego-browser 去 arXiv 核验一遍编号 + 读摘要，确认论文真实存在且内容匹配（避免套错人）。

## 1. pfb 消融组件清单（要映射的对象）

来自 `ablation-matrix-full.md` 的 A0-A13 矩阵 + S0-S5 阶段消融，pfb 的核心组件：

| # | 组件 | 对应消融因子 | 说明 |
|---|------|------------|------|
| C1 | 分解树 + edge 分类 + fanout cap | D1（分解 prompt） | cartesian/quotient 边、层级、fanout cap 8、quotient ≤20% |
| C2 | 核验三步（质询/逻辑/外部） | D2（no_challenge） | 反方质询→逻辑校验→外部核验，verified/degraded/failed 三态 |
| C3 | rework 闭环 | （状态机边） | 发现缺口→重新分解→再验证，max_rework 2、verified_rate 触发 |
| C4 | 质检门（正交性/可压缩复杂度） | D4（Q2/Q4） | 子维度正交性检查 + Jaccard 冗余惩罚 |
| C5 | 矛盾扫描 | D5（off/on） | 全局矛盾对检测 |
| C6 | 交叉验证置信度 | （L3 差异化） | 双源印证升级 conf |
| C7 | 缺口标注（留空） | （decomp KPI） | 分解+标注缺口+留空前置质检 |
| C8 | S_α 目标函数 | （收敛判据） | F_β(β=0.5) + 冗余惩罚 β=3.0 + mean+λ·std 剪枝 |
| C9 | LangGraph 状态机实现 | （基础设施） | checkpoint + rework 循环边 |
| C10 | judge-dependence 发现 | （论文核心） | 同族 vs 异族评委结论相反 |

## 2. 组件 × 前人工作映射表

| pfb 组件 | 前人工作（来源：competitor-survey.md §） | 重合度 | 复现 vs 创新 | 套磁对象 |
|---------|----------------------------------------|--------|------------|---------|
| **C1 分解树** | **Arbor**（RUC-NLPIR, arXiv:2606.11926 [待核验], §6.9.1）hypothesis tree + insight 传播；ablation 证明 w/o tree 63.64%、w/o insight feedback 54.54%（tree 和 insight 都不可或缺） | **高**（树结构同构） | 复现树结构 + **创新** edge 分类（cartesian/quotient）+ fanout cap 8 + quotient ≤20% 约束（前人没有） | **RUC-NLPIR**（Arbor 团队） |
| C1 分解树 | GPT Researcher（github.com/assafelovic/gpt-researcher, §1）deep mode = breadth×depth 递归树 | 中（检索树 vs 假设树） | 复现递归展开 + 创新「假设树 vs 检索树」的定位差异 | assafelovic（工程基线，非研究合作） |
| **C2 核验三步** | **FALCA**（BAAI+THU+CASIA, arXiv:2610.28361 [待核验], §6.5 末）Falsifier contradiction-first 找反例/查未满足约束/识别冲突；ablation w/o Falsifier -11.9（最大 drop） | **高**（falsification 同构） | 复现 falsification + **创新** 三步分离（质询/逻辑/外部）+ verified/degraded/failed 三态 + 经验事实排除条款 + 公式豁免 | **BAAI+THU+CASIA**（FALCA 团队） |
| C2 核验 | navinsreyas/research-agent（github, §1）credibility scorer：base 0.5 + authority(.edu/.gov)+0.2 + freshness+0.2 + depth+0.1 | 中（来源打分） | 复现来源权威度打分 + 创新「单源→多源印证」 | navinsreyas（小项目，9 commits） |
| **C3 rework 闭环** | **FALCA**（arXiv:2610.28361）Searcher 修订研究状态循环 | **高**（闭环同构） | 复现闭环 + **创新** 显式状态机 + max_rework 上限 + verified_rate 触发阈值 | BAAI+THU+CASIA |
| C3 rework | **Arbor**（arXiv:2606.11926）insight feedback / backpropagate（教训从子节点推到父节点） | **高**（insight 传播同构） | 复现 insight 传播 + 创新「rework 后把教训往树上推」的显式机制 | RUC-NLPIR |
| **C4 质检门** | 几乎无直接前人（competitor-survey §1 关键空白：「没有开源系统做分解+标注缺口+留空的前置质检」） | **低** | **pfb 独有创新**：正交性检查（子维度不重叠）+ Jaccard 冗余惩罚作为显式门 | 无直接对象（这是差异化卖点） |
| **C5 矛盾扫描** | FALCA（arXiv:2610.28361）Falsifier contradiction-first | 中（单节点 vs 全局） | 复现矛盾检测 + **创新** 全局扫描（非单节点）+ 矛盾对列表 | BAAI+THU+CASIA |
| **C6 交叉验证置信度** | competitor-survey §1 关键空白：「没有成熟的交叉验证置信度实现——现有 credibility scorer 全是单源打分」 | **无**（行业空白） | **pfb 独有创新**（L3 差异化）：双源印证升级 conf | navinsreyas（最接近的单源打分作者，可讨论升级路径） |
| **C7 缺口标注** | competitor-survey §1 关键空白：「没有开源系统做分解+标注缺口+留空的前置质检模块」 | **无**（行业空白） | **pfb 独有创新**：decomp 的 gap_check 维度覆盖率 + 留空 KPI | 无直接对象（差异化卖点） |
| **C8 S_α 目标函数** | 无直接前人 | **低** | **pfb 独有创新**：recall×precision 型 F_β + β=3.0 冗余惩罚 + mean+λ·std 不确定度剪枝 | 无直接对象 |
| **C9 LangGraph 状态机** | LangGraph（github.com/langchain-ai/langgraph, §6.10.1）checkpoint + retry + error handler；Orcana/Dapr/Pydantic AI（§6.10.1） | **高**（基础设施） | 复现 checkpoint 机制 + 创新「把 pfb 状态机映射成 LangGraph graph（rework 循环边）」 | LangChain 团队（基础设施，引用非合作） |
| **C10 judge-dependence** | Crucible（eren23/crucible, §6.7.2）judge separation（reward judge ≠ eval judge） | 中（都关注 judge 偏差） | 复现「judge 偏差」问题意识 + **创新** pfb 论文核心贡献：实证「评分结果依赖评委身份」（同族 +0.129 vs 异族 -0.187，方向相反） | **Crucible 作者（eren23）** |

## 3. 套磁优先级排序（按重合度 × 合作潜力）

| 优先级 | 团队/作者 | 重合组件 | 为什么值得联系 | 合作切入点 | 风险 |
|--------|----------|---------|--------------|-----------|------|
| **1** | **BAAI+THU+CASIA（FALCA）** | C2/C3/C5（falsification/rework/矛盾） | 重合度最高（falsification 是 FALCA 的主要增益来源 -11.9，跟 pfb rework 同构）；FALCA 在本地 HNSW 上跑，pfb 在开放 web 上跑（更难更真实） | 「开放 web vs 本地 HNSW」对比实验；pfb 的 rework 是 prompt 版 falsification（不需训练），FALCA 是 SFT+RL 版 | FALCA 代码未开源、需 8×H100；Falsifier 用同一 4B backbone（self-confirmation bias 风险） |
| **2** | **RUC-NLPIR（Arbor）** | C1/C3（hypothesis tree/insight 传播） | 树结构同构 + 支持本地模型（LiteLLM 接 vLLM，跟 pfb 的 27b 本地模型一致）；ablation 证明 tree + insight 都不可或缺 | edge 分类（cartesian/quotient）+ insight 传播机制对比；Arbor 的 held-out margin vs pfb 的 S_α | 项目新、社区早期 |
| **3** | **Crucible（eren23）** | C10（judge-dependence） | 都关注 judge 偏差，Crucible 用「不同模型族」解决，pfb 用「实证 judge-dependence」揭示问题 | judge-dependence 实证 + judge separation 方案对比 | 5 stars、早期项目 |
| **4** | **navinsreyas** | C2/C6（credibility scorer/交叉验证） | 唯一见到显式来源权威度打分（单源），pfb 要做双源印证升级 | 「单源→双源印证」升级路径讨论 | 9 commits 小项目 |
| **5** | LangChain 团队 | C9（LangGraph 基础设施） | pfb 用 LangGraph 做状态机，引用其 checkpoint 机制 | 引用非合作（基础设施层） | 非研究合作对象 |

## 4. 复现 vs 创新清单（写论文 related work 用）

### 复现前人（要引用对应论文，说明站在他们肩上）

| 组件 | 前人 | 引用 |
|------|------|------|
| 分解树结构 | Arbor | arXiv:2606.11926 [待核验] |
| falsification（反方质询） | FALCA | arXiv:2610.28361 [待核验] |
| rework 闭环 | FALCA + Arbor | 同上 |
| insight 传播 | Arbor | arXiv:2606.11926 [待核验] |
| 状态机 checkpoint | LangGraph | github.com/langchain-ai/langgraph |
| 来源权威度打分 | navinsreyas | github.com/navinsreyas/research-agent |
| judge 偏差问题意识 | Crucible | github.com/eren23/crucible |

### pfb 独有创新（前人没有，要强调差异化）

| 组件 | 创新点 | 为什么是创新（前人空白） |
|------|--------|------------------------|
| C1 edge 分类 | cartesian/quotient 边 + fanout cap 8 + quotient ≤20% | Arbor 的 hypothesis tree 没有 edge 分类约束 |
| C2 核验三态 | verified/degraded/failed + 经验事实排除 + 公式豁免 | FALCA 的 Falsifier 只给 verdict（reject/survive/uncertain），没有「降级定性」中间态 |
| C4 质检门 | 正交性检查 + Jaccard 冗余惩罚作为显式门 | competitor-survey §1：「没有开源系统做前置质检」 |
| C6 交叉验证置信度 | 双源印证升级 conf | competitor-survey §1：「现有 credibility scorer 全是单源打分」 |
| C7 缺口标注 | 分解+标注缺口+留空前置质检 | competitor-survey §1：「没有开源系统做分解+标注缺口+留空」 |
| C8 S_α 目标函数 | F_β + 冗余惩罚 + 不确定度剪枝 | 无直接前人 |
| C10 judge-dependence 实证 | 同族 +0.129 vs 异族 -0.187（方向相反） | Crucible 只提出「judge separation」方案，没有实证「评委身份翻转结论」 |

## 5. 来源与核验状态

- **所有前人工作来源**：`competitor-survey.md`（②类来源，工作区历史文件，2026-11-03/11-17 观察，485 行）。
- **arXiv 编号核验状态**：competitor-survey.md 记录的编号，**本轮未独立去 arXiv 核验**。高风险编号（套磁前必须核验）：
  - arXiv:2606.11926（Arbor）[待核验]
  - arXiv:2610.28361（FALCA）[待核验]
  - arXiv:2608.06714（ReASearch）[待核验]
  - arXiv:2602.22480（VeRO）[待核验]
  - arXiv:2603.28052（Meta-Harness）[待核验]
  - arXiv:2609.40330（Turbo Harness）[待核验]
  - arXiv:2605.27276（SIA-W）[待核验]
  - arXiv:2605.19156（ResearchArena）[待核验]
  - arXiv:2605.20025（AutoResearchClaw）[待核验]
- **核验动作**（套磁前做）：用 ego-browser 去 arXiv 搜编号 + 读摘要，确认论文真实存在且内容匹配。核验结果落盘本文件 §5 的核验状态列。
- **GitHub 链接**：competitor-survey.md 记录的，star 数/活跃度是 2026-11-03/11-17 观察值，可能过期。

## 6. 下一步

1. **套磁前核验**：ego-browser 去 arXiv 核验 §5 的 9 个编号（30 min），确认论文真实 + 内容匹配。
2. **套磁信**：按 §3 优先级，先写 FALCA 团队 + Arbor 团队的套磁信（强调「开放 web vs 本地 HNSW」+「prompt 版 falsification vs SFT+RL 版」的对比切入点）。
3. **论文 related work**：按 §4 组织，复现组件引用对应论文，创新组件强调差异化。
4. **标记复现/创新**：在 ablation-matrix-full.md 的每个臂标注「复现 Arbor/FALCA」或「pfb 独有创新」。
