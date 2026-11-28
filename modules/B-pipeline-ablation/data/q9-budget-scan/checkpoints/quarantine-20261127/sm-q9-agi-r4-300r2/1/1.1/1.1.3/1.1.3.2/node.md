# N101: TP=4 AllReduce 通信量公式：每次 Forward/Backward 的 Attention 和 FFN 层后需进行 AllReduce。单次 Al

- **status**: pending
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

父节点级核验未通过：不完备（子节点分别覆盖了Decode、Prefill和MTP三个阶段，彼此正交且无冗余。但是，父节点明确提到了'Batch_Size'对通信量的影响，而子节点1（Decode）固定Batch_Size=1，子节点3（MTP）虽提到B但未展开不同B值的影响，导致对父节点中'Batch_Size变量'这一关键维度的覆盖不完整（缺少通用公式或不同B值下的对比分析）。）
