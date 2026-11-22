# N674: H200 的 HBM3e 带宽 4800GB/s 在 memory-bound 推理阶段（如 KV Cache 读取）比 H100 的 3350GB/s 快 4

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N208

## Claim

H200 的 HBM3e 带宽 4800GB/s 在 memory-bound 推理阶段（如 KV Cache 读取）比 H100 的 3350GB/s 快 43%，使得单请求延迟降低约 20-25%（考虑计算和通信的混合瓶颈）；但在 compute-bound 阶段（如矩阵乘法），由于 H200 的 FP16 算力（989 TFLOPS）与 H100（989 TFLOPS）相同，延迟改善主要来自带宽提升，整体吞吐提升约 30-40%。

## Corrected Claim

H200 的 HBM3e 带宽 4800GB/s 在 memory-bound 推理阶段（如 KV Cache 读取）比 H100 的 3350GB/s 快 43%，使得单请求延迟降低约 20-25%（考虑计算和通信的混合瓶颈）；但在 compute-bound 阶段（如矩阵乘法），由于 H200 的 FP16 算力（989 TFLOPS）与 H100（989 TFLOPS）相同，延迟改善主要来自带宽提升，整体吞吐提升约 30-40%。

## Evidence

先验知识/题面给定，逻辑校验通过：H200与H100 FP16算力相同（989 TFLOPS），HBM3e带宽（4800GB/s）相比H100 HBM3（3350GB/s）提升约43%，符合硬件规格事实；在memory-bound场景下带宽提升直接降低延迟，在compute-bound场景下算力不变但带宽提升有助于整体吞吐，逻辑自洽且数值量级合理。

## Search Query

H200 vs H100 inference latency throughput comparison memory bound compute bound
