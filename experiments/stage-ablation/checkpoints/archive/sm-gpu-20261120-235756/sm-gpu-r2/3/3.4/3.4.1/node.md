# N74: RTX 4090 在 32K 长上下文推理（Prefill阶段）时的瞬时功耗峰值约为 450W（TDP满载），而在 Decode 阶段（每 token 生成）平

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19, N20, N21

## Claim

RTX 4090 在 32K 长上下文推理（Prefill阶段）时的瞬时功耗峰值约为 450W（TDP满载），而在 Decode 阶段（每 token 生成）平均功耗降至约 250W-300W（因计算密度低，GPU利用率下降），需区分 Prefill/Decode 两阶段的加权平均功耗以修正年电费估算。

## Corrected Claim

RTX 4090 在 32K 长上下文推理（Prefill阶段）时的瞬时功耗峰值约为 450W（TDP满载），而在 Decode 阶段（每 token 生成）平均功耗降至约 250W-300W（因计算密度低，GPU利用率下降），需区分 Prefill/Decode 两阶段的加权平均功耗以修正年电费估算。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 TDP为450W，Prefill阶段计算密集易达满载，Decode阶段受内存带宽限制导致GPU利用率下降，功耗降至250-300W符合硬件物理特性及工程经验。

## Search Query

RTX 4090 power consumption during LLM inference decode vs prefill watts
