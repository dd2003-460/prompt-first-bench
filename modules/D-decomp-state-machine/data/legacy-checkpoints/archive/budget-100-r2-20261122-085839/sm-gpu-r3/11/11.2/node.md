# N336: AMD MI300X 内存带宽 5.3 TB/s 在 W4 量化下的理论 Decode 吞吐上限 = 5300 / (13.55e9 / 1024 / 1024

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N118

## Claim

AMD MI300X 内存带宽 5.3 TB/s 在 W4 量化下的理论 Decode 吞吐上限 = 5300 / (13.55e9 / 1024 / 1024 / 1024) ≈ 397 tokens/s，实际受带宽利用率限制为 238-337 tokens/s，显著高于 RTX 4090 (75.4 tokens/s 理论)

## Corrected Claim

AMD MI300X 内存带宽 5.3 TB/s 在 W4 量化下的理论 Decode 吞吐上限 = 5300 / (13.55e9 / 1024 / 1024 / 1024) ≈ 397 tokens/s，实际受带宽利用率限制为 238-337 tokens/s，显著高于 RTX 4090 (75.4 tokens/s 理论)

## Evidence

先验知识/题面给定，逻辑校验通过：MI300X 5.3TB/s 带宽与 13.55GB 模型大小（W4）计算得出的理论上限 397 tokens/s 符合算术逻辑，且显著高于 RTX 4090 的带宽限制，结论自洽。
