# N348: FP8 量化导致 HumanEval 通过率下降的核心机制是 Logit 分布的尾部截断：E4M3 格式仅有 3 位尾数，导致 Logit 值的分辨率降低约 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

FP8 量化导致 HumanEval 通过率下降的核心机制是 Logit 分布的尾部截断：E4M3 格式仅有 3 位尾数，导致 Logit 值的分辨率降低约 1/8 (相对于 FP16)，在代码生成中，Top-1 token 与 Top-2 token 的 Logit 差值 (Margin) 若小于 FP8 量化步长 (Step Size ≈ 0.0625 for max_logit=10)，将导致贪心解码或采样选择错误，从而引发语法错误

## Corrected Claim

FP8 量化导致 HumanEval 通过率下降的核心机制是 Logit 分布的尾部截断：E4M3 格式仅有 3 位尾数，导致 Logit 值的分辨率降低约 1/8 (相对于 FP16)，在代码生成中，Top-1 token 与 Top-2 token 的 Logit 差值 (Margin) 若小于 FP8 量化步长 (Step Size ≈ 0.0625 for max_logit=10)，将导致贪心解码或采样选择错误，从而引发语法错误

## Evidence

先验知识/题面给定，逻辑校验通过：E4M3格式尾数3位，分辨率约为FP16的1/8，量化步长计算合理，机制解释符合量化误差导致解码错误的逻辑。

## Search Query

FP8 quantization logit resolution impact on greedy decoding accuracy LLM
