# N116: NVIDIA RTX 4090 D (中国特供版) 显存带宽降至 960GB/s (相比标准版 1008GB/s)，导致 Qwen3-27B W4 量化下的理论

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

NVIDIA RTX 4090 D (中国特供版) 显存带宽降至 960GB/s (相比标准版 1008GB/s)，导致 Qwen3-27B W4 量化下的理论吞吐量上限从 ~55 tok/s 降至 ~52 tok/s，若采购受限地区用户需将其作为 4090 的替代候选纳入性价比计算。

## Corrected Claim

NVIDIA RTX 4090 D (中国特供版) 显存带宽相比标准版有所降低，导致在特定大模型推理场景下的理论吞吐量上限略有下降，需作为 4090 的替代候选纳入性价比计算。

## Evidence

[质询]来源未提供显存带宽具体数值（960GB/s vs 1008GB/s）及Qwen3-27B W4量化下的具体吞吐量数据（55 tok/s vs 52 tok/s），属于缺乏直接证据支持的具体经验参数。 | 来源[1]确认了RTX 4090 D的存在及其作为高端显卡的定位，但未提及具体的显存带宽削减数值或特定模型下的吞吐量变化，无法直接支持具体数值，但逻辑上带宽降低导致吞吐量下降是合理的。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/675235528&rut=919725ba8bbfdd0ef157418e0b0ec3f262d267046aa78a067416d10acd59dab6', 'type': 'ddg', 'title': '特供中国4090d显卡，英伟达减量不减价 - 知乎'}
