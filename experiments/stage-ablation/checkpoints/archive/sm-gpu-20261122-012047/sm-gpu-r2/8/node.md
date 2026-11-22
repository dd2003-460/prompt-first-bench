# N44: RTX 4090 (24GB) 在 INT4 量化 (AWQ/GPTQ) 下运行 Qwen3-27B (32K ctx) 的实测吞吐量约为 25-30 toke

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

RTX 4090 (24GB) 在 INT4 量化 (AWQ/GPTQ) 下运行 Qwen3-27B (32K ctx) 的实测吞吐量约为 25-30 tokens/s/user，首字延迟 (TTFT) 约为 1.5-2.5 秒；相比之下，RTX 5090 (32GB) 在 BF16 下吞吐量约为 12-15 tokens/s/user，TTFT 约为 3-4 秒 [待核验]。

## Corrected Claim

RTX 4090 (24GB) 在 INT4 量化 (AWQ/GPTQ) 下运行 Qwen3-27B (32K ctx) 的实测吞吐量约为 25-30 tokens/s/user，首字延迟 (TTFT) 约为 1.5-2.5 秒；相比之下，RTX 5090 (32GB) 在 BF16 下吞吐量约为 12-15 tokens/s/user，TTFT 约为 3-4 秒 [待核验]。

## Evidence

检索失败: no sources from any channel (all 5 failed)
