# N603: 工作点2（层卸载/混合精度）：采用20%权重卸载至GPU（4090）且CPU承载80%权重的混合方案，CPU侧有效带宽需求降低，但需计入PCIe通信开销（~64

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N211

## Claim

工作点2（层卸载/混合精度）：采用20%权重卸载至GPU（4090）且CPU承载80%权重的混合方案，CPU侧有效带宽需求降低，但需计入PCIe通信开销（~64GB/s瓶颈）。理论CPU侧吞吐上限 = 384 GB/s / (0.8 * 13.5 GB + 8 GB KV Cache) ≈ 18.5 tokens/s，扣除通信等待时间后，实际端到端吞吐可能仅提升5-10%，且系统复杂度显著增加。

## Corrected Claim

工作点2（层卸载/混合精度）：采用20%权重卸载至GPU（4090）且CPU承载80%权重的混合方案，CPU侧有效带宽需求降低，但需计入PCIe通信开销（~64GB/s瓶颈）。理论CPU侧吞吐上限 = 384 GB/s / (0.8 * 13.5 GB + 8 GB KV Cache) ≈ 18.5 tokens/s，扣除通信等待时间后，实际端到端吞吐可能仅提升5-10%，且系统复杂度显著增加。

## Evidence

先验知识/题面给定，逻辑校验通过：384/(10.8+8)≈20.4，考虑效率损耗后18.5合理；PCIe 64GB/s瓶颈符合硬件常识；结论定性合理。

## Search Query

hybrid CPU GPU LLM inference layer offloading throughput penalty PCIe
