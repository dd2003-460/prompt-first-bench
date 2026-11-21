# Goal: research-agi-budget — 分解树 + 缺口清单

**发起**: 2026-11-22 D 睡前指令
**目标（D 原话）**: "目标就是 research 的 AGI，最好可以通过预算直接控制 AI 在 Pareto 边界上研究（预算大就如同 gold 里面一样，完整覆盖所有贡献因子，否则就会压缩细节）"
**D 的关键重述**: "如果我要求框架最终目标是我的条件下性价比以及最快达到 AGI，你反而可能工作刚好，因为 general 这一点不会有问题，然后就是我的硬件条件下如何最快可靠达到的问题了"

## 目标语义（D 的重述改变了什么）

| 旧框架（TCO 题） | 新框架（AGI 题） |
|---|---|
| 通用 prompt + 领域内容 = 污染（over-guidance） | 目标具体（D 硬件下最快达 AGI）→ 领域内容是**目标定义**，不是污染 |
| 不泄露 = prompt 零领域词 | 不泄露 = prompt 不含 **gold 答案骨架**（分解结构/数值），但可含目标定义（AGI、D 硬件条件） |
| TCO 是代理题 | AGI 是 D 的真实目标，TCO 是它的子问题（研究基础设施的性价比） |

**"不泄露"的精确边界**（2026-11-22 与 D 讨论确认）：
- 题面给的（TCO/性价比/单卡多卡/32K）= 题目边界，prompt 可复述
- 模型先验（TCO 怎么拆、GPU 选型看什么维度）= 模型能力，prompt 不该替它写
- gold 骨架（摊销+电费+故障损耗 的具体分解结构）= 答案，prompt 绝不能含
- 目标定义（AGI、D 硬件、最快可靠）= 新题面，prompt 应含

## 分解树

```
research-agi-budget（D 硬件条件下，预算控制 AI 在 Pareto 边界上研究）
├── A. matched 批收尾（阻塞项，~3-4h）
│   ├── A1. 监控批完成（pid 87154，nat 10/10 完成，soc 7/10，gpu 5/10）
│   │   └── 原子：后台监控进程，批退出时落盘完成标记
│   ├── A2. 恢复记账（driver bug 导致 runs_sm_matched/ 空，数据在 54 个 archive）
│   │   └── 原子：archive 的 synth json 已含 judge 分数 → 纯数据拷贝+stats，零 LLM 成本
│   └── A3. 出 matched 批 stats（SM vs bare，同负载）
│       └── 原子：ablation_stats.py 跑 30 SM + 30 bare，Welch/MWU/δ/CI
│
├── B. prompt 去污染修复（等 A 完成，批实时读 prompts.py 不能动）
│   ├── B1. 删时间尺度框架（5 个 L1 变体 + P1H_INDEX 的"即时/短期运营/长期持有"）
│   │   └── 原子：8 个常量改文本，byte-level diff 落盘，重跑 smoke 验证不崩
│   ├── B2. 领域例子换抽象占位符（P3_VERIFY/P4_SYNTHESIZE/EDGE_*/P1_L1_TEXT）
│   │   └── 原子：同上
│   └── B3. P1_DECOMPOSE 不动（legacy，不在生产路径）
│       └── 原子：标记 legacy，不修
│
├── C. merge 消融（等 A 完成，vLLM 负载释放后）
│   ├── C1. 重跑 719 节点树 synth，保存 per-layer 输出（当前只存了 final answer）
│   │   └── 原子：synth_rerun.py 加 per-layer 落盘，~834s 单 run
│   └── C2. Arm A（skip merge，concat L1-L5 → judge）vs Arm B（merge，0.4261）
│       └── 原子：judge 两臂，A↑=merge 是压缩元凶，A flat=per-layer 自压缩
│
├── D. AGI 题面 + gold 骨架（新题，research 类）
│   ├── D1. 题面定义（D 硬件条件：本地工作站，vLLM 8787，qwen3.8-27b-mtp NVFP4）
│   │   └── 原子：写题面，D 醒来确认（题面 = D 的目标，不能我代定）
│   ├── D2. gold 骨架（完整覆盖所有贡献因子 = "最快可靠达 AGI"的分解树）
│   │   └── 原子：调研+建树（arena 外包优先，登录过期则本地 conf-0.2）
│   └── D3. rubric（judge 判定点，对标 gold 骨架）
│       └── 原子：gold 树 → 判定点 × 层级（同 gpu 38 判定点格式）
│
└── E. 预算控制实验（Pareto 边界，等 D 完成）
    ├── E1. 预算轴定义（search 次数 / token / 时间，单变量）
    │   └── 原子：选 1 个预算参数（SM 已有 budget_nodes/per_layer_cap/max_rounds），
    │       扫 4-5 个档位（含 unlimited 上限档）
    ├── E2. 质量轴（judge depth/coverage，同现有 rubric）
    │   └── 原子：复用 judge_v2_depth.score_run
    ├── E3. 跑预算扫描（每档 ≥3 reps，同负载）
    │   └── 原子：batch driver，spec 驱动
    └── E4. Pareto 曲线（预算 vs 质量，找拐点 = 性价比最优点）
        └── 原子：stats + 画图，拐点 = 边际质量增益/边际预算成本 最大化的点
```

### E1 预算轴设计（2026-11-22 定稿，批跑期间完成）

**D 的机制要求**："预算大就如同 gold 里面一样，完整覆盖所有贡献因子，否则就会压缩细节"。
即：预算是**覆盖度**的控制旋钮，不是单纯的时间/成本上限。

**SM 现有预算参数盘点**（s5_state_machine.py:120-128，刚 grep）：

