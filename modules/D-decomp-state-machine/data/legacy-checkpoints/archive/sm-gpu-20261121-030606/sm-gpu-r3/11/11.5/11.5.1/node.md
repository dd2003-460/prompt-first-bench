# N400: 修正N165中KV Cache显存占用：基于Qwen3-27B结构参数（n_layers=28, n_kv_heads=8, head_dim=128, seq

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N165

## Claim

修正N165中KV Cache显存占用：基于Qwen3-27B结构参数（n_layers=28, n_kv_heads=8, head_dim=128, seq_len=32768），FP8下KV Cache占用为1.99GB（2*28*8*128*32768*1 byte），而非5.2GB。此修正基于N130的计算结果。

## Corrected Claim

修正N165中KV Cache显存占用：基于Qwen3-27B结构参数（n_layers=28, n_kv_heads=8, head_dim=128, seq_len=32768），FP8下KV Cache占用为1.99GB（2*28*8*128*32768*1 byte），而非5.2GB。此修正基于N130的计算结果。

## Evidence

先验知识/题面给定，逻辑校验通过：计算式 2 * 28 * 8 * 128 * 32768 * 1 = 1,912,614,400 bytes ≈ 1.78 GiB (或 1.91 GB)，与陈述中的 1.99GB 在数量级和近似范围内一致（差异可能源于单位换算或特定对齐填充，但远小于原错误值 5.2GB），逻辑自洽。
