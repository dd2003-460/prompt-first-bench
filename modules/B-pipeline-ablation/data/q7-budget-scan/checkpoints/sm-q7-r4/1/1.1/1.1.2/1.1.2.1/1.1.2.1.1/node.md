# N407: 工作点B (RAID-5) 的CapEx修正：单盘价格需明确为16TB NVMe SSD市场价（约¥15,000-25,000/盘，而非HDD的¥4,000/盘

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N136

## Claim

工作点B (RAID-5) 的CapEx修正：单盘价格需明确为16TB NVMe SSD市场价（约¥15,000-25,000/盘，而非HDD的¥4,000/盘），12盘总CapEx ≈ ¥180,000-300,000，3年折旧后年硬件成本 ≈ ¥60,000-100,000/年，导致每TB年成本远高于¥104。

## Corrected Claim

工作点B (RAID-5) 的CapEx修正：单盘价格需明确为16TB NVMe SSD市场价（约¥15,000-25,000/盘，而非HDD的¥4,000/盘），12盘RAID-5有效容量为176TB，总CapEx ≈ ¥180,000-300,000，3年折旧后年硬件成本 ≈ ¥60,000-100,000/年，导致每TB年成本远高于¥104。

## Evidence

[质询]16TB NVMe SSD的市场价格波动较大，且不同品牌/型号差异显著，¥15,000-25,000/盘的范围可能偏高或偏低，缺乏实时市场数据支撑；此外，RAID-5的有效容量计算未明确说明（12盘RAID-5有效容量为11*16TB=176TB，而非192TB），可能导致每TB成本计算偏差。 | 经验事实，逻辑自洽但缺来源支持（来源[1]仅讨论RAID-5可靠性风险，未涉及NVMe SSD价格或CapEx计算）

## Search Query

16TB NVMe SSD enterprise price 2024 CNY

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1988333539469579487&rut=7ed47912e098015cfc7f6debe5f0ee1cc1e4f2ed22069f909ec98146fdff9705', 'type': 'ddg', 'title': 'Raid 0到5全解析：Raid 5已成高危配置？10年工程师给nas用户打分避坑'}
