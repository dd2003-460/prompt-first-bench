# CJ-RUBRIC-ALIGN — 目标分解（阶段 01）

> origin: ai · 2026-11-04 · goal CJ-RUBRIC-ALIGN stage 01-create-goal

## 0. 任务元信息

| 字段 | 值 |
|------|-----|
| 任务名 | Cross-judge rubric 对齐：统一本地判官与异源判官 M1 评分口径 |
| 发起时间 | 2026-11-04 |
| 产出形态 | 代码（修 cross_judge.py JUDGE_PROMPT）+ 数据（重跑 90 cell 分数）+ 报告（对齐前后对比） |
| 对标物 | pfb bench/rubric-v3/（M4 独立源操作化定义，同仓库已有判据条款化先例） |

## 1. 本地背景扫描

| 必查项 | 查了吗 | 搜索命令/路径 | 发现 |
|--------|--------|---------------|------|
| 相关项目目录 | ✅ | `ls pfb/experiments/stage-ablation/` + `find . -name "*judge*"` | cross_judge.py（本地判官）、arena-judge-results.jsonl（90 行）、bench/rubric-v3/（M4 判据条款化先例 D1-D5） |
| 已有调研/报告 | ✅ | `cat runs/cross-judge-status.md` | n=90 完整分析已落盘：mean\|Δ\|=0.277, ρ=0.188；根因=rubric mismatch（zero-fact 规则 + 粒度）；两修复选项已列出待裁定 |
| 相关记忆 | ✅ | MEMORY.md "advance: payload..." 条 + session compacted summary | arena 回执门禁规则已知；cross-judge 结论已入 memory（rubric mismatch 非事实分歧） |
| 用户过往讨论 | ✅ | compacted context "Key Decisions" 节 | 成璐已知两选项（① zero-fact 触发条件 ② 断言粒度），尚未裁定选哪个 |

**小结**：本地已有 4 项资产（90 行 arena 分数、本地 scoring.md、cross-judge-status.md 分析、rubric-v3 判据条款化先例）。可复用全部，需新增 = 修改后的 JUDGE_PROMPT + 重跑脚本 + 对齐验证报告。

## 2. 调研对象全集

| 候选 | 纳入/排除 | 理由 |
|------|-----------|------|
| 本地 JUDGE_PROMPT（cross_judge.py L29-45） | **纳入** | 分歧直接来源："无可验证事实断言→M1=0" + 未指定断言粒度 |
| Arena 盲判 prompt（arena agent 自定） | **纳入** | 异源基准：key-assertion 4-12/cell，无 zero-fact 规则 |
| Perplexity 原子断言口径（13-40/cell） | **纳入** | 第三参考系：最细粒度，QUOTA_EXHAUSTED 不可复跑但历史数据在 scoring.md |
| Q3 假设替换问题（RTX 3090×4 → A100-80GB） | **纳入** | 已知 confound：若归 M4 则 Q3 各 arm M1 应升 0.05-0.10，影响对齐基线 |
| bench/rubric-v3 M4 判据（D1-D5） | **排除** | 那是 decomp 项目的工件质量 rubric（M1-M8 八维），不是 stage-ablation 的 M1 事实准确率；维度不同 |
| T8 Part C v3 rubric（J1/J2 双判官） | **排除** | 同上，decomp 消融矩阵的 pass/fail 判据，非 M1 连续分 |
| G1a/G1b 盲判协议（r54/r56） | **排除** | 二值 pass_rate 口径，非 M1 连续分；且已收口 |

**覆盖性自检**：还有没有该考虑没列的？——gold 文件本身（Q1-Q5.md）是评分锚点，不算"候选口径"；S0-S5 六 arm 的答案文本是评分对象不是口径。完备。

## 3. 正交维度拆解

### 3.1 维度定义

| 维度 | 含义 | 取值枚举 | 检查方法 |
|------|------|----------|----------|
| D1: zero-fact 规则 | 无事实断言时 M1 怎么算 | (a) 维持 M1=0 (b) 豁免→M1=null 不计入 (c) 按方法论质量给 0.5 封顶 | 逐题检查 Q1-Q5 哪些含可验证断言、哪些纯方法论 |
| D2: 断言粒度 | 一条"断言"的定义 | (a) 原子断言（每个数字/规格独立计数）(b) 关键断言（一个逻辑结论=一条）(c) gold 条目对齐（gold 里每条 bullet=一条） | 对同一答案用三种粒度数 claims_checked，看哪种使双通道一致 |
| D3: 评分范围 | M1 只评事实还是也评推导 | (a) 仅原始事实断言 (b) 事实+可复算推导 (c) 事实+推导+方法论判断 | 检查 Q4/Q5 答案里的"推导链"被哪个通道计入了 |

正交性检验：D1=D2=D3 能否同时取不同值？能——例如 (a)+(b)+(b) 和 (b)+(a)+(c) 是不同组合。✅
完备性：所有观察到的分歧能否归入某组合？Q4 local=0.291 vs arena=0.872 → D1(a) vs D1(b/c) + D2(a) vs D2(b)。Q1-Q3 分歧较小 → D3 差异主导。✅

### 3.2 分解树

