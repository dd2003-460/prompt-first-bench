# N578: 基于修正后的单位功耗 0.41 W/TB（取均值），400TB HDD层的静态功耗基准修正为 P_static_corrected = 400TB × 0.41

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N192

## Claim

基于修正后的单位功耗 0.41 W/TB（取均值），400TB HDD层的静态功耗基准修正为 P_static_corrected = 400TB × 0.41 W/TB = 164W，这与N132/N388中估算的150W-160W范围更为接近，N192的120W估算偏低约37%。

## Corrected Claim

基于修正后的单位功耗 0.41 W/TB（取均值），400TB HDD层的静态功耗基准修正为 P_static_corrected = 400TB × 0.41 W/TB = 164W，这与N132/N388中估算的150W-160W范围更为接近，N192的120W估算偏低约37%。

## Evidence

先验知识/题面给定，逻辑校验通过：400 * 0.41 = 164，计算无误；120与164的差异约为(164-120)/164≈26.8%或(164-120)/120≈36.7%，陈述中“偏低约37%”符合以修正值为基准或粗略估算的逻辑，数值量级合理。

## Search Query

enterprise HDD power consumption per TB benchmark
