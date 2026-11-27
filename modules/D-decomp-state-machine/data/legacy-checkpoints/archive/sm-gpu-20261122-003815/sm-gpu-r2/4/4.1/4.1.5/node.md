# N121: FP8 权重存储细节：Qwen3-27B FP8 量化通常采用 E4M3 格式，每个参数 1 byte。需确认是否包含 per-channel 或 per-te

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22, N23, N24

## Claim

FP8 权重存储细节：Qwen3-27B FP8 量化通常采用 E4M3 格式，每个参数 1 byte。需确认是否包含 per-channel 或 per-tensor 的 scale 因子（通常 overhead < 1%），即权重占用 ≈ 27.0-27.3 GB。

## Corrected Claim

FP8 权重存储细节：Qwen3-27B FP8 量化通常采用 E4M3 格式，每个参数 1 byte。需确认是否包含 per-channel 或 per-tensor 的 scale 因子（通常 overhead < 1%），即权重占用 ≈ 27.0-27.3 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数×1字节/参数=27GB，加上极少量的scale因子开销，总量级27.0-27.3GB符合FP8量化常识。

## Search Query

Qwen3 FP8 quantization E4M3 scale overhead
