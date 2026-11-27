# N462: vLLM FP8 KV Cache 质量损失评估：FP8 E4M3 动态范围 [-448, 448]，E5M2 动态范围 [-57344, 57344]，KV 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N143

## Claim

vLLM FP8 KV Cache 质量损失评估：FP8 E4M3 动态范围 [-448, 448]，E5M2 动态范围 [-57344, 57344]，KV Cache 值域通常在 [-1, 1]，E4M3 精度损失 <0.1% [待核验]，对生成质量影响可忽略，但需验证长上下文 (32K+) 下的累积误差

## Corrected Claim

vLLM FP8 KV Cache 使用 E4M3 格式，动态范围 [-448, 448]，E5M2 动态范围 [-57344, 57344]。KV Cache 值域通常在 [-1, 1]。FP8 量化相比 FP16 会引入一定精度损失，通常认为对生成质量影响较小，但具体误差幅度及长上下文 (32K+) 下的累积效应需通过校准和实验验证。

## Evidence

[质询]「E4M3 精度损失 <0.1%」这一具体数值缺乏来源直接支持，且对于浮点量化而言，相对误差通常取决于具体数值分布，断言全局小于0.1%可能过于乐观或混淆了平均误差与最大误差；此外，「对生成质量影响可忽略」是经验性结论，需依赖具体模型和任务验证，不能仅凭数值范围推导。 | 来源[1]和[3]确认了vLLM支持FP8 KV Cache及E4M3/E5M2格式，但未提供具体的精度损失百分比（<0.1%）或长上下文累积误差的具体量化数据；该数值属于经验事实，逻辑上虽自洽（FP8精度高于INT8，误差通常较小），但缺乏直接来源支持具体阈值，故降级。

## Search Query

FP8 E4M3 KV cache quality degradation long context benchmark

## Retrieval Sources

- {'url': 'https://docs.vllm.ai/en/v0.6.0/quantization/fp8_e4m3_kvcache.html&rut=9a308dc13cc05bb2f7ca9dfd0b0ded4ed621fd900155b2f45367b197802d3fae', 'type': 'ddg', 'title': 'FP8 E4M3 KV Cache — vLLM'}
- {'url': 'https://tensormesh.ai/learn/kv-cache-quantization/&rut=de0dc6b456684be07ef81f590c8dbb38d0515943e5cc39c259154d3cf5a60f75', 'type': 'ddg', 'title': 'KV Cache Quantization: FP8, FP4, and What They Cost You'}
- {'url': 'https://docs.vllm.cc/en/latest/features/quantization/quantized_kvcache.html&rut=70095e7d0992ac316658e8e7f70aa92939f88b2018704dd547d41c2856f97256', 'type': 'ddg', 'title': 'Quantized KV Cache - vLLM'}
