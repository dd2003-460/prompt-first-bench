# 分解树：pfb-hardening-v2 任务规划（v3 · 状态机 + 推理激活）

> origin: ai · 2026-11-09 · 成璐指令「基于北极星详细规划 goal 任务；肯定不是拆东墙补西墙加 rule；状态机可能很关键；泛化的推理如何激活也很关键」
> 本文件是 goal-pfb-hardening-v2.md 的执行层分解。旧 Phase 1「修管线三件套」中未落地的部分被本文件取代（P4 hedging/rule 6 已落地 commit 2db5f907；rule 9b 敏感性待 v15 smoke 定去留）。

## 核心判断（先于分解）

**为什么不再加 rule**：rule 9b 的 v15 早期信号（cov 0.167/0.0/0.5 vs v14 均值 0.578）说明往 prompt 里塞强制规则会稀释基础覆盖——模型把注意力从"题目直接问的"挪到"新规则要求的"。soc rule 7 也是同构失败（point-0 命中率 54%→17%）。两个独立证据指向同一结论：**prompt 层的"行为塑造"有容量上限，继续加 rule 是负收益**。

**所以杠杆换方向**：
1. **结构**（状态机）：把"何时停、何时回退、预算给谁"从固定流程变成目标函数驱动的决策。这是 S_α 北极星的第一个工程落地。
2. **激活**（推理倾向）：模型大概率已经"懂"贝叶斯更新、最概然估计这些东西（27b 的训练语料里有），但单轮生成时没有调用的**动机和时机**。问题不是教它知识，是让它在正确的节点上调用已有的推理程序。这比加规则便宜得多——不加新内容，只改触发条件。

## 分解树

```
goal: S5 稳定超过 S0 (nat cov≥0.634, gpu depth≥0.50) → 可发表消融报告
│
├─ A. 收口在途实验（前置，~1h）
│   ├─ A1 nat-v15 smoke 6/6 跑完 → rule 9b 判决
│   │    缺口: 无（进程在跑，PID 38258，剩 ~3 rep）
│   │    判决标准: mean(cov) ≥ 0.578 → 保留; < 0.578 → 回滚（git revert d0f6228f 的 rule 部分）
│   └─ A2 T53 survey 回收（arena, ~1h）
│        缺口: arena 完成后需 fetch session 分支 + 核对 AC1-AC4
│
├─ B. 状态机重构（主押注，替代旧 Phase 2）
│   ├─ B1 设计文档: tasks/state-machine-design.md
│   │    内容: 状态图 / 转移条件 / S_α 收敛判据 / 预算分配策略 / 终止与回滚点
│   │    缺口: [待核验] ToT 的 value function 具体形式（T53 Q1/Q2 应覆盖，回来对齐）
│   │    验收: 文档含完整状态转移表 + 每个转移的量化触发条件（不允许"视情况"）
│   ├─ B2 实现 s5_state.py（新文件，不动 s5_pipeline.py 直到并行验证通过）
│   │    状态: P1_DECOMPOSE / P15_GAP / P2_SEARCH / P3_VERIFY / P4_SYNTHESIZE / EVALUATE
│   │    回退边: EVALUATE→P4（数字没进答案）/ P3→P2（空 evidence）/ P2→P1（某分支检索全空→重拆该分支）
│   │    终止: ΔS_α < ε（连续 2 轮边际增益 < 阈值）或 wall > 预算或 max_iter
│   │    验收: GPU 单 rep × 3 smoke，depth ≥ 0.50，wall < 30min/rep，无死循环（迭代轨迹落盘可审计）
│   └─ B3 消融对比: state-on vs state-off（现有线性管线）× nat 30 reps
│        口径: 同 judge 族（binary coverage + depth v13），workers=1，temp=0.7/top_p=0.95，zero-width 扰码
│        验收: state-on mean cov ≥ state-off 且 ≥ 0.634 → G3 提前达成路径成立
│
├─ C. 推理激活（第二押注，与 B 正交可并行）
│   ├─ C1 机制调研（外包 arena T54）
│   │    问题: "激活 LLM 已有但默认不调用的推理程序"有没有成熟做法？
│   │    线索（凭记忆，全部待 T54 核验）: CoT 的 step-by-step 触发效应 / self-consistency /
│   │    retrieval-augmented reasoning 的 trigger design / "reasoning activation" 类工作是否存在
│   │    产出: research/reasoning-activation-survey.md，≥5 篇 + 每条标"是否适用于 prompt 层零训练设定"
│   │    验收: 给出 ≥3 个候选激活机制，按"改动量小→大"排序，附预期风险
│   ├─ C2 最小实验: 假设性节点的条件化贝叶斯表述
│   │    动机: nat 题 p2/p3 失分集中在"参数取值不同→结果区间"类节点；模型知道贝叶斯但只在
│   │    被明确要求时才写。改法 = 不改 P1 规则，改 P3 verify 的输出 schema：当节点 claim 含
│   │    参数依赖时，evidence 字段强制要求 f(参数±Δ) 的形式（这是对输出格式的要求，不是新知识注入）
│   │    对照: nat 30 reps，C2-on vs C2-off（=当前 v14/v15 配置）
│   │    验收: p2/p3 逐点命中率提升 ≥ 0.10（v14 基线 p2=0.27, p3=0.44），且不伤 p0/p1/p4/p5
│   └─ C3 （可选，看 C1/C2 结果）self-consistency over 分解树
│        缺口: 成本 ×3，仅在 C2 不足时启用
│
├─ D. Judge/gold 校准（soc + gpu 专项，不阻塞 B/C）
│   ├─ D1 soc point-0 gold 定义放宽（之前判定 TOO NARROW）
│   │    缺口: 需要列出当前 gold 文本 vs 实际合理回答的 diff 样本 ≥ 5 例
│   └─ D2 gpu judge 复核: S0-gpu cov=0.167 是否部分源于 gold 过严
│        缺口: 抽 5 个 S0-gpu 低分 rep 人工过一遍 judge 打分合理性
│
└─ E. 论文与发布（G3 后）
     ├─ E1 跨臂矩阵: S0/A3/A4/S5-linear/S5-state × nat/soc/gpu（state 版数据来自 B3）
     ├─ E2 underdetermined 条件指标 + 统计检验（bootstrap CI）
     └─ E3 related work 写入 T51/T52/T53/T54 撞车结论
```

