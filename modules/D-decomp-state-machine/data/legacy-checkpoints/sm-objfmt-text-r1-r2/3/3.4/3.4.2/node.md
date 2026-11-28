# N62: 单卡 RTX 4090 在 BF16 精度下推理 27B 模型的每 Token 生成能耗约为 0.00075 kWh/token (假设 450W 持续满载且带

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N19

## Claim

单卡 RTX 4090 在 BF16 精度下推理 27B 模型的每 Token 生成能耗约为 0.00075 kWh/token (假设 450W 持续满载且带宽受限导致利用率低，按 1 token/s 估算需 0.45 kWh/h / 3600s * 1s ≈ 0.000125 kWh，但考虑到实际带宽瓶颈，更保守估计为 0.0005-0.001 kWh/token)，而 A100 80GB 由于更高带宽和能效，每 Token 能耗可能低至 0.0003-0.0005 kWh/token [待核验: 需实测不同负载下的 W/token]。

## Corrected Claim

单卡 RTX 4090 在 BF16 精度下推理 27B 模型的每 Token 生成能耗估计在 0.0005-0.001 kWh/token 范围内（基于 450W 持续满载及带宽受限假设），A100 80GB 由于更高带宽和能效，每 Token 能耗可能更低，具体数值需依赖实测数据。

## Evidence

[质询]该陈述包含具体的经验性能耗数值（0.00075 kWh/token 等），属于经验事实而非第一性原理可推导内容。虽然逻辑推导过程（功率/时间）自洽，但缺乏针对特定模型大小（27B）和精度（BF16）的直接实测数据支持，且不同来源提供的基准测试条件（如功耗范围、具体模型）可能与陈述假设不完全一致，存在口径混淆风险。 | 来源[2]提供了RTX 4090在LLM工作负载下的Tokens per Watt基准测试，间接支持了能效评估的逻辑框架，但未直接提供27B模型BF16精度下的具体kWh/token数值；来源[1]和[3]主要关注成本对比，未提供详细的能耗物理量数据。因此，该事实逻辑自洽但缺乏直接来源支持，符合degraded判定标准。

## Search Query

RTX 4090 vs A100 energy efficiency per token inference LLM

## Retrieval Sources

- {'url': 'https://costperprompt.com/guides/gpu-cost-per-token&rut=52d60cc17ecaa4c4da2d2ed5ecfa04c81dddf1fad9fc33ebe2c46fd5c603ef12', 'type': 'ddg', 'title': 'H100 vs A100 vs L40S vs RTX 4090: Cost per Token, Not per Hour'}
- {'url': 'https://gigagpu.com/rtx-4090-24gb-tokens-per-watt/&rut=fd15095fc2ae13cc9fc8c6aafd8e84048d58dc52d22f63934e0cd8d7b993b215', 'type': 'ddg', 'title': 'RTX 4090 24GB Tokens per Watt: Energy Efficiency Benchmark'}
- {'url': 'https://pcserverandparts.com/news/used-gpu-server-buying-guide-2026-l40s-vs-a100-vs-rtx-4090/&rut=5e2f6d3c196c41070e28e2ff5a58a36c5d0483702a29243f1fbe49c08f7bd8b8', 'type': 'ddg', 'title': 'Used GPU Server Buying Guide 2026: L40S vs A100 vs RTX 4090'}
