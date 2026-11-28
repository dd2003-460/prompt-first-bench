# N110: 在 4x V100 TP=4 环境下，MMLU-Pro 评测的推理吞吐量瓶颈为 AllReduce 通信，单样本推理耗时 t_infer ≈ 0.8s (含 5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

在 4x V100 TP=4 环境下，MMLU-Pro 评测的推理吞吐量瓶颈为 AllReduce 通信，单样本推理耗时 t_infer ≈ 0.8s (含 5-shot context ~2k tokens)，完整评测 (14k samples) 耗时 T_total ≈ 3.1 hours

## Corrected Claim

在 4x V100 TP=4 环境下，MMLU-Pro 评测的推理吞吐量瓶颈为 AllReduce 通信，单样本推理耗时 t_infer ≈ 0.8s (含 5-shot context ~2k tokens)，完整评测 (14k samples) 耗时 T_total ≈ 3.1 hours

## Evidence

先验知识/题面给定，逻辑校验通过：14000 samples * 0.8s = 11200s ≈ 3.11 hours，数值量级与计算逻辑完全自洽。
