# N126: 多卡方案的带宽聚合效应：双卡 RTX 3090 (NVLink) 总带宽 ~1872GB/s，但 KV Cache 需跨卡同步，有效带宽降至 ~900GB/s 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

多卡方案的带宽聚合效应：双卡 RTX 3090 (NVLink) 总带宽 ~1872GB/s，但 KV Cache 需跨卡同步，有效带宽降至 ~900GB/s (NVLink 112.5GB/s 为瓶颈)；双卡 L40S (PCIe 4.0) 总带宽 ~1728GB/s，但有效带宽降至 ~64GB/s (PCIe 瓶颈)，导致多卡方案在长上下文下性能优势可能消失

## Corrected Claim

多卡方案的带宽聚合效应：双卡 RTX 3090 (NVLink) 总带宽 ~1872GB/s，但 KV Cache 需跨卡同步，受 NVLink 带宽（双向 225GB/s）限制，有效带宽显著降低；双卡 L40S (PCIe 4.0) 总带宽 ~1728GB/s，但受 PCIe 带宽（双向 ~64GB/s）限制，有效带宽大幅降低，导致多卡方案在长上下文下性能优势可能减弱或消失，具体取决于通信与计算的优化程度。

## Evidence

[质询]数值量级与物理直觉存在矛盾：双卡L40S通过PCIe 4.0 x16连接，理论单向带宽约32GB/s，双向约64GB/s。虽然64GB/s作为PCIe瓶颈的数值在量级上是合理的，但将其直接等同于'有效带宽'并断言'性能优势消失'过于绝对，忽略了计算与通信重叠（overlap）以及KV Cache同步并非每层都需全量同步等优化手段。此外，RTX 3090 NVLink带宽为225GB/s（双向），而非112.5GB/s（单向），若按双向计算，瓶颈应为225GB/s，而非112.5GB/s，导致900GB/s的有效带宽估算缺乏严谨推导。 | 先验知识/题面给定，逻辑校验发现NVLink带宽数值混淆（单向vs双向）及有效带宽估算过于简化，缺乏对通信-计算重叠等关键因素的考量，故降级。

## Search Query

multi-GPU LLM inference NVLink vs PCIe bandwidth bottleneck
