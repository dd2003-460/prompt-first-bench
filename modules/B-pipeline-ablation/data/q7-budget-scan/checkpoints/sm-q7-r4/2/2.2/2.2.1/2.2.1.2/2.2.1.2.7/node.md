# N520: PUE值的地域与季节性修正：1.4 PUE为平均值，但数据中心在夏季制冷负荷高时PUE可达1.5-1.6，冬季降至1.2-1.3。采用加权平均 PUE_weig

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N170, N171, N172

## Claim

PUE值的地域与季节性修正：1.4 PUE为平均值，但数据中心在夏季制冷负荷高时PUE可达1.5-1.6，冬季降至1.2-1.3。采用加权平均 PUE_weighted = (4个月*1.5 + 4个月*1.4 + 4个月*1.3) / 12 = 1.4。若位于高湿度地区，PUE可能恒定在1.5，则年电费增加至 0.315 * 1.5 * 0.8 * 8760 ≈ ¥3,312/年，差异约7%。

## Corrected Claim

PUE值的地域与季节性修正：1.4 PUE为平均值，但数据中心在夏季制冷负荷高时PUE可达1.5-1.6，冬季降至1.2-1.3。采用加权平均 PUE_weighted = (4个月*1.5 + 4个月*1.4 + 4个月*1.3) / 12 = 1.4。若位于高湿度地区，PUE可能恒定在1.5，则年电费增加至 0.315 * 1.5 * 0.8 * 8760 ≈ ¥3,312/年，差异约7%。

## Evidence

先验知识/题面给定，逻辑校验通过：PUE季节性波动范围（1.2-1.6）及加权平均计算符合数据中心能耗常识，数学推导无误。

## Search Query

data center PUE seasonal variation summer winter average
