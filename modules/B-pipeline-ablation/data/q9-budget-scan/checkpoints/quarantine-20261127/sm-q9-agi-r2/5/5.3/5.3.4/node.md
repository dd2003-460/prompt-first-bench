# N83: 嵌入模型对新颖性评分敏感度的影响：使用 bge-large-en-v1.5 (1024维) 相比 all-MiniLM-L6-v2 (384维)，在区分细微语义

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23

## Claim

嵌入模型对新颖性评分敏感度的影响：使用 bge-large-en-v1.5 (1024维) 相比 all-MiniLM-L6-v2 (384维)，在区分细微语义差异上的余弦距离分辨率提高约 15%；具体表现为：对于相似度 >0.95 的近邻文献，bge-large 能更准确地将 S_nov 压低 0.3-0.5 分，避免将微调改进误判为高创新；但 bge-large 嵌入计算耗时 T_embed 是 MiniLM 的 3 倍 (3.6s/doc vs 1.2s/doc)，需权衡精度与索引更新频率。

## Corrected Claim

嵌入模型对新颖性评分敏感度有显著影响：通常较高维度的模型（如 bge-large-en-v1.5）相比低维度模型（如 all-MiniLM-L6-v2）在区分细微语义差异上具有更高的余弦距离分辨率，能更准确地区分近邻文献的创新度，避免将微调改进误判为高创新；但其计算耗时通常显著高于轻量级模型，需在精度与索引更新频率间权衡。

## Evidence

[质询]具体的性能提升数值（15%分辨率、0.3-0.5分压低幅度、3倍耗时比）属于特定实验环境下的经验数据，缺乏通用基准测试的直接支持，不同硬件和负载下波动较大。 | 先验知识/题面给定，逻辑校验通过；但具体数值为经验事实，无外部来源直接支持，故降级。

## Search Query

bge-large-en-v1.5 vs all-MiniLM-L6-v2 novelty detection sensitivity
