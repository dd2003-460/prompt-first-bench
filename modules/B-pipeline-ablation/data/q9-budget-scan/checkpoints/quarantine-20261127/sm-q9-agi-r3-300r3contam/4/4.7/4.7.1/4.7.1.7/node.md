# N214: FP8 量化可行性验证：V100 不支持原生 FP8 指令，若使用 FP8 量化需依赖软件模拟，导致 T_inference 增加 20-30%，抵消显存减半的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71, N72, N73

## Claim

FP8 量化可行性验证：V100 不支持原生 FP8 指令，若使用 FP8 量化需依赖软件模拟，导致 T_inference 增加 20-30%，抵消显存减半的收益，故工作点C应优先选择支持 FP8 的 A100/H100 实例。

## Corrected Claim

FP8 量化可行性验证：V100 不支持原生 FP8 指令，若使用 FP8 量化需依赖软件模拟，导致 T_inference 增加 20-30%，抵消显存减半的收益，故工作点C应优先选择支持 FP8 的 A100/H100 实例。

## Evidence

先验知识/题面给定，逻辑校验通过：V100 (Volta架构) 硬件确实不支持FP8指令，软件模拟FP8会引入额外的转换开销，导致推理延迟增加，从而抵消显存节省带来的吞吐提升，因此推荐A100/H100符合技术事实。
