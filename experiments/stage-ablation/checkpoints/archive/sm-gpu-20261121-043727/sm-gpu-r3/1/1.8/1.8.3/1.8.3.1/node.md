# N157: A100 (Ampere) 在 FP8 推理任务中，若使用软件模拟（如 PyTorch 的 torch.float8 或 TensorRT 的 FP8 插件），

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N61

## Claim

A100 (Ampere) 在 FP8 推理任务中，若使用软件模拟（如 PyTorch 的 torch.float8 或 TensorRT 的 FP8 插件），其有效算力约为原生 INT8 算力的 50%-70%，且引入额外的转换开销（约 5-10% 延迟），导致其有效 T_decode 比原生 INT8 方案慢 1.2-1.5 倍，因此 A100 在 FP8 场景下性价比低于同代 INT8 优化方案。

## Corrected Claim

A100 (Ampere) 在 FP8 推理任务中，若使用软件模拟，由于缺乏原生硬件支持，其有效算力通常低于原生 INT8 方案，并引入额外的转换开销，导致其有效 T_decode 比原生 INT8 方案慢，因此 A100 在 FP8 场景下性价比低于同代 INT8 优化方案。

## Evidence

[质询]数值量级与具体百分比（50%-70%算力、5-10%延迟、1.2-1.5倍慢）缺乏通用基准支持，且A100硬件本身不支持原生FP8，软件模拟FP8通常通过INT8或FP16路径实现，其性能表现高度依赖具体算子实现和框架优化，直接断言固定倍率存在过度简化风险。 | 先验知识/题面给定，逻辑校验通过：A100无原生FP8硬件单元，软件模拟必然引入额外开销，导致性能低于原生INT8路径，定性结论合理，但具体数值缺乏来源支持且存在实现差异。
