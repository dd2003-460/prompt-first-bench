# N246: 2x RTX 4090 方案中单卡故障导致的服务降级模式定义：在 Tensor Parallelism (TP=2) 架构下，若一张卡故障，系统无法直接降级为单

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

2x RTX 4090 方案中单卡故障导致的服务降级模式定义：在 Tensor Parallelism (TP=2) 架构下，若一张卡故障，系统无法直接降级为单卡运行（因为模型权重被分片），必须重启服务并重新加载模型，导致 100% 服务中断而非 N73 中假设的 50% 降级；因此实际可用性损失应基于全停模型计算。

## Corrected Claim

2x RTX 4090 方案中单卡故障导致的服务降级模式定义：在 Tensor Parallelism (TP=2) 架构下，若一张卡故障，系统无法直接降级为单卡运行（因为模型权重被分片），必须重启服务并重新加载模型，导致 100% 服务中断而非 N73 中假设的 50% 降级；因此实际可用性损失应基于全停模型计算。

## Evidence

先验知识/题面给定，逻辑校验通过：Tensor Parallelism 要求所有参与分片的 GPU 同时在线以完成矩阵乘法，单卡故障导致通信阻塞或计算缺失，无法通过简单移除节点降级为单卡运行（除非重新加载完整权重），故全停模型符合技术逻辑。
