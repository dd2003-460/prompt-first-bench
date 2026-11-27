# N347: Qwen3-27B 在 FP8 (E4M3) 精度下 HumanEval (Pass@1) 的准确率为 84.5% (估算值，基于同类 20-30B 模型 FP

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N110

## Claim

Qwen3-27B 在 FP8 (E4M3) 精度下 HumanEval (Pass@1) 的准确率为 84.5% (估算值，基于同类 20-30B 模型 FP8 量化通常损失 1-2% 的经验法则，具体数值需通过 TensorRT-LLM 或 vLLM FP8 后端实测 [待核验])

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 精度下 HumanEval (Pass@1) 的准确率预计约为 84.5%（估算值，基于同类模型 FP8 量化通常损失 1-2% 的经验法则，具体数值需通过实测确认）

## Evidence

[质询]该数值为基于经验法则的估算值，缺乏针对 Qwen3-27B 在 FP8 精度下 HumanEval 具体表现的直接实测数据支持，且不同量化实现（如 TensorRT-LLM vs vLLM）可能导致细微差异，经验法则的 1-2% 损失范围较宽，无法精确锁定 84.5% 这一具体数值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体数值属于需实测验证的经验参数，不适用第一性原理推导）

## Search Query

Qwen3-27B FP8 quantization HumanEval Pass@1 degradation benchmark
