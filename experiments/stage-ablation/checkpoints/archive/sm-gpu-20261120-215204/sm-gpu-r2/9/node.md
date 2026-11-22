# N37: AMD MI300X (192GB HBM3) 作为非典型候选，其单卡显存足以支持 BF16 Qwen3-27B + 32K Context 无需量化，且 HB

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

AMD MI300X (192GB HBM3) 作为非典型候选，其单卡显存足以支持 BF16 Qwen3-27B + 32K Context 无需量化，且 HBM3 带宽 (5.3 TB/s) 远高于 RTX 4090 (1 TB/s)，理论 Tokens/s 可达 90+，但软件栈 (ROCm) 对 Qwen3 的支持稳定性需验证，价格约 $20,000-25,000。

## Corrected Claim

AMD MI300X (192GB HBM3) 单卡显存足以支持 BF16 Qwen3-27B + 32K Context 无需量化，HBM3 带宽 (5.3 TB/s) 远高于 RTX 4090，理论性能潜力大，但具体推理速度（如90+ Tokens/s）及价格（$20,000-25,000）需进一步验证，且 ROCm 对 Qwen3 的支持稳定性需确认。

## Evidence

[质询]来源[1]摘要中存在明显的单位错误（将5.325 TB/s误写为5.325 TFLOPS），且该来源仅确认了硬件规格（192GB HBM3, 5.3TB/s带宽），未提供关于Qwen3-27B在ROCm上的具体推理性能（90+ Tokens/s）或价格（$20,000-25,000）的直接证据。 | 来源[1]直接支持了192GB HBM3显存和5.3TB/s带宽的硬件规格，逻辑上足以支撑BF16 Qwen3-27B + 32K Context的显存需求；但推理速度（90+ Tokens/s）和价格属于经验事实，缺乏直接来源支持，且来源摘要存在单位笔误，故降级。

## Retrieval Sources

- {'url': 'https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html&rut=6bd1d4a5b76525d5cf51f2f1fddd8511344271395216d7375ac569e93a84ee85', 'type': 'ddg', 'title': 'AMD Instinct™ MI300X Accelerators'}
