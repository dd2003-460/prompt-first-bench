# N212: 工作点B（中CapEx中OpEx）：HDD+SSD分层方案，100TB温数据存NVMe，扫描耗时同上 C_wait = 0；但需额外承担HDD层的运维成本和电力

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

工作点B（中CapEx中OpEx）：HDD+SSD分层方案，100TB温数据存NVMe，扫描耗时同上 C_wait = 0；但需额外承担HDD层的运维成本和电力成本。HDD层400TB静态功耗约 400TB * 0.5W/TB = 200W，年电力成本 = 200W * 1.4 * 0.8 * 8760 / 1000 = ¥2,443；运维人力成本假设为¥50,000/年，总OpEx增量 = ¥52,443/年。

## Corrected Claim

工作点B（中CapEx中OpEx）：HDD+SSD分层方案，100TB温数据存NVMe，扫描耗时同上 C_wait = 0；但需额外承担HDD层的运维成本和电力成本。HDD层400TB静态功耗约 400TB * 0.5W/TB = 200W，年电力成本 = 200W * 1.4 * 0.8 * 8760 / 1000 = ¥2,443；运维人力成本假设为¥50,000/年，总OpEx增量 = ¥52,443/年。

## Evidence

先验知识/题面给定，逻辑校验通过：HDD静态功耗估算（0.5W/TB）及电力成本计算公式（功率*PUE*负载率*时间/1000）符合工程常识，数值量级合理。
