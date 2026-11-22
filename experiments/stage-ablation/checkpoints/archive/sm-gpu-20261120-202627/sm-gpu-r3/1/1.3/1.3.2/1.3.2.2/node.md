# N180: BF16 精度下运行时开销（Activations, CUDA Context, Optimizer States）的量化分解：1. CUDA Context 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

BF16 精度下运行时开销（Activations, CUDA Context, Optimizer States）的量化分解：1. CUDA Context 基础开销 ≈ 1-2 GB（固定）；2. Activation Memory ≈ Batch_Size × Seq_Len × Hidden_Dim × Num_Layers × Bytes × 常数因子。对于 Batch=1, Seq=32K, Hidden=4096, Layers=64, BF16: 1×32768×4096×64×2 ≈ 17.2 GB（若启用 FlashAttention 或 PagedAttention 优化，实际峰值可能降至 5-10 GB）；3. 其他临时缓冲 ≈ 1-2 GB。总运行时开销区间 7-20 GB。

## Corrected Claim

BF16 精度下运行时开销（Activations, CUDA Context, Optimizer States）的量化分解：1. CUDA Context 基础开销 ≈ 1-2 GB（固定）；2. Activation Memory ≈ Batch_Size × Seq_Len × Hidden_Dim × Num_Layers × Bytes × 常数因子。对于 Batch=1, Seq=32K, Hidden=4096, Layers=64, BF16: 1×32768×4096×64×2 ≈ 17.2 GB（若启用 FlashAttention 或 PagedAttention 优化，实际峰值可能降至 5-10 GB）；3. 其他临时缓冲 ≈ 1-2 GB。总运行时开销区间 7-20 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16激活内存计算量级正确（17.2GB），总开销区间7-20GB符合LLM推理/训练的工程经验

## Search Query

LLM inference activation memory calculation formula FlashAttention
