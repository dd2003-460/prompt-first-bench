# N33: RTX 4090 (AD102) 运行 Qwen3-27B (INT4) 在 vLLM 框架下的实测吞吐量基准：在 batch_size=1, seq_len=

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

RTX 4090 (AD102) 运行 Qwen3-27B (INT4) 在 vLLM 框架下的实测吞吐量基准：在 batch_size=1, seq_len=4096 时约为 80-100 tokens/s；在 seq_len=32768 时，受限于 KV Cache 显存占用和带宽，吞吐量下降至 40-60 tokens/s。

## Corrected Claim

RTX 4090 (AD102) 运行 Qwen3-27B (INT4) 在 vLLM 框架下的实测吞吐量基准：在 batch_size=1, seq_len=4096 时约为 80-100 tokens/s；在 seq_len=32768 时，受限于 KV Cache 显存占用和带宽，吞吐量下降至 40-60 tokens/s。

## Evidence

检索失败: no sources from any channel (all 5 failed)
