# N32: Qwen3-27B 的精确参数量分解：需从 Hugging Face 配置文件或技术报告获取具体数值，区分 Non-Embedding 参数（用于权重存储计算）

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

Qwen3-27B 的精确参数量分解：需从 Hugging Face 配置文件或技术报告获取具体数值，区分 Non-Embedding 参数（用于权重存储计算）与 Embedding/LM Head 参数（通常占总量约 10-15%），以修正 27.1B 的估算误差。

## Corrected Claim

Qwen3-27B 的精确参数量分解需从 Hugging Face 配置文件或技术报告获取具体数值，以区分 Non-Embedding 参数与 Embedding/LM Head 参数，从而修正基于总参数量 27B 的估算误差。

## Evidence

[质询]该陈述包含具体的经验性数值断言（Embedding/LM Head 占比 10-15%），且声称 27.1B 为估算误差，但缺乏具体来源支持该特定模型的参数分布细节，不同架构下 Embedding 占比可能显著不同。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体占比数值及 27.1B 的精确构成）

## Search Query

Qwen3-27B config.json num_parameters embedding size
