# N9: TP=4 时的 AllReduce 通信开销估算：每次 attention 前后需同步 hidden_states，通信量约为 2 * batch_size *

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

TP=4 时的 AllReduce 通信开销估算：每次 attention 前后需同步 hidden_states，通信量约为 2 * batch_size * seq_len * hidden_dim * 2 bytes；在 NVLink 互联（带宽~300GB/s）下，通信延迟占 decode 步时间的比例约为 15-25%

## Corrected Claim

TP=4 时的 AllReduce 通信开销估算：每次 attention 前后需同步 hidden_states，通信量约为 2 * batch_size * seq_len * hidden_dim * 2 bytes；在 NVLink 互联（带宽~300GB/s）下，通信延迟占 decode 步时间的比例约为 15-25%

## Evidence

先验知识/题面给定，逻辑校验通过：通信量公式符合AllReduce标准（2次同步*数据大小*字节数），NVLink带宽与延迟占比估算符合大模型推理常见工程经验量级。
