# N64: 最大安全序列长度 (Max_Safe_Seq) 推导：已知单卡可用 KV 显存 ~12.6 GB (N9)。在 max_num_seqs=8 并发下，总可用 K

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

最大安全序列长度 (Max_Safe_Seq) 推导：已知单卡可用 KV 显存 ~12.6 GB (N9)。在 max_num_seqs=8 并发下，总可用 KV 空间 = 12.6 GB * 4 (cards) / 8 (seqs) = 6.3 GB/seq (假设 TP 均匀分摊 KV)。若单 token KV 为 64 KB (FP8)，则 Max_Safe_Seq = 6.3 * 1024 * 1024 KB / 64 KB ≈ 102,400 tokens。若为 FP16 (128 KB)，则 Max_Safe_Seq ≈ 51,200 tokens。这与 max_model_len=262144 存在巨大缺口，证实 N18 的瓶颈判断。

## Corrected Claim

最大安全序列长度 (Max_Safe_Seq) 推导：已知单卡可用 KV 显存 ~12.6 GB (N9)。在 max_num_seqs=8 并发下，总可用 KV 空间 = 12.6 GB * 4 (cards) / 8 (seqs) = 6.3 GB/seq (假设 TP 均匀分摊 KV)。若单 token KV 为 64 KB (FP8)，则 Max_Safe_Seq = 6.3 * 1024 * 1024 KB / 64 KB ≈ 102,400 tokens。若为 FP16 (128 KB)，则 Max_Safe_Seq ≈ 51,200 tokens。这与 max_model_len=262144 存在巨大缺口，证实 N18 的瓶颈判断。

## Evidence

先验知识/题面给定，逻辑校验通过：算术推导正确（12.6*4/8=6.3GB; 6.3*1024^2/64≈102400），量级合理，符合KV Cache显存计算的基本逻辑。
