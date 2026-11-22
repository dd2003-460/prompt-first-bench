# N439: AMD MI300X 在本地工作站部署中，ROCm 6.0+ 对 vLLM 的支持尚处于实验阶段，缺乏针对 32K 长上下文 KV Cache 的 PagedA

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

AMD MI300X 在本地工作站部署中，ROCm 6.0+ 对 vLLM 的支持尚处于实验阶段，缺乏针对 32K 长上下文 KV Cache 的 PagedAttention 深度优化，且驱动稳定性问题（如偶发 Kernel Hang）导致其 7x24 可用性低于 NVIDIA 方案，预计额外增加 5-10% 的运维监控成本，需计入 TCO 隐性成本。

## Corrected Claim

AMD MI300X 在本地工作站部署中，ROCm 6.0+ 对 vLLM 的支持尚处于实验阶段，缺乏针对 32K 长上下文 KV Cache 的 PagedAttention 深度优化，且驱动稳定性问题（如偶发 Kernel Hang）导致其 7x24 可用性低于 NVIDIA 方案，预计额外增加 5-10% 的运维监控成本，需计入 TCO 隐性成本。

## Evidence

检索失败: no sources from any channel (all 5 failed)
