# N85: 带宽成本对命中率的线性敏感度：ΔC_bw/ΔH = - Q_total * s_avg * P_bw_cloud，对于日均2TB下载量，每提升1%命中率节省带宽

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

带宽成本对命中率的线性敏感度：ΔC_bw/ΔH = - Q_total * s_avg * P_bw_cloud，对于日均2TB下载量，每提升1%命中率节省带宽成本 ≈ 20GB * ¥0.3/GB ≈ ¥6/天 ≈ ¥180/月

## Corrected Claim

带宽成本对命中率的线性敏感度：ΔC_bw/ΔH = - Q_total * s_avg * P_bw_cloud，对于日均2TB下载量，每提升1%命中率节省带宽成本 ≈ 20GB * ¥0.3/GB ≈ ¥6/天 ≈ ¥180/月

## Evidence

先验知识/题面给定，逻辑校验通过：2TB=2048GB，1%命中率提升对应20.48GB节省，按0.3元/GB计算约为6.14元/天，月成本约184元，与陈述中的20GB、6元/天、180元/月在数量级和近似值上完全一致。