| 参数 | 默认 | 控制什么 | 与"覆盖度"的关系 |
|---|---|---|---|
| `max_nodes` | 150 | 树总节点数硬顶 | **直接**：节点=贡献因子，预算↑=覆盖↑ |
| `max_depth` | 4 | 层级深度 | 间接：深度=分解粒度 |
| `max_kids_per_parent` | 8 | 单父子节点数 | 间接：广度 |
| `contribution_threshold` | 0.10 | 边际贡献<0.10 不展开 | 自然停止点（非预算，是剪枝） |
| per-layer max_tokens | 4000/8000 | 每层输出长度 | 细节密度（"压缩细节"的直接来源） |

**选 `max_nodes` 为主预算轴**，理由（单变量原则）：
1. 它是唯一**直接等价于贡献因子覆盖数**的标量——D 的"预算大=完整覆盖"逐字对应
2. SM 按 J_decomp 贡献度排序展开 → 小预算 = 自动取 top-K 贡献因子（Pareto 选择的机制已内置）
3. 成本单调：节点数 ≈ LLM 调用数 ≈ 时间/电费，预算轴=成本轴，Pareto 曲线可直接换算钱

**扫描档位**（5 档，含上限档）：
- B1: max_nodes=50（强压缩，~1/3 gold 覆盖）
- B2: max_nodes=100
- B3: max_nodes=150（当前默认）
- B4: max_nodes=300
- B5: max_nodes=719（= 719 节点树规模，"unlimited"档，gold 级覆盖）

**固定变量**（单变量原则，全部不动）：max_depth=5（resume 已证明 L5 必要）、max_kids=8、β=3.0、θ=0.10、prompt（B 修复后版本）、题（gpu，gold 最完整）、seed=42。

**质量轴**：judge_v2_depth 的 depth + coverage（现有 rubric，38 判定点）。
**每档 ≥3 reps**（方差来源已知：vLLM 并发非确定性，T53b 已量化）。
**Pareto 输出**：(cost=节点数/时间, quality=depth) 散点 → 包络线 → 拐点 = Δquality/Δcost 跌破阈值的点。
**预期**：B1→B3 陡升（覆盖主导），B3→B5 趋平（边际贡献因子价值低）→ 拐点在 B3 附近 = 性价比最优点。若 B4/B5 仍陡 → 当前默认 150 是欠预算，应上调。

**次预算轴（第二轮，视第一轮结果）**：per-layer max_tokens（4000 vs 8000 vs 16000）控制"细节密度"——D 说的"压缩细节"是 synth 侧，decompose 侧的细节密度由 per-layer tokens 控制。第一轮确认 max_nodes 轴形状后再扫，避免两轴混淆。

**正交性自检**：
- A（收尾）vs B（修复）：A 是数据回收，B 是代码修改，不重叠 ✓
- B（prompt 修复）vs C（merge 消融）：B 改 decompose prompt，C 改 synth 路径，不同阶段 ✓
- C（merge 消融）vs E（预算实验）：C 是单变量消融（merge on/off），E 是预算扫描，不同变量 ✓
- D（AGI 题）vs E（预算实验）：D 是题面+gold（输入），E 是实验（消费 D 的产出），依赖关系非重叠 ✓

**完备性自检**：D 的指令三要素 = ①定 goal 安排实验（A-E 覆盖）②不泄露（B + D 的边界定义覆盖）③预算控制 Pareto（E 覆盖）。无遗漏。

## 缺口清单

| 子项 | 缺什么 | 补法 |
|---|---|---|
| A2 恢复记账 | archive 54 目录 → runs_sm_matched/ 的映射关系（哪轮对应哪个 archive） | 按时间戳+qid+round 匹配，[待核验]：archive 目录名 sm-{qid}-{ts} 的 ts 是否唯一对应 round |
| B1 删时间尺度 | 删后模型是否还覆盖"时间维度"（gpu 题的 3 年 TCO 持有期） | 重跑 1 轮 smoke 对比节点数 [待核验] |
| C1 per-layer 输出 | synth_rerun.py 当前不落盘 per-layer 文本 | 改代码加落盘（~10 行） |
| D1 题面 | D 的"硬件条件"精确边界（哪些硬件算"我的条件下"） | D 醒来确认，[待核验]：是否含云端 API 预算 |
| D2 gold 骨架 | "最快可靠达 AGI"的完整贡献因子分解（无现成 gold） | 调研（arena/本地），[待核验]：AGI 的可操作定义（D 的 AGI = 什么能力阈值） |
| E1 预算轴 | 哪个预算参数最能控制"覆盖度 vs 压缩"（search 次数 vs token vs 轮数） | 先跑 1 个参数扫描，看哪个轴的 Pareto 曲线最陡 [待核验] |
| E4 拐点 | 性价比最优点的量化定义 | 边际质量增益/边际预算成本 最大化，[待核验]：是否需要归一化 |

## 执行顺序（D 睡眠期间）

1. **现在**：A1 监控（后台）+ 本文件落盘
2. **批完成时**（~3-4h）：A2 恢复记账 + A3 stats（零 LLM）
3. **之后**：B prompt 修复（改 prompts.py + smoke）
4. **之后**：C merge 消融（1 个 LLM run）
5. **D 醒来后**：D1 题面确认 → D2/D3 gold+rubric → E 预算实验

**不做的**（D 睡眠期间）：
- 不动 prompts.py（批在跑，实时读）
- 不派 arena（登录过期，T-PR-16 阻塞）
- 不定 AGI 题面（D 的目标，D 确认）
- 不跑新 LLM 实验（vLLM 负载给批）
