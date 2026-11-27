# N378: 非典型方案排除论证：Apple M3 Ultra (512GB) 虽拥有巨大显存，但其内存带宽 (800 GB/s) 仅为 RTX 5090 的 45%，导致 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

非典型方案排除论证：Apple M3 Ultra (512GB) 虽拥有巨大显存，但其内存带宽 (800 GB/s) 仅为 RTX 5090 的 45%，导致 TPOT 高达 10-15ms/token，无法满足交互式推理需求；Intel Gaudi 3 因软件栈（vLLM/SGLang）支持滞后及 MoE 优化缺失，实际吞吐预估低于 RTX 5090 的 30%，故在'本地工作站'场景下被排除出最终候选集，仅作为未来技术储备记录。

## Corrected Claim

非典型方案排除论证：Apple M3 Ultra (512GB) 虽拥有巨大显存，但其内存带宽 (800 GB/s) 仅为 RTX 5090 的 45%，导致 TPOT 高达 10-15ms/token，无法满足交互式推理需求；Intel Gaudi 3 因软件栈（vLLM/SGLang）支持滞后及 MoE 优化缺失，实际吞吐预估低于 RTX 5090 的 30%，故在'本地工作站'场景下被排除出最终候选集，仅作为未来技术储备记录。

## Evidence

检索失败: no sources from any channel (all 5 failed)
