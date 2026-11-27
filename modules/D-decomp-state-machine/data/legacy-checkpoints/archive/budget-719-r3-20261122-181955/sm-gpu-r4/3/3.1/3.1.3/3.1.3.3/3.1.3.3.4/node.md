# N786: 修正后的 Prefill 理论吞吐量上限计算：Total_FLOPs = 24.27e15；若 RTX 4090 有效算力为 70 TFLOPS (70e12 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N280

## Claim

修正后的 Prefill 理论吞吐量上限计算：Total_FLOPs = 24.27e15；若 RTX 4090 有效算力为 70 TFLOPS (70e12 FLOPs/s)，理论 Prefill 时间 = 24.27e15 / 70e12 = 346.7 s；对应吞吐量 = 32768 / 346.7 ≈ 94.5 tokens/s；此值远低于仅基于线性层估算的 1000+ tokens/s，验证了长上下文下计算瓶颈的本质变化。

## Corrected Claim

修正后的 Prefill 理论吞吐量上限计算：Total_FLOPs = 24.27e15；若 RTX 4090 有效算力为 70 TFLOPS (70e12 FLOPs/s)，理论 Prefill 时间 = 24.27e15 / 70e12 = 346.7 s；对应吞吐量 = 32768 / 346.7 ≈ 94.5 tokens/s；此值远低于仅基于线性层估算的 1000+ tokens/s，验证了长上下文下计算瓶颈的本质变化。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 24.27e15 / 70e12 ≈ 346.71s 及 32768 / 346.71 ≈ 94.5 tokens/s 均准确无误，量纲与逻辑自洽。

## Search Query

LLM prefill throughput calculation long context attention dominant
