# N248: 2x RTX 4090 方案中 INT4 权重的显存占用细节修正：INT4 权重实际占用 13.5GB (27B * 0.5 bytes) + 量化校准开销 (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

2x RTX 4090 方案中 INT4 权重的显存占用细节修正：INT4 权重实际占用 13.5GB (27B * 0.5 bytes) + 量化校准开销 (scale/zero-point, 约 1.5GB) = 15.0GB。加上 FP8 KV Cache (6.29GB) 和激活值/缓冲 (约 2GB)，总占用 23.29GB < 24GB，余量仅 0.71GB，极高风险 OOM。需确认是否支持 PagedAttention 动态管理以缓解碎片。

## Corrected Claim

2x RTX 4090 方案中 INT4 权重的显存占用细节修正：INT4 权重实际占用 13.5GB (27B * 0.5 bytes) + 量化校准开销 (scale/zero-point, 约 1.5GB) = 15.0GB。加上 FP8 KV Cache (6.29GB) 和激活值/缓冲 (约 2GB)，总占用 23.29GB < 24GB，余量仅 0.71GB，极高风险 OOM。需确认是否支持 PagedAttention 动态管理以缓解碎片。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数INT4权重约13.5GB，加上量化开销、KV Cache及激活值，总显存占用约23.29GB，小于24GB但余量极小，符合大模型推理显存估算逻辑。
