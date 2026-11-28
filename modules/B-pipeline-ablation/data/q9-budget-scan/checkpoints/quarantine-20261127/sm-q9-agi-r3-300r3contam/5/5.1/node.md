# N21: 硬件参数不确定性：V100-SXM2-16GB 的实际可用显存因驱动版本和 CUDA 内存碎片而异，波动范围 ±5%（±0.8GB），影响 max_model_

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N5

## Claim

硬件参数不确定性：V100-SXM2-16GB 的实际可用显存因驱动版本和 CUDA 内存碎片而异，波动范围 ±5%（±0.8GB），影响 max_model_len=262144 的稳定性，需通过压力测试确定安全余量 ≥10%

## Corrected Claim

V100-SXM2-16GB 的实际可用显存受驱动版本和 CUDA 内存碎片影响，存在一定波动，建议通过压力测试确定安全余量以保障长上下文（如 max_model_len=262144）的稳定性。

## Evidence

[质询]具体数值（±5%波动、≥10%安全余量）缺乏权威来源支持，属于经验性工程估算而非固定硬件规格，不同驱动和负载下差异可能更大或更小。 | 来源[3]确认了V100 SXM2 16GB的硬件存在及基本规格，但未提供关于显存碎片化波动范围或特定max_model_len稳定性的具体数据；该陈述包含具体的经验参数（±5%, ≥10%），属于经验事实，逻辑自洽但缺乏直接来源支持，故降级。

## Search Query

V100 SXM2 16GB CUDA memory fragmentation driver version variability benchmark

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1910043824199303266&rut=72c00b8dbb787fad5f72822643f1277bae5662b23a55cbe868ed751c13f6304d', 'type': 'ddg', 'title': 'SXM2版V100显卡很麻烦但很香：14B大模型速度超50!附折腾攻略'}
- {'url': 'https://zhuanlan.zhihu.com/p/1927666998030078159&rut=dff025158196350ff8a48acfd01eb654d15422ddd1245a999d90b141174e8f80', 'type': 'ddg', 'title': '2025年AI本地部署性价比之王!双卡V100!32G显存，低价高能，碾压2080Ti 22G'}
- {'url': 'https://www.techpowerup.com/gpu-specs/tesla-v100-sxm2-16-gb.c3018&rut=a47f18b50a50a5e62aee9efe0e38c9243d1182563870374f50e477082b8c012f', 'type': 'ddg', 'title': 'NVIDIA Tesla V100 SXM2 16 GB Specs - TechPowerUp'}
