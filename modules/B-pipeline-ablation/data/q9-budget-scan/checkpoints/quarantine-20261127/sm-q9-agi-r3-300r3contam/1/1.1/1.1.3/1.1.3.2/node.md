# N101: TP=4 AllReduce 通信量公式：每次 Forward/Backward 的 Attention 和 FFN 层后需进行 AllReduce。单次 Al

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

TP=4 AllReduce 通信量公式：每次 Forward/Backward 的 Attention 和 FFN 层后需进行 AllReduce。单次 AllReduce 数据量 Data_Size = Batch_Size * Seq_Len * Hidden_Dim * Dtype_Bytes。对于 FP16/BF16 梯度同步，Dtype_Bytes=2。在 Prefill 阶段，Seq_Len 较大，通信量大；在 Decode 阶段，Seq_Len=1，通信量小但频率高。

## Corrected Claim

TP=4 AllReduce 通信量公式：每次 Forward/Backward 的 Attention 和 FFN 层后需进行 AllReduce。单次 AllReduce 数据量 Data_Size = Batch_Size * Seq_Len * Hidden_Dim * Dtype_Bytes。对于 FP16/BF16 梯度同步，Dtype_Bytes=2。在 Prefill 阶段，Seq_Len 较大，通信量大；在 Decode 阶段，Seq_Len=1，通信量小但频率高。

## Evidence

先验知识/题面给定，逻辑校验通过
