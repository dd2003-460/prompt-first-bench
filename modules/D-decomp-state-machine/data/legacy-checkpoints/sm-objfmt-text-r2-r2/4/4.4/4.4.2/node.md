# N84: 数据中心双卡（2x H100 SXM）若采用 NVLink 互联，单个 NVLink Bridge 的成本约为 $500，且主板必须支持 SXM 模组，导致主机

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

数据中心双卡（2x H100 SXM）若采用 NVLink 互联，单个 NVLink Bridge 的成本约为 $500，且主板必须支持 SXM 模组，导致主机板成本增加约 $2,000，总互联硬件溢价约为 $2,500。

## Corrected Claim

数据中心双卡（2x H100 SXM）若采用 NVLink 互联，需使用专用 NVLink Bridge 和支持 SXM 模组的主板，这将带来显著的硬件成本增加（具体金额随市场波动，通常包含数百美元的桥接器和数千美元的主板/基板溢价）。

## Evidence

[质询]具体价格数值（$500 NVLink Bridge, $2000 主板溢价, $2500 总溢价）属于高度波动的市场经验数据，缺乏权威来源直接支持，且不同时期、不同供应商报价差异巨大，易产生误导。 | 来源[1][2]确认了H100 SXM需使用NVLink互联及SXM模组特性，但未提供具体成本数据；该事实为经验性市场价格，逻辑自洽但缺来源直接支持，故降级。

## Search Query

NVIDIA NVLink bridge cost H100 SXM motherboard premium

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29056781/article/details/170745888&rut=d9d89612f3dfcd69dda251350fa06b1a65b49e00e07b7fcae63d5a793fae50ad', 'type': 'ddg', 'title': 'H100 Sxm与nvl选型指南：算力、显存、互联与功耗避坑-csdn博客'}
- {'url': 'https://blog.csdn.net/weixin_29061509/article/details/170386538&rut=a1bc116ca79185a465d683a7e73669f88234c90152a1d7406df1c36e68b8f4ef', 'type': 'ddg', 'title': 'H100 Sxm与nvl选型：先看显存、功耗、互联，再看峰值算力-csdn博客'}
- {'url': 'https://ask.csdn.net/questions/8650789&rut=fe2861feda545553df4b5d53265a2d659e867fd0cf10dddb42f233771906701f', 'type': 'ddg', 'title': 'V100sxm2双卡常见技术问题：如何优化双卡并行计算性能？_编程语言-csdn问答'}
