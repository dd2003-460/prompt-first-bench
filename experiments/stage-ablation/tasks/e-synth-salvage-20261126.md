# E-SYNTH salvage（deleg_eeae304a 死于 27b 输出上限，0 产出）

# origin: ai · 2026-11-26 · 从 transcript result 行提取，供 S1 sub 起点用（非权威，以数据文件重算为准）

## Q7 预算扫描（sub 死前算出的部分，口径=judge_v1，CI 为 95%）
- budget 50 (nnodes [50,50,50]): cov 0.1026 [0.0473, 0.1578] | depth 0.6 | total 0.3513
- budget 100 (nnodes [150,150,150]): cov 0.1795 [0.1065, 0.2524] | depth 0.8 | total 0.4897
- （150/300/719 档未及算出——从 q7-scan-scores.json 重算）

## 死因
读了 6 个输入文件（含 243 行的 k7-pareto-newjudge.md）后撞输出上限，4 次续写全截断。
缓解：S1 只读 4 个数据文件（json 为主），写 1 个 json，不写 prose；S2 只读 S1 产出 + 2 个 md。
