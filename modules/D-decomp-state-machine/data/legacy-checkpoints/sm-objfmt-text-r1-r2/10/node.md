# N23: 吞吐量 (Throughput) 与硬件参数的映射：在 Batch Size = 1 时，Throughput ≈ Memory_Bandwidth / Wei

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

吞吐量 (Throughput) 与硬件参数的映射：在 Batch Size = 1 时，Throughput ≈ Memory_Bandwidth / Weight_Size_GB；当 Batch Size 增大至饱和点 (Batch_Saturation) 时，Throughput 转为 Compute-Bound，公式变为 Throughput ≈ GPU_FLOPS / (Model_Size * Seq_Len * 2)。RTX 4090 的 Batch_Saturation 通常低于 A100/H100，意味着多用户并发场景下 4090 的边际收益下降更快。

## Corrected Claim

吞吐量与硬件参数的映射关系取决于具体模型架构和实现细节。在 Memory-Bound 阶段，吞吐量受限于内存带宽与权重加载量；在 Compute-Bound 阶段，吞吐量近似等于 GPU 算力除以每 Token 所需的浮点运算次数（FLOPs/Token）。RTX 4090 由于显存带宽和容量限制，其达到计算饱和所需的 Batch Size 通常小于 A100/H100，但在高并发场景下的边际收益需结合具体模型大小评估。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：分别对应低负载（Memory-Bound）、转折点（Batch_Saturation定义）、高负载（Compute-Bound）以及物理约束（显存限制）。虽然子节点2和3都涉及FLOPS，但分别定义了临界点和饱和后的状态，属于不同阶段，不构成冗余。完备性上，涵盖了公式推导、具体硬件对比及多用户场景下的边际效应分析。）

## Retrieval Sources

- {'url': 'https://www.zhihu.com/question/596311688&rut=69014751954fea5b996fefe14381eee636fe7f86ad57a332d2241bf385cc9abf', 'type': 'ddg', 'title': '大模型训练的性能指标：吞吐率 Throughput 是指什么？'}
