# N164: HDD工作点2（大容量18TB）：选用Seagate Exos X20 18TB，单价约¥550/盘，400TB有效数据需约24块盘（RAID6 N=26, M

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

HDD工作点2（大容量18TB）：选用Seagate Exos X20 18TB，单价约¥550/盘，400TB有效数据需约24块盘（RAID6 N=26, M=2），物理总容量468TB，冗余开销14.5%，虽单价高但盘数减少降低了控制器端口占用和运维复杂度。

## Corrected Claim

HDD工作点2（大容量18TB）：选用Seagate Exos X20 18TB，单价约¥550/盘（需根据实际采购价核实），400TB有效数据需配置26块盘（RAID6，可用24块），物理总容量468TB，冗余开销约14.5%，盘数减少有助于降低控制器端口占用和运维复杂度。

## Evidence

[质询]具体型号（Seagate Exos X20 18TB）的市场单价（¥550）及具体冗余开销比例（14.5%）属于经验事实，缺乏实时市场数据支持，且不同采购渠道价格波动较大，无法从第一性原理推导。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）。计算逻辑验证：400TB有效数据，RAID6 (N=26, M=2) 意味着可用盘数24，单盘18TB，总物理容量 24*18=432TB（注：原陈述称468TB有误，26*18=468TB是总盘数容量，但通常RAID6 N=26指总盘数26，可用24。若N=26为总盘数，则物理总容量468TB正确，有效容量432TB > 400TB，逻辑成立。冗余开销 = (468-400)/468 ≈ 14.5%，逻辑自洽。但单价为经验数据。

## Search Query

enterprise 18TB CMR HDD price per unit 2024
