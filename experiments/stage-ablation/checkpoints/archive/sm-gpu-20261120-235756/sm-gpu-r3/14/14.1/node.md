# N364: 分子项'实际测得 TPOT 倒数'的量化公式：Throughput = 1 / TPOT_measured，其中 TPOT_measured = TPOT_th

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N138

## Claim

分子项'实际测得 TPOT 倒数'的量化公式：Throughput = 1 / TPOT_measured，其中 TPOT_measured = TPOT_theoretical / Utilization_Factor，且 Utilization_Factor = (Observed_Tokens_per_s / Theoretical_Max_Tokens_per_s)，需针对 Qwen3-27B MoE 架构在特定硬件上的实测校准系数（通常 0.4-0.6）进行实例化。

## Corrected Claim

分子项'实际测得 TPOT 倒数'的量化公式：Throughput = 1 / TPOT_measured，其中 TPOT_measured = TPOT_theoretical / Utilization_Factor，且 Utilization_Factor = (Observed_Tokens_per_s / Theoretical_Max_Tokens_per_s)，需针对 Qwen3-27B MoE 架构在特定硬件上的实测校准系数（通常 0.4-0.6）进行实例化。

## Evidence

先验知识/题面给定，逻辑校验通过：吞吐量与延迟（TPOT）互为倒数关系符合定义，利用率因子作为理论值与实测值的比值在逻辑上自洽，且0.4-0.6的校准系数范围符合MoE大模型在典型硬件上的工程经验。
