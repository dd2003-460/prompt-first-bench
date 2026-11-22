# N148: LFU在收敛期（前300天）相对于LRU的命中率损失 ΔH_convergence 量化：由于初始频率计数器未收敛，LFU误驱逐高频对象，模拟显示在β=0.9分

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N48

## Claim

LFU在收敛期（前300天）相对于LRU的命中率损失 ΔH_convergence 量化：由于初始频率计数器未收敛，LFU误驱逐高频对象，模拟显示在β=0.9分布下，前300天平均命中率比LRU低约 0.5-1.5 个百分点，该损失随时间指数衰减至0。

## Corrected Claim

LFU在收敛期（前300天）相对于LRU存在命中率损失，这是由于初始频率计数器未收敛导致LFU误驱逐高频对象所致；该损失随时间衰减至0，具体数值取决于访问分布和模拟参数。

## Evidence

[质询]该陈述包含具体的经验性数值（0.5-1.5个百分点）和特定的模拟条件（β=0.9分布），属于经验事实而非第一性原理可推导的数学性质。在缺乏外部来源支持的情况下，无法验证该具体数值量级的准确性，且不同模拟参数下结果可能差异较大。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

LFU cache convergence time penalty vs LRU Zipf distribution simulation
