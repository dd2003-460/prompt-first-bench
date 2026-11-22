# N90: Qwen3-27B量化精度吞吐量变化系数（FP8/INT8/NVFP4）的不确定性：需通过至少3个独立软件栈（vLLM, TensorRT-LLM, llama

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

Qwen3-27B量化精度吞吐量变化系数（FP8/INT8/NVFP4）的不确定性：需通过至少3个独立软件栈（vLLM, TensorRT-LLM, llama.cpp）的基准测试确定系数范围，若各栈间系数方差>0.2x，则TCO计算中必须采用保守估计（取最小吞吐量），以避免高估性能导致选型错误。

## Corrected Claim

Qwen3-27B量化精度吞吐量变化系数存在不确定性，建议通过多个主流软件栈（如vLLM, TensorRT-LLM等）的基准测试评估差异；若各栈间性能差异显著，TCO计算中应采用保守估计（取最小吞吐量）以避免选型错误。

## Evidence

[质询]该陈述包含具体的工程经验阈值（方差>0.2x）和特定的软件栈组合要求，属于经验事实而非第一性原理可推导结论；且参考来源主要关注精度损失或单一框架部署，未提供跨三个独立软件栈（vLLM, TensorRT-LLM, llama.cpp）的吞吐量基准测试数据以验证该阈值的有效性。 | 逻辑自洽（保守估计避免高估性能符合工程直觉），但来源[1][2][3]仅涉及Qwen3.8-27B在SGLang/vLLM/NInfer下的精度或单点性能，未覆盖多栈吞吐量方差及0.2x阈值的实证支持，属经验事实缺来源直接支持。

## Search Query

Qwen3-27B FP8 INT8 NVFP4 inference throughput benchmark vLLM TensorRT-LLM variance

## Retrieval Sources

- {'url': 'https://linux.do/t/topic/2821819&rut=21235c15048a7077dfe7a3b57ffaffc49bd7518af4041d1339f170ec02b35ca0', 'type': 'ddg', 'title': 'Qwen3.8-27B BF16 / FP8 / NVFP4 实测 - 开发调优 - LINUX DO'}
- {'url': 'https://blog.csdn.net/weixin_29056781/article/details/166022297&rut=90c2b8874e00fe7c65b297d67da0c9b8864d2183e939c714938b3ce2952db9f2', 'type': 'ddg', 'title': 'Qwen3.8-27B FP8量化部署实战：从显存计算到性能调优-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00936/article/details/170614004&rut=c60ffca162aedc2213199bf11cfbba0d544f4286ea33981546790c2e2edad0e9', 'type': 'ddg', 'title': 'Qwen3.8-27B-nvfp4-NInfer评测报告解读：AIME 96.67%背后，NVFP4量化精度损失到底有多'}
