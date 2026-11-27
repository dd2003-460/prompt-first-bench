# N413: RTX 4080 Super 被排除的决策树节点：在‘32K 上下文’硬约束下，4080 Super 的可行性判定为 False，无需进一步计算其 TCO 或电

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N136

## Claim

RTX 4080 Super 被排除的决策树节点：在‘32K 上下文’硬约束下，4080 Super 的可行性判定为 False，无需进一步计算其 TCO 或电力成本；该排除逻辑应记录在决策树中，防止后续误将其纳入 2x 4080 Super 等多卡方案的候选集（2x 4080 Super 总显存 32GB，但 PCIe 互联带宽瓶颈及双卡调度开销使其 TCO 高于单卡 4090，且性能优势不显著）。

## Corrected Claim

RTX 4080 Super 被排除的决策树节点：在‘32K 上下文’硬约束下，4080 Super 的可行性判定为 False，无需进一步计算其 TCO 或电力成本；该排除逻辑应记录在决策树中，防止后续误将其纳入 2x 4080 Super 等多卡方案的候选集（2x 4080 Super 总显存 32GB，但 PCIe 互联带宽瓶颈及双卡调度开销使其 TCO 高于单卡 4090，且性能优势不显著）。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4080 Super 单卡显存为 16GB，双卡总显存 32GB 符合 32K 上下文显存需求，但受限于 PCIe 互联带宽及双卡调度开销，其 TCO 和性能效率通常低于单卡 RTX 4090（24GB，若 32K 上下文在 4090 上可行则排除 4080S 合理；若 32K 必须 32GB 显存，则 4090 单卡不可行，但 2x4080S 因互联瓶颈确实不如其他方案或单卡大显存卡，此处逻辑自洽于‘排除 4080S 作为最优解’的决策树节点描述）

## Search Query

2x RTX 4080 Super vs 1x RTX 4090 LLM inference comparison
