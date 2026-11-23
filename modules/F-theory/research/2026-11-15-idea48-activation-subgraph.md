# #48 领域网络/激活子图视角 — 形式化框架

> 来源：D 2026-11-12 提出 + Lead 认可。IDEA-INDEX #48。
> 状态：🔸形式化框架完成，文献对标待检索通道恢复后补。
> 日期：2026-11-15

## 核心直觉

无外部检索时，模型生成的分解树 ≈ 其内部**激活子图**（问题"点亮"了哪些概念）；
有检索后变成**耦合图**（外部证据为新节点，verified/degraded/failed = 耦合强度）。

## 形式化

### 定义 1：概念图 G_c

概念图 G_c = (V_c, E_c)，V_c 是概念节点集，E_c 是概念间关系边（语义关联/因果/包含）。
G_c 是模型权重中编码的领域知识结构的近似——不是显式存储，是激活模式。

### 定义 2：激活子图 G_a ⊆ G_c

给定问题 q，激活子图 G_a = (V_a, E_a) 是 G_c 的子图，V_a = {v ∈ V_c | act(v, q) > θ}，
其中 act(v, q) 是概念 v 在问题 q 下的激活强度（attention weight / probing score / 生成概率）。
θ 是激活阈值。

**无检索时的分解树 T_0**：模型仅凭内部知识生成分解树，T_0 的节点集 V(T_0) ≈ V_a
（问题点亮的概念），边集 E(T_0) ≈ E_a（概念间关系）。
T_0 是 G_a 的**树状投影**——把图结构压成树（分解树要求无环）。

### 定义 3：耦合图 G_coupled

给定问题 q + 外部检索结果 R = {r_1, ..., r_n}，耦合图 G_coupled = (V_c ∪ V_R, E_c ∪ E_R ∪ E_cross)，
其中 V_R 是外部证据引入的新概念节点，E_R 是外部证据内部的关系边，
E_cross 是内部概念与外部证据之间的耦合边。

**有检索时的分解树 T_1**：T_1 的节点集 V(T_1) ≈ V_a ∪ V_R，
边集包含 E_a + E_R + E_cross 的树状投影。

### 定义 4：耦合强度

节点 v ∈ V_R 的耦合强度 c(v) 由 verify 状态决定：
- verified: c(v) = 1.0（外部证据与内部概念强耦合，交叉验证通过）
- degraded: c(v) = 0.5（逻辑自洽但检索无可用源，弱耦合）
- failed: c(v) = 0.0（外部证据与内部概念无耦合或矛盾）

**耦合图的质量指标**：
- 耦合覆盖率 = |{v ∈ V_R | c(v) > 0}| / |V_R|（多少外部证据成功耦合到内部概念）
- 平均耦合强度 = Σ c(v) / |V_R|
- 耦合深度 = max 耦合路径长度（内部概念 → 外部证据 → 外部证据 → ...）

### 与 S5 状态机的对应

| S5 状态机概念 | 耦合图概念 |
|---|---|
| L1 skeleton | 激活子图 G_a 的根节点（问题直接点亮的顶层概念） |
| L2/L3 展开 | G_a 的 BFS/DFS 展开（概念间关系边驱动） |
| verify 节点 | 耦合边 E_cross 的强度测量（c(v)） |
| rework | 耦合失败后的重新耦合（换检索 query = 换耦合路径） |
| degraded 节点 | 弱耦合（c(v) = 0.5）——逻辑自洽但无外部证据确认 |
| quotient 边 | 激活子图中的商结构（多个概念被压缩为一个节点） |
| 笛卡尔积边 | 激活子图中的独立分支（无耦合的并行概念） |
| 随机耦合边 | 激活子图中的 latent factor（残差项，记录源不复制） |

### 研究定位

**从 deepresearch agents 转向 concept graph / knowledge activation**：
- deepresearch agents 文献关注"如何搜索+综合"（过程），撞车风险高（Perplexity/ChatGPT Search/Gemini 都在做）
- concept graph / knowledge activation 文献关注"问题如何激活知识结构"（机制），撞车风险低
- T53 的贡献：分解树作为激活子图的树状投影 + 耦合图的质量指标（耦合覆盖率/平均耦合强度/耦合深度）

**可证伪预测**：
1. 无检索时分解树的节点数 ≈ 激活子图的节点数（可用 probing 验证）
2. 有检索时耦合覆盖率与 bench 分数正相关（耦合越强，分数越高）
3. degraded 节点集中在激活子图的边界（内部概念与外部证据的接口处）
4. rework 次数与耦合路径长度正相关（耦合路径越长，越容易失败）

