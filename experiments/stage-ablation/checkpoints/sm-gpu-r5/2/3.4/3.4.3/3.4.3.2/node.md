# N161: vLLM 对 Intel Arc (Xe-HPG) 的支持状态：截至 2024 年，vLLM 官方仅支持 NVIDIA/AMD ROCm/Intel Gaudi

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

vLLM 对 Intel Arc (Xe-HPG) 的支持状态：截至 2024 年，vLLM 官方仅支持 NVIDIA/AMD ROCm/Intel Gaudi/TPU，不支持 Intel Arc；若强行通过 IPEX 或社区 fork 运行，缺少 Flash Attention 2/3 内核，导致 Attention 计算回退至非优化路径，吞吐量下降 30-50% [待核验]。

## Corrected Claim

vLLM 对 Intel Arc (Xe-HPG) 的支持状态：截至 2024 年，vLLM 官方仅支持 NVIDIA/AMD ROCm/Intel Gaudi/TPU，不支持 Intel Arc；若强行通过 IPEX 或社区 fork 运行，缺少 Flash Attention 2/3 内核，导致 Attention 计算回退至非优化路径，吞吐量显著下降。

## Evidence

[质询]吞吐量下降 30-50% 的具体数值缺乏来源支持，且不同模型/硬件配置下性能差异巨大，该具体区间可能不准确或过于绝对。 | 参考来源 [1] 与 vLLM 或 Intel Arc 无关，无可用外部证据；该陈述包含经验事实（具体性能下降百分比），逻辑自洽但缺来源支持，故降级。

## Search Query

vLLM Intel Arc Xe-HPG support status Flash Attention kernel missing

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/2406.10598v1', 'type': 'arxiv', 'title': 'Double Multi-Head Attention Multimodal System for Odyssey 2024 Speech Emotion Re'}
