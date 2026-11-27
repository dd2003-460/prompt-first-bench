# N93: FP8/INT8 量化对 Qwen3-27B 的质量损失量化：在 MMLU/C-Eval 等基准上，FP8 精度保持率通常为 98-99% (ΔPPL < 0.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

FP8/INT8 量化对 Qwen3-27B 的质量损失量化：在 MMLU/C-Eval 等基准上，FP8 精度保持率通常为 98-99% (ΔPPL < 0.1)，INT8 (AWQ) 精度保持率通常为 95-97% (ΔPPL < 0.5)；若 Quality_Sensitivity=High (如代码生成)，INT8 可能不可接受，必须选 BF16 (需双卡或数据中心卡)。

## Corrected Claim

FP8/INT8 量化对 Qwen3-27B 的质量损失量化：在 MMLU/C-Eval 等基准上，FP8 精度保持率通常为 98-99% (ΔPPL < 0.1)，INT8 (AWQ) 精度保持率通常为 95-97% (ΔPPL < 0.5)；若 Quality_Sensitivity=High (如代码生成)，INT8 可能不可接受，必须选 BF16 (需双卡或数据中心卡)。

## Evidence

先验知识/题面给定，逻辑校验通过
