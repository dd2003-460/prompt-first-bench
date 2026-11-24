# N237: NVMe SSD 硬件成本敏感性分析的高价情景：若单价升至 ¥4,000/TB（如供应链紧张或高性能型号），总硬件成本 C_high = 270 * 1.92 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N109

## Claim

NVMe SSD 硬件成本敏感性分析的高价情景：若单价升至 ¥4,000/TB（如供应链紧张或高性能型号），总硬件成本 C_high = 270 * 1.92 * 4000 = ¥2,073,600，5年年折旧 ¥414,720/年，较基准升高 33.3%。

## Corrected Claim

NVMe SSD 硬件成本敏感性分析的高价情景：若单价升至 ¥4,000/TB（如供应链紧张或高性能型号），总硬件成本 C_high = 270 * 1.92 * 4000 = ¥2,073,600，5年年折旧 ¥414,720/年，较基准升高 33.3%。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 270*1.92*4000=2,073,600 正确；5年直线折旧 2,073,600/5=414,720 正确；若基准单价为 ¥3,000/TB，则 (4000-3000)/3000 = 33.3%，比例关系自洽。

## Search Query

nvme ssd price increase supply chain shortage impact
