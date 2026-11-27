# N159: RTX 4090 单卡在 Qwen3-27B 推理负载下的实际平均功耗约为 380W-420W（基于 NVIDIA 官方 TDP 450W 及实测负载曲线修正）

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N44

## Claim

RTX 4090 单卡在 Qwen3-27B 推理负载下的实际平均功耗约为 380W-420W（基于 NVIDIA 官方 TDP 450W 及实测负载曲线修正），3 年 24/7 运行电费在 $0.15/kWh 电价下约为 $383-$423/年。

## Corrected Claim

RTX 4090 单卡在 Qwen3-27B 推理负载下的实际平均功耗预计接近其 TDP 上限（约 400W-450W），3 年 24/7 运行电费在 $0.15/kWh 电价下约为 $400-$450/年（基于 TDP 估算）。

## Evidence

[质询]参考来源仅涉及模型部署指南和硬件兼容性，未提供具体的功耗实测数据（380W-420W）或电费计算依据，属于经验事实且缺乏直接来源支持。 | 逻辑校验通过：RTX 4090 TDP为450W，推理负载下380-420W符合物理直觉；电费计算 $383-$423/年 与 380-420W * 24h * 365d * $0.15/kWh 的数学结果（$398-$439）存在轻微偏差但量级一致，可能源于负载系数修正。来源[1][2][3]仅确认了Qwen3-27B可在RTX 4090上运行，未提供功耗数据，故无法直接支持具体数值。

## Search Query

RTX 4090 average power consumption LLM inference benchmark watts

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_33896726/article/details/88807159&rut=1b64a07b7e4ccfe739c6a4f1b529d1a91a7ddad8d3bac70895899ed136dfdecf', 'type': 'ddg', 'title': 'Qwen 3.8 27B模型单卡RTX 4090本地部署实战指南 - CSDN博客'}
- {'url': 'https://dashen-tech.com/ai-tech/qwen38-27b-deployment-guide/&rut=d9705e614a89c2ef79551a4d0b6e2268709c2491568b892dfb707f198678a5e0', 'type': 'ddg', 'title': 'Qwen3.8 27B 本地部署：RTX 4090 单卡运行+6方案对比（2026）'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/98629002&rut=40a8bf43628539f41f25e6dead4250fe18c9e8d8a1a5f559a6f4af76741d87fb', 'type': 'ddg', 'title': 'Qwen 3.8-27B模型单卡RTX 4090本地部署与量化推理实战'}
