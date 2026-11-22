# N35: Qwen3-27B模型在BF16下的权重显存占用精确计算：参数量27.2B（以官方config.json为准）* 2 bytes/param = 54.4GB

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

Qwen3-27B模型在BF16下的权重显存占用精确计算：参数量27.2B（以官方config.json为准）* 2 bytes/param = 54.4GB

## Corrected Claim

Qwen3-27B模型在BF16下的权重显存占用约为54.4GB（基于27.2B参数量估算），具体数值需以官方config.json为准。

## Evidence

[质询]来源[1]中提到的模型名称为'Qwen 3.8 27B'，与陈述中的'Qwen3-27B'存在版本/命名不一致，且来源主要讨论FP8和Q4量化，未直接提供BF16下的精确参数量或显存占用数据，无法直接证实27.2B这一具体数值。 | 逻辑上27.2B * 2 bytes = 54.4GB计算正确，但来源[1]仅提及Qwen 3.8 27B的FP8版本需30G，未直接支持BF16下54.4GB的精确值，且模型命名存在差异，属于间接支持且存在不确定性。

## Search Query

Qwen3-27B model config.json num_parameters exact value

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2077790223518406650&rut=4827fb43589c8ea1aba1b47234fef8f38dd8f26616580c4ba8cb540184243b49', 'type': 'ddg', 'title': '在 16G 显卡上部署 Qwen3.8 27B 最佳实践方案 - 知乎'}
