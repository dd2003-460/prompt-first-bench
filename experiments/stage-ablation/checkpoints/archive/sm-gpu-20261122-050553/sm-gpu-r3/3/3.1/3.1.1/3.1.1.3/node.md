# N193: Qwen3-27B 的架构参数 D_head（每头维度）需确认为 128 维（基于隐藏层维度 8192 / 64 头 = 128），需引用官方配置确认隐藏层维度

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N63

## Claim

Qwen3-27B 的架构参数 D_head（每头维度）需确认为 128 维（基于隐藏层维度 8192 / 64 头 = 128），需引用官方配置确认隐藏层维度及头数，以计算单头 KV 占用。

## Corrected Claim

Qwen3-27B 的架构参数 D_head 需通过官方配置确认隐藏层维度及头数后计算（若隐藏层为8192且头数为64，则D_head为128），以计算单头 KV 占用。

## Evidence

[质询]该陈述包含具体的硬件/模型架构参数（隐藏层维度8192、头数64、D_head 128），属于经验事实。虽然数学计算（8192/64=128）在逻辑上自洽，但缺乏官方配置来源直接确认Qwen3-27B的具体架构参数，存在参数记忆错误或版本混淆的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体架构参数）

## Search Query

Qwen3-27B hidden_size head_dim 128
