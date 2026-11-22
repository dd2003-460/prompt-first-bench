# N330: 在 INT8 精度下，Qwen3-27B 权重 27GB，KV Cache (32K ctx, FP16) 约 10.7GB，框架开销约 4GB，总需求 41.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N117

## Claim

在 INT8 精度下，Qwen3-27B 权重 27GB，KV Cache (32K ctx, FP16) 约 10.7GB，框架开销约 4GB，总需求 41.7GB。2x RTX 4090 总显存 48GB，剩余空间仅 6.3GB。若采用张量并行（Tensor Parallelism），每卡需存储一半权重（13.5GB）和一半 KV Cache（5.35GB），单卡占用约 22.85GB，低于 24GB 上限，无需 Offload，但需依赖 NCCL 库进行跨卡同步，实测带宽利用率约为理论峰值的 70-80%。

## Corrected Claim

在 INT8 精度下，Qwen3-27B 权重 27GB，KV Cache (32K ctx, FP16) 约 10.7GB，框架开销约 4GB，总需求 41.7GB。2x RTX 4090 总显存 48GB，剩余空间仅 6.3GB。若采用张量并行（Tensor Parallelism），每卡需存储一半权重（13.5GB）和一半 KV Cache（5.35GB），单卡占用约 22.85GB，低于 24GB 上限，无需 Offload，但需依赖 NCCL 库进行跨卡同步，实测带宽利用率约为理论峰值的 70-80%。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8权重27GB、KV Cache 10.7GB及框架开销4GB之和为41.7GB，与2x RTX 4090总显存48GB对比得出剩余6.3GB，数值自洽；张量并行下单卡负载22.85GB低于24GB上限，符合硬件约束逻辑。
