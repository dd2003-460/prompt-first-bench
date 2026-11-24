# N234: 工作点2（中性价比最优）：H_l1=0.90, H_l2=0.95，RTT_user_edge_tail_p99=50ms，T_proc_edge=8ms，L1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

工作点2（中性价比最优）：H_l1=0.90, H_l2=0.95，RTT_user_edge_tail_p99=50ms，T_proc_edge=8ms，L1 Miss项=0.10*25ms=2.5ms，L2 Miss项=0.10*0.05*60ms=0.3ms，P99_tail ≈ 60.8ms，满足 T=150ms。

## Corrected Claim

工作点2（中性价比最优）：H_l1=0.90, H_l2=0.95，RTT_user_edge_tail_p99=50ms，T_proc_edge=8ms，L1 Miss项=0.10*25ms=2.5ms，L2 Miss项=0.10*0.05*60ms=0.3ms，P99_tail ≈ 60.8ms，满足 T=150ms。

## Evidence

先验知识/题面给定，逻辑校验通过：各项延迟相加（50+8+2.5+0.3=60.8ms）与结论一致，且满足150ms约束。