```
CJ-RUBRIC-ALIGN
├── A: 诊断固化（把散落在 status.md 的分析变成可执行 spec）
│   ├── A1: 从 90 行 arena jsonl + scoring.md 提取 per-cell (arm,q,run) 三元组对照表 → 落盘 alignment-inputs.json（原子：动作=python 脚本合并两源，判据=json 可加载且 90 行齐全）
│   └── A2: 标注每 cell 的"分歧类型"（zero-fact / granularity / derivation-scope / noise）→ 落盘 divergence-taxonomy.md（原子：动作=按规则分类 90 cell，判据=每 cell 有且仅有一个主类型标签）
├── B: 口径裁定（三维度各选一个值，形成统一 rubric spec）
│   ├── B1: D1 裁定——Q4/Q5 是否豁免 zero-fact（原子：动作=读 gold Q4/Q5 判断其是否含可验证断言，判据=spec 里写明触发条件）
│   ├── B2: D2 裁定——断言粒度选 (a)/(b)/(c)（原子：动作=对 5 个代表 cell 手工用三种粒度计数，选使双通道 Δ 最小的，判据=spec 里有计数示例）
│   └── B3: D3 裁定——推导是否计入（原子：动作=检查 Q3 A100 替换 case，判据=spec 里 M1 定义含/不含"可复算推导"）
├── C: 实施（改代码 + 重跑）
│   ├── C1: 修改 cross_judge.py JUDGE_PROMPT 按 B 节 spec（原子：动作=patch prompt 文本，判据=prompt 含新规则且旧 zero-fact 行已删/改）
│   ├── C2: 本地 :8787 重跑 90 cell M1（原子：动作=python cross_judge.py --all，判据=输出 jsonl 90 行且 m1∈[0,1]）
│   └── C3: 计算对齐指标（原子：动作=python 算 spearman/pearson/arm-rank，判据=报告含数值表）
└── D: 验收
    ├── D1: 双通道 spearman ρ≥0.6（原子：动作=C3 输出直接读，判据=ρ 值）
    ├── D2: arm 排序一致（S0 最差共识保持 + top-1 一致或差 ≤1 位）（原子：动作=C3 输出，判据=rank 表）
    └── D3: 若 ρ<0.6 → 回退 B 节换组合重跑（最多 2 轮）（原子：动作=改 spec 重跑 C，判据=第二轮 ρ 值）
```

**原子性自检**：A1/A2/B1-B3/C1-C3/D1-D3 共 11 个叶子，每个有明确执行动作+完成判据，不可再拆。✅

## 4. 量化定义

| 指标 | 公式 | 数据来源 | 单位 |
|------|------|----------|------|
| 对齐度 ρ | Spearman rank correlation(local_M1_i, arena_M1_i), i=1..90 | alignment-inputs.json + C2 输出 | [-1,1] |
| 平均绝对差 | mean(\|local_M1_i − arena_M1_i\|), i=1..90 | 同上 | [0,1] |
| arm 排序一致性 | Kendall τ(arm_rank_local, arm_rank_arena), arms={S0..S5} | C3 输出 | [-1,1] |
| zero-fact 命中率 | count(cell where local_M1=0 AND answer_len>1000) / total_cells | C2 输出 | [0,1] |

## 5. 任务书（arena 外包用）

**调研问题**：如何修改本地判官 JUDGE_PROMPT 的 M1 评分规则，使本地 27B 判官与 arena 异源判官在 90 cell 上的 M1 分数达到 spearman ρ≥0.6 且 arm 排序一致？

**已知背景**：
- 当前本地 prompt 规则："无可验证事实断言→M1=0" + 未指定断言粒度
- Arena 实际行为：key-assertion 4-12/cell，无 zero-fact 规则，推导计入
- Q4/Q5 是最大分歧源（local 0.291 vs arena 0.872）
- 仓库内 gold Q1-Q5.md 已就位，arena-judge-results.jsonl 90 行在 main

**候选范围**：D1{维持/豁免/封顶} × D2{原子/关键/gold对齐} × D3{仅事实/含推导/含方法论} = 18 种组合，先验最优猜测 = D1(豁免)+D2(关键)+D3(含推导)

**产出要求**：
1. `runs/rubric-alignment-spec.md`：最终选定组合 + 理由 + 计数示例
2. `runs/alignment-inputs.json`：90 cell 对照表
3. 修改后的 JUDGE_PROMPT 全文（贴进 spec 附录）
4. 失败降级：arena 不可用 → 本地 :8787 走完整 loop，conf-0.2

**验收标准**：见 §6。

## 6. 验收标准

- [ ] A1: alignment-inputs.json 落盘，90 行，每行含 (arm, q, run, local_m1, arena_m1, answer_chars)
- [ ] A2: divergence-taxonomy.md 落盘，90 cell 各有类型标签
- [ ] B1-B3: rubric-alignment-spec.md 落盘，三维度各有一个选定值+理由
- [ ] C1: cross_judge.py JUDGE_PROMPT 已修改（git diff 可见）
- [ ] C2: 本地重跑 90 cell 完成，jsonl 落盘
- [ ] C3/D1: spearman ρ≥0.6
- [ ] C3/D2: Kendall τ(arm_rank)≥0.5 且 S0 仍为双通道最差
- [ ] 若 D1 不达标：记录原因 + 换组合重试 ≤2 轮，最终报告如实登记