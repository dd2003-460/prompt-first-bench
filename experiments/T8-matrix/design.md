# T8 矩阵实验设计（v1）

依据：tasks/T8-prompt-ablation.md（轴定义 + Part C/D 协议）。本文件只登记**已执行/进行中**的 run，未开跑的变体不预写。

## M8 口径（复用 intermediate-rounds-audit.md §口径定义）
M8 = Σ(核验条目通过三测的权重) / Σ(全部核验条目权重)；权重 = 通道 conf（独立 LLM 交叉 1.0 / agent 自检 0.2 / 未执行 0）。表演型质疑计 0 且单列。

## 已落点（V-full × T-select，行为层）
| # | run | 域 | M8 | verdict | 工件 |
|---|-----|----|----|---------|------|
| 1 | T6 r1 | 机械键盘选购 | 0.93 | pass | loop-artifacts/stages/（无域后缀，N1 前）+ T8-audit/intermediate-rounds-audit.md |
| 2 | T7.1 | 会议室预约系统 | 1.00 | pass (conf-0.2 自复核) | loop-artifacts/stages/T7.1-* + T8-audit/t71-meeting-volume-C.md |
| 3 | T8-matrix-run-r1 | 待定（任务书 tasks/T8-matrix-run-r1.md 已 push） | pending | — | runs/tselect-vfull-r1/ |

## 待开跑（顺序门禁：r1 完成 + top-k 嫌疑段由 C2 行为代理指标定出后才开 C3 paired runs）
- C2 行为代理指标计算（零成本，对已有工件直接算）→ 定 top-k≤3 嫌疑段
- C3: V-noralph 等变体 paired runs（一次删一段，含阳性对照 V-nofreeze）
- Part D: V-arena-native 对比 run

## 结构约定
- run 目录：runs/<task-type>-<variant>-<domain>/（m8-scorecard.md + 关键工件指针）
- stages/ 工件命名：<domain>-<file>.md（N1 规范，r1 起执行）
