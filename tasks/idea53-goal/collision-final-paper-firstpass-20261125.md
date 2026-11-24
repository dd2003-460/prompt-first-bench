# idea53 最终闭式 paper 碰撞核查 · 初判（arXiv 6 组检索）

# origin: ai · 2026-11-25 04:52 · Lead 直查（arXiv API，6 组查询）
# 对象：最终 paper（闭式数学路线，eb1b0598c 转向后）——区别于 arena 五轮查的旧 claim（GPU run 树 + 交叉梯度 MI）
# 背景：subagent 审计发现五轮碰撞核查全查旧 claim 域，最终 paper 零轮（audit-final-20261125.md）
# 方法：arXiv API 6 组（closed-form GPU perf / microarch analytical / roofline bottleneck / MI incremental / pre-registered / hw-spec predict），每组 top 结果判撞

## 结论（一行）

**未见直接撞车**：四元组合（闭式数学 × 增量贡献测量 × 深浅判断对比 × 瓶颈诊断）在 arXiv 检索范围内无同构工作。最近邻 4 个全部可切割（见下表）。conf 0.6（单源 arXiv 相关性排序检索，非穷尽）。

> **2026-11-25 05:10 更新（arena round6 交叉核验完成）**：conf 0.6 → **0.7**。arena 会话 01a20b11 第六轮（commit bb387d43f @ arena/f8477718-prompt-first-bench，result.md 追加5 节，git 核验通过：指纹 6d50c871 ✓ + 4 近邻逐个 arXiv abs 实抓属实 + 非 arXiv 源全查）。新增近邻 5 个（SA-Scheduler ACM 10.1145/3842670 同族度最高但用途=调度无信息论读数 / AMALI ISCA'25 / MLSYSIM 2607.02558 / 微基准解析建模 2605.04178 / 瓶颈翻转 2608.13696）——均无「surface-vs-deep 判定增量信息的闭式度量+预注册」同构读数。总判断：**未撞车（窄空白）conf 0.7**。venue 排序：arXiv 即时 → ICML 2027 ML4Systems 类 workshop (P≈0.5-0.6) → MLSys workshop (P≈0.5) → NeurIPS E&D 错配 (P≈0.05-0.08) → ACL 砍。最难一击 + 三条件防守见 result.md 追加5。

## 最近邻 4 个（全部可切割）

| ID | 标题 | 为什么不是撞车 | 处置 |
|---|---|---|---|
| 2610.10924 | TME 第四项（fp64 仿真闭式阈值 OI*≈0.56 FLOP/B, B300） | 同为"硬件 spec 闭式推导"，但对象是**数值仿真**（FP8 仿 FP64 的 GEMM 阈值），不是瓶颈诊断的判断增量贡献。量不同、域不同 | Related Work 引用（闭式 GPU 分析先例） |
| 2402.08964 | Predicting UX from Hardware Specs（54 台笔记本回归） | 同为"spec→性能预测"，但是**经验回归**非闭式解析，对象是用户体验非瓶颈诊断，无深浅判断对比 | Related Work 引用（spec-based prediction 家族） |
| 2607.13184 | Microflow（微架构因果可观测性, MFIR） | 同为"微架构根因分析"，但是**仿真内 IR 框架**（instruction-centric 批判），非闭式定量测量，无增量贡献形式化 | Related Work 引用（根因分析方向） |
| 2512.01644 | LLM Inference on GPUs 系统刻画（四维框架） | 同为 GPU 性能分析，但是**经验刻画**（observation→foresight），非闭式数学，无判断增量测量 | Related Work 引用（GPU 性能分析现状综述） |

## 切割逻辑（novelty 在哪）

paper 的不可约组合 = **闭式**（不跑 GPU，纯 spec+workload prior 解析）× **增量贡献**（I(深层判断|浅层枚举) 的定量测量）× **预注册**（held-out 先锁）。
- 2610.10924 有"闭式"无"增量贡献测量"（它推的是单一阈值，不是判断间的贡献分解）
- 2402.08964 有"spec→预测"无"闭式"（经验回归）无"增量贡献"
- 2607.13184 / 2512.01644 有"微架构分析"无"闭式"无"增量贡献形式化"

## 检索覆盖（诚实边界）

- 6 组查询 × top 结果，arXiv 相关性排序（非穷尽）
- 未覆盖：非 arXiv 期刊（IEEE TC/TCAD、ACM TOS 等）、工业白皮书、专利
- 未覆盖：cs.OS/cs.DC 全量（只查了 cs.AR 为主的相关性命中）
- 因此 conf 0.6，不是 0.9——**待 arena 交叉核验**（D 08:53 三连催的"问一遍"在最终 paper 上的补做）

## 下一步

1. [已做] 初判落盘（本文件）
2. [已做 2026-11-25 05:10] arena 交叉核验轮（round6）：commit bb387d43f，conf 0.6→0.7，venue 排序 + 最难一击已出
3. [进行中] 补 References（0 引用→≥15）：暂存 6 条已核验 bib @ submission-staging/references.bib（a2363cc10）；round6 新增近邻（SA-Scheduler/AMALI/MLSYSIM/2605.04178/2608.13696）是第二批，待并入
