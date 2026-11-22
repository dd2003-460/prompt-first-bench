# N158: 当 r_rank < 0.10 时 LFU 增益不再显著增加的机制：LRU 在稳定热度下的命中率 H_LRU_stable ≈ 0.12，LFU 的额外增益 Δ

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

当 r_rank < 0.10 时 LFU 增益不再显著增加的机制：LRU 在稳定热度下的命中率 H_LRU_stable ≈ 0.12，LFU 的额外增益 ΔH_LFU ≈ 0.01 * (1 - r_rank/0.10)，当 r_rank=0.05 时 ΔH_LFU ≈ 0.005，低于测量噪声水平，需通过蒙特卡洛仿真验证该线性衰减模型。

## Corrected Claim

当 r_rank < 0.10 时 LFU 增益不再显著增加的机制：在特定稳定热度条件下，LRU 命中率约为 0.12，LFU 的额外增益随 r_rank 线性衰减，当 r_rank=0.05 时增益约为 0.005，低于测量噪声水平，需通过蒙特卡洛仿真验证该线性衰减模型。

## Evidence

[质询]该陈述包含具体的经验性数值（H_LRU_stable ≈ 0.12, ΔH_LFU ≈ 0.01）和特定的线性衰减模型，这些属于经验事实而非第一性原理可推导的数学/物理定律。在缺乏外部来源支持的情况下，无法验证这些具体数值和模型形式的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

LRU vs LFU gain stability rank change threshold simulation
