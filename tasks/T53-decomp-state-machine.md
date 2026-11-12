# T53 — 目标函数驱动的 decomp 状态机重构 + deepresearch 泛化 bench

> origin: ai (成璐 2026-11-09 指令立项)
> 状态：decomp 完成，待 arena 派发
> 关联：v17 Goodhart 诊断 (d5bb7d06)、T-PR-15 (文字目标函数 hack 调研, 进行中)

## 硬约束（写两遍，不可违反）

### 严禁泄漏（第一遍）

**状态机任何位置不得泄漏题目本身。** 具体含义：
- 所有 LLM prompt 中不出现题目原文（只传结构化参数：父节点 claim + 层级 + 已确认事实列表）
- 所有日志 / 中间产物 / JSON 输出中不包含题目文本
- 防泄漏 SOP 索引 → `research/sm-leak-sop.md`（审计方法 + 实体提取策略 + 误报处理）

### 严禁泄漏（第二遍 · 强调）

再重复一次：**严禁状态机任何地方泄漏题目本身。** 这不是"尽量不泄漏"，是硬门禁——leak_check() 命中即 raise LeakError 中止整轮运行。评估泄漏的 SOP 见 `research/sm-leak-sop.md`（含：怎么提取题目实体、什么算泄漏什么不算、误报怎么处理、每轮审计的执行时机）。

### 验收标准：打赢 SOTA（第一遍）

**在大部分 bench（至少 5 个 deepresearch 相关题）上打赢最新开源 SOTA 基准。** 具体含义：
- 选 ≥5 道 deepresearch 类问题（多跳推理 + 事实检索混合）
- 对照基线包含当前最新开源 deepresearch agent 的公开结果（如 GPT-4o-based DeepResearch、OpenAI o3-pro 等 [待核验具体哪个版本]）
- 状态机最终答案质量（judge 分）≥ SOTA 基线在同等题目上的分数
- 口径：异族 judge (B-face 7b) 打分 0-1，数字正确 0.5 + 对比/单位正确 0.5，n=3 median

### 验收标准：打赢 SOTA（第二遍 · 强调）

再重复一次：**验收标准是在大部分 bench（至少 5 个）打赢最新开源 SOTA 相关基准。** 不是"超过朴素 CoT"，不是"节点数更少"——是最终答案质量打赢 SOTA。如果打不赢，说明状态机的分解+核验+返工循环没有产生足够的质量增益，需要回去改目标函数设计。SOTA 对标清单和 judge 口径详见 `research/sm-bench-sota-criteria.md`。

## 背景（为什么做）

v17 暴露的问题链：S_α = Σₙ[n·ln(kₙ)+α·kₙ·ln(n)] 对节点数单调增、不罚冗余 → 模型制造同义变体刷分（1930 节点 / GPU 单题，真实正交维度仅 6-8）。根因不是模型没读懂，是**目标函数设计缺陷**。成璐的判断："按照目标函数这个思路去改出我想要的 decomp 状态机"——即把"该不该拆/该不该停/该不该返工"全部变成可机器裁决的目标函数判断，而不是靠 LLM 自觉或 R1 这种弱判据。

## 分解树（正交子项）

### A. 状态机核心设计（本地 Lead 做，需要读现有代码）

| 子项 | 内容 | 缺口标注 |
|------|------|----------|
| A1 | 定义状态集合：{IDLE, DECOMPOSE, VERIFY, REWORK, STOP} + 状态转移条件 | [待设计] 每个转移的目标函数是什么？ |
| A2 | 拆解目标函数 J_decomp：边际信息增益（不是节点数）作为继续拆的判据 | [待核验] 怎么算"边际信息增益"的可计算代理？候选：新节点与已有节点的语义距离中位数 < 阈值 → 停 |
| A3 | 核验目标函数 J_verify：已核验比例 × 证据强度加权，低于阈值 → 触发返工 | [待设计] 证据强度怎么量化？（URL 可达性 / 数字一致性 / 多源交叉） |
| A4 | 返工循环：VERIFY 失败 → REWORK（重新拆解该父节点，换角度）→ 再 VERIFY，最多 K 次 | [待设计] K 取多少？返工时 prompt 怎么带"上次失败原因"而不泄漏题目？ |
| A5 | 停止目标函数 J_stop：全局收敛判据（J_decomp 连续 M 轮 < ε 且 J_verify ≥ θ） | [待设计] ε/θ 取值需 bench 标定 |
| A6 | **防泄漏约束**：状态机所有 prompt / 日志 / 中间产物不得包含题目原文 | [关键] 需要审计机制：每轮输出 grep 题目关键实体，命中即报错中止 |
| A7 | S_α 修正版：加冗余惩罚项（如 -β·redundancy_score），保留层级结构奖励 | [待设计] redundancy_score 怎么算（embedding 相似度 / n-gram 重叠） |

