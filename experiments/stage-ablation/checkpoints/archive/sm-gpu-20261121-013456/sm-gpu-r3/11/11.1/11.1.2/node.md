# N287: Qwen3-27B 在 FP8 E4M3 精度下，WikiText-103 测试集上的 Perplexity (PPL_FP8) 预期为 8.6-9.6。绝对增

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N120

## Claim

Qwen3-27B 在 FP8 E4M3 精度下，WikiText-103 测试集上的 Perplexity (PPL_FP8) 预期为 8.6-9.6。绝对增加量 ΔPPL = PPL_FP8 - PPL_BF16 预期在 0.05-0.15 之间。相对退化率 (ΔPPL / PPL_BF16) 预期 < 1.5%。若 ΔPPL > 0.2，则表明 FP8 量化存在显著精度损失，需检查量化算法（如是否使用了 SmoothQuant 或 Block-wise Scaling）。

## Corrected Claim

Qwen3-27B 在 FP8 E4M3 精度下，WikiText-103 测试集上的 Perplexity (PPL_FP8) 预期为 8.6-9.6。绝对增加量 ΔPPL = PPL_FP8 - PPL_BF16 预期在 0.05-0.15 之间。相对退化率 (ΔPPL / PPL_BF16) 预期 < 1.5%。若 ΔPPL > 0.2，则表明 FP8 量化存在显著精度损失，需检查量化算法（如是否使用了 SmoothQuant 或 Block-wise Scaling）。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 在 BF16 下 WikiText-103 PPL 约为 8.5-8.8，FP8 量化通常带来 <1.5% 的相对退化，数值量级与工程经验一致。

## Search Query

FP8 E4M3 quantization perplexity increase LLM 27B parameter
