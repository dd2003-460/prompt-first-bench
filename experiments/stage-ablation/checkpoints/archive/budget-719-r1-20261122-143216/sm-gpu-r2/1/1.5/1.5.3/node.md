# N55: NVFP4 量化所需的校准数据集（Calibration Set）大小与选择对最终精度的敏感度分析，需确定最小有效校准集大小（通常 128-512 样本），若校

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

NVFP4 量化所需的校准数据集（Calibration Set）大小与选择对最终精度的敏感度分析，需确定最小有效校准集大小（通常 128-512 样本），若校准集不足导致精度损失不可控，则需增加校准成本或放弃 NVFP4

## Corrected Claim

NVFP4 量化所需的校准数据集大小与选择对最终精度具有显著影响，需通过实验确定最小有效校准集大小（通常建议在 128-512 样本范围内进行验证），若校准集不足导致精度损失不可控，则需增加校准成本或放弃 NVFP4 方案。

## Evidence

[质询]该陈述包含具体的经验参数（128-512样本）和特定的工程决策逻辑（NVFP4量化校准敏感度），属于经验事实而非第一性原理可推导内容，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

NVFP4 quantization calibration dataset size sensitivity accuracy impact
