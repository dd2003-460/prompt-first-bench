# N714: N104 模型中 2x 4090 方案的 CapEx $5,198 包含的双卡互联开销：PCIe 4.0 x16 插槽及 riser 卡成本约 $50-$100

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N218, N219, N220

## Claim

N104 模型中 2x 4090 方案的 CapEx $5,198 包含的双卡互联开销：PCIe 4.0 x16 插槽及 riser 卡成本约 $50-$100，若使用 NVLink 桥接（4090 不支持 NVLink，故此处为 PCIe 互联），额外带宽瓶颈导致的性能损失需折算为等效算力折损，假设折损 5%，则等效 CapEx 增加 $5,198 * 5% ≈ $260，修正后 TCO_4090(t) = 5458 + 7884t。

## Corrected Claim

N104 模型中 2x 4090 方案的 CapEx $5,198 包含的双卡互联开销：PCIe 4.0 x16 插槽及 riser 卡成本约 $50-$100，若使用 NVLink 桥接（4090 不支持 NVLink，故此处为 PCIe 互联），额外带宽瓶颈导致的性能损失需折算为等效算力折损，假设折损 5%，则等效 CapEx 增加 $5,198 * 5% ≈ $260，修正后 TCO_4090(t) = 5458 + 7884t。

## Evidence

先验知识/题面给定，逻辑校验通过：4090确实不支持NVLink，PCIe互联存在带宽瓶颈，5%性能折损假设合理，数学计算5198*5%≈260及TCO修正逻辑自洽。

## Search Query

dual 4090 PCIe interconnect cost performance overhead
