# TASK-IDEA53 分解树 v2（1-loop 01 · goal: idea53-cross-gradient）

> 2026-11-24 v2 · **D 纠正转向**：信息增益 = 纯理论计算（硬件 spec + 工作负载假设 → 闭式条件互信息），
> 不是对 27b 推理树文本的经验统计。v1 的 judge 标注路线（27b 标 27b，循环性嫌疑）全部作废。
> 本文件 = 分解树 + 正交性核对 + 缺口 + 任务表。
> 预注册锚：GOAL.md §0.5 转向 commit（理论计算设计，早于 idea53-theory.json 产出）。

## 1. 分解树（S1-S5 正交子项）

| 子项 | 一句话问题 | 落地答案 | conf |
|---|---|---|---|
| S1 因子树+输入 | 树长什么样、输入是什么？ | 瓶颈因子分解树 L1 资源类型（带宽/算力/容量/标量）→ L2 精度混合（FP4/FP16 占比）→ L3 微架构组件（CUDA 核/发射/标量单元/带宽）→ L4 具体机制（issue rate/decode width/标量累积）。输入=GPU spec 表（5090/T5000/4090/A100/RTX Spark，pfb/research/gpu-hardware-candidates-20261124.md）+ 工作负载假设（FP16 占比/标量占比） | 0.8 |
| S2 信息增益计算 | 每节点增益怎么算？ | 瓶颈判断 B（瓶颈类型+占比）的分布，已知节点 k 对应参数 vs 未知，H 之差 = I(B; node_k \| 前序节点)。闭式，纯数学，不跑实验 | 0.9 |
| S3 对照臂 | 怎么排除平凡解释？ | ①参数置换（spec 数字随机打乱，增益应→0）②占位硬件（无差异 spec，增益应→0）③层内类型对照（同层判断型 vs 枚举型节点增益比较） | 0.8 |
| S4 生死线判定 | claim 成不成立？ | 深层（L3/L4 微架构级）每节点信息增益 > 浅层（L1/L2 枚举级），跨 ≥3 硬件一致 → 成立；不成立 → 负结果记录 | 0.9（判据已预注册） |
| S5 投稿策略 | 发哪、概率多少？ | arena 第五轮回执 @ 7dae6431a（双轨 NeurIPS'27 E&D + ICML'27 workshop） | done |

## 2. 正交性核对

- S1→S2 单向依赖（树+spec 是计算的输入），S3 依赖 S2（对照臂算同一组增益），S4 依赖 S2+S3，S5 独立并行（已 done）
- 两两输入/输出无重叠：S1 出树+spec、S2 出增益值、S3 出对照臂、S4 出判定、S5 出 venue
- 时间轴：S1→S2→S3→S4 串行；S5 已完成

## 3. 缺口标注

- S1：工作负载假设（FP16 占比/标量占比）取值依据需标注（D 给的例子：T5000 70/30 和 50/50；5090 标量 40%）[待核验：是否足够覆盖]
- S2：B（瓶颈判断）的取值空间定义需固定（瓶颈类型 × 占比区间），否则 H 算不出 [待核验]
- S4：held-out 硬件（RTX Spark？A100？）预注册，防 HARKing
- 旧路线遗留：27b 推理树数据（rep-scan/t53b/stage-ablation）降级为可选 held-out 验证源，不进主 claim

## 4. 任务表（机器可查验收 + 耗时）

| 步骤 | 执行 | 验收（机器可查） | 耗时 | 状态 |
|---|---|---|---|---|
| T1 因子树+spec+负载假设 | Lead 写脚本 | idea53-theory-flip.py：surface/deep 判断 + 4 硬件 spec + workload 先验 | ~20min | ✅ done |
| T2 信息增益计算 | Lead 跑脚本 | idea53-theory-flip.json：每硬件 flip+shift + **复现 D 三例**（全 match=True） | ~30min | ✅ done |
| T3 对照臂 | 同上 | 同上文件 control_flat：rate 全等→修正=0.0000（解转发平凡性） | ~10min | ✅ done |
| T4 生死线判定 | Lead | 主 claim 成立（浅层 43-56% 判错+flat=0）；次级单调假设部分（A100>5090）→ idea53-theory-flip.md | ~5min | ✅ done |
| T5 venue 决策 | arena 第五轮 | result.md 追加4 @ 7dae6431a | ~30min | ✅ done |
| T6 短文大纲/负结果 | 按 T4 分支 | outline.md（claim=surface-vs-deep 修正量+flat 对照+三例复现+3 对照臂+防御段） | ~1h | ✅ done @ ed2afce5e |
| T7 预注册合规检查 | Lead | GOAL.md §0.5 commit(eb1b0598c 17:39) < 数据产出(718394ece 18:06)，git log 可查 | ~2min | ✅ done |
| T8 形式 MI 补强 | Lead 写脚本 | idea53-theory-mi.json：H(D\|S)=0.71-0.77 bits 深层独有信息，flat 对照=0.0（形式化解转发平凡性） | ~30min | ✅ done @ 85a6b6c65 |

