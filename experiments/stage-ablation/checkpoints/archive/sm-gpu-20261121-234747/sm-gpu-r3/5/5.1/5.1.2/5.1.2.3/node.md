# N325: FP8 量化在 Qwen3-27B 上的质量损失量化：MMLU 准确率下降 ΔMMLU ≈ 0.3-0.8%（基于 7B/14B 模型外推，[待核验]）；Per

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N118

## Claim

FP8 量化在 Qwen3-27B 上的质量损失量化：MMLU 准确率下降 ΔMMLU ≈ 0.3-0.8%（基于 7B/14B 模型外推，[待核验]）；Perplexity 增加 ΔPPL ≈ 0.05-0.15；若业务容忍度为 2% MMLU 下降，则 FP8 满足要求；若容忍度 <0.5%，则需回退至 BF16，但 BF16 显存需求 54GB 超出 24GB/48GB 单卡/双卡限制，需升级至 L40S 48GB + Offload

## Corrected Claim

FP8 量化在 Qwen3-27B 上的质量损失需实测确定，通常 MMLU 准确率下降在 0.5%-1.5% 之间（视量化方法而定）；Perplexity 增加约 0.05-0.2；若业务容忍度为 2% MMLU 下降，FP8 通常满足要求；若容忍度 <0.5%，则需回退至 BF16，但 BF16 显存需求约 54GB 超出 24GB/48GB 单卡/双卡限制，需升级至 L40S 48GB + Offload 或采用更激进的量化策略。

## Evidence

[质询]数值量级与外推逻辑存疑：将7B/14B模型的FP8量化损失直接外推至27B模型缺乏理论依据，且0.3-0.8%的MMLU下降范围对于大模型而言可能过于乐观或过于悲观，具体取决于量化算法（如SmoothQuant, GPTQ等）和校准数据，不能简单视为固定区间。 | 先验知识/题面给定，逻辑校验通过（显存计算54GB>48GB成立，但量化损失数值为经验估计且标注了[待核验]，缺乏直接来源支持具体数值区间）

## Search Query

Qwen3-27B FP8 quantization MMLU perplexity degradation benchmark
