# 阶段 02：资料搜集与证据固化 — RUBRIC-V3-FULL-AUDIT / G4 漏洞对照

> goal: rubric-v3-audit-g4 · 2026-10-30
> web-llm 回执：`loop-artifacts/prompt-first/02-web-llm-cross-check.md`（ok=true, successful_provider_ids=[] —— 三 provider 全部 error，登录态失效；按任务书失败降级条款记录后继续本地证据提取，不阻塞）

## 仓库内证据固化（F1-F3）

事实源（全部只读）：
- gap-analysis Q2 原文：`git show aea3d6b:receipts/rubric-v3-gap-analysis.md` §Q2（五条 S1-S5 + ResearcherBench/RACE 补充段）
- 草案协议：`git show origin/rubric-v3:bench/rubric-v3/DRAFT-rubric-v3.md`（§0 原则 / §1 O1-O4 / §3 实验设计 / §4 候选集补丁 / §6 开放问题）
- 消融实现：`git show origin/rubric-v3:bench/rubric-v3/ablation/TASK-ablation.md` + main 冻结数据 `{hit-matrix.json, prior-estimates.json, judge-blindtest-r1.json, gold-tree.md, stats-recomputed.json, stats-w3w4.json}`
- 外部对抗核验：`git show origin/rubric-v3:receipts/adversarial-check-rubric-v3.json`（arena-agent-mode 会话，verdict=revise，32 findings：12 blocker / 16 major / 4 minor）
- 前序 loop：G1-contradiction-audit.md / g2-rootcause.md / g3-w3w4-completion.md（main）

### F1 · 口径界定落地

判定对象 = **当前可运行的完整链条**（草案协议 + 已执行消融 + 已落盘冻结数据）。规则：草案写了但从未执行的防护条款 → 按「纸面存在、实证缺失」计入，最多判「部分规避」，不得判「已规避」。

### F2 · 五条解释逐条对照（核心结果）

**S1 · 构念错配**（短答案/终态任务没有研究树构念，强加节点树测错构念）
- 我们协议的暴露面：rubric-v3 的 O3 节点命中制只对「有可构建 gold 树的长程研究任务」有效。
- 机制检查：草案 §3.1 域选择明确限定适用域（第一格 decomp 硬件域——gold 现成；第二格选「gold 需新建的域」并验证可构建性）；§5 声明 v3 从 C5 升级而来、总量纲兼容旧分。协议没有声称通用到 GAIA/SWE-bench 类终态任务。
- 执行痕迹：消融实际只在硬件域跑（8 个 C0 run），未越界套用。
- **判定：已规避**（设计层显式域限定 + 执行未越界）。限定语：第二格（新域可构建性验证）从未执行（空缺 G1：本仓无 T17 文件，adversarial-check Q6-minor 亦指出）——所以「已规避」仅覆盖第一格，跨域迁移能力未验证。

**S2 · 唯一 gold 路径偏置**（构造唯一推理树造成路径偏置、漏标、reference 依赖）
- 我们协议的暴露面：gold-tree.md 是单一 Lead 构建的唯一分解树；O3 命中制把「像 Lead 的分解习惯」当成正确性信号。
- 机制检查：
  - (a) 草案 §6 开放问题 1 的对策只有「judge 不看过程来源 + 执行环境隔离（workspace 无 gold/）」——adversarial-check Q1-blocker-2 明确指出这挡不住「rubric 作者与 gold 作者是同一人」的同源依赖，且 §4 补丁把同一套分解习惯搬进题面，使「命中 gold」与「被引导写出 gold 形状」不可区分。该 finding 未被后续修订吸收（DRAFT 仍为原状）。
  - (b) O2 规定「发现 gold 没有的新深层矛盾 = 额外加分候选（记入 gold 更新提案，**不在本次计分内**）」——砍掉了唯一抗同源的出口（adversarial-check Q1-blocker-2 fix(2) 要求把它改成正式计分项，未采纳）。
  - (c) 双 gold（第三方独立建同域 gold 报差值）建议未实施；R5.2-third-scorer（异源 judge）在 queue 中仍未完成。
  - (d) 缓解因素：gold set 本身经 r71b 冻结（G2 确认「gold set 本身不因此被判错」）+ 节点数矛盾 35→31 已修正入库——这是数据卫生层面的部分防护，但不是路径偏置防护。
- **判定：未规避**。evidence：adversarial-check-rubric-v3.json Q1-blocker-2（同源依赖 + 修复建议未采纳）；DRAFT-rubric-v3.md §1-O2「不在本次计分内」条款；tasks/goal-queue.md R5.2-third-scorer 未完成行。这是五条中最严重的一条——它直接污染 O3 的构念效度解读（G2/G3 的所有 top-5 分析都建立在单源 gold 上）。

