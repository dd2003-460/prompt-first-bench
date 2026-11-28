# N706: 两类错误对科研循环可信度的量化影响：SDC 导致结论错误的概率 P(wrong | SDC) ≈ 1.0（若未被检测），而 CUDA Error 导致的结果丢弃

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N258

## Claim

两类错误对科研循环可信度的量化影响：SDC 导致结论错误的概率 P(wrong | SDC) ≈ 1.0（若未被检测），而 CUDA Error 导致的结果丢弃率 P(discard | Crash) = 1.0，但可通过 checkpoint 恢复避免进度丢失，净损失仅为当前迭代剩余时间。

## Corrected Claim

两类错误对科研循环可信度的量化影响：SDC 导致结论错误的概率 P(wrong | SDC) ≈ 1.0（若未被检测），而 CUDA Error 导致的结果丢弃率 P(discard | Crash) = 1.0，但可通过 checkpoint 恢复避免进度丢失，净损失仅为当前迭代剩余时间。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

silent data corruption impact on scientific simulation result validity
