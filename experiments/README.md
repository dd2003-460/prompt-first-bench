# pfb 实验索引（T8 prompt-first 消融研究）

| 目录 | 内容 | 状态 |
|------|------|------|
| T8-audit/ | Part A: 中间轮次真实性审计（三测协议：具体性/可证伪/反事实） | in-progress |
| T8-audit/decomp-bench-volume-B.md | Part A 分卷 B: decomp-bench ablation-L1 review 记录（r4 报告 + arena Q1-Q5），含 F2 复算（C2 数据勘误+正式检验） | done（已回写 r4 原文 @ decomp-bench 686e460） |
| T8-audit/t71-meeting-volume-C.md | Part A 分卷 C: T7.1 会议室域审计（X1-X13/A1-A14/U1-U18 三测，M8=1.00 形式真实性满分，成本模型 exit 0 复跑） | done |
| T8-lit/ | Part B: 文献调研（multi-stage pipeline prompt 贡献度等 ≥4 问） | pending |
| T8-matrix/ | 矩阵实验 (任务类型 × prompt 变体)：design.md + runs/ + report.md | pending |
| T8-arena-compare/ | Part D: arena-native vs pfb 流程对比（7 维度） | pending |

设计依据：`tasks/T8-prompt-ablation.md`（v6 三机分工版）。
