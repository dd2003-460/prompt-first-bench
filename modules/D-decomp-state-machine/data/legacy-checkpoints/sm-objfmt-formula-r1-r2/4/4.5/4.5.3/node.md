# N94: FP8 量化误差的主要来源分解：注意力分数（Attention Scores）的累积误差贡献约 40-60% 的总精度损失，LayerNorm 归一化误差贡献约

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

FP8 量化误差的主要来源分解：注意力分数（Attention Scores）的累积误差贡献约 40-60% 的总精度损失，LayerNorm 归一化误差贡献约 20-30%，其余来自 FFN 层激活值截断 [待核验具体消融实验数据]

## Corrected Claim

FP8 量化误差主要来源于注意力分数累积误差、LayerNorm 归一化误差及 FFN 层激活值截断，其中注意力分数通常被认为是主要贡献因素之一，但具体占比需依赖特定模型的消融实验数据确定。

## Evidence

[质询]具体百分比数值（40-60%, 20-30%）缺乏通用共识，不同模型架构、数据集及量化策略下误差分布差异巨大，且该陈述本身标注了[待核验具体消融实验数据]，表明其为未经证实的假设或特定实验结果，不具备普适性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值无法从第一性原理推出，属于特定实验数据）。

## Search Query

FP8 quantization error source attribution attention scores vs layernorm ablation study
