# N139: AMD RX 7900 XTX 的显存带宽为 1936 GB/s (GDDR6)，在 W4 量化 (权重 13.5GB) 下，理论解码吞吐上限 ≈ 1936 /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

AMD RX 7900 XTX 的显存带宽为 1936 GB/s (GDDR6)，在 W4 量化 (权重 13.5GB) 下，理论解码吞吐上限 ≈ 1936 / 13.5 ≈ 143 tokens/s，实际受限于计算单元效率，通常远低于此带宽上限。

## Corrected Claim

AMD RX 7900 XTX 的显存带宽为 1936 GB/s (GDDR6)，在 W4 量化 (权重 13.5GB) 下，理论解码吞吐上限 ≈ 1936 / 13.5 ≈ 143 tokens/s，实际受限于计算单元效率，通常远低于此带宽上限。

## Evidence

先验知识/题面给定，逻辑校验通过：AMD RX 7900 XTX 显存带宽确为 1936 GB/s，1936/13.5≈143.4 计算正确，且符合大模型推理中带宽瓶颈的基本原理。
