# N207: H100 SXM5 的显存带宽为 3350 GB/s，在 FP8 精度下 Qwen3-27B 权重占用 27GB，理论 Decode 吞吐上限为 3350/27

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

H100 SXM5 的显存带宽为 3350 GB/s，在 FP8 精度下 Qwen3-27B 权重占用 27GB，理论 Decode 吞吐上限为 3350/27 ≈ 124 Tokens/s；在 BF16 精度下权重占用 54GB，理论上限为 3350/54 ≈ 62 Tokens/s，带宽限制下的吞吐比约为 2.0 倍，与算力比一致。

## Corrected Claim

H100 SXM5 的显存带宽为 3350 GB/s，在 FP8 精度下 Qwen3-27B 权重占用 27GB，理论 Decode 吞吐上限为 3350/27 ≈ 124 Tokens/s；在 BF16 精度下权重占用 54GB，理论上限为 3350/54 ≈ 62 Tokens/s，带宽限制下的吞吐比约为 2.0 倍，与算力比一致。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 显存带宽 3.35TB/s 为公认规格；Qwen3-27B 参数量约 27B，FP8 单字节/参数对应 27GB，BF16 双字节/参数对应 54GB；带宽除以权重大小即为单流 Decode 理论上限，计算 3350/27≈124 和 3350/54≈62 正确，且 2.0 倍带宽比与 2.0 倍算力比（FP8 vs BF16）在算术上自洽。
