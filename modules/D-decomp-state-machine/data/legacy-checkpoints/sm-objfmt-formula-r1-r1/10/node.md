# N43: 主流推理框架（vLLM, SGLang, TensorRT-LLM）对 Qwen3-27B 在 RTX 4090/5090 上支持 FP8 或 NVFP4 量化

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

主流推理框架（vLLM, SGLang, TensorRT-LLM）对 Qwen3-27B 在 RTX 4090/5090 上支持 FP8 或 NVFP4 量化的具体版本要求及已知 Bug 列表，特别是 FlashAttention-3 或 PagedAttention 在消费级硬件上的显存碎片化优化效果

## Corrected Claim

主流推理框架（vLLM, SGLang, TensorRT-LLM）支持大模型推理部署，但关于Qwen3-27B在RTX 4090/5090上FP8/NVFP4量化的具体版本要求、已知Bug及FlashAttention-3/PagedAttention显存碎片化优化效果的详细数据需查阅各框架最新官方文档或社区Issue，现有通用综述未提供此级别细节。

## Evidence

[质询]参考来源仅为通用框架介绍，完全缺失关于Qwen3-27B在特定消费级显卡（RTX 4090/5090）上FP8/NVFP4量化的具体版本要求、Bug列表以及FlashAttention-3/PagedAttention显存碎片化优化的详细数据，属于严重的信息缺失而非错误，但无法验证具体细节。 | 来源[1][2]仅提供了vLLM/SGLang/TensorRT-LLM的宏观对比，未覆盖Qwen3-27B量化支持细节及消费级硬件特定优化效果，属间接相关但无直接支持；鉴于该陈述包含大量具体经验参数（版本、Bug、优化效果），且缺乏直接来源支持，依据经验事实排除条款降级。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1982034147640878673&rut=c31863dae80e7b20c14bfa5e39ed8aac4c86514c4f7da1af0bea31b3a2902677', 'type': 'ddg', 'title': '大模型推理框架全景对比：vLLM、SGLang、TensorRT-LLM，选择适合你的部署方案!'}
- {'url': 'https://zhuanlan.zhihu.com/p/1992396693031888660&rut=017724879daaa481c2f1f090a25028194a75847b15f8de152f3351194511866a', 'type': 'ddg', 'title': '一文讲清：主流大模型推理部署框架：vLLM、SGLang、TensorRT-LLM、ollama、XInference'}
