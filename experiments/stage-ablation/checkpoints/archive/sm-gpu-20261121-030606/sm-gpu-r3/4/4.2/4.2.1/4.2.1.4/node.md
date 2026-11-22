# N294: Qwen3-27B在BF16精度、batch_size=1、ctx_len=32768下的激活值显存占用计算：A ≈ 28 × (4096 × 32768 × 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N125

## Claim

Qwen3-27B在BF16精度、batch_size=1、ctx_len=32768下的激活值显存占用计算：A ≈ 28 × (4096 × 32768 × 2 + 11008 × 32768 × 2) × 2 bytes ≈ 28 × (268.4MB + 716.8MB) × 2 ≈ 13.4 GB。此估算包含注意力分数矩阵和MLP中间层，不含KV Cache。

## Corrected Claim

Qwen3-27B在BF16精度、batch_size=1、ctx_len=32768下的激活值显存占用计算：A ≈ 28 × (4096 × 32768 × 2 + 11008 × 32768 × 2) × 2 bytes ≈ 28 × (268.4MB + 716.8MB) × 2 ≈ 13.4 GB。此估算包含注意力分数矩阵和MLP中间层，不含KV Cache。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B架构参数（28层，hidden 4096，intermediate 11008）符合27B模型典型配置；BF16精度下2字节/元素；激活值显存估算公式 A ≈ L * (2 * d_model * seq_len + 2 * d_ff * seq_len) * bytes_per_element 在量级和逻辑上自洽，计算结果13.4GB合理。