### B. 实现（本地 Lead 做，改 s5_hierarchy.py 或新建 s5_sm.py）

| 子项 | 内容 | 缺口 |
|------|------|------|
| B1 | 新建 `s5_state_machine.py`（不动 v17 原文件，留对照） | 状态机类 + 目标函数模块 |
| B2 | 接入现有 search_node / verify_node / call_llm | 工具全给：search + verify + gap_check |
| B3 | 防泄漏审计钩子：每轮 decompose/verify 输出后跑 leak_check() | [待设计] 题目实体提取方法（简单：取题目中 >4 字的中文词 + 英文专名） |
| B4 | 单题 smoke test（GPU 题）：对比 v17 的 1930 节点 vs 新状态机的节点数 + 正交维度数 | 预期：节点数大幅下降（几十~百级），正交维度保持 6-8 |

### C. 泛化 bench（deepresearch 相关）

| 子项 | 内容 | 缺口 |
|------|------|------|
| C1 | 选 5-10 个 deepresearch 类问题（多跳推理 + 事实检索混合） | [待核验] 用哪些题？候选：HotpotQA hard / 2WikiMultihop / 自拟 |
| C2 | 跑状态机 on 每题，记录：节点数 / 轮数 / 核验通过率 / 返工次数 / 最终答案质量 | 答案质量怎么评？[待设计] 异族 judge (B-face 7b) 打分 or 人工抽检 |
| C3 | 对照基线：(a) v17 无限预算 (b) 朴素 CoT 无分解 (c) 固定深度 3 层分解 | 三个基线都要跑 |
| C4 | 汇总报告：节点效率（有效维度/总节点）、防泄漏通过率、核验覆盖率 | 落盘 `experiments/stage-ablation/runs/s5-sm-bench-report.md` |

### D. SOP + 错误路径 + goal 索引（成璐明确要求）

| 子项 | 内容 |
|------|------|
| D1 | 所有错误路径文档化：`research/sm-error-paths.md`（每种失败模式 + 触发条件 + 处理） |
| D2 | 修改路径记录：`research/sm-modification-log.md`（每次改目标函数/状态转移的原因 + 前后对比） |
| D3 | 思考 SOP：`research/sm-thinking-sop.md`（设计决策的推理过程，为什么选这个目标函数而不是那个） |
| D4 | goal 内留索引：本文件顶部 + goal JSON 里指向 A-D 四块的关键文件 |
| D5 | idea 检索入口：`lit-survey/IDEA-INDEX.md`（33 条 idea 全量登记，含提出时间/业内完成度标记/落点地址；T53 相关 = #9,#10,#30-33） |

## 验收标准（AC）

1. **AC1 节点效率**：GPU 单题新状态机节点数 ≤ 200（v17 是 1930），正交维度 ≥ 6
2. **AC2 防泄漏**：bench 全程 leak_check 零命中（任何轮次输出含题目实体 → 自动 fail）。SOP: `research/sm-leak-sop.md`
3. **AC3 核验覆盖**：≥ 90% 的 search 节点有 verified/degraded 状态（非空 evidence）
4. **AC4 打赢 SOTA**：≥5 道 deepresearch 题上，状态机答案质量（judge 分）≥ 最新开源 SOTA 基准分数。SOTA 对标: `research/sm-bench-sota-criteria.md`
5. **AC5 返工生效**：至少 1 道题触发了 REWORK 且返工后核验通过（证明循环真的在工作）
6. **AC6 SOP 落盘**：D1-D3 + sm-leak-sop + sm-bench-sota-criteria 五个文件存在且非空
7. **AC7 可复现**：bench 脚本一键跑通，seed 固定，结果可重放

## 缺口清单（汇总）

