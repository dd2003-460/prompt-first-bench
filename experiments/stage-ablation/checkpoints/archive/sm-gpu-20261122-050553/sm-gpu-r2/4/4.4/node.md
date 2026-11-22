# N23: 高成本低性能工作点：1×A100 40GB 方案，TCO_3yr = $15000 + (0.4kW × 8760h × 3 × $0.10) ≈ $15000

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5, N6

## Claim

高成本低性能工作点：1×A100 40GB 方案，TCO_3yr = $15000 + (0.4kW × 8760h × 3 × $0.10) ≈ $15000 + $1051 = $16051；优势是单卡部署简化运维，劣势是显存容量大但吞吐量受限于单卡带宽。

## Corrected Claim

1×A100 40GB 方案，假设硬件成本为 $15,000，功耗为 0.4kW，电价 $0.10/kWh，则 3 年 TCO ≈ $16,051。优势是单卡部署简化运维，劣势是吞吐量受限于单卡带宽。

## Evidence

父节点级核验未通过：不完备（子节点在成本（TCO）、计算性能（吞吐量）和显存约束（KV Cache）三个维度上划分清晰，无重复或矛盾，正交性良好。但父节点明确提到了‘单卡部署简化运维’这一优势，而子节点仅涵盖了劣势（成本修正、带宽瓶颈、显存限制），完全遗漏了对运维/部署优势的分析，导致覆盖不全。）

## Search Query

A100 40GB 3 year TCO calculation electricity cost
