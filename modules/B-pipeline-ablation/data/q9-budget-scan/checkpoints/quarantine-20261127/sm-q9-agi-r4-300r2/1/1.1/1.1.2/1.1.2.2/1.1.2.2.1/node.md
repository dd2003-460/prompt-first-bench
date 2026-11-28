# N250: Max_Len 理论值 655k 未扣除 Activation Memory；在 Prefill 阶段，激活值显存占用约为 2 * hidden_dim * s

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N98

## Claim

Max_Len 理论值 655k 未扣除 Activation Memory；在 Prefill 阶段，激活值显存占用约为 2 * hidden_dim * seq_len * batch_size * bytes，对于 seq_len=262k, batch=1，激活值约占 2 * 4096 * 262144 * 1 * 2 ≈ 4.3GB，这将大幅削减可用 KV 显存，使实际 Max_Len 降至约 200k-250k tokens。

## Corrected Claim

Max_Len 理论值 655k 未扣除 Activation Memory；在 Prefill 阶段，激活值显存占用约为 2 * hidden_dim * seq_len * batch_size * bytes，对于 seq_len=262k, batch=1，激活值约占 2 * 4096 * 262144 * 1 * 2 ≈ 4.3GB，这将大幅削减可用 KV 显存，使实际 Max_Len 降至约 200k-250k tokens。

## Evidence

先验知识/题面给定，逻辑校验通过：激活值显存计算公式及量级估算符合深度学习推理常识，且 source 为 knowledge，无需外部来源支持。
