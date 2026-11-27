# N336: RTX 4090 上 FP8 模拟的性能损耗量化：由于 FP8 需反量化为 BF16/INT8 进行计算，其有效算力受限于 BF16 Tensor Core 峰

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N133

## Claim

RTX 4090 上 FP8 模拟的性能损耗量化：由于 FP8 需反量化为 BF16/INT8 进行计算，其有效算力受限于 BF16 Tensor Core 峰值 (RTX 4090 BF16 ~165 TFLOPS) 或 INT8 峰值 (~330 TOPS)。相比原生 FP8 支持硬件 (如 H100 FP8 ~1979 TFLOPS 稀疏/989 TFLOPS 稠密)，RTX 4090 的 FP8 '模拟' 吞吐仅为其 BF16 性能的 ~100% (因反量化开销，实际可能略低于 BF16，约 95-100%)，而非 FP8 理论加速比。因此，在 RTX 4090 上使用 FP8 量化无性能收益，仅有显存节省收益 (24GB vs 58GB)。

## Corrected Claim

RTX 4090 上 FP8 模拟的性能损耗量化：由于 FP8 需反量化为 BF16/INT8 进行计算，其有效算力受限于 BF16 Tensor Core 峰值 (RTX 4090 BF16 ~165 TFLOPS) 或 INT8 峰值 (~330 TOPS)。相比原生 FP8 支持硬件 (如 H100 FP8 ~1979 TFLOPS 稀疏/989 TFLOPS 稠密)，RTX 4090 的 FP8 '模拟' 吞吐仅为其 BF16 性能的 ~100% (因反量化开销，实际可能略低于 BF16，约 95-100%)，而非 FP8 理论加速比。因此，在 RTX 4090 上使用 FP8 量化无性能收益，仅有显存节省收益 (24GB vs 58GB)。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 (Ada Lovelace架构) 确实不支持原生FP8 Tensor Core，FP8计算需反量化为BF16/FP16执行，故算力上限受限于BF16峰值，无计算加速收益，仅有显存节省收益。
