# N291: 本地 NVMe SSD 阵列扩容的最小物理粒度为单块 SSD 容量（1.92TB 或 3.84TB），若需精确扩容 ΔC_TB，实际购买容量 C_buy = c

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N136

## Claim

本地 NVMe SSD 阵列扩容的最小物理粒度为单块 SSD 容量（1.92TB 或 3.84TB），若需精确扩容 ΔC_TB，实际购买容量 C_buy = ceil(ΔC_TB / C_ssd) * C_ssd，浪费率 w = (C_buy - ΔC_TB) / C_buy，当 ΔC_TB 远小于 C_ssd 时 w 可高达 50%，远高于 N136 所述的 3-5% 常态浪费。

## Corrected Claim

本地 NVMe SSD 阵列扩容的最小物理粒度为单块 SSD 容量（1.92TB 或 3.84TB），若需精确扩容 ΔC_TB，实际购买容量 C_buy = ceil(ΔC_TB / C_ssd) * C_ssd，浪费率 w = (C_buy - ΔC_TB) / C_buy，当 ΔC_TB 远小于 C_ssd 时 w 可高达 50%，远高于 N136 所述的 3-5% 常态浪费。

## Evidence

父节点级核验未通过：不完备（父节点核心在于定义‘最小物理粒度’导致的离散化扩容逻辑及其高浪费率（w）的计算与阈值对比。现有的唯一子节点仅提供了用于计算浪费‘货币价值’的价格参数，完全缺失了对父节点中数学公式（ceil逻辑、w计算公式）、物理约束（SSD容量规格）以及关键结论（w可达50% vs 3-5%常态）的分解覆盖。）

## Search Query

RAID expansion minimum granularity waste ratio SSD size
