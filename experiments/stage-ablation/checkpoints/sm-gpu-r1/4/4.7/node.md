# N24: 软件栈兼容性风险：消费级 GPU（如 RTX 4090）支持 CUDA 12.x，但部分数据中心特性（如 MIG、多实例 GPU）不可用；数据中心卡（如 H10

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

软件栈兼容性风险：消费级 GPU（如 RTX 4090）支持 CUDA 12.x，但部分数据中心特性（如 MIG、多实例 GPU）不可用；数据中心卡（如 H100）支持 MIG 分割，可将 1 卡虚拟为 7 个实例，提升利用率；需量化 MIG 对 27B 模型推理的适用性（27B 需要至少 2 个 MIG 实例，每个实例 24GB HBM）

## Corrected Claim

软件栈兼容性风险：消费级 GPU（如 RTX 4090）支持 CUDA 12.x，但部分数据中心特性（如 MIG、多实例 GPU）不可用；数据中心卡（如 H100）支持 MIG 分割，可将 1 卡虚拟为 7 个实例，提升利用率；需量化 MIG 对 27B 模型推理的适用性（27B 需要至少 2 个 MIG 实例，每个实例 24GB HBM）

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 不支持 MIG 是已知事实；H100 支持 MIG 且最大可分割为 7 个实例（1g.24gb）符合 NVIDIA 官方规格；27B 模型 FP16 权重约 54GB，需 2 个 24GB 实例（共 48GB）加上 KV Cache 和激活值，逻辑上合理且自洽。

## Search Query

NVIDIA MIG Multi-Instance GPU H100 partitioning memory
