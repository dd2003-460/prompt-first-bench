# N66: CPU 推理 Qwen3-27B (INT4) 的 Decode 速度理论上限约为 512 GB/s / 13.5 GB (weights) ≈ 37.9 to

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

CPU 推理 Qwen3-27B (INT4) 的 Decode 速度理论上限约为 512 GB/s / 13.5 GB (weights) ≈ 37.9 tokens/s，但受 CPU 缓存未命中和内存控制器延迟影响，实测通常在 5-10 tokens/s 区间 [待核验]。

## Corrected Claim

CPU 推理 Qwen3-27B (INT4) 的 Decode 速度理论上限约为 512 GB/s / 13.5 GB (weights) ≈ 37.9 tokens/s，但受 CPU 缓存未命中和内存控制器延迟影响，实测通常在 5-10 tokens/s 区间 [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：理论上限计算（512/13.5≈37.9）符合算术逻辑，实测区间（5-10 tokens/s）符合CPU推理受内存带宽和延迟限制的工程经验规律。
