# N554: INT4 (AWQ) 精度下 Qwen3-27B 的权重占用修正：AWQ 通常保留部分敏感层为 FP16/BF16，实际权重文件大小可能略高于纯 INT4 的 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N230

## Claim

INT4 (AWQ) 精度下 Qwen3-27B 的权重占用修正：AWQ 通常保留部分敏感层为 FP16/BF16，实际权重文件大小可能略高于纯 INT4 的 13.5 GB（例如 14-15 GB），需查阅具体 AWQ 量化配置（如 group_size=128, 敏感层比例）以确定精确权重大小，进而修正总显存需求。

## Corrected Claim

AWQ 量化通常保留部分敏感层为高精度（如 FP16/BF16），导致实际权重文件大小略高于纯 INT4 理论值（13.5 GB），具体大小取决于量化配置（如 group_size 和敏感层比例），需查阅具体模型配置以确定精确显存需求。

## Evidence

[质询]该陈述包含具体的经验性数值范围（14-15 GB）和配置细节（group_size=128），属于经验事实，无法仅从第一性原理严格推出，且缺乏来源支持以确认具体数值量级的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

AWQ quantization Qwen3-27B weight size sensitive layers FP16 ratio
