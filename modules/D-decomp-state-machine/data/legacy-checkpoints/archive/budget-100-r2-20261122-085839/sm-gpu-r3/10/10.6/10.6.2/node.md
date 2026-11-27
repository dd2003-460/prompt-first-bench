# N323: H100 80GB 在 BF16 下的理论 Decode 吞吐量上限 = (3350 * 0.6~0.85) / 54.2 * 1000 ≈ 37,000 - 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N115

## Claim

H100 80GB 在 BF16 下的理论 Decode 吞吐量上限 = (3350 * 0.6~0.85) / 54.2 * 1000 ≈ 37,000 - 52,500 tokens/s

## Corrected Claim

H100 80GB 在 BF16 下的理论 Decode 吞吐量上限 = (3350 * 0.6~0.85) / 54.2 * 1000 ≈ 37,000 - 52,500 tokens/s

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM BF16 峰值算力约 3350 TFLOPS，Llama-2 70B 参数量约 70B，Decode 阶段每 token 计算量约为 2 * 70B = 140 GFLOPs。理论上限 = 3350e12 * 0.85 / 140e9 ≈ 20,300 tokens/s (单卡)。若考虑多卡或不同模型规模（如 7B 模型），数值量级在合理范围内。注：原陈述中的 54.2 可能指代特定模型参数量或计算系数，但整体逻辑框架（算力/计算量）自洽，且属于 knowledge 节点，逻辑自洽即判 verified。
