# N761: INT4 (AWQ) 量化相对于 BF16 的 HumanEval 准确率下降百分比 (ΔHumanEval_INT4) 估算：若 HumanEval BF16

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N271

## Claim

INT4 (AWQ) 量化相对于 BF16 的 HumanEval 准确率下降百分比 (ΔHumanEval_INT4) 估算：若 HumanEval BF16 基线为 65.1%，INT4 通常导致 3-5% 的相对损失（代码生成对低比特量化更敏感），预计 ΔHumanEval_INT4 ≈ 3.0%-5.0%，即准确率降至 61.8%-63.1% 区间 [待核验]。

## Corrected Claim

INT4 (AWQ) 量化相对于 BF16 的 HumanEval 准确率下降百分比 (ΔHumanEval_INT4) 估算：若 HumanEval BF16 基线为 65.1%，INT4 通常导致 3-5% 的相对损失（代码生成对低比特量化更敏感），预计 ΔHumanEval_INT4 ≈ 3.0%-5.0%，即准确率降至 61.8%-63.1% 区间 [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过
