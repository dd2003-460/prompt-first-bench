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
| T6 短文大纲/负结果 | 按 T4 分支 | 成立→outline.md（claim=surface-vs-deep 修正量+flat 对照+三例复现）；含 W2 预注册冻结 | ~1h | 排队 |
| T7 预注册合规检查 | Lead | GOAL.md §0.5 commit(eb1b0598c) 时间 < T2 数据产出时间（git log 可查） | ~2min | 排队 |
| T8 形式 MI 补强 | 待派 | flip/shift→H(surface)-H(surface\|deep) 严格互信息（审稿防御：当前是可解释得分非 MI） | ~30min | 排队 |

总耗时 ~1.5h（T1-T4 已完），无外部依赖（纯数学 + 本地 spec 文件）。

## 5. 与 #10 的关系

- #53 成立 → 反哺 #10 analysis 章节（因子树信息增益 = #10 的"瓶颈定位模块"）
- #53 不成立 → 负结果进 #10 limitation
- 两 goal 不互斥
