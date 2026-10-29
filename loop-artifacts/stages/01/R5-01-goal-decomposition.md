# 阶段 01：目标分解 — R5 独立 judge 盲测（W3 构念效度跨 judge 验证）

> origin: ai · 2026-10-30 · 执行通道 = Claude Code ralph loop（任务书 `tasks/R5-judge-blindtest-task-brief.md`，main d22b5fb）
> 本阶段只做因素分解与空缺识别，不估 p̃、不算权重。

## 1. 目标交付物

| # | 交付物 | 落点 |
|---|--------|------|
| D1 | 31 节点独立 p̃ + w2 + rationale（盲估，不看 prior-estimates.json 数值） | `bench/rubric-v3/ablation/judge-blindtest-r1.json` |
| D2 | W3 top-5 节点清单（按 w1×w2 降序前 5） | 同文件 `w3_top5` |
| D3 | 构念效度判定 construct_validity_pass（top-5 中 ≥3 个带 gold 标记 → true） | 同文件字段 |
| D4 | 跨 judge Spearman ρ（本 judge p̃ vs 原 judge p̃，31 节点口径） | 回执 + 04 工件 |
| D5 | 全部锚点清单（gold 标记节点全集 + 各方案 top-5 对照） | 回执 + 04.5 工件 |
| D6 | 六阶段 loop 工件全量落盘 + commit + push 到分支 + ls-remote 记录 | `loop-artifacts/stages/<N>/` + receipts |

## 2. 影响因素正交分解

### F1 盲估输入面（决定 p̃ 合法性）
- **F1a 允许看**：节点文本（名称+公式行）、父节点上下文（父的文本与子拆分集合的存在性）、gold 标注的**存在性**（■瓶颈/★订正 符号在不在该节点上）。
- **F1b 禁止看**：prior-estimates.json 的任何数值（p̃/w1/w2/reason 文本）、stats-recomputed.json / stats-w3w4.json 的具体分数、ablation-result.md 里原 judge 的估计叙述。
- **F1c 灰色地带裁定**（本阶段冻结，防后续漂移）：
  - gold-tree.md 里的 SHARE 份额数字 → **可看**（w1 从 hit-matrix/gold-tree 推导是任务书明示允许的；且 SHARE 不是"原 judge 估计值"）。
  - gold-tree.md 里的 BOUND 倍数（如 8.00x、2.2x）、黑盒编号（B2/B5/B6…）→ **可看**（属节点文本的一部分，描述节点性质，非 judge 先验）。
  - runs-C0-run*.md 的命中情况（hit-matrix 已固化）→ **可看**（用于理解"哪些拆分模型实际想到了"，但注意：hit 率高 ≠ p̃ 高，p̃ 是先验不是后验；只作辅助信号，rationale 里须区分）。
  - prompt-V0.txt 题面 → **可看**（父上下文的上游，定义"无 gold 的 LLM"面对的原始问题）。
  - 原 judge 的 reason 文本 → **禁止**（等于间接泄露其 p̃ 判断依据）。

### F2 估计方法（决定 p̃ 质量）
- **F2a p̃ 语义**：一个没见过 gold 的 LLM，在**父节点上下文**下盲生成该层子拆分时，提出"这一刀"的先验概率 ∈ (0,1]。
  - 关键操作化：p̃ 是**条件于父上下文的单刀概率**，不是"31 节点树整体被生成的联合概率"。同一父下的多个子拆分各自独立估。
  - 根节点 N-0：无父上下文。原 judge 政策 = p̃=null、w2=1（中性）。本 judge **沿用同政策**（否则两 judge 口径不可比，Spearman 会混入口径差异）。
- **F2b 估计锚点**（每个节点必须走一遍的思维程序）：
  1. 站在父节点语境下问："一个通用 LLM 做这个分解，第一反应会切哪几刀？"
  2. 该节点对应的"那一刀"在第一反应集合里吗？→ 在则 p̃ 高（0.4–0.7），边缘则中（0.15–0.4），需要领域洞察/反直觉才想到则低（0.01–0.15）。
  3. 用 hit-matrix 做 sanity check：8 run 里 h=1 的比例若为 0/8，说明连真实模型都没想到 → p̃ 应偏低（但不强制 <0.1，因为 p̃ 是先验）；若 8/8，说明极常见 → p̃ 偏高。
  4. 写一句话 rationale：为什么容易/不容易想到这一刀（机制层面，不引用任何原 judge 措辞）。
- **F2c 失败降级**：某节点无法估计 → p̃=null + rationale 写原因，不虚构。null >10 个 → 回执标 blocked 停。

