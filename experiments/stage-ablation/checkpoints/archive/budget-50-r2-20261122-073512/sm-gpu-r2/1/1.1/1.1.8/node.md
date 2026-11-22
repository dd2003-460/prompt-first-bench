# N46: 激活值 (Activations) 的峰值显存占用计算公式：A_peak = B (batch_size) × S (seq_len) × H (hidden_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

激活值 (Activations) 的峰值显存占用计算公式：A_peak = B (batch_size) × S (seq_len) × H (hidden_dim) × P (bytes_per_param) × K (layers)

## Corrected Claim

激活值 (Activations) 的峰值显存占用计算公式：A_peak = B (batch_size) × S (seq_len) × H (hidden_dim) × P (bytes_per_param) × K (layers)

## Evidence

先验知识/题面给定，逻辑校验通过
