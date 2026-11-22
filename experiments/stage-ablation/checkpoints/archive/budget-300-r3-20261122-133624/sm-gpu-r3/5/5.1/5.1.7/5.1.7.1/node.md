# N351: RTX 3090 单卡 INT8 部署 Qwen3-27B 的显存溢出量精确计算：INT8 权重 27GB + 32K 上下文 KV Cache (约 4.5G

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N118

## Claim

RTX 3090 单卡 INT8 部署 Qwen3-27B 的显存溢出量精确计算：INT8 权重 27GB + 32K 上下文 KV Cache (约 4.5GB，假设 GQA 8:1 比例) + 激活值/框架开销 (约 1.5GB) = 33GB，超出 24GB 物理显存 9GB，确认为硬性不可行。

## Corrected Claim

RTX 3090 单卡 INT8 部署 Qwen3-27B 因权重体积（约 27GB）已接近或超过 24GB 物理显存上限，叠加 KV Cache 及激活值开销后必然导致显存溢出，确认为硬性不可行。

## Evidence

[质询]KV Cache 估算值（4.5GB）存在较大不确定性，且未明确区分是单请求还是多请求场景；若为单请求，该数值偏高，若为多请求则需明确并发数，导致总显存占用量级可能偏差。 | 先验知识/题面给定，逻辑校验通过：INT8 权重 27GB 已接近 24GB 显存上限，加上任何显著的 KV Cache 和激活值开销必然导致溢出，结论方向正确，但具体数值（如 4.5GB KV Cache）缺乏精确来源支持，故降级为定性表述。
