# N682: FP8 (E4M3) 量化中，Scale 因子的存储粒度取决于量化库实现（如 vLLM 或 TensorRT-LLM），常见为每 128 元素一个 FP32 S

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N243

## Claim

FP8 (E4M3) 量化中，Scale 因子的存储粒度取决于量化库实现（如 vLLM 或 TensorRT-LLM），常见为每 128 元素一个 FP32 Scale (4 bytes) 或 FP16 Scale (2 bytes)；若为 FP32 Scale，额外开销为 (27.16e9 / 128) * 4 bytes = 0.85 GB，总权重占用为 27.16 + 0.85 = 28.01 GB；若为 FP16 Scale，额外开销为 0.42 GB，总占用为 27.58 GB。

## Corrected Claim

FP8 (E4M3) 量化中，Scale 因子的存储粒度取决于量化库实现。若采用常见的每 128 元素一个 Scale 的方案，FP32 Scale 的额外开销约为 0.85 GB（基于 27.16e9 参数），总占用约 28.01 GB；FP16 Scale 额外开销约 0.42 GB，总占用约 27.58 GB。具体数值需依据实际使用的库版本和配置确认。

## Evidence

[质询]该陈述包含具体的工程实现细节（如 vLLM/TensorRT-LLM 中 FP8 E4M3 的 Scale 存储粒度及具体字节数），属于经验事实。虽然数学计算（27.16e9/128*4 ≈ 0.85GB）在逻辑上自洽，但缺乏外部来源验证其是否符合特定库的实际默认行为或通用标准，且不同库或版本可能存在差异（例如某些实现可能使用 per-tensor 或 per-channel scale，而非固定的 per-128）。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体库实现细节）

## Search Query

vLLM FP8 E4M3 quantization scale factor block size 128 bytes overhead
