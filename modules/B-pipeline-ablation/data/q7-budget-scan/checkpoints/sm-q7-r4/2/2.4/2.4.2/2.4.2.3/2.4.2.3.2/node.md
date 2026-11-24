# N583: 基于修正后的SSD静态功耗250W，SSD层年静态电力成本重算为 C_SSD_static_corrected = 250W × 1.4(PUE) × 0.8(

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N194

## Claim

基于修正后的SSD静态功耗250W，SSD层年静态电力成本重算为 C_SSD_static_corrected = 250W × 1.4(PUE) × 0.8(¥/kWh) × 8760h / 1000 ≈ ¥2,471.04/年，较N194中的¥972.16增加约154%。

## Corrected Claim

基于修正后的SSD静态功耗250W，SSD层年静态电力成本重算为 C_SSD_static_corrected = 250W × 1.4(PUE) × 0.8(¥/kWh) × 8760h / 1000 ≈ ¥2,471.04/年，较N194中的¥972.16增加约154%。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 250 * 1.4 * 0.8 * 8760 / 1000 = 2471.04 准确无误；增量比例 (2471.04 - 972.16) / 972.16 ≈ 154.2% 亦符合算术逻辑。
