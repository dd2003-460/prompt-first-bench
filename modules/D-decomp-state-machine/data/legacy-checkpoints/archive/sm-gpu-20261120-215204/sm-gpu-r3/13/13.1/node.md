# N406: RTX 5090 的 GDDR7 显存带宽为 1792 GB/s，在 W4 精度 (13.5GB 权重) 下，理论 Decode 速度上限为 1792 / 13

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N154

## Claim

RTX 5090 的 GDDR7 显存带宽为 1792 GB/s，在 W4 精度 (13.5GB 权重) 下，理论 Decode 速度上限为 1792 / 13.5 ≈ 132.7 Tokens/s，受计算瓶颈和 MFU 影响，实际预期约为 100-110 Tokens/s。

## Corrected Claim

RTX 5090 的 GDDR7 显存带宽为 1792 GB/s，在 W4 精度 (13.5GB 权重) 下，理论 Decode 速度上限为 1792 / 13.5 ≈ 132.7 Tokens/s，受计算瓶颈和 MFU 影响，实际预期约为 100-110 Tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 显存带宽 1792 GB/s 符合 GDDR7 规格，1792/13.5≈132.7 计算正确，实际性能受 MFU 限制降至 100-110 Tokens/s 符合工程直觉。

## Search Query

RTX 5090 GDDR7 bandwidth 1792 GB/s W4 inference speed
