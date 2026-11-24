# TASK-IDEA53 分解树（1-loop 01 · goal: idea53-cross-gradient）

> 2026-11-24 · D 指令"定 idea53 这个目标"。本文件 = 分解树 + 正交性核对 + 缺口 + 任务表。
> 预注册锚点：GOAL.md @ 20c029300（16:18，早于一切数据产出）。

## 1. 分解树（S1-S5 正交子项）

| 子项 | 一句话问题 | 落地答案 | conf |
|---|---|---|---|
| S1 标签构造 | V_coarse/V_fine 怎么标？ | V_coarse=is_bottleneck 词表（已有）；V_fine=27b judge 判"是否含具体哪一环的定位"（降级=机制词正则）。判据已预注册（GOAL.md §4），不用深度信息 | 0.8 |
| S2 交叉梯度计算 | 两条梯度各层值？ | I(L_k;V_coarse) + I(L_k;V_fine\|V_coarse)，闭式 MI 纯离线（复用 idea53-info-theoretic-contribution.py 框架）。三源：rep-scan/t53b/stage-ablation | 0.9（方法已验证，第三轮跑过） |
| S3 对照臂 | 怎么排除平凡解释？ | 四条：深度置换（MI→0）/ fake-run 占位（MI→0）/ 浅深配平 / 层内类型对照（解 type×depth 混淆）。arena 第四轮 82a67df96 指定 | 0.8 |
| S4 生死线判定 | claim 成不成立？ | fine-conditional 随深度升（L4>L1，三源一致）→ 成立；不升 → 死，出负结果记录（排除"深层整体贡献大"的误读版 claim） | 0.9（判据已预注册） |
| S5 投稿策略 | 发哪、概率多少？ | arena 第五轮回执（对标/免费 venue/概率/最快路径）。held-out=stage-ablation 域（预注册） | 待 arena |

## 2. 正交性核对

- S1→S2 单向依赖（标签是计算的输入），S3 依赖 S2（对照臂算的是同一组 MI），S4 依赖 S2+S3，S5 独立并行（不依赖数据）
- 两两输入/输出无重叠：S1 出标签、S2 出 MI 值、S3 出对照臂 MI、S4 出判定、S5 出 venue 决策
- 时间轴：S1→S2→S3→S4 串行（数据链）；S5 并行（已在跑）

## 3. 缺口标注

- S1：V_fine 27b 打标质量未验证（需抽样人核一致性 ≥0.7，否则用降级判据并标注）
- S2：三源 level 口径不同（第三轮已确认不可合并，分源报告）
- S4：held-out 域只有 stage-ablation 一个（外部树复验缺，投稿时标 gap）
- S5：arena 第五轮未回（venue 概率数字缺）

## 4. 任务表（机器可查验收 + 耗时）

| 步骤 | 执行 | 验收（机器可查） | 耗时 | 状态 |
|---|---|---|---|---|
| T1 V_fine 打标 | subagent deleg_53e3a082 | idea53-cross-gradient.json 含 v_fine_labels 字段，n≥3 源节点数 | ~30min | running |
| T2 两条梯度 | 同上 | 同上文件含 i_coarse[i][layer] + i_fine_cond[i][layer]，三源 | ~10min | 排队 |
| T3 对照臂×4 | 同上 | 同上文件含 controls 字段（4 臂各层值） | ~10min | 排队 |
| T4 生死线判定 | Lead 读 json 一行判 | 结论落盘 .md（升/不升 + 三源一致性） | ~5min | 排队 |
| T5 venue 决策 | arena 第五轮 | result.md 追加4 小节 commit（对标+venue+概率）@ 7dae6431a | ~30min | ✅ done |
| T6 短文大纲/负结果 | 按 T4 分支 | 成立→outline.md（claim/方法/结果/对照/limitation）；不成立→negative-result.md；含 W2 预注册冻结（OpenReview/OSF 免费存档） | ~1h | 排队 |
| T7 预注册合规检查 | Lead | GOAL.md commit 时间(20c029300 16:18) < T1 数据产出时间（git log 可查） | ~2min | 排队 |

总耗时 ~2.5h（T1-T4 串行 + T5 并行），无外部依赖（27b 本地 + arena 免费）。

## 5. 与 #10 的关系

- #53 成立 → 反哺 #10 analysis 章节（交叉梯度 = #10 的"瓶颈定位模块"，arena 第三/四轮一致建议）
- #53 不成立 → 负结果进 #10 limitation（"层→瓶颈判定信息量极小"本身是可发表分析发现）
- 两 goal 不互斥，#53 数据全部可复用进 #10
