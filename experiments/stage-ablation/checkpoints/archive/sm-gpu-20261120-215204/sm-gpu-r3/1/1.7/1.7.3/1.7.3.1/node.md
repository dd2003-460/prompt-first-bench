# N197: 2×RTX 4090 在 Decode 阶段 (Batch=1) 的有效吞吐提升率计算：单卡 4090 理论 38 Tokens/s，双卡理论 76 Token

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N68

## Claim

2×RTX 4090 在 Decode 阶段 (Batch=1) 的有效吞吐提升率计算：单卡 4090 理论 38 Tokens/s，双卡理论 76 Tokens/s，但受 PCIe 同步 (1.05ms/token) 和内存带宽竞争影响，实际效率因子 η=0.55，实际吞吐 ≈ 42 Tokens/s，提升率仅为 1.1x，远低于 N68 声称的 1.5-1.7x，表明 N68 的估算未计入通信瓶颈。

## Corrected Claim

2×RTX 4090 在 Decode 阶段 (Batch=1) 的有效吞吐受 PCIe 同步和内存带宽竞争影响，实际效率因子通常显著低于 1（例如约 0.55），导致实际吞吐提升率远低于线性叠加（如 1.1x 而非 1.5-1.7x），表明 N68 的估算未充分计入通信瓶颈。

## Evidence

[质询]效率因子 η=0.55 及由此推导出的 42 Tokens/s 和 1.1x 提升率属于具体的经验性工程估算，缺乏通用物理定律或第一性原理的直接推导支持，且不同硬件配置、驱动版本及具体模型架构下，PCIe 同步开销与内存带宽竞争的实际影响差异巨大，该特定数值可能不具备普适性。 | 先验知识/题面给定，逻辑校验通过（数学计算自洽：38*0.55≈20.9，20.9*2≈41.8≈42，42/38≈1.1），但作为经验事实缺乏外部来源直接支持，故降级。

## Search Query

RTX 4090 dual card LLM inference throughput efficiency
