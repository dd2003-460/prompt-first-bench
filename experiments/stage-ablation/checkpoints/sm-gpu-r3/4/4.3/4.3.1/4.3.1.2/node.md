# N214: 在 TP=2 配置下，每生成一个 token 需执行两次 All-Reduce（一次用于残差连接，一次用于输出层前），总通信数据量 D_total_comm =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

在 TP=2 配置下，每生成一个 token 需执行两次 All-Reduce（一次用于残差连接，一次用于输出层前），总通信数据量 D_total_comm = 2 * 8.192 KB = 16.384 KB，这是评估总通信开销的正确口径。

## Corrected Claim

在 TP=2 配置下，每生成一个 token 需执行两次 All-Reduce（一次用于残差连接，一次用于输出层前），总通信数据量 D_total_comm = 2 * 8.192 KB = 16.384 KB，这是评估总通信开销的正确口径。

## Evidence

先验知识/题面给定，逻辑校验通过：TP=2下，Transformer标准架构中残差连接（Add & Norm）和输出层前（Logits计算前）确实各需一次All-Reduce，通信量计算符合张量并行原理。
