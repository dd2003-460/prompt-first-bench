# N422: RTX 3090 Ti 在 INT4 量化下的质量损失量化：基于 AWQ 量化方法在 Qwen3-27B 上的 MMLU 基准测试，INT4 权重通常导致 0.

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N141

## Claim

RTX 3090 Ti 在 INT4 量化下的质量损失量化：基于 AWQ 量化方法在 Qwen3-27B 上的 MMLU 基准测试，INT4 权重通常导致 0.5-1.5% 的 MMLU 分数下降（N117），但需结合 32K 长上下文下的幻觉率（Hallucination Rate）和困惑度（Perplexity）增加幅度进行综合评估，若幻觉率增加 > 5%，则质量损失不可接受。

## Corrected Claim

RTX 3090 Ti 在 INT4 量化下（基于 AWQ 方法）通常会导致模型性能轻微下降（如 MMLU 分数小幅降低），具体幅度取决于模型架构和数据分布；在长上下文场景下，需综合评估幻觉率和困惑度的变化，若幻觉率显著增加（具体阈值需根据业务容忍度设定），则质量损失可能不可接受。

## Evidence

[质询]该陈述包含具体的经验性数值阈值（MMLU下降0.5-1.5%、幻觉率增加>5%），这些并非第一性原理可推导的数学或物理定律，而是依赖于特定模型、数据集和量化实现的经验统计结果。不同模型（如Qwen3-27B与其他模型）和不同量化方法（AWQ vs GPTQ）下的具体数值差异可能很大，且‘幻觉率增加>5%即不可接受’属于主观工程标准而非客观事实。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且具体数值阈值无法从第一性原理严格推出）

## Search Query

AWQ INT4 quantization Qwen3-27B MMLU benchmark hallucination rate perplexity increase 32K context
