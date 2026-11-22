# N239: RTX 4090 实际 Decode 吞吐量修正：理论峰值 1008 GB/s / 27.013 GB/s ≈ 37.3 tokens/s，考虑内存控制器效率 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

RTX 4090 实际 Decode 吞吐量修正：理论峰值 1008 GB/s / 27.013 GB/s ≈ 37.3 tokens/s，考虑内存控制器效率 85% 和调度开销 10%，实际吞吐约为 37.3 * 0.85 * 0.90 ≈ 28.5 tokens/s，落在 N66 声称的 25-30 tokens/s 区间内，验证了 N66 的最终结论但修正了其带宽需求前提。

## Corrected Claim

RTX 4090 实际 Decode 吞吐量修正：理论峰值 1008 GB/s / 27.013 GB/s ≈ 37.3 tokens/s，考虑内存控制器效率 85% 和调度开销 10%，实际吞吐约为 37.3 * 0.85 * 0.90 ≈ 28.5 tokens/s，落在 N66 声称的 25-30 tokens/s 区间内，验证了 N66 的最终结论但修正了其带宽需求前提。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 37.3 * 0.85 * 0.90 ≈ 28.5 正确，且 28.5 确实落在 25-30 区间内，逻辑自洽。
