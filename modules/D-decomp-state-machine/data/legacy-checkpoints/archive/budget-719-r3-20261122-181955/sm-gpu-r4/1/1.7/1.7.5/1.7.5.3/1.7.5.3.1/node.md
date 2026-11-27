# N668: L40S 在 32K 上下文 BF16 精度下的显存余量与并发能力：48GB 显存 - 54GB 权重（BF16）= -6GB，显存不足，必须使用 INT8 量

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N238

## Claim

L40S 在 32K 上下文 BF16 精度下的显存余量与并发能力：48GB 显存 - 54GB 权重（BF16）= -6GB，显存不足，必须使用 INT8 量化（权重 27GB）或 FP8（权重 27GB），剩余显存 = 48 - 27 - 2 = 19GB，可支持 19GB / 8GB = 2.375，即最大 2 个并发请求 [knowledge: '模型先验知识：显存容量计算'] [修正自矛盾检测：N380 指出 BF16 权重 54GB 无法在 32GB 卡上运行，同理 L40S 48GB 也无法加载 BF16 权重]

## Corrected Claim

L40S 在 32K 上下文 BF16 精度下的显存余量与并发能力：48GB 显存 - 54GB 权重（BF16）= -6GB，显存不足，必须使用 INT8 量化（权重 27GB）或 FP8（权重 27GB），剩余显存 = 48 - 27 - 2 = 19GB，可支持 19GB / 8GB = 2.375，即最大 2 个并发请求 [knowledge: '模型先验知识：显存容量计算'] [修正自矛盾检测：N380 指出 BF16 权重 54GB 无法在 32GB 卡上运行，同理 L40S 48GB 也无法加载 BF16 权重]

## Evidence

先验知识/题面给定，逻辑校验通过：L40S 48GB 显存无法容纳 54GB BF16 权重，量化至 INT8/FP8 后权重约 27GB，剩余显存约 19GB，按每请求 8GB 估算可支持 2 个并发，计算逻辑自洽且符合工程常识。
