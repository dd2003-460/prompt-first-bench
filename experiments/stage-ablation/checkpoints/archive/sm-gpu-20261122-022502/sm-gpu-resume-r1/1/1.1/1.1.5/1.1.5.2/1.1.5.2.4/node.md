# N466: TensorRT-LLM FP8 KV Cache 质量损失评估：与 vLLM 相同，FP8 E4M3 精度损失 <0.1% [待核验]，但 TensorRT-

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N144

## Claim

TensorRT-LLM FP8 KV Cache 质量损失评估：与 vLLM 相同，FP8 E4M3 精度损失 <0.1% [待核验]，但 TensorRT-LLM 的 FP8 计算路径可能引入额外舍入误差，需对比 BF16 基线验证困惑度 (perplexity) 差异 <0.5%

## Corrected Claim

TensorRT-LLM 支持 FP8 (E4M3) KV Cache 量化，其精度损失通常较低，但具体数值（如 <0.1% 或困惑度差异 <0.5%）需通过对比 BF16 基线进行实际验证，不能直接断言与 vLLM 完全相同。

## Evidence

[质询]陈述中引用的具体数值（精度损失 <0.1%、困惑度差异 <0.5%）属于经验事实，且声称 TensorRT-LLM 与 vLLM 在 FP8 KV Cache 上的质量损失“相同”，但参考来源仅确认了两者均支持 FP8 (E4M3) 量化，并未提供具体的精度损失基准数据或证明两者误差完全一致。 | 来源 [2] 确认 TensorRT-LLM 支持 FP8 (E4M3) KV Cache 量化，与 vLLM 类似，但所有来源均未提供具体的精度损失数值（<0.1%）或困惑度差异（<0.5%）的实证数据，属于经验事实且缺乏直接来源支持。

## Search Query

TensorRT-LLM FP8 perplexity degradation benchmark

## Retrieval Sources

- {'url': 'https://miraclefarms.github.io/notes/2026/05/27/vllm-trtllm-kv-cache-quantization/&rut=f764cbc7fe61c3995813198c49863acbc69284999c2662fc51f2d4f9d08836f8', 'type': 'ddg', 'title': 'vLLM vs TensorRT-LLM KV Cache 量化实操指南 | MiracleFarms'}
- {'url': 'https://blog.squeezebits.com/vllm-vs-tensorrtllm-8-kv-cache-quantization-35079&rut=f296815ed928b7c1a5337485c425a29b74dd156eb415776cb0aeef2d3576bf68', 'type': 'ddg', 'title': '[vLLM vs TensorRT-LLM] #8. KV Cache Quantization'}
- {'url': 'https://blog.csdn.net/2601_96690100/article/details/164291800&rut=dafe60a8f6cd2f29ba462d5bc1dbd815f34ed6d1c652043e8a44d0667c1c9668', 'type': 'ddg', 'title': '大模型推理优化：vLLM与TensorRT-LLM配置参数深度解析与选型实践-CSDN博客'}