## 正交性核对

- B（状态机）改的是**控制流**：何时停/回退/分配预算。C（推理激活）改的是**单节点的内容质量**：给定一个节点，怎么让它产出更完整的推理。两者作用面不相交——B 的消融可以拿任意 C 版本做底座，反之亦然。
- D（judge 校准）改的是**测量仪器**，必须在 B3/E1 的最终比较前完成，否则数字不可信；但它不影响 B/C 的内部迭代（内部用旧 judge 排序即可，最后统一换）。
- A 是纯收口，无决策风险。

## 执行顺序与资源

| 序 | 任务 | 方式 | 预计耗时 | 依赖 |
|---|---|---|---|---|
| 1 | A1 v15 收口 | 本地等进程 | ~1h | 无 |
| 2 | T54 派发（C1） | arena | 派发 10min，跑 1-2h | 无（可与 A 并行） |
| 3 | B1 设计文档 | 我写（等 T53 回来后对齐 ToT 部分） | ~2h | T53 |
| 4 | C2 最小实验 | 我改 P3 schema + 跑 nat 30 | 改 1h + 跑 ~6h | A1（确定 rule 9b 去留后基线才干净） |
| 5 | B2 实现 | 我写 s5_state.py | ~半天 | B1 |
| 6 | B3 消融 | 跑 nat 30 × 2 配置 | ~12h | B2 |
| 7 | D1/D2 | 我抽样本核 | ~2h | 无，随时插空 |
| 8 | E | 视 G3 结果 | — | B3+C2+D 全过 |

**并行窗口**：T54 在 arena 跑的同时，本地做 B1 设计 + C2 改造；C2 的 30-rep 跑起来后（~6h），中间穿插 B2 实现；B3 的 12h 长跑期间做 D 校准 + 等 T53/T54 收尾。

## 退出/降级条件

- B3 显示 state-on ≤ state-off（连续 2 批）→ 状态机路线降级为"仅 P4 回退"子集，主押注转 C 线
- C2 显示 schema 约束伤基础覆盖（重蹈 rule 9b 覆辙）→ 回滚，等 T54 结果选下一个激活机制
- T53 发现 S_α 作 reward 已有强先例 → 调整论文定位（从"首次提出"改为"prompt 层实例化 + 对比"），不改变执行计划
- 8787 不可用 > 4h → 全部 run 暂停保留断点（沿用现有 recovery-check.sh）

## Decision Log
- 2026-11-09: 放弃"继续加 rule"路线（证据: rule 9b v15 早期 cov 崩 + soc rule 7 point-0 崩，两例同构）
- 2026-11-09: 主押注定为状态机（结构杠杆）+ 推理激活（内容杠杆），双押注正交并行
- 2026-11-09: C2 选"输出 schema 约束"而非"prompt 注入知识"——前者不增加模型认知负担，后者已被两次证伪