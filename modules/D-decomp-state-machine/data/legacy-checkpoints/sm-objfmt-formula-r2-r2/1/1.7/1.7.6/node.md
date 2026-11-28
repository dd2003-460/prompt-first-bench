# N67: Qwen3-27B 在 Tensor Parallelism (TP=2) 下，每次 AllReduce 通信的数据量约为 54 MB (27B params 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

Qwen3-27B 在 Tensor Parallelism (TP=2) 下，每次 AllReduce 通信的数据量约为 54 MB (27B params * 2 bytes * 2 activations per layer / 2 cards / 1024^2)，具体随 Batch Size 线性增加。

## Corrected Claim

Qwen3-27B 在 TP=2 下，单次 AllReduce 通信的数据量取决于具体的张量形状（如隐藏层维度、序列长度、批大小等），并非简单由参数量推导得出；总通信开销随层数和 Batch Size 线性增加。

## Evidence

[质询]公式中 '2 activations per layer' 表述模糊且缺乏标准定义，AllReduce 数据量通常取决于激活值大小（Batch Size × Seq Len × Hidden Dim）或梯度大小，而非简单的参数量乘以固定系数；此外，TP 下 AllReduce 发生在每层前向和反向传播中，总通信量与层数成正比，公式未体现层数因子，导致量级估算可能严重偏离实际（例如忽略了层数 N 的影响，或者将单次通信与总通信混淆）。 | 先验知识/题面给定，逻辑校验发现公式推导存在概念混淆（未包含层数因子，激活值定义不清），无法确认 54MB 这一具体数值的准确性，故降级。
