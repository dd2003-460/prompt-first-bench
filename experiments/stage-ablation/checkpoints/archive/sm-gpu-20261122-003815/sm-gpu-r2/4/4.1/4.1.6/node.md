# N122: FP8 KV Cache 可行性与精度权衡：主流推理引擎（vLLM, TensorRT-LLM）支持 FP8 KV Cache。若 KV Cache 使用 FP

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22, N23, N24

## Claim

FP8 KV Cache 可行性与精度权衡：主流推理引擎（vLLM, TensorRT-LLM）支持 FP8 KV Cache。若 KV Cache 使用 FP8，显存减半（从 N45 的 BF16 值除以 2），但需评估长上下文下 FP8 KV 累积误差对生成质量的影响（通常 <1% PPL 增加）。

## Corrected Claim

FP8 KV Cache 可行性与精度权衡：主流推理引擎（vLLM, TensorRT-LLM）支持 FP8 KV Cache。若 KV Cache 使用 FP8，显存减半（从 N45 的 BF16 值除以 2），但需评估长上下文下 FP8 KV 累积误差对生成质量的影响（通常 <1% PPL 增加）。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8为8位格式，BF16为16位格式，显存占用减半符合数学逻辑；主流引擎支持FP8 KV Cache及精度损失在可接受范围内（<1% PPL）符合当前大模型推理工程实践共识。

## Search Query

vLLM FP8 KV cache accuracy impact
