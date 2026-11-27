# N206: 基于修正后的 FLOPs (3.12 TFLOPs) 和 MFU，RTX 4090 的 Prefill 延迟 T_prefill ≈ 3.12e12 / (33

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N99

## Claim

基于修正后的 FLOPs (3.12 TFLOPs) 和 MFU，RTX 4090 的 Prefill 延迟 T_prefill ≈ 3.12e12 / (330e9 * 0.45) ≈ 21 秒；H100 SXM 的 T_prefill ≈ 3.12e12 / (990e9 * 0.55) ≈ 5.8 秒；两者差距约为 3.6 倍

## Corrected Claim

基于修正后的 FLOPs (3.12 TFLOPs) 和 MFU，RTX 4090 的 Prefill 延迟 T_prefill ≈ 3.12e12 / (330e9 * 0.45) ≈ 21 秒；H100 SXM 的 T_prefill ≈ 3.12e12 / (990e9 * 0.55) ≈ 5.8 秒；两者差距约为 3.6 倍

## Evidence

父节点级核验未通过：有冗余（子节点分别针对 RTX 4090 和 H100 SXM 进行了独立的延迟估算和可行性分析，两者在对象上正交，且共同覆盖了父节点提到的两个硬件平台及性能差距（通过对比隐含）。然而，这两个子节点本质上是同一计算逻辑（T = FLOPs / (Peak * MFU)）在不同硬件参数下的具体实例化，结构高度同构，属于典型的‘参数化冗余’。）

## Search Query

RTX 4090 H100 prefill latency 32k context LLM
