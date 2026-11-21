# T53b post-62-runs 分解树
# origin: ai | 2026-11-21 | 规划纪律：派发只执行本表内条目

## 分解树（正交子项）

```
post-62-runs
├── A. 收口（T53b 本 goal 的 04-verify + 05-accept）
│   ├── A1 stats_summary: python3 ablation_stats.py（cc-state 已有条目，batch 不取，Lead 手动）
│   ├── A2 repro_check: 好轮次（cov/depth > mean+1SE）同参重跑 3 次，波动 < 0.05
│   ├── A3 webllm 混淆变量处置: 选项 (a) 接受降级数据（watchlist 已倾向），5 个 OK run 标离群
│   └── A4 结论对标 DESIGN.md 假设（05-accept gate）
├── B. 数据完整性
│   ├── B1 parent_ids 持久化修复（已确认 bug：字段丢失 3-12% + 脱钩 25%）
│   └── B2 KB staging → corpus: 6 张 GPU 卡 mv（hardware-staging/ → corpus）
├── C. 架构（S28 推理/计算分离）
│   ├── C1 SM 重构: LLM 只产效率函数 f(H)，脚本做实例化（β≈0 确定性计算）
│   └── C2 条件集 C 跟踪（S30）: 每个 f(H) 附带前提条件集，缓存失效 = C' vs C 检验
├── D. 测量（K^t 框架验证）
│   ├── D1 62 run 全量 K^t 复测: 模式数/压缩比/信息密度（5-run 基线: 11 模式, 144x, 0.7%）
│   └── D2 微架构效率缺口: Roofline 有、SM 级效率无（watchlist 已记）
└── E. 下一套实验（新 goal，非本 goal）
    ├── E1 "general 改法" 实验: 实例折叠 + 冗余检测 + 信息密度指标 → 新 batch
    │   目标函数（S29）: 压缩（节点数↓）vs 覆盖（信息不丢）vs 解码时间（脚本展开 β≈0）
    └── E2 webllm 效应配对实验: 同 (qid,arm,round) with/without 各 2-3 个（需登录窗口）
```

## 分解 = K^t tradeoff 单循环（S34，替代原"四维度检查"平铺）

本分解树本身是 K^t 复杂度在条件 C 下的 tradeoff 产物，不是"四个维度的检查清单"。
四个环节是同一循环的不同面：正交 = 压缩的约束、完备 = 压缩的终止条件、
目标函数 = tradeoff 的判据、tradeoff = 压缩本身。

### 压缩·结构化（分解树本身 + 正交约束）
- A/B/C/D/E 互不重叠：A=收口（本 goal 内）、B=数据完整性（独立于架构）、C=架构（谁算）、D=测量（量什么）、E=下一套（新 goal）。
- C1 vs C2 正交：C1 是"谁计算"（LLM vs 脚本），C2 是"何时失效"（条件集检验）——不同轴。
- A3 与 E2 正交：A3 是"接受现有数据的口径"，E2 是"补测 webllm 维度"——一个收口一个开新。

### 停止条件·预算（何时停 = 完备的终止条件，S33 阶段性）
拆到"充分到方便优化"即停，缺口标 [待核验] 不阻塞：
- **缺：A1-A4 的验收口径**。stats_summary 的"好轮次"判据 = cov/depth > mean+1SE（repro_check cmd 已写），但 A4 对标 DESIGN.md 的具体假设列表未列 [待核验: DESIGN.md 假设清单]。
- **缺：C1 的验收判据**。"LLM 只产效率函数"怎么验证？→ 可机判：重构后 SM 输出 JSON 里 f(H) 节点数 ≈ 14（K-bound），实例节点由脚本生成不占 LLM token。[待设计]
- **缺：C2 的条件集格式**。~~C 集用什么 schema？[待设计]~~ **已定（T8, v1.1）**：type/source/sensitivity/drift_sensitive 四字段 + 三分类机判规则；待 62-run 数据回填验证。
- **缺：E1 的目标函数正交维度**。E1 的目标函数候选：{压缩比, 覆盖保持率, 解码时间, 可靠性}。是否完备？[待核验: 是否有遗漏维度，如"新鲜度"（S30 条件域漂移检测）]
- **缺：D2 微架构效率的测量方案**。Roofline 有（带宽×算力），SM 级效率无——怎么补？[待调研: 业界 SM 级效率模型]

### 新信息·理论（压缩的依据 = 目标函数定义 K 下界）
- **T53b 本 goal 目标** = 验证 DESIGN.md 假设（formula vs text 臂消融）。K 下界 = 统计量（coverage/depth 均值±SE + 95%CI，n=10）。
- **post-62-runs 工作目标** = 把 T53b 的"发现"（组合爆炸、K^t 框架、条件集）变成"可验证的改法"。K 下界 = 14 原子（11 效率函数 + 3 微架构系数）。
- **下一套实验（E1）目标** = 验证"general 改法"是否真的压缩了（节点数↓ 且覆盖不丢）。这是**科研目标**（高复用、高可靠）——K 下界 = 14 原子，不是工程目标（新鲜度、实测贴合）。

