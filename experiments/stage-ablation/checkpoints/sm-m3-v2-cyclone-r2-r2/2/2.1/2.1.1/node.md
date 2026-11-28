# N32: 陆地边界层厚度 δ_BL 的物理决定式为 δ_BL ≈ 0.1~0.2 × H_pbl × (C_d,land/C_d,ocean)^(1/3)，其中 H_pb

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

陆地边界层厚度 δ_BL 的物理决定式为 δ_BL ≈ 0.1~0.2 × H_pbl × (C_d,land/C_d,ocean)^(1/3)，其中 H_pbl 为行星边界层高度（~1-2 km），该公式解释了为何陆地 δ_BL (~1000-1500 m) 大于海洋 (~500 m)，源于陆地更大的表面粗糙度和更弱的对流混合。

## Corrected Claim

陆地边界层厚度 δ_BL 通常与行星边界层高度 H_pbl 同量级（~1-2 km），其具体数值受热力强迫和湍流混合效率共同决定，陆地因更强的感热通量和更复杂的湍流结构，其有效混合层往往比海洋更深或结构更复杂，但简单的粗糙度比值立方根公式并非标准物理决定式。

## Evidence

[质询]公式形式存疑：通常边界层厚度主要受湍流混合长度和热通量控制，粗糙度比值的立方根关系并非标准教科书中的通用决定式，且陆地与海洋的δ_BL差异更多归因于热力驱动（感热通量）而非单纯的动量粗糙度比值。 | source=knowledge，逻辑量级自洽（H_pbl ~1km，系数0.1-0.2得出100-200m? 不对，题目说δ_BL ~1000-1500m，若H_pbl=1km，系数需接近1。这里存在数值矛盾：0.1*1000m = 100m，而非1000m。因此逻辑校验发现数值量级错误。

## Search Query

planetary boundary layer depth land ocean ratio tropical cyclone friction coefficient
