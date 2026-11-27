# N868: 框架选择对硬件选型的影响：若 vLLM 的 16% 增益可抵消使用更便宜硬件的劣势，则需比较 'RTX 4090 + vLLM' vs 'RTX 3090 + 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N271

## Claim

框架选择对硬件选型的影响：若 vLLM 的 16% 增益可抵消使用更便宜硬件的劣势，则需比较 'RTX 4090 + vLLM' vs 'RTX 3090 + llama.cpp' 的性价比，RTX 3090 价格为 $999，带宽 936 GB/s (vs 4090 的 1008 GB/s)，理论吞吐比 = (936 * 0.82) / (1008 * 0.95) = 0.786，即 3090 + llama.cpp 吞吐仅为 4090 + vLLM 的 78.6%，但价格仅为 62.5%，性价比 = 0.786 / 0.625 = 1.258，即 3090 + llama.cpp 性价比更高 [待核验 3090 实际带宽与价格]

## Corrected Claim

框架选择对硬件选型的影响：若 vLLM 的 16% 增益可抵消使用更便宜硬件的劣势，则需比较 'RTX 4090 + vLLM' vs 'RTX 3090 + llama.cpp' 的性价比，RTX 3090 价格为 $999，带宽 936 GB/s (vs 4090 的 1008 GB/s)，理论吞吐比 = (936 * 0.82) / (1008 * 0.95) = 0.786，即 3090 + llama.cpp 吞吐仅为 4090 + vLLM 的 78.6%，但价格仅为 62.5%，性价比 = 0.786 / 0.625 = 1.258，即 3090 + llama.cpp 性价比更高 [需进一步验证 3090 实际带宽与价格及框架性能增益]

## Evidence

[质询]RTX 3090 的显存带宽实际为 936 GB/s，但 RTX 4090 的显存带宽为 1008 GB/s 这一数据存在争议，部分来源指出 4090 带宽为 1008 GB/s，但需确认是否包含 ECC 或其他因素；此外，llama.cpp 和 vLLM 的性能增益（0.82 和 0.95）缺乏具体基准测试支持，可能因模型大小、批次大小等因素变化。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 3090 memory bandwidth GB/s price vs RTX 4090 llama.cpp vLLM throughput comparison
