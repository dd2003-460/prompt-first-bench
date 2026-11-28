# N29: 4x V100-SXM2-16GB (TP=4) 部署 27B NVFP4 模型的理论峰值吞吐量上限：受限于 V100 Tensor Core 对 FP16/B

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

4x V100-SXM2-16GB (TP=4) 部署 27B NVFP4 模型的理论峰值吞吐量上限：受限于 V100 Tensor Core 对 FP16/BF16 的支持及 NVFP4 反量化开销，实际可持续吞吐量约为 15-20 tokens/s (per sequence)，在 max-num-seqs=8 并发下总吞吐约为 120-160 tokens/s，显存占用率 >95% (KV Cache 占主导)，导致无法增加 batch size 以提升利用率。

## Corrected Claim

在 4x V100-SXM2-32GB (TP=4) 部署 27B NVFP4 模型（使用 FP16 计算内核）且 max-num-seqs=8 的配置下，由于 V100 缺乏原生低精度支持及反量化开销，吞吐量受限，具体数值需实测验证，通常显著低于 A100/H100 同等配置。

## Evidence

[质询]来源 [1] 仅确认了硬件配置（4x V100-SXM2 32GB, TP4）、软件环境（vLLM fork, FP16 compute, NVFP4 checkpoint）及并发设置（max 8 seqs），但完全未提供具体的吞吐量数值（15-20 tokens/s）或显存占用率（>95%）数据。此外，V100 不支持原生 FP4 计算，NVFP4 需反量化为 FP16 执行，其具体性能瓶颈和显存压力高度依赖具体的 KV Cache 长度配置和 Batch 调度策略，仅凭配置无法唯一确定该特定吞吐量区间。 | 来源 [1] 证实了实验环境配置（4x V100, TP4, NVFP4, max 8 seqs），但未包含任何关于吞吐量或显存占用的具体数值支持，属于间接相关但缺乏直接数据支撑。

## Retrieval Sources

- {'url': 'https://github.com/1CatAI/1Cat-vLLM&rut=b6cd44db340e9db1102937ea77dab9d86ddd553d05c2d59a6de0ab26a6381afd', 'type': 'ddg', 'title': 'GitHub - 1CatAI/1Cat-vLLM: V100 / SM70-focused vLLM engineering fork ...'}
