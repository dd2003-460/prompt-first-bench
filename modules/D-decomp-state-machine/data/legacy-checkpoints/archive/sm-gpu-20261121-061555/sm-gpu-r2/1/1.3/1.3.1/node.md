# N46: Tesla P40 (Pascal) 的二手市场价格区间为 $300-$500，显存 24GB GDDR5，带宽 348 GB/s，TDP 250W；其缺乏 F

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

Tesla P40 (Pascal) 的二手市场价格区间为 $300-$500，显存 24GB GDDR5，带宽 348 GB/s，TDP 250W；其缺乏 FP16/BF16 硬件加速，仅支持 INT8/FP32，需核实其在 LLM 推理中的实际吞吐量（tokens/s）及功耗效率，以评估其作为极致低成本方案的可行性 [待核验]

## Corrected Claim

Tesla P40 (Pascal) 显存 24GB GDDR5，带宽 348 GB/s，TDP 250W；其架构对 FP16/BF16 支持有限（无原生 BF16，FP16 性能较低），主要支持 INT8/FP32。二手市场价格波动较大，需实时查询市场数据以评估其作为低成本方案的可行性。

## Evidence

[质询]该陈述包含具体的硬件规格（显存、带宽、TDP）和市场行情（价格区间），属于经验事实。虽然P40的规格（24GB GDDR5, 348GB/s, 250W）在技术上是准确的，但二手市场价格波动较大且随时间变化，$300-$500的区间可能因地区、成色和市场供需而显著偏离，且缺乏实时来源支持。此外，'缺乏FP16/BF16硬件加速'的表述虽在Pascal架构上基本成立（Pascal主要优化FP32/INT8，FP16性能较低且无BF16支持），但具体吞吐量需实测，无法仅凭规格推断。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。P40硬件规格符合Pascal架构特征，但价格区间和具体推理性能缺乏外部证据验证。

## Search Query

Tesla P40 LLM inference benchmark tokens per second INT8 used price
