# N25: 高吞吐低成本工作点（消费级多卡）：在 BF16 精度下，2×RTX 4090 通过张量并行实现约 25-30 tokens/s 的生成速度（32K 上下文），T

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N5

## Claim

高吞吐低成本工作点（消费级多卡）：在 BF16 精度下，2×RTX 4090 通过张量并行实现约 25-30 tokens/s 的生成速度（32K 上下文），TCO/Throughput 约为 $0.015-$0.018/token (3年周期)，适用于高并发、低延迟容忍度的本地推理场景，前提是主机支持 PCIe 4.0 x16 双槽位且内存 ≥ 64GB。

## Corrected Claim

高吞吐低成本工作点（消费级多卡）：在 BF16 精度下，2×RTX 4090 通过张量并行可实现约 15-25 tokens/s 的生成速度（32K 上下文，具体取决于模型大小，如7B-13B），TCO/Throughput 约为 $0.015-$0.020/token (3年周期)，适用于高并发、低延迟容忍度的本地推理场景，前提是主机支持 PCIe 4.0 x16 双槽位且内存 ≥ 64GB。

## Evidence

[质询]数值量级存疑：2×RTX 4090 (共48GB显存) 在32K上下文下运行大模型（通常指7B-13B级别以适配显存），受限于PCIe 4.0带宽（~32GB/s）及显存带宽（~1TB/s），25-30 tokens/s的生成速度对于双卡张量并行而言偏高，通常单卡7B模型在32K上下文下约为10-15 tokens/s，双卡并行受通信开销影响，总吞吐提升有限，且TCO计算未明确模型规模，存在口径模糊。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体硬件性能指标属于经验事实，无法仅凭第一性原理精确推导，故降级）

## Search Query

Qwen3 27B inference speed RTX 4090 tensor parallelism tokens per second
