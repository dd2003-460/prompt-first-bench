# N214: 在 TP=2 配置下，每生成一个 token 需执行两次 All-Reduce（一次用于残差连接，一次用于输出层前），总通信数据量 D_total_comm =

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N102

## Claim

在 TP=2 配置下，每生成一个 token 需执行两次 All-Reduce（一次用于残差连接，一次用于输出层前），总通信数据量 D_total_comm = 2 * 8.192 KB = 16.384 KB，这是评估总通信开销的正确口径。

## Corrected Claim

在 TP=2 配置下，每生成一个 token 需执行两次 All-Reduce（一次用于残差连接，一次用于输出层前），总通信数据量 D_total_comm = 2 * 8.192 KB = 16.384 KB，这是评估总通信开销的正确口径。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 5 column 13 (char 79)
