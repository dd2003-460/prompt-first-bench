# N28: [待核验] 关键参数时效性风险：(1) GPU价格：2024Q4-2025Q1价格波动±15%，需实时查证；(2) 软件栈成熟度：ROCm 6.0 vs CUD

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

[待核验] 关键参数时效性风险：(1) GPU价格：2024Q4-2025Q1价格波动±15%，需实时查证；(2) 软件栈成熟度：ROCm 6.0 vs CUDA 12.4，对Qwen3-27B的支持程度需查证；(3) 量化质量：FP8/INT4对Qwen3-27B的perplexity损失需查证（不同量化算法差异大）；(4) 电力成本：地区电价差异大，需用户具体数据。

## Corrected Claim

关键参数时效性风险：(1) GPU价格：2024Q4-2025Q1价格波动显著（如H100租赁价曾暴涨40%），需实时查证；(2) 软件栈成熟度：ROCm 6.0 vs CUDA 12.4，对Qwen3-27B的支持程度需查证；(3) 量化质量：FP8/INT4对Qwen3-27B的perplexity损失需查证（不同量化算法差异大）；(4) 电力成本：地区电价差异大，需用户具体数据。

## Evidence

[质询]陈述中关于GPU价格波动幅度（±15%）的具体数值缺乏来源支持，且参考来源[1]提到H100租赁价暴涨40%，与±15%的波动范围存在潜在矛盾或口径差异（租赁价vs购买价，或不同时间段）。 | 逻辑自洽，但参考来源[1]仅提及H100租赁价上涨40%，未直接支持±15%的波动幅度，且其他参数（ROCm版本、量化损失、电价）均无来源覆盖，属于经验事实且缺来源支持。

## Search Query

Qwen3-27B FP8 INT4 quantization perplexity loss benchmark 2025

## Retrieval Sources

- {'url': 'https://www.sohu.com/a/1005119475_122362510&rut=a3bcc03ddb81ea859fc55521fb755346c04be7bea5676ae32e2379011424e4bb', 'type': 'ddg', 'title': '算力荒加剧!英伟达h100租赁价暴涨40% Ai浪潮下的gpu争夺战_价格_产能_供给'}
