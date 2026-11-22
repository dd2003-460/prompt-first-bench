# T-PR-17 — Prompt 序列消融：decomp + 缺口

**发起**: 2026-11-22 D 新 idea（原话）："在不同prompt（也就是不同完成度的checkpoint）基础上渐进消融查看prompt序列是否影响最终结果"
**落点**: modules/B-pipeline-ablation/（消融模块）+ experiments/stage-ablation/（执行脚本）
**前置**: 本地覆盖检查已完成——t26-prompt-style-research.md 覆盖 prompt **风格**（情绪/PUA，19 篇），不覆盖 prompt **序列/顺序** → 真缺口，非重复。

## 实验语义（对齐）

SM 生产路径有固定 prompt 序列：P1_L1_SKELETON → P1H_INDEX（逐层 decompose）→ P3_VERIFY → P4_SYNTHESIZE。
实验 = 从**同一中间状态**（checkpoint）出发，用**不同后续 prompt 序列**继续，比较最终 depth。

**核心问题**：路径依赖——同一 checkpoint 下，不同序列 → 同一终态（序列只是搬运工，checkpoint 决定一切）还是不同终态（顺序效应真实存在，序列本身携带信息）？

**为什么值得做**（与主线 goal 的关系）：
- 若序列无影响 → 可以简化 pipeline（砍 verify/换顺序省 token），且 checkpoint 成为完整状态（可任意续跑/换策略）
- 若序列有影响 → 序列是隐式控制变量，当前固定序列可能是（偶然）最优，需要显式优化；且 resume 语义要包含"从哪段序列继续"

## 分解树

```
T-PR-17 prompt 序列消融
├── F1. 本地覆盖检查 ✅（t26=风格不序列；resume 机制已有 gpu-resume 先例）
├── F2. 文献滚雪球（arena T-PR-17 派发）
│   ├── C1. 多阶段 LLM pipeline 的 prompt/instruction 顺序效应先例？
│   ├── C2. 从中间状态用不同后续序列续跑、比终态的先例？（path dependence）
│   └── C3. 机制层：长上下文中指令位置效应（lost-in-middle 家族）
├── F3. 实验设计（等 F2 结果定对照组）
│   ├── 变量1: checkpoint 深度（L1/L2/L3 完成态，同一 seed 同一题）
│   ├── 变量2: 后续序列变体（canonical / verify 删除 / 顺序置换 / minimal）
│   └── 固定: 题（gpu）、seed、max_depth=5、prompt 内容（只动顺序/取舍）
├── F4. 执行（等 K7 完成释放 vLLM；每 cell ≥3 reps）
└── F5. 分析（depth 差异 + Welch/MWU + 效应量；与 K7 的节点数轴正交性核对）
```

## 缺口清单

| 子项 | 缺什么 | 补法 |
|---|---|---|
| F2 文献 | C1-C3 先例全集 | arena T-PR-17（本任务书），arXiv + OpenReview + web |
| F3 序列变体 | 哪些变体有区分度（先验：verify 删除最可能动分，因为 verify 是相关性过滤器） | F2 结果 + SM 现有常量盘点 |
| F3 checkpoint 恢复 | resume 是否完整保留状态（parent_ids 持久化 bug 已知，T5 未修） | 核验 checkpoint json 字段完整性，[待核验] |
| F4 资源 | vLLM 被 K7 占用（~2.9h） | K7 完成后串行（单变量原则：同负载） |
| F5 判分 | judge 噪声 ~0.1 比预期效应可能更大 | reps≥3 + bootstrap CI；若效应 <judge 噪声 → 结论=不可检测而非无影响 |

## 正交性自检

- F2（文献）vs F4（实验）：一个查先例一个跑数据，不重叠 ✓
- 与 K7（预算轴）：K7 动 max_nodes，本实验动序列，不同变量 ✓
- 与 K6（merge 消融）：K6 动 synth 内部 merge on/off，本实验动跨阶段序列，不同层级 ✓

## 完备性自检

D 的 idea 三要素 = ①不同完成度 checkpoint（F3 变量1）②渐进消融（F3 变量2 序列变体）③prompt 序列是否影响最终结果（F5 分析）。全覆盖。
