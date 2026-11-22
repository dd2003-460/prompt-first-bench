# N272: 4×A100 80GB (SXM4) 系统的总功耗通常包含GPU功耗（4*400W=1600W）及服务器其他组件（CPU/内存/风扇/PSU损耗）约400-60

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N97

## Claim

4×A100 80GB (SXM4) 系统的总功耗通常包含GPU功耗（4*400W=1600W）及服务器其他组件（CPU/内存/风扇/PSU损耗）约400-600W，总系统功耗约为2000-2200W，3年电力成本按$0.10/kWh计算约为$1,752-$1,920，而非原估$42,336（原估错误地使用了小时数而非总能量转换，或误将W当作kW且未除以1000）

## Corrected Claim

4×A100 80GB (SXM4) 系统的总功耗通常包含GPU功耗（4*400W=1600W）及服务器其他组件（CPU/内存/风扇/PSU损耗）约400-600W，总系统功耗约为2000-2200W，3年电力成本按$0.10/kWh计算约为$1,752-$1,920，而非原估$42,336（原估错误地使用了小时数而非总能量转换，或误将W当作kW且未除以1000）

## Search Query

A100 server total power consumption watts TCO calculation
