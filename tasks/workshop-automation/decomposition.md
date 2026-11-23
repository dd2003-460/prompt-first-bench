# decomp: 自动化补重复实验 + 两个小工作 idea 评估

> origin: ai · 2026-11-22 · 触发：D 指令"先试着自动化实验" + 两个 idea（瓶颈理论树模型 / checkpoint 作 cache 一致性）
> 最终目标（不动）：产出一个可投 workshop 的、judge 严格且不变的实验，并评估两个 idea 能否成为独立小工作。

## 分解树

### A. 自动化补重复实验（D 明确指令"先试着自动化实验"，最高优先级）

- **A1 judge v1.0 代码**：spec 已冻结（judge-v1.0-spec.md, f6072397f），代码未写。三层：L-机械（sympy+数值容差）/ L-结构（去重深度/节点/分支）/ L-覆盖（embedding 0.80+MAGNET）。复用 tjudge1_formula.py + tjudge1 的 embedding 匹配。
- **A2 三阈值标定**：cosine 0.80（用 gold 36 unit 做 ROC）/ 权重 0.4-0.3-0.3（消融）/ 数值容差 10%（gold 数值分布）。标完冻结。
- **A3 补重复 runner**：5 预算点（50/100/150/300/719）× 8-12 重复。复用 k7 的 budget scan launcher（k6k7_serial_launcher.sh）。
- **A4 checkpoint 前缀缓存**：L1/L2 checkpoint 共享前缀，vLLM prefix caching 省成本。[待核验] vLLM 是否真生效 + checkpoint 语义是否等价（= Idea 2 的实验）。
- **A5 统计**：效应大小 + CI + p 值（配对 t / Wilcoxon）。复用 k7_pareto.py 的 bootstrap_ci。

### B. Idea 1：瓶颈理论 + 树结构计算模型（深节点信息收益）

- **B1 滚雪球调研（撞车检查，D 明确前提）**：本地已查 3 轮 arXiv（2411.11984 线性版已有，树级没找到 conf 0.6）。需补：① 读 ICLR 2027 在审 4 篇 RSI 论文（重点核对树级信息增益）② 树搜索/MDP 里的 state-value 分解 ③ HPC 瓶颈分析理论（Roofline 等）是否已有"深节点信息收益"形式。
- **B2 理论形式化**：节点 v 条件信息增益 I(answer; v | tree\{v}) = H(answer|tree\{v}) − H(answer|tree)。难点：评测时不知道 answer，条件熵算不出。[待核验] 是否有代理（用 gold 当 answer 代理 / 用模型自身 logprob）。
- **B3 瓶颈分类**：不同瓶颈（compute/memory/bandwidth）下深节点信息收益差异。
- **B4 小工作可行性评估**：能否成独立 workshop / 只能当主论文的 discussion。
- **B5 preprint 路径**：拿到理论结果后，arXiv（需 cs domain 背书，见 arxiv-endorsement-policy）→ 套磁 / workshop。

### C. Idea 2：checkpoint 作 cache 的一致性

- **C1 实验设计**：同一题，(a) 从头跑 L0→L4 vs (b) 从 checkpoint L2→L4。
- **C2 统计一致性**：统计平均下两者差距多大（配对检验）。
- **C3 节省收益**：时间/成本节省比例。
- **C4 小工作可行性**：能否成独立 workshop（"Cost-Efficient Evaluation via Checkpoint Prefix Caching"）。
- [待核验] vLLM prefix caching 对"不同后缀同一前缀"是否真省（continuous batching 下非确定）。

### D. 顶会 workshop 对标调研（2026-11-24 D 指令"弄个完整的调研-对标-核验流程"）

- **D1 调研**（外包 arena，会话 01a1ca66）：NeurIPS/ICLR/ICML/AAAI/ACL 2025-2026 workshop track 实际论文——agent 评测/deep research/metacognition/LLM judge 方向。交付：论文清单（标题/venue/一句话方法/与草稿 3 卖点的重叠度）+ 撞车风险排序。
- **D2 对标**（Lead）：草稿 3 卖点（过程测量框架/负结果+裸臂对照/机械 judge 可复现）逐条对 D1 清单，标"独有/部分重叠/撞车"。
- **D3 对抗核验**（arena 第二轮）：最强 claim"没人做 agent 内部过程级测量"找反例（不是找支持）；找到反例 → 降级 claim 措辞进草稿 §3。
- **D4 落盘**：结论写 `experiments/stage-ablation/workshop-benchmark-survey-20261124.md`，标 conf + 来源 URL。

## 缺口标注（汇总）

| 缺口 | 阻塞谁 | 怎么补 |
|---|---|---|
| judge v1.0 代码未写 | A1→A2→A5 | 复用 tjudge1 写 |
| 三阈值未标定 | A2 | gold 36 unit ROC + 消融 |
| vLLM prefix caching 是否生效 | A4, C2, C3 | 实测（C1 实验顺带验证） |
| checkpoint 语义等价性 | A4, C2 | 实测（C1 实验） |
| 树级信息增益是否撞车 | B1→B4 | 读 ICLR 2027 4 篇 + arXiv 补查 |
| 条件信息增益评测时怎么算 | B2 | 理论 + 代理方案 |
| ICLR 2027 4 篇在审论文全文 | B1 | OpenReview 拉全文 |
| 顶会 workshop 实际论文清单（agent 评测方向） | D2→D3 | arena 调研（D1，任务书 tasks/T-WKS-BENCH-task.md） |
| "过程级测量"claim 是否有反例 | D3 | arena 对抗核验（D3） |

## 执行顺序（产投比排序）

1. **A1+A2**（judge 代码 + 标定）：阻塞一切实验，~半天，纯本地不占 vLLM
2. **C1 实验**（checkpoint vs 从头跑）：同时验证 A4（prefix caching）+ C2（一致性）+ C3（节省），一石三鸟，vLLM 空闲可跑
3. **A3**（补重复 runner）：judge 标定完 + C1 验证 prefix caching 后开跑
4. **B1**（撞车调研）：读 ICLR 2027 4 篇，可与实验并行（不占 vLLM）
5. **B2-B4**（理论 + 可行性）：B1 之后
6. **A5**（统计）：A3 跑完后
7. **B5**（preprint 路径）：理论结果出来后
8. **D1→D4**（workshop 对标）：D 指令优先级，arena 调研可与 A3 补重复并行（不占 vLLM）；D2/D3 在 D1 落盘后做

## 留空（不编）

- 补重复具体 n（8 还是 12）：[待标定] 用 C1 实测标准差定
- 三阈值最终值：[待标定] A2 后冻结
- Idea 1/2 能否成小工作：[待评估] B4/C4 后
- ICLR 2027 4 篇是否撞车：[待核验] B1 后
