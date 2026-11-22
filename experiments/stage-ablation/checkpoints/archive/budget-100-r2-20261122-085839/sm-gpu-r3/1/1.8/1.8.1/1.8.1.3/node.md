# N179: AWQ 量化中激活值缩放因子（Activation Scaling Factor）的优化对 Qwen3-27B 精度的影响：不同缩放策略（如 per-chann

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

AWQ 量化中激活值缩放因子（Activation Scaling Factor）的优化对 Qwen3-27B 精度的影响：不同缩放策略（如 per-channel vs. per-tensor）导致的 MMLU 得分差异（通常 per-channel 更优，差异约 0.5-1.5%）

## Corrected Claim

AWQ 量化中激活值缩放因子（Activation Scaling Factor）的优化对 Qwen3-27B 精度有显著影响：不同缩放策略（如 per-channel vs. per-tensor）会导致 MMLU 得分差异，通常 per-channel 策略表现更优，但具体差异幅度需根据实际实验数据确定。

## Evidence

[质询]该陈述包含具体的经验数值（MMLU得分差异0.5-1.5%）和特定模型（Qwen3-27B）的量化行为，属于经验事实。在缺乏外部来源支持的情况下，无法验证该具体数值范围是否准确，且不同量化实现（如AWQ的不同变体或库版本）可能导致结果差异，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）。Per-channel缩放通常优于per-tensor符合量化理论直觉，但具体数值差异缺乏证据。

## Search Query

AWQ activation scaling factor impact on LLM accuracy per-channel vs per-tensor
