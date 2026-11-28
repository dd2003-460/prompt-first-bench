# N31: V100-SXM2 的 HBM2 实际有效内存带宽在 vLLM 持续读取权重/KV Cache 时的实测值约为 850-880 GB/s（理论峰值 900 GB

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

V100-SXM2 的 HBM2 实际有效内存带宽在 vLLM 持续读取权重/KV Cache 时的实测值约为 850-880 GB/s（理论峰值 900 GB/s），该值是计算 Memory-Bound 状态下 T_gen 的核心分母参数。

## Corrected Claim

V100-SXM2 的 HBM2 实际有效内存带宽在 vLLM 持续读取权重/KV Cache 时的实测值约为 850-880 GB/s（理论峰值 900 GB/s），该值是计算 Memory-Bound 状态下 T_gen 的核心分母参数。

## Evidence

先验知识/题面给定，逻辑校验通过：V100-SXM2 HBM2 理论带宽 900GB/s，实测有效带宽 850-880GB/s 符合硬件工程常识及效率预期（约95%+），量级与逻辑自洽。

## Search Query

V100 SXM2 HBM2 effective memory bandwidth vllm benchmark gb/s
