# N173: Qwen3-27B 若采用 MoE（Mixture of Experts）架构，需区分 Total Parameters（总参数量，影响权重文件大小）与 Act

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N48, N49, N50

## Claim

Qwen3-27B 若采用 MoE（Mixture of Experts）架构，需区分 Total Parameters（总参数量，影响权重文件大小）与 Active Parameters（激活参数量，影响计算量和部分 KV Cache 逻辑）；若为 MoE，BF16 权重文件大小 = Total_Params * 2 bytes，但推理时的显存带宽瓶颈主要由 Active 路径和路由矩阵决定，需确认 Qwen3-27B 是否为 MoE 结构（目前公开信息多指向稠密模型，需 [待核验] 确认最新版本是否引入 MoE）。

## Corrected Claim

Qwen3-27B 若采用 MoE 架构，需区分 Total Parameters 与 Active Parameters；BF16 权重文件大小 = Total_Params * 2 bytes，推理显存带宽瓶颈主要由 Active 路径决定。目前公开信息多指向稠密模型，具体架构需以官方最新技术报告为准。

## Evidence

[质询]该陈述包含具体的硬件/模型架构经验事实（Qwen3-27B 是否为 MoE 结构、BF16 权重计算逻辑），属于经验事实范畴，且当前检索无可用来源支持，无法排除模型实际架构与陈述假设不符的可能性。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据）

## Search Query

Qwen3-27B architecture dense vs MoE structure
