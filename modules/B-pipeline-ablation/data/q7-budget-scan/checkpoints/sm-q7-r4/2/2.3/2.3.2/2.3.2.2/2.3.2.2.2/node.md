# N560: 针对 400TB 冷数据，若平均对象大小 S_avg = 1MB，则 K_bloat = 1，无额外计费惩罚；若 S_avg 降至 32KB，则 K_bloat

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N184

## Claim

针对 400TB 冷数据，若平均对象大小 S_avg = 1MB，则 K_bloat = 1，无额外计费惩罚；若 S_avg 降至 32KB，则 K_bloat = 64KB/32KB = 2，有效计费容量翻倍至 800TB，月度存储成本从 ¥12,288 (400TB*1024*0.03) 升至 ¥24,576。

## Corrected Claim

针对 400TB 冷数据，若平均对象大小 S_avg = 1MB，则 K_bloat = 1，无额外计费惩罚；若 S_avg 降至 32KB，则 K_bloat = 64KB/32KB = 2，有效计费容量翻倍至 800TB，月度存储成本从 ¥12,288 (400TB*1024*0.03) 升至 ¥24,576。

## Evidence

先验知识/题面给定，逻辑校验通过：K_bloat计算符合定义（64KB/32KB=2），成本计算符合线性关系（400TB*1024GB/TB*0.03元/GB=12288元，翻倍后为24576元），数值量级与逻辑自洽。
