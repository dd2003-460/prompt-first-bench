# N23: 吞吐量 (Throughput) 与硬件参数的映射：在 Batch Size = 1 时，Throughput ≈ Memory_Bandwidth / Wei

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

吞吐量 (Throughput) 与硬件参数的映射：在 Batch Size = 1 时，Throughput ≈ Memory_Bandwidth / Weight_Size_GB；当 Batch Size 增大至饱和点 (Batch_Saturation) 时，Throughput 转为 Compute-Bound，公式变为 Throughput ≈ GPU_FLOPS / (Model_Size * Seq_Len * 2)。RTX 4090 的 Batch_Saturation 通常低于 A100/H100，意味着多用户并发场景下 4090 的边际收益下降更快。

## Corrected Claim

吞吐量与硬件参数的映射关系取决于具体模型架构和实现细节。在 Memory-Bound 阶段，吞吐量受限于内存带宽与权重加载量；在 Compute-Bound 阶段，吞吐量近似等于 GPU 算力除以每 Token 所需的浮点运算次数（FLOPs/Token）。RTX 4090 由于显存带宽和容量限制，其达到计算饱和所需的 Batch Size 通常小于 A100/H100，但在高并发场景下的边际收益需结合具体模型大小评估。

## Evidence

[质询]公式中分母使用 'Model_Size' 存在歧义，若指参数量则量纲错误（应为 FLOPs/Token），若指权重字节数则与分子 FLOPS 单位不匹配；且 RTX 4090 与 A100/H100 的 Batch_Saturation 对比缺乏具体模型规模前提，不同模型下结论可能反转。 | 来源 [1] 仅讨论 Batch Size 与并行策略，未提供吞吐量与硬件参数的映射公式或具体 GPU 对比数据，无法支持该经验事实；公式量纲存在潜在错误。

## Retrieval Sources

- {'url': 'https://www.zhihu.com/question/596311688&rut=69014751954fea5b996fefe14381eee636fe7f86ad57a332d2241bf385cc9abf', 'type': 'ddg', 'title': '大模型训练的性能指标：吞吐率 Throughput 是指什么？'}
