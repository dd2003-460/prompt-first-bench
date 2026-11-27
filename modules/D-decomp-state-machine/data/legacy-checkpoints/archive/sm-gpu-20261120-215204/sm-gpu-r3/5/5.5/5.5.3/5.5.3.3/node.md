# N374: 工作点 C (单卡高显存替代)：1×RTX 6000 Ada (48GB, $6,800) + 主流工作站 (~$1,500)，总 Capex ~$8,300；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N133

## Claim

工作点 C (单卡高显存替代)：1×RTX 6000 Ada (48GB, $6,800) + 主流工作站 (~$1,500)，总 Capex ~$8,300；约束：单卡无需 Tensor Parallel，PCIe 带宽瓶颈消除，但价格高，仅当 2×4090 方案因散热/噪音不可行时考虑，性价比低于 2×4090。

## Corrected Claim

工作点 C (单卡高显存替代)：1×RTX 6000 Ada (48GB, $6,800) + 主流工作站 (~$1,500)，总 Capex ~$8,300；约束：单卡无需 Tensor Parallel，PCIe 带宽瓶颈消除，但价格高，仅当 2×4090 方案因散热/噪音不可行时考虑，性价比低于 2×4090。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 6000 Ada 48GB 显存规格及约 $6,800 价格符合市场常识，单卡无需 Tensor Parallel 且消除 PCIe 瓶颈的逻辑自洽，总成本计算正确。
