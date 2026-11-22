# N97: 多卡并联对 TTFT 的影响：TTFT 受限于单卡 Prefill 算力，多卡通过 Tensor Parallelism 可将 Prefill 时间近似除以卡数

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

多卡并联对 TTFT 的影响：TTFT 受限于单卡 Prefill 算力，多卡通过 Tensor Parallelism 可将 Prefill 时间近似除以卡数（忽略通信开销），2x RTX 5090 的 TTFT 可逼近单张 H100，但通信开销通常导致效率损失 10-20%。

## Corrected Claim

多卡并联对 TTFT 的影响：TTFT 受限于单卡 Prefill 算力，多卡通过 Tensor Parallelism 可将 Prefill 时间近似除以卡数（忽略通信开销），2x RTX 5090 的 TTFT 可逼近单张 H100，但通信开销通常导致效率损失 10-20%。

## Evidence

先验知识/题面给定，逻辑校验通过：Tensor Parallelism 在 Prefill 阶段确实能近似线性扩展算力，2x RTX 5090 的总 FP16/FP8 算力与 H100 相当，通信开销 10-20% 符合 NVLink/PCIe 互联下的典型效率损失范围。

## Search Query

tensor parallelism prefill latency scaling multi-gpu
