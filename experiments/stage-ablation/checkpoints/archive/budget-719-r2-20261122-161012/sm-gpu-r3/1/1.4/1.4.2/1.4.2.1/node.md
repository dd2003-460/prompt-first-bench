# N162: H100 SXM 单卡在 BF16 推理负载下的平均功耗约为 550W-600W（低于 700W TDP），3 年 24/7 运行电费在 $0.15/kWh 电

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45

## Claim

H100 SXM 单卡在 BF16 推理负载下的平均功耗约为 550W-600W（低于 700W TDP），3 年 24/7 运行电费在 $0.15/kWh 电价下约为 $560-$610/年，显著高于 RTX 4090 单卡。

## Corrected Claim

H100 SXM 单卡在 BF16 推理负载下的平均功耗通常低于其 700W TDP，具体数值取决于负载情况；在 $0.15/kWh 电价下，3 年 24/7 运行的电费估算需基于实际平均功耗计算，通常显著高于消费级显卡如 RTX 4090。

## Evidence

[质询]参考来源中未包含H100 SXM的具体功耗数值（TDP或平均功耗）及电费计算数据，无法直接验证550W-600W的功耗范围及$560-$610/年的电费估算。 | 逻辑校验通过：H100 SXM TDP为700W，BF16推理负载下平均功耗低于TDP符合物理直觉；电费计算 $0.15/kWh * 550W * 24h * 365d ≈ $729 (若按550W) 或 $0.15 * 600 * 24 * 365 ≈ $793，此处claim中的$560-$610数值偏低，可能基于更低的平均负载或不同的电价/效率假设，但量级合理。来源[2][3]确认了H100 SXM的存在及规格，但未提供功耗和电费数据，属于经验事实且缺乏直接来源支持。

## Search Query

H100 SXM average power consumption LLM inference benchmark watts

## Retrieval Sources

- {'url': 'https://ask.csdn.net/questions/8230483&rut=7c042a3d47146e30ae80ab22a7f0a8b0da2c3ef3f7bb03cb2ed42860f7ba15f4', 'type': 'ddg', 'title': 'A100和H100在bf16精度下的TFLOPS性能差异是多少？ - CSDN问答'}
- {'url': 'https://inferencex.semianalysis.com/zh/chips/h100&rut=f6f89a20f67a8aabf94d85cb223b75a35e5f2d36db1b8a3ed4a5d3a6bf86b885', 'type': 'ddg', 'title': 'NVIDIA H100 SXM 规格、价格与功耗 | InferenceX'}
- {'url': 'https://inferencex.semianalysis.com/chips/h100&rut=4ae57c5cc3bdbd2a33288624e598152e576547d47cab5c116a3fa2215e7eadcc', 'type': 'ddg', 'title': 'NVIDIA H100 SXM Specs: ~$1.17/hr, 80 GB HBM3 | InferenceX'}
