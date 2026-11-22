# N194: Qwen3-27B 在 FFN (Feed-Forward Network) 层的中间激活峰值显存占用：Bytes = seq_len * d_ff * byt

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N64

## Claim

Qwen3-27B 在 FFN (Feed-Forward Network) 层的中间激活峰值显存占用：Bytes = seq_len * d_ff * bytes_per_element，其中 d_ff 通常为 4 * d_model = 20480 (需确认 Qwen3 具体配置，若为 SwiGLU 则可能为 8/3 * d_model * 2 等变体，暂按 4*d_model 估算), seq_len=32768, bytes_per_element=2 (BF16)，计算得出 32768 * 20480 * 2 = 1,342,177,280 bytes ≈ 1.25 GB。

## Corrected Claim

Qwen3-27B 在 FFN 层的中间激活峰值显存占用估算约为 1.25 GB（基于 d_ff=20480, seq_len=32768, BF16 假设，具体数值需依据实际模型配置确认）。

## Evidence

[质询]Qwen3-27B 的具体 FFN 维度（d_ff）配置未确认，且 SwiGLU 结构下的中间激活显存计算通常涉及门控机制，直接按 4*d_model 估算可能存在量级偏差或结构假设错误。 | 经验事实，逻辑自洽但缺来源支持
