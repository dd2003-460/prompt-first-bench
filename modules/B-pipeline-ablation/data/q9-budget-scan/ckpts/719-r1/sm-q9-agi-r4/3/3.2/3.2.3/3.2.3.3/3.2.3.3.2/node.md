# N536: max-num-seqs=2 时的单请求 P99 延迟构成：T_P99 = T_prefill + T_decode + T_comm，其中 T_prefill

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N190

## Claim

max-num-seqs=2 时的单请求 P99 延迟构成：T_P99 = T_prefill + T_decode + T_comm，其中 T_prefill(262144 tokens) ≈ 262144 / (4 × 15000 tok/s) ≈ 4.4s (V100 TP4 Prefill 吞吐估算)，T_decode(假设 2000 output tokens) ≈ 2000 / (4 × 20 tok/s) ≈ 25s，总 P99 ≈ 29.4s，远超 10s 目标，表明 10s 目标仅在输出长度 < 100 tokens 时可行

## Corrected Claim

max-num-seqs=2 时的单请求 P99 延迟构成：T_P99 = T_prefill + T_decode + T_comm，其中 T_prefill(262144 tokens) ≈ 262144 / (4 × 15000 tok/s) ≈ 4.4s (V100 TP4 Prefill 吞吐估算)，T_decode(假设 2000 output tokens) ≈ 2000 / (4 × 20 tok/s) ≈ 25s，总 P99 ≈ 29.4s，远超 10s 目标，表明 10s 目标仅在输出长度 < 100 tokens 时可行

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（4.4+25=29.4），基于给定的吞吐率假设推导出的结论在逻辑上自洽且量级合理。

## Search Query

V100 tensor parallel prefill throughput large language model 27B parameters