| # | 子项 | 缺什么 | 类型 |
|---|------|--------|------|
| G1 | A2 J_decomp | "边际信息增益"的可计算代理未定（候选：embedding 距离中位数 / n-gram 重叠率） | [待核验] 需实验标定阈值 |
| G2 | A3 J_verify | 证据强度量化方法未定（URL 可达 / 数字一致 / 多源交叉，权重？） | [待设计] |
| G3 | A5 J_stop | ε/θ 取值无先验，需 bench 数据回标 | [待核验] |
| G4 | C1 bench 题目 | 具体用哪 5-10 道 deepresearch 题未选 | [待核验] HotpotQA hard vs 2WikiMultihop vs 自拟 |
| G5 | C2 答案质量评判 | judge 方案未定（B-face 7b 打分 or 人工抽检 or 两者结合） | [待设计] |
| G6 | B3 防泄漏审计 | 题目实体提取方法粗糙（>4字中文词+英文专名），可能漏检或误报 | [待设计] |
| G7 | A4 返工 K 值 | REWORK 最大次数未定（K=2? K=3?） | [待核验] 需 smoke test 观察 |
| G8 | 正交完备度量 | S_α' 无正交性项：数值变化可伪装成正交扩展（Decision 15）；概念级独立性度量选型未定（LLM-judge vs embedding） | [待设计] r9 基线出来后 A/B 标定 |

## 执行安排

- **A+B 本地做**（Lead）：需要读现有代码、改 Python、跑 smoke test。不外包。
- **C 部分外包 arena**：bench 的"跑 + 记录"可以 arena 代劳（它有执行层），但状态机代码本身本地改完再给它跑。
- **D 本地做**：文档类。

## E. 自写目标函数 + 方差感知（成璐 2026-11-12 追问 · 新增正交子项）

> 触发：成璐指出"目标函数看起来确实可以激活，但我们几乎是拍脑袋随机赶着 AI"，并问"让他自己写目标函数、优化啥的怎么样了，他可以准确度量信息并且考虑 var 这种问题吗"。

### 代码审计结论（来源①，2026-11-12 grep s5_state_machine.py）

| 事实 | 证据 | 含义 |
|------|------|------|
| Decision 19 的 `objective`（Final_Score 公式）**不进任何决策回路** | line 390/426/603/966/1008/1032 只读/写/打印/落盘；`_verify_batch`/`classify_edge`/`marginal_gain` 全不读它 | 目标函数现在是**装饰品**——模型 r1 自估一个公式，但不驱动 decompose/verify/stop |
| 真正驱动展开的是两个拍脑袋阈值 | `gain_threshold=0.50`（n-gram Jaccard 边际增益, line 105）、`contribution_threshold=0.10`（line 118） | "拍脑袋随机赶着 AI"精确命中这里 |
| `contribution` 是 LLM **单次调用 temperature=0.0 的点值** | classify_edge line 255/274，无多次采样 | **没有任何 variance/方差度量**——全文件搜不到 std/variance/多采样逻辑 |
| "var" 仅以 `high_var` 布尔 flag 存在 | prompt line 233/246，剪枝豁免 line 716 | 定性二元（防黑天鹅被剪），**非数值不确定性传播** |

### 已有调研基础（来源②，research/longterm-vision-survey.md）

- Q4 判决 conf 0.7：Eureka[2310.12931]/Text2Reward[2309.11489]/OptiMUS[2310.06116]/OMNI-EPIC[2405.15568] 全是 **task-specific** 目标生成器，**跨任务泛化的元目标学习器未见**。
- OP2 双层可辨识性（外层学目标形式/参数 α，内层优化行为）是理论框架；IRL 病态性是负面基线（无真值时反推目标不可辨识）。
- 里程碑 M1（6mo）= S_α 单形式 α 自动定参 = "元目标"最小可运行版。

### 正交子项（E 块）

| 子项 | 内容 | 缺口标注 |
|------|------|----------|
| E1 | **让 objective 进决策回路**：把 Decision 19 自估公式从装饰品变成 classify_edge/marginal_gain 的实际输入 | [待设计] 怎么把 Final_Score 分解成 per-edge 的 contribution 权重？现在 contribution 是独立 LLM 调用，和 objective 脱节 |
| E2 | **contribution 加方差**：同一 edge 多次采样（temp>0, n≥5）取 mean±std，剪枝判据改成 `mean - λ·std < threshold`（不确定就保留，防误剪） | [待核验] n 取多少、λ 怎么标定、成本 ×n 是否可接受（当前每 edge 一次 LLM 调用） |
| E3 | **self-written objective 的 grounding**：模型自估的 Final_Score 公式本身没有验证——谁保证它不是乱写的？需要 gold 题反向校验（用已知答案的题检验公式是否区分优劣） | [待核验] 跨任务泛化元目标学习器是否真的未见（survey 说未见，需 arena 交叉核验 2025-2026 最新） |
| E4 | **var-aware 停止判据**：J_stop 现在只看 gain 均值连续 M 轮 < ε，应改成考虑 gain 的方差（方差大 = 还在探索，不该停） | [待设计] 与 E2 共享采样机制 |
| E5 | **idea 生成视角**：成璐提"原生涌现很适合跑 idea"——decomp 状态机的涌现结构（frontier 扩展 + contribution 排序）能否当 idea 生成器？目标函数自优化 = 自动发现哪些维度组合有信息量 | [待设计] 这是新方向，先落 candidate 不立项 |