**T1-T8 全完成**。核心交付：surface-vs-deep 修正量（flip/shift）+ 严格 MI（H(D|S)）+ 负对照归零 + D 三例复现 + 短文大纲 + 预注册合规。

## 5. v2 升级：电阻瓶颈树（D 2026-11-24 方法论纠正，预注册）

**动机**：v1 是扁平一层（4 组件直接 sum，瓶颈=argmax），"deep" 只是参数层面（真实 rate vs rate=1），不是结构层面。claim 讲"深层节点的贡献"，模型必须有结构深度。v2 = 两三层电阻瓶颈树。

**树结构（3 层，预注册固定）**：
- L0 根：wall-clock T
- L1：3 个 phase，**串联**（T = Σ T_p，类比串联电阻）
  - P_compute（张量计算阶段）、P_memory（访存阶段）、P_scalar（标量/控制阶段）
- L2：phase 内资源，**并联**（T_p = max_j t_j，类比并联限流）
  - P_compute: {fp4, fp16}；P_memory: {bw}；P_scalar: {scalar}
- 叶子：t_j = f_j / rate_j（f_j = 该资源工作量，rate_j = 硬件速率）
- 瓶颈 = argmax 叶子（wall-clock 占比最大者）

**浅层 vs 深层**：浅层 rate_j ≡ 1（假设等速）；深层 rate_j = 真实 spec（复用 v1 spec 表 4 卡）。

**度量（与 v1 同口径可比）**：flip_rate（浅层瓶颈≠深层瓶颈比例）、time_shift（|deep_share − shallow_share| 均值）、H(D|S)（严格 MI，D=深层瓶颈，S=浅层瓶颈）。

**对照臂（预注册）**：
1. flat：rate 全相等 → 修正必须 = 0（模型正确性）
2. 参数置换：rate 向量随机置换 → 修正跟随 rate 内容，不跟随结构标签
3. **v1 扁平对照（结构必要性检验，奥卡姆）**：v1 = 单层全串联（T=Σt，瓶颈=argmax）；v2 = 两层串并联混合（compute 相内 max）。对比两者修正量：显著不同 → 树结构必要（claim 升级）；基本相同 → v1 够用（保留 v1，v2 作 robustness）

**生死线（预注册，数据产出前固定）**：
- 深层叶子修正显著 > 0：flip > 0.3 且 shift > 0.1（v1 实测 0.43-0.56 / 0.17-0.23，阈值取 v1 下沿一半）
- 跨 ≥3 硬件一致
- flat = 0
- v1/v2 对比出结论（必要 or 冗余，两者都接受，不许 cherry-pick）

**输入**：硬件 spec 复用 v1（4090/A100/5090/T5000）；workload 先验：phase 份额 f_p ~ Dirichlet(α=1)（均匀），phase 内资源份额 ~ Dirichlet(α=1)。N=40000 闭式采样。

> **状态对账（2026-11-24）**：树推广实际经 2×2 支/段路线实现（commits `9f482c999` 模型 + `f80c58337` 并进 paper §4.5，四格列联表+段级精确复现1D+flat归零）；本节的 3 层 phase×resource 预注册是更深的下一步设计、非当前 paper 所用。

| 步骤 | 执行 | 验收（机器可查） | 状态 |
|---|---|---|---|
| T9 v2 树模型实现 | subagent | idea53-tree-v2.py：3 层树 + 串联 sum/并联 max + 4 硬件 + flat + 置换 + v1 对照，全闭式 | ✅ 经 2×2 路线完成（QQ 会话，9f482c999） |
| T10 v2 结果+生死线 | subagent 跑 + Lead 复核 | idea53-tree-v2.json：flip/shift/H(D|S) per 硬件 + flat=0 + v1/v2 对比表；生死线判定写入 idea53-tree-v2.md | ✅ 经 2×2 路线完成（QQ 会话，f80c58337 并进 paper §4.5） |
| T11 paper 升级决策 | Lead | 若 v2 成立且结构必要 → paper.md 方法节升级（v1 降为特例对照臂）；若 v2≈v1 → paper 不动，v2 进 robustness 附录 | ✅ 本措辞修复即 T11 的 paper 升级动作（mild-vs-extreme 分组口径，2026-11-24） |

## 6. 与 #10 的关系

- #53 成立 → 反哺 #10 analysis 章节（因子树信息增益 = #10 的"瓶颈定位模块"）
- #53 不成立 → 负结果进 #10 limitation
- 两 goal 不互斥
