# N64: 最大安全序列长度 (Max_Safe_Seq) 推导：已知单卡可用 KV 显存 ~12.6 GB (N9)。在 max_num_seqs=8 并发下，总可用 K

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

最大安全序列长度 (Max_Safe_Seq) 推导：已知单卡可用 KV 显存 ~12.6 GB (N9)。在 max_num_seqs=8 并发下，总可用 KV 空间 = 12.6 GB * 4 (cards) / 8 (seqs) = 6.3 GB/seq (假设 TP 均匀分摊 KV)。若单 token KV 为 64 KB (FP8)，则 Max_Safe_Seq = 6.3 * 1024 * 1024 KB / 64 KB ≈ 102,400 tokens。若为 FP16 (128 KB)，则 Max_Safe_Seq ≈ 51,200 tokens。这与 max_model_len=262144 存在巨大缺口，证实 N18 的瓶颈判断。

## Corrected Claim

最大安全序列长度 (Max_Safe_Seq) 推导：已知单卡可用 KV 显存 ~12.6 GB (N9)。在 max_num_seqs=8 并发下，总可用 KV 空间 = 12.6 GB * 4 (cards) / 8 (seqs) = 6.3 GB/seq (假设 TP 均匀分摊 KV)。若单 token KV 为 64 KB (FP8)，则 Max_Safe_Seq = 6.3 * 1024 * 1024 KB / 64 KB ≈ 102,400 tokens。若为 FP16 (128 KB)，则 Max_Safe_Seq ≈ 51,200 tokens。这与 max_model_len=262144 存在巨大缺口，证实 N18 的瓶颈判断。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点结构清晰：第一个节点定义了资源约束（分母），后两个节点分别针对两种量化格式（FP8/FP16）给出了具体的推导结果（分子/结果）。它们共同构成了父节点推导的完整逻辑链（前提->计算->结论），且互不重叠。虽然FP8和FP16看似是同一公式的不同参数，但在学术分解中，将关键假设下的不同场景拆分为独立结论有助于明确风险等级（如子节点2提到的OOM风险 vs 子节点3提到的性能减半），因此保留为独立节点是合理的，不构成有害冗余。）
