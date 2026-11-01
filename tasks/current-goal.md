# 当前 Goal：RV3G8-ablation-attribution

【目标】正式矩阵消融归因分析——用双裁判盲评的变体总分+维度均值矩阵，拆解 D1（候选集构造规则）与 D2（边界类型声明）各自的贡献，对照 pilot 9-run 排序，产出归因小节草稿供 DRAFT v2 §3.1 第二步并入。

【阶段】rubric-v3 正式实验（7 变体 × 3 run = 21 答卷 + 双裁判盲评已完成收口 @ r180），进入归因分析阶段。

【SOP 索引】tasks/ralph-loop-runner.md（runner 循环协议）；DRAFT-rubric-v3-v2.md §3.1（pilot→定维度流程）；bench/rubric-v3/ablation/formal-matrix/blind-eval/BLIND-EVAL-REPORT.md（输入数据）。

【验收标准】① 归因矩阵落盘 formal-matrix/attribution-analysis.md（D1/D2 主效应 + 交互，每变体对 V0-baseline 的 Δ 分按维度拆解）；② sham 对照检验通过（V-sham/V3-sham 与对应真实变体的差 ≤ 噪声带，否则触发占位块长度/位置混杂讨论）；③ 结论带同判官限定语（非独立 IRR）+ O3 结构性缺口单列；④ 数字全部可从 judge-{1,2}-scores.json 复算（附复算脚本或命令）。

【失败降级】数据不足以支撑某项归因 → 如实标注 unverified 并说明缺什么，不硬凑结论。
