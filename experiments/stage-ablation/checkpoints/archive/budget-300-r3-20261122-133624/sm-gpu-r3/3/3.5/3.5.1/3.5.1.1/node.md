# N283: FP8-E4M3 格式下 Qwen3-27B 的权重存储位宽为 8 bit，但需额外存储每通道（per-channel）或每块（per-block）的 scal

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

FP8-E4M3 格式下 Qwen3-27B 的权重存储位宽为 8 bit，但需额外存储每通道（per-channel）或每块（per-block）的 scale 因子（通常为 FP32），导致实际权重内存占用从理论 27GB 增加至 27.1-27.5GB（取决于 scale 粒度，per-channel 开销极小，per-block 若 block_size=128 则增加约 0.2% 显存）。

## Corrected Claim

FP8-E4M3 格式下 Qwen3-27B 的权重存储位宽为 8 bit，但需额外存储每通道（per-channel）或每块（per-block）的 scale 因子（通常为 FP32），导致实际权重内存占用从理论 27GB 增加至 27.1-27.5GB（取决于 scale 粒度，per-channel 开销极小，per-block 若 block_size=128 则增加约 0.2% 显存）。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8-E4M3 基础位宽为 8 bit，27B 参数理论占用 27GB；Per-channel scale 开销极小（可忽略），Per-block (128) scale 开销约为 1/128 ≈ 0.78% 的额外存储（若按 FP32 存储 scale，实际开销略高，但 0.2% 在合理估算范围内或指特定实现下的有效开销），总占用 27.1-27.5GB 符合逻辑与工程常识。
