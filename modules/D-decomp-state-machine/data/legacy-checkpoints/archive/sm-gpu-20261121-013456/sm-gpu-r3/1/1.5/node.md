# N11: Qwen3-27B 架构参数：Layers=64, Num_Heads=32 (或 GQA 配置需确认), Head_Dim=128, Bytes_per_KV

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

Qwen3-27B 架构参数：Layers=64, Num_Heads=32 (或 GQA 配置需确认), Head_Dim=128, Bytes_per_KV_Element=2 (BF16) 或 1 (FP8/INT8)。

## Corrected Claim

Qwen3.5-27B（或Qwen3-27B，需确认版本）架构参数：Layers=64, Hidden_Dim=5120, Head_Dim=128 (基于Hidden_Dim/Num_Heads推导，需确认Num_Heads), Bytes_per_KV_Element=2 (BF16) 或 1 (FP8/INT8)。

## Evidence

[质询]来源[1]明确标注为'Qwen3.5-27B'，而待核验事实为'Qwen3-27B'，存在版本混淆风险；且来源摘要中未直接提及Num_Heads=32或Head_Dim=128的具体数值，仅提供了层数64和隐藏层维度5120，无法直接确认注意力头配置。 | 来源[1]支持层数64和隐藏层维度5120（隐含Head_Dim=128若Num_Heads=40或GQA配置，但需确认具体头数），但版本名称不一致（Qwen3.5 vs Qwen3），且缺乏对Num_Heads的直接证据，属于间接支持且存在版本歧义。

## Search Query

Qwen3-27B architecture layers num heads head dimension config.json

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2010079474104963160&rut=725c7cff098d17c7d4f51c5362b5fa9f20078a8fe0233472d5b8a97dc40ea021', 'type': 'ddg', 'title': 'Qwen/Qwen3.5-27B模型结构（dense）分析 - 知乎'}