**S3 · 细粒度标注/judge 可靠性成本**（粒度越细标注与误判表面积越大；领域 judge 可能打平差异）
- 我们协议的暴露面：p̃ 逐节点估计（31 节点 × 多 judge）+ κ≥0.6 换位双判门禁 + 逐节点 evidence ≤40 字核验。
- 机制检查：
  - (a) **草案协议 vs 实际执行的落差**：DRAFT §1-O3 先验获取协议要求「≥3 个 LLM 服务相同 prompt 盲生成分解树，按语义类统计出现频率，p̃=(k+0.5)/(N+1) 平滑」——TASK-ablation.md Step 2 实际执行的是「你（作为 judge LLM）对每个节点回答盲生成概率大概是多少」即**单 judge 主观自评**，无多模型盲生成、无语义归并统计、无平滑公式。prior-estimates.json 的 p̃ 值是单点判断不是频率估计。
  - (b) **judge 门禁执行状态 unverified**：κ≥0.6 换位双判在消融评分中未见执行回执（空缺 G3）；实际发生的「第二次意见」是 blindtest（fresh-context 同族 subagent），它是构念效度检验不是评分一致性门禁，且底座同源（G2 R4 边界声明）。
  - (c) 成本确实发生了：G1 抽检 75/248 cell 形式核验、G2 62/62 w2 复算、blindtest 全 31 节点重估——细粒度的验证成本是实付的，且暴露了真实缺陷（C1-C4、双源偏差），说明投入换到了信息。
  - (d) 「领域 judge 把差异打平」的对应物：blindtest 新 judge 的保守下界效应（G2 F2(b)：5 个低 p̃ 节点被抬到 ≥0.3）正是「judge 个体倾向压平极端值」的实例——机制存在且已被观测到，但协议层没有针对它的防护（如多 judge 取分布而非单点）。
- **判定：部分规避**。evidence：DRAFT-rubric-v3.md §1-O3 先验获取协议（纸面）vs TASK-ablation.md Step 2 W2 条目（实际执行）的差异；g2-rootcause.md F2(b) 保守下界清单；blindtest 回执无 κ 门禁记录。纸面协议是完整的（甚至超前于 survey 里多数 bench），但执行层降档为单 judge 自评——「部分规避」的准确含义：**风险被识别且有设计，但设计的防护力未经执行检验，且实际执行弱于设计**。

**S4 · 单一终点可比性 vs p̃ 数据集/版本依赖**（排行榜倾向保留跨题可比较的单一终点；节点/surprisal 权重引入 p̃ 的数据集和版本依赖）
- 我们协议的暴露面：O3 分数依赖 (i) 特定域的 gold 树 (ii) 特定模型池的 p̃ 估计 (iii) 特定 ε 截断参数——三者都不可跨域直接迁移。
- 机制检查：
  - (a) **p̃ 冻结纪律存在**：prior-estimates.json 带 `source_baseline_commit: 8ee73de` + weight_formula + epsilon 字段，p̃ 估计一次落盘后作为冻结输入消费（G1 A3 断言其只读）。这正面回应了「版本依赖」——至少在本域内 p̃ 不会漂移。
  - (b) **跨域可比性无机制**：O3 分数是域内归一化（Σw·h/Σw），跨域比较需要重建 gold 树 + 重估 p̃，协议承认这一点（§3.1 第二格要「测 gold 覆盖度在新域上的可构建性」）但没有给出任何跨域分数对齐方法。这与 S4 描述的 bench 惯例（保留单一可比较终点）相反方向——rubric-v3 主动选择了更细但更不可比的尺度。
  - (c) **O1 候选集扩展指令的域特定性**：§4 补丁的「四分区」（当代旗舰/上代主流/老马/非 GPU）是硬件域特化的，adversarial-check Q1-blocker-3 指出它还是「答案注射」（点名 ≥5 年旧卡 + 生态/成本/瓶颈三问 = gold 答案结构）。跨域复用需重写整个补丁。
  - (d) 缓解因素：草案 §0 原则 2「所有分数对比 baseline 才有意义」+ V0-baseline 变体设计——域内可比性是有保障的，牺牲的是跨域可比性，这是明示的设计取舍而非疏漏。
- **判定：部分规避**。evidence：prior-estimates.json 元数据字段（冻结纪律）；DRAFT-rubric-v3.md §0-2 / §3.1 / §4（域内 baseline 对照 + 域特定补丁）；adversarial-check Q1-blocker-3（补丁域特定 + 答案注射）。准确含义：**版本依赖被冻结纪律管控（已规避子项），跨域可比性被主动放弃且无补偿机制（未规避子项）**——整体记部分规避。

