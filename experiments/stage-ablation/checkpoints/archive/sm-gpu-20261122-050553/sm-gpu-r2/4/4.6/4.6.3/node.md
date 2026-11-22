# N97: RTX 4090 单卡推理 Qwen3-27B (W4) 的功耗修正：满载功耗并非恒定 450W，而是随 batch size 和序列长度变化；在 32K 长上

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N25, N26, N27

## Claim

RTX 4090 单卡推理 Qwen3-27B (W4) 的功耗修正：满载功耗并非恒定 450W，而是随 batch size 和序列长度变化；在 32K 长上下文推理场景下，显存读取主导，功耗可能降至 350-400W，导致原 TCO 计算中的电力成本高估 10-15%。

## Corrected Claim

RTX 4090 单卡推理 Qwen3-27B (W4) 的功耗并非恒定 450W，而是随负载变化；在 32K 长上下文推理场景下，由于显存读取主导，功耗可能低于峰值，导致原 TCO 计算中的电力成本存在高估风险。

## Evidence

[质询]该陈述包含具体的经验性数值（350-400W功耗区间、10-15%成本偏差），属于硬件性能与能耗的经验事实，无法仅通过第一性原理严格推导得出，且缺乏直接来源支持。 | 经验事实，逻辑自洽（长上下文推理显存带宽瓶颈导致计算单元空闲，功耗低于峰值符合物理直觉），但缺来源支持。

## Search Query

RTX 4090 LLM inference power consumption 32k context batch size watts