### F3 计算链（决定 W3 与 ρ 的正确性）
- **F3a w2 公式**：w2_v = 1 + min(−log₂ p̃_v, log₂(1/0.01))，ε=0.01，封顶 8。p̃=null → w2=1（中性，同原 judge root_policy 推广）。
- **F3b w1 来源**：从 gold-tree.md 的 SHARE 份额映射（TASK-ablation Step 2 规则：父 SHARE≥0.25 → w≈2；0.1–0.25 → ≈1.5；<0.1 → ≈1.2；根下直接子节点父 SHARE=1.0 → w=5）。**复用原 judge 的 parent_share→w1 映射表**（这是确定性规则输出，不是主观估计，复用以保持 W3 可比；映射本身在 prior-estimates.json 里可见，但它是规则派生值——本阶段裁定：允许读 w1 列，禁止读 p_tilde/w2/reason 列）。
- **F3c W3**：W3_v = w1_v × w2_v（乘法组合，r70c 定义）。
- **F3d Spearman ρ**：对 31 节点（含 N-0 双 null 的处理：剔除 N-0，n=30 配对）计算本 judge p̃ 序列与原 judge p̃ 序列的 Spearman 秩相关。ρ<0.6 → 结论标"prior 不稳定，W3 不可信"。
- **F3e 验收门槛**：31 节点全有 p̃+rationale（或合规 null）；W3 top-5 中 ≥3 个 gold 标记 → pass=true。

### F4 锚点定义（决定构念效度计数）
- **F4a gold 标记集（严格口径，r71b 已冻结）**：{N-2.1 ■瓶颈#1, N-3.2.2 ★2倍分歧, N-2 ★F-B订正, N-4 ■瓶颈#2, N-1.3 ★F-C订正}，共 5 节点。
- **F4b 窄口径（§4 三节点）**：{N-2.1, N-3.2.2, N-2}。两口径都报，主判定用严格口径（r71b 结论：两口径下四方案计数一致，严格口径更稳健）。
- **F4c 锚点清单（D5）内容**：gold 标记集 + 本 judge W3 top-5 + 原 judge W3 top-5（来自 stats-w3w4.json，属结果数据非 p̃ 估计，允许引用）+ 逐节点命中对照。

### F5 流程合规（决定任务是否被 Lead 接受）
- 六阶段工件逐一落盘 `loop-artifacts/stages/<N>/`，命名 `R5-*` 前缀防与旧工件混淆。
- 每阶段结束跑 `ralph prompt-first review .`（Stop Hook 自动；手动补跑亦可），revise 则修复再审。
- 完成后 commit + push 到本分支 `r73-judge-blindtest-r1`，`git ls-remote` 输出写入 receipts。

## 3. 已知条件（人类已提供 / 项目可推导）

| 条件 | 来源 |
|------|------|
| 31 节点 ID 全集 + 父子结构 | gold-tree.md（main 分支） |
| hit-matrix 8×31 命中 | hit-matrix.json（r69 产出，已核验） |
| w1 映射规则 + 原 judge w1 值 | TASK-ablation.md Step 2 + prior-estimates.json w1 列（规则派生，F1c 裁定可用） |
| w2/W3 公式与 ε | 任务书 §3 + bench.md O3 节 |
| gold 标记集两口径 | stats-w3w4.json construct_validity + r71b 复核 |
| 原 judge W3 top-5 = [N-3.2.2, N-3.2.4, N-2.1, N-2, N-1.1.3]（3/5 过线） | stats-w3w4.json（结果数据，仅用于 D5 对照） |
| 本 judge 身份 = Claude Code 会话内模型（qwen3.8-27b 运行时标识），与原 judge（arena 侧 LLM）不同家族 | 环境事实 |

## 4. 空缺条件（仍需研究/待验证）

| # | 空缺 | 阻塞什么 | 02 阶段动作 |
|---|------|---------|------------|
| G1 | 31 节点各自的 p̃ 值 | D1/D2/D3 全部 | 03/04 逐节点盲估（本任务核心工作，非外部资料搜集） |
| G2 | 原 judge 的完整 p̃ 序列（31 节点） | D4 Spearman | 02 阶段读取 prior-estimates.json p_tilde 列（**此读取发生在盲估完成之后**，顺序即隔离机制） |
| G3 | 本 judge 模型名精确字符串 | D1 `judge` 字段 | 02 阶段确认运行时模型标识 |
| G4 | ralph review CLI 在本环境的可用性 | F5 门禁 | 02 阶段试跑一次 `ralph prompt-first review .` 探测 |
| G5 | 分支推送权限（push 到 dd2003-460/prompt-first-bench） | D6 | 02 阶段 `git ls-remote` 探测 |

## 5. 边界与不做的事

- 不改 gold tree、hit-matrix、runs 文件（TASK-ablation 约束继承）。
- 不重判 hit-matrix（那是 r69 已完成且 r70b 复算核验过的数据）。
- 不重新设计权重公式（W3=w1×w2 是 r70c 冻结的候选，本任务只验证它）。
- 不把本 judge 的 p̃ 回写 prior-estimates.json（新文件 judge-blindtest-r1.json，原文件不动）。

## 6. 阶段 02 第一批行动

1. 读 prompt-V0.txt（父上下文上游）+ gold-tree.md 全文（节点文本面）。
2. 探测 G3/G4/G5（模型标识、ralph review、ls-remote 权限）。
3. **盲估窗口开启**：在读取 prior-estimates.json p_tilde 列之前，完成 03 行动分解 + 04 的 31 节点 p̃ 估计（顺序纪律是本任务的核心合规点）。
4. 盲估完成后才读 prior-estimates.json 取原 judge p̃ 序列，算 Spearman。