### 新信息·自然/社会校验（C' 来源，唯一正和信息）
- **A（收口）** = 62 run 的已有信息 → 统计量（K^t 管理）；校验 = 统计显著性（95%CI 不跨 0）。
- **B（数据完整性）** = parent_ids 修复 = 提高已有信息的表达效率（减少字段丢失）；校验 = 修复后字段非空率。
- **C（架构）** = 推理/计算分离 = 把"确定性展开"从 LLM 移到脚本（β≈0），LLM 只干"定律选择 + 有效性判断"（唯一非确定性判断点）；校验 = f(H) 节点数 ≈ 14 + 脚本展开结果与 LLM 展开一致率。
- **D（测量）** = K^t 复测 = 压缩域的度量；微架构效率 = 泛化域的工具（新定律）；校验 = 复测数字与 47-run 子集一致。
- **E（下一套）** = 新条件 C'（general 改法）→ 用数学/物理工具（实例折叠、冗余检测）展开隐含信息 → 压缩成新结论（节点数↓ 且覆盖保持）；校验 = 新 batch 的 A/B 对比。

## 优先级（P1 实际问题 > P2 完成度低 > P3 可理解性）

| 条目 | 优先级 | 理由 |
|---|---|---|
| A1-A4 | P1 | 本 goal 收口，不跑完 04-verify/05-accept 不能 stage_advance |
| B1 | P1 | 数据完整性，parent_ids 丢失影响所有下游分析 |
| B2 | P2 | 数据移动，可逆，不阻塞 |
| C1 | P1 | 架构核心，S28 推理/计算分离是 K^t 框架的落地 |
| C2 | P2 | 依赖 C1（先有 f(H) 再谈 C 集），但可并行设计 schema |
| D1 | P1 | 62 run 全量 K^t 复测，验证 5-run 基线（11 模式）是否稳定 |
| D2 | P2 | 微架构效率缺口，需调研，不阻塞 |
| E1 | P1 | 下一套实验，验证 general 改法，但依赖 C1（先重构再跑） |
| E2 | P2 | webllm 效应，需登录窗口，不阻塞 |

## 任务表（派发只执行表内条目）

| # | 条目 | 动作 | 依赖 | 状态 |
|---|---|---|---|---|
| T1 | A1 | 62 run 跑完后 `python3 ablation_stats.py` | 62 run done | **已完成（11-21 10:25）**：62 SM run 全跑完（r09 缺口重跑中），stats 出 nat/soc/gpu 三臂 Δ（nat +0.141 / soc +0.186 / gpu -0.007 cov） |
| T2 | A2 | 好轮次重跑 3 次 | T1 | 待 T1（判据 cov/depth>mean+1SE，波动<0.05） |
| T3 | A3 | webllm 混淆变量处置（选项 a 落盘） | 无 | **已完成（11-21）**：watchlist 落盘采纳 (a)——5 OK run 标离群剔除、主统计"webllm 缺席"口径、webllm 效应=E2 配对实验 |
| T4 | A4 | 结论对标 DESIGN.md | T1 | 待 T1 |
| T5 | B1 | parent_ids 持久化修复 | 62 run done（不动在跑代码） | 待 62 run |
| T6 | B2 | KB staging → corpus（6 卡 mv） | 62 run done | 待 62 run |
| T7 | C1 | SM 重构: 推理/计算分离 | 62 run done + B1 | 待 62 run |
| T8 | C2 | 条件集 C schema 设计 | 无（可并行） | **已完成（11-21）**：kt-framework-v1.1 补 C schema（type/source/sensitivity/drift_sensitive + 三分类机判 + 完备性检验）；待 62-run 回填验证 |
| T9 | D1 | 62 run 全量 K^t 复测 | 62 run done | 待 62 run |
| T10 | D2 | 微架构效率测量方案调研 | 无 | **降级（11-21 D 纠正）**：工程级具体问题（GPU 场景专用，不 general），不占主线。移到工程维护层，E1 需要时再启动 |
| T11 | E1 | general 改法实验（新 goal） | T7 | 待 T7 |
| T12 | E2 | webllm 效应配对实验 | 登录窗口 | 待登录 |
| T13 | 管线固化 | 跑-存档-增量-继续跑 固化 | 无 | **已完成（11-21）**：pipeline_snapshot.py（幂等 manifest+delta，commit 882f754ca）+ cron 每 10min（job 3eae1ea698b3，no_agent 纯脚本，跨 session 持久）；跑/继续跑/存档现有管线已有，补的是"记录增量变化"环 |

## 空缺清单
- [ ] A4: DESIGN.md 假设清单 [待核验]
- [ ] C1: 验收判据（f(H) 节点数 ≈ 14）[待设计]
- [x] C2: 条件集 schema [已定 v1.1，待 62-run 回填验证]
- [ ] E1: 目标函数正交维度完备性 [待核验]
- [ ] D2: 业界 SM 级效率模型 [待调研]
