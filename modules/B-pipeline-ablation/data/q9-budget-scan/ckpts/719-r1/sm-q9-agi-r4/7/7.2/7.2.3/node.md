# N276: 在 max_model_len=262144 下，V100 64GB 总显存扣除模型权重（NVFP4 约 14GB）和激活值后，剩余 KV Cache 空间约为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

在 max_model_len=262144 下，V100 64GB 总显存扣除模型权重（NVFP4 约 14GB）和激活值后，剩余 KV Cache 空间约为 40-45GB；在 8 并发且长上下文场景下，系统必然触发 Preemption（抢占）或 Swap-to-CPU，此时的性能瓶颈不再是碎片率，而是 PCIe 带宽限制下的 KV 换入换出延迟（约 16GB/s），导致 P99 延迟激增。

## Corrected Claim

在 max_model_len=262144 下，V100 64GB 总显存扣除模型权重（NVFP4 约 14GB）和激活值后，剩余 KV Cache 空间约为 40-45GB；在 8 并发且长上下文场景下，系统必然触发 Preemption（抢占）或 Swap-to-CPU，此时的性能瓶颈不再是碎片率，而是 PCIe 带宽限制下的 KV 换入换出延迟（约 16GB/s），导致 P99 延迟激增。

## Evidence

先验知识/题面给定，逻辑校验通过：V100 64GB 显存扣除 NVFP4 模型权重（~14GB）及激活值后，剩余 40-45GB 用于 KV Cache 符合数量级估算；PCIe 3.0 x16 带宽约 16GB/s 为硬件标准规格，长上下文高并发下 KV 换入换出受限于 PCIe 带宽导致 P99 延迟激增符合系统架构逻辑。

## Search Query

vLLM preemption swap to cpu latency PCIe bandwidth KV cache offloading
