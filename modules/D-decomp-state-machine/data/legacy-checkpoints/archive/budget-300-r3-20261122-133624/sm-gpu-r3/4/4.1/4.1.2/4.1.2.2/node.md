# N307: PCIe 5.0平台TP=2方案在低并发（B=1）下的可行性边界：即使通信占比高达64%，若单卡显存不足（如24GB卡无法运行32K上下文INT8模型），TP=

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99

## Claim

PCIe 5.0平台TP=2方案在低并发（B=1）下的可行性边界：即使通信占比高达64%，若单卡显存不足（如24GB卡无法运行32K上下文INT8模型），TP=2仍是唯一可行方案。此时性价比判定从'性能最优'转为'可行性唯一'，需对比'2×PCIe卡（高延迟但可行）'与'1×大显存卡（高成本但低延迟）'的TCO差异，预计2×4090 TCO仍低于1×A100 80GB，但用户体验（延迟）显著下降。

## Corrected Claim

PCIe 5.0平台TP=2方案在低并发（B=1）下的可行性边界：即使通信占比高达64%，若单卡显存不足（如24GB卡可能无法运行32K上下文INT8模型），TP=2可能是唯一可行方案。此时性价比判定从'性能最优'转为'可行性唯一'，需对比'2×PCIe卡（高延迟但可行）'与'1×大显存卡（高成本但低延迟）'的TCO差异，预计2×4090 TCO可能低于1×A100 80GB，但用户体验（延迟）显著下降。

## Evidence

[质询]该陈述包含具体的硬件性能参数（如24GB卡无法运行32K上下文INT8模型）和TCO对比结论（2×4090 < 1×A100 80GB），属于经验事实。在缺乏外部来源支持的情况下，无法验证这些具体数值和成本对比的准确性，且不同模型架构和量化方式可能导致显存需求差异，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

PCIe tensor parallel feasibility vs single card large memory TCO comparison LLM inference
