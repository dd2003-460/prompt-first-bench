# N23: TP=4下AllReduce通信量为2 * batch_size * seq_len * 4096 * 2 bytes，在seq_len=4096、batch_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

TP=4下AllReduce通信量为2 * batch_size * seq_len * 4096 * 2 bytes，在seq_len=4096、batch_size=8时，单次通信量约为512MB

## Corrected Claim

TP=4下AllReduce通信量为2 * batch_size * seq_len * 4096 * 2 bytes，在seq_len=4096、batch_size=8时，单次通信量约为512MB

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程为 2 * 8 * 4096 * 4096 * 2 = 536,870,912 bytes，即 512 MiB，数值量级与公式推导完全一致。