### 验收标准（E 块）

- **EA1**：objective 进入 classify_edge 回路后，GPU 单题节点数相比"objective 装饰"版本有可测变化（证明它真的在驱动，不是摆设）。
- **EA2**：contribution 加方差后，drb-2 那批"all 5 failed" degraded 节点的剪枝决策更稳（方差大的保留率上升，误剪率下降）。
- **EA3**：self-written objective 通过 ≥1 道 gold 题的反向校验（公式对已知优劣的答案给出正确排序）。

## 当前进度

- [x] decomp 分解树（本文件）
- [x] E 块：自写目标函数 + 方差感知 decomp（2026-11-12，含代码审计 + 调研基础 + 5 子项 + EA1-EA3）
- [ ] E 块 arena 交叉核验（E3：跨任务泛化元目标学习器现状 + var-aware objective 最新工作）
- [ ] A1-A7 状态机设计（下一步）
- [ ] B1-B4 实现 + smoke
- [ ] C1-C4 bench
- [ ] D1-D4 SOP
## E 块落地状态（2026-11-12 更新 · 来源①本轮 grep s5_state_machine.py）

**D 的问题"不知道放哪里怎么加入"——答案：E2/E4 的代码已经写进主循环了，只是没开开关。**

| 子项 | 代码现状 | 证据（line） | 剩余工作 |
|------|----------|--------------|----------|
| E2 contribution 方差 | `classify_edge_var`（多采样 mean±std + λ·std 保守剪枝判据）**已实现且已接线**：L1 frontier 处 `use_var = contrib_samples > 1` 分支调用它，剪枝用 `mean + λ·std < θ`（乐观估计不够才剪，防误剪） | L285-337 函数体；L768-789 调用+判据；config L119-121（contrib_samples=1, contrib_temperature=0.0, lambda_uncertainty=1.0） | **只差标定**：n 取几、temp 取多少、λ 怎么定——这是网页 LLM 校准三问的第一个对象。成本 ×n（当前 n=1 零开销退化） |
| E4 var-aware J_stop | `stop_std_max=0.15` **已接线**：gain 窗口 std > 阈值 → reset low_gain_streak（还在探索不计数停止） | config L121；J_stop 段 ~L897 | 同上，并入同一轮校准 |
| E1 objective 进回路 | **仍是装饰品**（未动）：Decision 19 的自估公式只落盘/打印，classify_edge/marginal_gain 都不读它 | L482-492（写入）、L661/L1085/L1109（落盘） | 待设计：把 Final_Score 分解成 per-edge 权重喂给 classify_edge。survey §5.5 M1（α 自动定参）是它的远期形态，近期最小版 = objective.factors 的文本注入 classify_edge prompt |
| E3 objective grounding | 未动 | — | gold 题反向校验脚本（EA3）；arena 交叉核验 deferred 到 T-PR-15 后 |
| E5 idea 生成视角 | 未动 | — | 保持 candidate，不立项 |

### 接入路径（回答"怎么加入"）

1. **现在就能开的**：`contrib_samples=3, contrib_temperature=0.3`（或校准后的值）→ E2/E4 全链路激活，每 edge 3 次 LLM 调用。gpu run（pid 11150）跑完后用它重跑一题做 EA1/EA2 对照（同题对比 n=1 vs n=3 的节点数/剪枝分布）。
2. **理论指导从哪来**：这就是 L15 闭环协议 Step 3 的校准三问对象——(a) "单点 temp=0 估计 + 固定阈值 0.10 剪枝，理论上缺什么？" (b) "标准做法是什么（cite: LLM self-consistency / test-time compute 文献）？" (c) "最小修改 + 预期失效模式？" ego-browser ≥2 源，落 calibration-log.md，commit 引用条目号。
3. **E1 是下一个台阶**：objective 从装饰品变驱动，先做文本注入版（factors 进 prompt），验证 EA1（节点数可测变化），再考虑数值分解版。

### 与 survey 的对齐

survey §5.3 三个缺口里，我们现在的位置 = 缺口 2 的最小实例（无真值闭环下的目标质量评估 → pfb 用 judge/gold 覆盖率兜底，现成基建）。M1 里程碑（S_α α 自动定参）的前置就是 E1+E2 落地。
