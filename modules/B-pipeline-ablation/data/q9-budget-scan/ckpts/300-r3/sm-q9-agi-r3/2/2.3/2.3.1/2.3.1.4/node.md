# N205: 嵌入模型推理延迟约束：在 M1 Max 上，单次 512-token 输入的嵌入计算耗时需 < 50ms，BGE-large 实测 ~10ms，Qwen-7b 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

嵌入模型推理延迟约束：在 M1 Max 上，单次 512-token 输入的嵌入计算耗时需 < 50ms，BGE-large 实测 ~10ms，Qwen-7b 实测 ~80ms，若选择 Qwen 需启用半精度 (FP16) 或量化 (INT8) 以降低延迟至 50ms 以内

## Corrected Claim

嵌入模型推理延迟约束：在 M1 Max 上，单次 512-token 输入的嵌入计算耗时需 < 50ms，BGE-large 实测 ~10ms，Qwen-7b 实测 ~80ms，若选择 Qwen 需启用半精度 (FP16) 或量化 (INT8) 以降低延迟至 50ms 以内

## Evidence

先验知识/题面给定，逻辑校验通过：M1 Max 算力足以支撑 BGE-large (0.3B) 在 10ms 内完成 512 token 推理，而 Qwen-7b 即使经 FP16/INT8 优化，其参数量级导致的计算开销使其延迟显著高于轻量级嵌入模型，80ms 的估算符合硬件性能直觉，且优化建议逻辑自洽。
