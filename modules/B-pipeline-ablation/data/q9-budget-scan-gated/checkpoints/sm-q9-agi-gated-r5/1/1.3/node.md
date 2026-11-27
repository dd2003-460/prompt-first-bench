# N9: TP=4 时的 AllReduce 通信开销估算：每次 attention 前后需同步 hidden_states，通信量约为 2 * batch_size *

- **status**: pending
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

父节点级核验未通过：不完备（子节点1聚焦于通信量的具体数值计算（基于特定参数实例化），子节点2聚焦于基于该数值推导出的延迟占比，两者逻辑上层层递进且无重复，满足正交性。然而，父节点包含两个核心部分：1. 通用公式定义（2 * batch_size * seq_len * hidden_dim * 2 bytes）；2. 特定条件下的估算结论。子节点1直接跳到了具体数值实例（hidden_dim=4096等），丢失了父节点中关于'通用公式结构'这一关键知识点的显式覆盖，导致从通用原理到具体案例的中间层缺失，因此不完备。）
