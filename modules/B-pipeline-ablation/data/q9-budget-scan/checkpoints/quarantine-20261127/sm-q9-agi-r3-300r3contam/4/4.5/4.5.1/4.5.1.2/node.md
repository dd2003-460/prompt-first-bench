# N187: 批处理效率因子 η_batch 的定义与估算公式：η_batch = T_seq_1 / (T_seq_N / N)，其中T_seq_1为单序列推理耗时，T_s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

批处理效率因子 η_batch 的定义与估算公式：η_batch = T_seq_1 / (T_seq_N / N)，其中T_seq_1为单序列推理耗时，T_seq_N为N并发序列总耗时，用于修正E_queries_per_cycle中的线性假设偏差

## Corrected Claim

批处理效率因子 η_batch 的定义与估算公式：η_batch = T_seq_1 / (T_seq_N / N)，其中T_seq_1为单序列推理耗时，T_seq_N为N并发序列总耗时，用于修正E_queries_per_cycle中的线性假设偏差

## Evidence

先验知识/题面给定，逻辑校验通过：该定义符合批处理加速比（Speedup）的标准数学表达，量纲一致（时间/时间=无量纲因子），用于修正线性假设偏差的逻辑自洽。
