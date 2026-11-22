# N28: 2×RTX 3090通过PCIe 4.0互联进行27B模型推理时，由于KV Cache分片导致的通信开销约为单卡性能的15-20%损耗，使得其有效吞吐量低于单卡

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

2×RTX 3090通过PCIe 4.0互联进行27B模型推理时，由于KV Cache分片导致的通信开销约为单卡性能的15-20%损耗，使得其有效吞吐量低于单卡RTX 4090的80%；该系数需基于NCCL all-reduce基准测试或具体推理框架（如DeepSpeed）的多卡扩展效率报告

## Corrected Claim

2×RTX 3090通过PCIe 4.0互联进行27B模型推理时，由于KV Cache分片导致的通信开销约为单卡性能的15-20%损耗，使得其有效吞吐量低于单卡RTX 4090的80%；该系数需基于NCCL all-reduce基准测试或具体推理框架（如DeepSpeed）的多卡扩展效率报告

## Evidence

检索失败: no sources from any channel (all 5 failed)
