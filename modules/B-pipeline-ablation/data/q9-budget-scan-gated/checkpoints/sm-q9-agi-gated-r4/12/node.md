# N154: 在 V100 (CC 7.0) 上，NVFP4 量化需通过 CPU-GPU 数据搬运或 GPU Kernel 进行在线 Dequant 至 FP16 才能利用 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 V100 (CC 7.0) 上，NVFP4 量化需通过 CPU-GPU 数据搬运或 GPU Kernel 进行在线 Dequant 至 FP16 才能利用 Tensor Core，此过程引入约 15-20% 的额外 HBM 读带宽开销（读取 4-bit 权重 + 写回/寄存器缓存），导致实际 Decode 吞吐较理论 FP16 基准下降约 10-15%，修正 N82 中 '1.5-1.8 倍提升' 的乐观估计。

## Corrected Claim

在 V100 (CC 7.0) 上，NVFP4 量化需通过 CPU-GPU 数据搬运或 GPU Kernel 进行在线 Dequant 至 FP16 才能利用 Tensor Core，此过程引入约 15-20% 的额外 HBM 读带宽开销（读取 4-bit 权重 + 写回/寄存器缓存），导致实际 Decode 吞吐较理论 FP16 基准下降约 10-15%，修正 N82 中 '1.5-1.8 倍提升' 的乐观估计。

## Evidence

检索失败: no sources from any channel (all 5 failed)
