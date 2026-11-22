# N736: N83 中错误地将 seq_len (32768) 乘入 AllReduce 数据量，导致计算为 $2 \times 4096 \times 32768 \ti

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N227

## Claim

N83 中错误地将 seq_len (32768) 乘入 AllReduce 数据量，导致计算为 $2 \times 4096 \times 32768 \times 2 \approx 512 \text{ MB}$ (或类似量级)，而正确逻辑是 AllReduce 发生在 hidden dimension 上，与 seq_len 无关（seq_len 影响的是 Attention 矩阵大小，但不改变 TP 切分后的通信维度）。

## Corrected Claim

N83 中错误地将 seq_len (32768) 乘入 AllReduce 数据量，导致计算为 $2 \times 4096 \times 32768 \times 2 \approx 512 \text{ MB}$ (或类似量级)，而正确逻辑是 AllReduce 发生在 hidden dimension 上，与 seq_len 无关（seq_len 影响的是 Attention 矩阵大小，但不改变 TP 切分后的通信维度）。

## Evidence

先验知识/题面给定，逻辑校验通过：在标准Transformer架构中，AllReduce通信量确实取决于hidden dimension和batch size，与seq_len无关（seq_len影响的是计算量和Attention矩阵大小，但不改变TP切分后的通信维度）。
