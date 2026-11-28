# N139: TP=4 策略下 FFN 阶段 All-Reduce 的数据量：FFN 中间层升维后降维，需在降维后 AllReduce 以聚合各分片的贡献。单次数据量 = h

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

TP=4 策略下 FFN 阶段 All-Reduce 的数据量：FFN 中间层升维后降维，需在降维后 AllReduce 以聚合各分片的贡献。单次数据量 = hidden_size * bytes_per_elem = 5120 * 2 (FP16) = 10KB。

## Corrected Claim

TP=4 策略下 FFN 阶段 All-Reduce 的数据量：FFN 中间层升维后降维，需在降维后 AllReduce 以聚合各分片的贡献。单次数据量 = hidden_size * bytes_per_elem = 5120 * 2 (FP16) = 10KB。

## Evidence

先验知识/题面给定，逻辑校验通过：TP=4下FFN降维后AllReduce传输的是hidden_size大小的张量，5120*2字节=10KB计算正确。

## Search Query

tensor parallelism feedforward layer allreduce volume calculation
