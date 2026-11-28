# N226: GPQA Diamond 分项得分修正：Qwen3.8-27B 在 GPQA Diamond 物理子集得分为 58.2%（非 62.1%），化学 54.1%（非

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N68

## Claim

GPQA Diamond 分项得分修正：Qwen3.8-27B 在 GPQA Diamond 物理子集得分为 58.2%（非 62.1%），化学 54.1%（非 55.4%），生物 55.3%（非 56.8%），加权平均 55.9%；原数值可能混淆了 Qwen2.5-72B 或使用了不同评测版本

## Corrected Claim

Qwen3.8-27B 在 GPQA Diamond 上的具体分项得分（物理 58.2%，化学 54.1%，生物 55.3%，加权 55.9%）缺乏公开权威来源的直接证实，建议核实模型版本号及评测基准的具体配置。

## Evidence

[质询]参考来源仅提及对 Qwen3.8-27B 进行了独立本地评估，但未提供具体的物理、化学、生物子项得分及加权平均值，无法验证具体数值（58.2%, 54.1%, 55.3%, 55.9%）的准确性；此外，'Qwen3.8-27B' 这一型号名称本身存疑（通常 Qwen 系列为 2.5 或 3 代，3.8 代非标准命名，可能是笔误或特定微调版本），导致事实基础薄弱。 | 来源 [1] 确认了对该模型进行 GPQA 评测的行为，但未包含具体分项数据，属于间接支持且缺乏数值佐证；鉴于具体数值属于经验事实且无直接来源支持，依据经验事实排除条款降级。

## Search Query

Qwen3.8-27B GPQA Diamond benchmark score physics chemistry biology subset breakdown

## Retrieval Sources

- {'url': 'https://github.com/lunncing/qwen38-gsq-gpqa-benchmark&rut=d303fecb59d4cf67bd94ba4bac0983d634925f086636ad8aa77fb81b35b5e418', 'type': 'ddg', 'title': 'GitHub - lunncing/qwen38-gsq-gpqa-benchmark'}
