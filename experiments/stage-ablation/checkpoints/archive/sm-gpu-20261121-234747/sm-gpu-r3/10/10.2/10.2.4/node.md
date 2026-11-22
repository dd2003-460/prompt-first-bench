# N490: FP8 量化中 E4M3 格式与 E5M2 格式对 MMLU 准确率的影响差异：E4M3 (7位尾数) 通常用于权重存储，E5M2 (5位尾数) 用于激活值；需

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N155

## Claim

FP8 量化中 E4M3 格式与 E5M2 格式对 MMLU 准确率的影响差异：E4M3 (7位尾数) 通常用于权重存储，E5M2 (5位尾数) 用于激活值；需引用具体论文或实测数据说明在 27B 模型混合精度配置下，两种格式组合导致的 ΔMMLU 差异是否在 0.05% 以内 [待核验]

## Corrected Claim

FP8 量化中 E4M3 格式通常用于权重存储，E5M2 格式用于激活值；在 27B 模型混合精度配置下，两种格式组合导致的 MMLU 准确率差异极小（通常可忽略不计），但具体数值需参考特定论文或实测数据。

## Evidence

[质询]该陈述包含具体的经验性结论（ΔMMLU < 0.05%）和特定的硬件/模型配置（27B模型），属于经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

FP8 E4M3 vs E5M2 MMLU accuracy difference LLM quantization