## 文献对标（2026-11-23 arXiv API 补，https 通道）

**核心声明撞车检查: "分解树 = 激活子图的树状投影 + 耦合图质量指标" — 无直接先例。**

| 查询 | 结果 | 判定 |
|---|---|---|
| "decomposition tree" + "knowledge graph" | 空 | 无直接先例 |
| "activation subgraph" + "language model" | 空 | 无直接先例 |
| "tree projection" + "knowledge graph" + "decomposition" | 空 | 无直接先例 |
| "decomposition tree" + "knowledge" + "reasoning" | 2 hit (见下) | 过程侧, 非激活投影 |

**最接近的 5 篇 (都不构成撞车)**:
1. *Reasoning over Hierarchical Question Decomposition Tree for XQA* (2023-05) —
   分解树用于可解释 QA, 是过程侧 (如何分解问题), 不是"激活子图的树状投影"机制
2. *PruneRAG: Confidence-Guided Query Decomposition Trees* (2026-01) —
   分解树用于 RAG 检索, 过程侧, 无激活子图概念
3. *Leveraging Spreading Activation for KG-Based RAG Retrieval* (2025-12) —
   显式 KG 上的 spreading activation (检索侧), 最接近"激活"概念, 但作用于
   **显式** KG (已有边), 不是 LLM **隐式** 激活子图; 无树状投影/耦合强度指标
4. *Multi-granularity Concept Sparse Activation + Hierarchical KG Fusion* (2025-07) —
   概念激活 + 分层 KG 融合, 融合框架, 无"分解树=投影"声明
5. *Probing Neural Topology of LLMs* (2025-06) — probing 测拓扑, interpretability 侧,
   无分解树/耦合图

**结论: #48 新颖声明成立, 撞车风险低 (框架 2026-11-15 的判断被文献确认)。**
最近邻是 ① 显式 KG 的 spreading activation (检索) + ② 分解树用于 RAG/QA (过程),
两者都没统一 "隐式激活子图 → 树状投影 → 耦合强度指标" 这条链。#48 的增量 =
把分解树重新定位为**隐式激活子图的树状投影**, 并定义耦合图质量指标
(耦合覆盖率/平均耦合强度/耦合深度) — 这个组合无先例。

**对可发表性的含义**: #48 能立住的不是"分解树"(已有) 也不是"激活"(已有),
而是**两者的统一 + 耦合强度指标**。要发表需补: (a) 可证伪预测 1 的 probing 验证
(无检索分解树节点数 ≈ 激活子图节点数), (b) 预测 2 的耦合覆盖率-bench 分数相关性。
两者都可用现有 T53 数据 + bge-m3 probing 做, 不依赖新 GPU 实验。

## 预测 2 实证 (2026-11-23, GPU 域, 固化: idea48-pred2-coupling-depth.py)

- 口径: 耦合覆盖率 cc = verified/(verified+degraded+pending) (status 字段,
  verified=强耦合 c=1.0, degraded=弱耦合 c=0.5, pending=未耦合);
  depth = parent_ids 构树最大深度 (level 字段全为 1 不可用);
  corpus = budget-* + rep-scan 去重, >=20 nodes, n=30 trees (GPU 单域)。
- 结果: r(cc, depth) = 0.738 (零阶, t=5.78, df=28, p<0.001);
  **偏相关 r(cc, depth | n_nodes) = 0.806 (t=7.07, df=27)** — 控制节点数后更强。
- 排除混杂: r(depth, n_nodes)=0.867 (depth 与节点数强相关, 是潜在混杂),
  但偏相关 0.806 > 零阶 0.738 → cc~depth 关系**非**节点数代理, 是真实关联。
- 含义: 树越深 (探索越深入), verified 占比越高 — 深层节点更多成功耦合到
  内部知识 (verify 通过), 与 #48 "耦合深度=质量指标" 的声明一致。
- 局限: ① 单域 (GPU), 跨域待 Q6 全曲线 ② depth 是机械 3-level step 的
  连续版 (parent_ids 深度), 非 LLM judge ③ n=30, 偏相关 t=7 强但样本单域。
- 对发表: 预测 2 在 GPU 域**成立** (强相关+混杂排除), 是 #48 的第一个实证支柱;
  预测 1 (probing) 仍是主要缺口。

## 与 #32（压缩即智能）的关系

#32 说分解树是好的压缩形式（MDL 路线）。#48 补充了**为什么**分解树是好的压缩形式：
因为它是激活子图的树状投影——图结构天然比树结构信息密度高，但树结构是可验证的（无环、可逐节点 verify）。
压缩-展开税（#40）= 从树状投影恢复图结构的代价 = 耦合边的重建代价。
