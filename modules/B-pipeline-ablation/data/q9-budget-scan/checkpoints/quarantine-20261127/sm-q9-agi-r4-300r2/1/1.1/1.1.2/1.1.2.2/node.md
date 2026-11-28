# N98: 最大上下文长度理论上限计算：Max_Len = Available_KV_Mem / (Bytes_per_token_kv * num_seqs); 若单卡可

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30

## Claim

最大上下文长度理论上限计算：Max_Len = Available_KV_Mem / (Bytes_per_token_kv * num_seqs); 若单卡可用 KV 显存为 10.53 GB (10530 MB)，且 max_num_seqs=8 (假设均匀分配或全局池化)，在 FP8 下 Max_Len ≈ (10530 * 1024 * 1024) / (2048 * 8) ≈ 655,360 tokens (理论值，需减去激活值等动态开销)。

## Corrected Claim

最大上下文长度理论上限计算：Max_Len = Available_KV_Mem / (Bytes_per_token_kv * num_seqs); 若单卡可用 KV 显存为 10.53 GB (10530 MB)，且 max_num_seqs=8 (假设均匀分配或全局池化)，在 FP8 下 Max_Len ≈ (10530 * 1024 * 1024) / (2048 * 8) ≈ 655,360 tokens (理论值，需减去激活值等动态开销)。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别针对‘激活值内存占用’和‘PagedAttention管理开销/碎片化’两个独立维度进行修正，二者互不重叠且共同覆盖了父节点中提到的‘需减去激活值等动态开销’这一关键限制条件，逻辑清晰无冗余。）
