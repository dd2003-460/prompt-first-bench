# N684: HDD 单盘功耗规格核验：企业级 16TB HDD（如 Seagate Exos X20 或 WD Ultrastar DC HC560）空闲功耗典型值 4.5

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N253

## Claim

HDD 单盘功耗规格核验：企业级 16TB HDD（如 Seagate Exos X20 或 WD Ultrastar DC HC560）空闲功耗典型值 4.5-5.5W，活跃功耗 7-9W（非 N253 假设的 5W/10W）；若取中值 5W/8W，平均功耗 = 0.8*5 + 0.2*8 = 5.6W，40 盘总功耗 = 224W，较 N253 估算低 6.7%，需按实际型号规格表修正

## Corrected Claim

企业级16TB HDD（如Seagate Exos X16/X20）空闲功耗典型值约4.5-5.5W，活跃功耗约7-9W；若取中值5W/8W，平均功耗为5.6W，40盘总功耗为224W。具体数值需以实际型号官方规格书为准。

## Evidence

[质询]参考来源仅提供了Seagate Exos X16的产品链接和简介，未包含具体的功耗数值（Idle/Active Watts），无法直接验证4.5-5.5W/7-9W的具体范围及计算结果；且来源指向X16而非Claim中提到的X20或WD HC560，存在型号不完全匹配的问题。 | 逻辑推导自洽（0.8*5+0.2*8=5.6W, 5.6*40=224W），但参考来源[1][2][3]均未提供具体功耗数据，属于经验事实且缺乏直接来源支持。

## Search Query

Seagate Exos X20 16TB power consumption idle active watts

## Retrieval Sources

- {'url': 'https://www.seagate.com/support/internal-hard-drives/enterprise-hard-drives/exos-X16/&rut=a9a0ec00325d87008048b32fbfdb39e20b1731be485fd7ff40a41454e05c2396', 'type': 'ddg', 'title': 'Exos X16 - Seagate US'}
- {'url': 'https://www.newegg.com/seagate-exos-x16-st16000nm001g-16tb/p/1Z4-002P-015K6&rut=4df35d08b5a9ba9be3253a1f11d4cc19dcd024c0d50c597df97d4a147ce0136b', 'type': 'ddg', 'title': 'Seagate Exos 16TB Enterprise HDD 7200 RPM 3.5" Internal Hard Drive ...'}
- {'url': 'https://www.seagate.com/www-content/datasheets/pdfs/exos-x16-DS2011-2-1910CN-zh_CN.pdf&rut=1f3f450372efeded0a83e529113ac12b76c016053f1d346ede35645bfc3d9390', 'type': 'ddg', 'title': 'PDF 产品资料 - Seagate'}
