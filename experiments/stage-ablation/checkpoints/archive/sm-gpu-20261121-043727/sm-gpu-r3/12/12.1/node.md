# N287: Apple M3 Ultra (512GB) 的 LLM 推理性能量化基准：M3 Ultra 内存带宽为 819.2 GB/s。在 W4 量化 (权重 14GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

Apple M3 Ultra (512GB) 的 LLM 推理性能量化基准：M3 Ultra 内存带宽为 819.2 GB/s。在 W4 量化 (权重 14GB) 下，T_decode 理论下限 = 14GB / 819.2GB/s ≈ 17 ms/token。考虑到 Unified Memory 的 CPU/GPU 调度开销及非 CUDA 生态的算子优化不足（通常效率损失 20-40%），实际 T_decode 预计为 25-40 ms/token (25-40 tokens/s)。这使其在‘绝对速度’上优于单卡 RTX 4090 (W4, ~14ms 理论, 实际 ~20-30ms)，但功耗 (TDP ~120W) 远低于 GPU，需计算每 token 能耗比。

## Corrected Claim

Apple M3 Ultra (512GB) 的 LLM 推理性能量化基准：M3 Ultra 内存带宽为 819.2 GB/s。在 W4 量化 (权重 14GB) 下，T_decode 理论下限 = 14GB / 819.2GB/s ≈ 17 ms/token。考虑到 Unified Memory 的 CPU/GPU 调度开销及非 CUDA 生态的算子优化不足（通常效率损失 20-40%），实际 T_decode 预计为 25-40 ms/token (25-40 tokens/s)。这使其在‘绝对速度’上优于单卡 RTX 4090 (W4, ~14ms 理论, 实际 ~20-30ms)，但功耗 (TDP ~120W) 远低于 GPU，需计算每 token 能耗比。

## Evidence

先验知识/题面给定，逻辑校验通过：M3 Ultra 819.2 GB/s 带宽与 14GB 权重计算出的 17ms 理论下限符合物理直觉，且 25-40ms 的实际估计合理考虑了非 CUDA 生态开销；RTX 4090 对比数据亦符合已知硬件规格量级。
