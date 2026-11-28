# N36: TP=4 下 AllReduce 数据量精确计算：对于 Transformer 层，AllReduce 发生在 Attention Output Project

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

TP=4 下 AllReduce 数据量精确计算：对于 Transformer 层，AllReduce 发生在 Attention Output Projection 和 MLP 中间层。数据量 = batch_size * seq_len * hidden_size * dtype_bytes。对于 decode 阶段 (batch=1, seq_len=1, hidden=5120, fp16)，数据量 = 1*1*5120*2 = 10.24 KB/层。若有 32 层，总通信量 = 327.68 KB/step。N8 中提到的 40 MB 可能是 prefill 阶段或错误估算。需区分 prefill (seq_len=262144) 和 decode (seq_len=1) 两种场景下的通信瓶颈差异。

## Corrected Claim

TP=4 下 AllReduce 数据量精确计算：对于 Transformer 层，AllReduce 发生在 Attention Output Projection 和 MLP 中间层。数据量 = batch_size * seq_len * hidden_size * dtype_bytes。对于 decode 阶段 (batch=1, seq_len=1, hidden=5120, fp16)，数据量 = 1*1*5120*2 = 10.24 KB/层。若有 32 层，总通信量 = 327.68 KB/step。N8 中提到的 40 MB 可能是 prefill 阶段或错误估算。需区分 prefill (seq_len=262144) 和 decode (seq_len=1) 两种场景下的通信瓶颈差异。

## Evidence

先验知识/题面给定，逻辑校验通过：TP=4下AllReduce通信量计算符合Transformer并行原理，数值量级合理（10.24KB/层 * 32层 = 327.68KB），且正确区分了prefill与decode阶段的通信瓶颈差异。

## Search Query

tensor parallel allreduce data volume calculation transformer hidden size decode step vs prefill
