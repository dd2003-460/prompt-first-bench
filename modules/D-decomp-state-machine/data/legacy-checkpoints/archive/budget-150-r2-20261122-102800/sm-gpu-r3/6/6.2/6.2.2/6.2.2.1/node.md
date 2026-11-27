# N342: H100 (Hopper) FP8 原生支持机制：Tensor Core 直接支持 E4M3/E5M2 格式，无需反量化；在 TensorRT-LLM 中启用 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N136

## Claim

H100 (Hopper) FP8 原生支持机制：Tensor Core 直接支持 E4M3/E5M2 格式，无需反量化；在 TensorRT-LLM 中启用 FP8 后，Decode 阶段吞吐率相比 BF16 提升约 1.8-2.2 倍（取决于 Batch Size 和序列长度），Prefill 阶段提升约 1.5-1.8 倍。

## Corrected Claim

H100 (Hopper) Tensor Core 原生支持 FP8 (E4M3/E5M2) 格式，无需反量化；在 TensorRT-LLM 中启用 FP8 通常能显著提升 Decode 和 Prefill 阶段的吞吐率，具体提升倍数取决于 Batch Size、序列长度及硬件配置。

## Evidence

[质询]具体吞吐提升倍数（1.8-2.2x Decode, 1.5-1.8x Prefill）属于高度依赖具体硬件配置、软件版本、Batch Size及序列长度的经验性数据，缺乏通用性，且无来源支持该特定数值范围。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

H100 FP8 vs BF16 inference throughput benchmark TensorRT-LLM
