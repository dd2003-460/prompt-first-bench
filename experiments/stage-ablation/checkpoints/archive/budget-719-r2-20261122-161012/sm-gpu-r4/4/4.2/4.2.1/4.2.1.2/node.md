# N205: RTX 4090 在 BF16 下的实际 MFU (Model FLOPs Utilization) 在 Prefill 阶段约为 40%-50%，受限于 Te

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99

## Claim

RTX 4090 在 BF16 下的实际 MFU (Model FLOPs Utilization) 在 Prefill 阶段约为 40%-50%，受限于 Tensor Core 利用率及内存访问模式；H100 SXM 在相同负载下 MFU 约为 50%-60%，因 HBM3 带宽及 Tensor Core 架构优化

## Corrected Claim

RTX 4090 在 BF16 下的实际 MFU (Model FLOPs Utilization) 在 Prefill 阶段约为 40%-50%，受限于 Tensor Core 利用率及内存访问模式；H100 SXM 在相同负载下 MFU 约为 50%-60%，因 HBM3 带宽及 Tensor Core 架构优化

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

RTX 4090 H100 MFU LLM inference prefill benchmark
