# N206: AWQ 算法在 Qwen3-27B 4-bit 量化下的困惑度增加量 ΔPPL 具体数值需查阅官方或社区基准，通常认为 AWQ 的 ΔPPL 比 GPTQ 低 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

AWQ 算法在 Qwen3-27B 4-bit 量化下的困惑度增加量 ΔPPL 具体数值需查阅官方或社区基准，通常认为 AWQ 的 ΔPPL 比 GPTQ 低 10-20% 是指相对值，若 GPTQ ΔPPL=1.2，则 AWQ ΔPPL≈0.96-1.08；具体数值需对比同一校准集下的 PPL 测试 [待核验]。

## Corrected Claim

AWQ 算法在 Qwen3-27B 4-bit 量化下的困惑度增加量 ΔPPL 具体数值需查阅官方或社区基准。通常认为 AWQ 的 ΔPPL 相对 GPTQ 较低，但具体相对降低幅度（如 10-20%）及绝对数值（如 GPTQ ΔPPL=1.2 时 AWQ ΔPPL≈0.96-1.08）需基于同一校准集下的 PPL 测试数据验证，不同模型和校准集下表现可能存在差异。

## Evidence

[质询]该陈述包含具体的经验性数值范围（10-20%）和特定模型（Qwen3-27B）的量化表现，属于经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

AWQ vs GPTQ Qwen3 perplexity comparison 4bit
