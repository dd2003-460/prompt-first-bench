# N352: HumanEval 0-shot 评测中，Qwen3-27B 平均生成代码长度约为 150-200 tokens，在 4x V100 (TP=4) 上以 20-

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N111

## Claim

HumanEval 0-shot 评测中，Qwen3-27B 平均生成代码长度约为 150-200 tokens，在 4x V100 (TP=4) 上以 20-30 tok/s 的速度运行，单次生成耗时 T_gen ≈ 5-10s，这是评测吞吐量的主要瓶颈，而非单元测试执行时间

## Corrected Claim

HumanEval 0-shot 评测中，Qwen3-27B 平均生成代码长度约为 150-200 tokens，在 4x V100 (TP=4) 上以 20-30 tok/s 的速度运行，单次生成耗时 T_gen ≈ 5-10s，这是评测吞吐量的主要瓶颈，而非单元测试执行时间

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型在4xV100(TP=4)上推理速度20-30 tok/s符合硬件算力预期，150-200 tokens生成耗时5-10s计算自洽，且通常代码生成耗时远高于单元测试执行，瓶颈判断合理。