**S5 · surprisal 统计/构念风险**（稀有不等于重要、正确或有证据；需验证 p̃ 估计稳定 + 稀有节点质量相关性）
- 我们协议的暴露面：这正是 G1-G3 的主战场。gap-analysis 写这条时的措辞是前瞻警告（「即使公式被截断，也要验证 p̃ 的估计稳定和『稀有节点质量』相关性」）——现在有了实证回答。
- 机制检查（引用前序 loop，不重复推导）：
  - (a) **p̃ 估计稳定性：未通过**。同族双 judge 的 p̃ Spearman ρ=0.688（G1 S2）；|Δp̃| median 0.130 / max 0.48（N-1.1.4 0.12→0.60）；|Δw2|≥2 的节点 7 个，含 N-2.1（7.64→2.74）、N-1.3.1（7.06→2.74）、N-3.2.2（6.06→2.32）——头部权重对 judge 个体高度敏感。结构性共同偏差：N-1/N-2 零命中高估在两 judge 下同时出现（G2 F2(a)），说明盲测 fresh-context 不能消除同源模型的共享先验错误。
  - (b) **稀有≠重要：被证实为真实风险**。orig judge 下 W3 top-5 gold 计数 3/5（过线）→ new judge 1/5（否决）（G1 C4 / G2）；per-run top-5 口径下无任何 run 在任何方案下达 ≥3 gold 标记（G1 新发现）；W4 的 gold 平均排名 6.4→8.6 恶化（G3）。gap-analysis 担心的「罕见节点的高权重本身不是重要性证据」在 ablation-result.md §4 初检（2/5 < 3 门槛）和 blindtest 翻转中两次得到印证。
  - (c) 协议层的应对：ε=0.01 截顶（权重上限 ≈8，防单点 p̃→0 爆炸）+ 「p̃ 是模型发现率不是人类 prior」的命名纪律 + 消融前置（TASK-ablation.md 背景节明确要求做无权重/importance/surprisal 三对照）——这些是**事前**存在的防护；**事后**的防护（G2 三选项 O1/O2/O3 + G3 决策矩阵）是审计链补上的。
- **判定：部分规避**。evidence：G1-contradiction-audit.md §2 C1/C4 + S2 信号；g2-rootcause.md F2/F4；g3-w3w4-completion.md §F2/§F3；本阶段计算的跨 judge p̃ 分歧统计（ρ=0.688，|Δp̃| max 0.48，|Δw2|≥2 共 7 节点）。准确含义：**风险被事前识别并有截断/命名/消融三重防护（设计层已规避），但风险实际发生且规模超出防护预期（实证层未规避）**——净效果部分规避，且是五条中唯一一条「防护存在但被穿透」的。

### F3 · 交叉引用去重登记

| gap-analysis Q2 前瞻警告 | 闭环状态 | 引用 |
|--------------------------|----------|------|
| 「需验证 p̃ 估计稳定」 | 已闭环（负面）：ρ=0.688 同族相关但头部权重剧变 | G1 S2 + 本阶段 F2-S5(a) |
| 「需验证稀有节点质量相关性」 | 已闭环（负面）：top-5 gold 3/5↔1/5 翻转 | G1 C4 + G2 + G3 |
| 「与无权重/importance-only 做冻结数据消融」 | 已闭环：W0-W4 五方案消融完成 | ablation-result.md + stats-recomputed.json + stats-w3w4.json |
| 「p̃ 受模型池/prompt/语义归并影响」 | 部分闭环：模型池维度实测（同族两 judge）；prompt/语义归并维度未测（单 judge 自评无归并步骤） | G2 R4 + 本阶段 F2-S3(a) |
| adversarial-check 32 findings（同源/泄漏/机械可判/统计功效） | 未闭环：DRAFT 未修订，verdict=revise 维持 | origin/rubric-v3 receipt（G6 定稿输入） |

## 暂定结论（供 02.5 对抗核验）

1. **五条判定：S1 已规避（限第一格）/ S2 未规避 / S3 部分规避 / S4 部分规避 / S5 部分规避**。无一条「完全未规避」，但也只有一条「已规避」——gap-analysis 的结构性担忧在我们协议里大部分是真实的。
2. **最严重漏洞 = S2 同源 gold 依赖**：它不是某次实验的噪声，而是 O3 构念效度解读的系统性偏置来源；adversarial-check 已独立指出且修复建议（双 gold / 新发现计分 / 冻结顺序哈希）未采纳。
3. **「纸面协议 vs 实际执行」落差是 G4 的核心模式**：S3 的 p̃ 多模型盲生成协议、S3 的 κ 门禁、S4 的第二格验证——都是设计完整但执行降档或缺席。这个模式本身就是给 G5 的优化线索（哪些防护值得机械化强制执行）。
4. **负面预判待核**：「S1 已规避」可能是最脆弱的判定——如果第二格永远不做，「域限定」只是「只在验证过的一个域里用」，不构成对 S1 风险的真正规避而只是回避。02.5 应攻击这条。

## 仍未解决

- S2 的修复（双 gold / 异源 judge）依赖 R5.2-third-scorer + 用户决策，本轮只能登记不能闭环。
- κ 门禁执行回执缺失（空缺 G3）——无法确认评分一致性是否达标，只能标 unverified。
- adversarial-check 32 findings 的逐条处置属 G6 定稿范围，本 goal 只做 S2/S3 相关的证据引用。