# N235: 工作点3（高成本低性）：H_l1=0.80, H_l2=0.90，RTT_user_edge_tail_p99=60ms，T_proc_edge=12ms，L1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

工作点3（高成本低性）：H_l1=0.80, H_l2=0.90，RTT_user_edge_tail_p99=60ms，T_proc_edge=12ms，L1 Miss项=0.20*30ms=6ms，L2 Miss项=0.20*0.10*80ms=1.6ms，P99_tail ≈ 79.6ms，满足 T=200ms 但回源成本占比高。

## Corrected Claim

工作点3（高成本低性）：H_l1=0.80, H_l2=0.90，RTT_user_edge_tail_p99=60ms，T_proc_edge=12ms，L1 Miss项=0.20*30ms=6ms，L2 Miss项=0.20*0.10*80ms=1.6ms，P99_tail ≈ 79.6ms，满足 T=200ms 但回源成本占比高。

## Evidence

先验知识/题面给定，逻辑校验通过：各项延迟相加（60+12+6+1.6=79.6ms）符合线性叠加模型，且79.6ms < 200ms，数值量级与逻辑自洽。
