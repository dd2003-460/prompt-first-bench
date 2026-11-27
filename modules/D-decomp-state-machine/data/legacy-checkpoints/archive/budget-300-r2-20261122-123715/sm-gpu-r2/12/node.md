# N118: Apple M2 Ultra (192GB) 在 Qwen3-27B W4 量化下，首字延迟 (TTFT) 在 32K 上下文预填充阶段约为 2-4 秒，主要受

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Apple M2 Ultra (192GB) 在 Qwen3-27B W4 量化下，首字延迟 (TTFT) 在 32K 上下文预填充阶段约为 2-4 秒，主要受限于 800GB/s 内存带宽下的 Prompt Processing 瓶颈；相比之下，RTX 4090 由于 1008GB/s 带宽及更优的 KV Cache 预填充优化，TTFT 通常可控制在 1-2 秒内。

## Corrected Claim

Apple M2 Ultra (192GB) 在 Qwen3-27B W4 量化下，首字延迟 (TTFT) 在 32K 上下文预填充阶段约为 2-4 秒，主要受限于 800GB/s 内存带宽下的 Prompt Processing 瓶颈；相比之下，RTX 4090 由于 1008GB/s 带宽及更优的 KV Cache 预填充优化，TTFT 通常可控制在 1-2 秒内。

## Evidence

检索失败: no sources from any channel (all 5 failed)
