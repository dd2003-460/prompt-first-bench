# N48: Apple Mac Studio 的整机功耗上限取决于配置：M2 Ultra (192GB) 基础功耗约 100W (idle) 至 250-300W (pea

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

Apple Mac Studio 的整机功耗上限取决于配置：M2 Ultra (192GB) 基础功耗约 100W (idle) 至 250-300W (peak load)，相比 RTX 4090 的 450W 峰值功耗，在 24/7 运行场景下电力成本节省约 40-50%，但需扣除因吞吐量降低导致的单位 Token 能耗上升（若吞吐量减半，单位 Token 能耗可能持平或更高）。

## Corrected Claim

Apple Mac Studio (M2 Ultra) 的整机功耗上限显著低于配备 RTX 4090 的同等性能工作站，在 24/7 运行场景下电力成本有显著节省，但需考虑吞吐量差异对单位 Token 能耗的影响。

## Evidence

[质询]具体功耗数值（M2 Ultra 100W-300W, RTX 4090 450W）及由此推导的40-50%成本节省比例属于经验事实，缺乏来源支持，且RTX 4090峰值功耗通常标称更高（如450W TGP，实际整机功耗可能更高），M2 Ultra峰值功耗数据也需具体负载验证，数值精度存疑。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Mac Studio M2 Ultra power consumption peak watts LLM inference
