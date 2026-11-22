# N84: INT4 (AWQ/GPTQ) 精度下的总内存需求计算：Weights = 27B * 0.5 bytes = 13.5 GB；KV Cache (32K, B

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

INT4 (AWQ/GPTQ) 精度下的总内存需求计算：Weights = 27B * 0.5 bytes = 13.5 GB；KV Cache (32K, BF16) ≈ 5.37 GB（KV Cache 通常不量化以保持精度）；Overhead ≈ 3 GB；Total ≈ 21.87 GB。此数值可适配 RTX 4090 (24GB)，但需预留 2.13 GB 余量用于操作系统驱动及临时缓冲区，实际可用显存需 > 22 GB [待核验]，需确认 AWQ 量化后 KV Cache 是否必须保持 BF16。

## Corrected Claim

INT4 (AWQ/GPTQ) 量化下，27B 模型权重占用约 13.5 GB。KV Cache 大小取决于序列长度和模型架构，通常不量化以保持精度（但部分现代框架支持量化 KV Cache），32K 上下文下 KV Cache 可能在数 GB 量级。加上推理框架开销，总显存需求通常在 20-25 GB 之间，可能适配 RTX 4090 (24GB)，但需根据具体模型架构和推理框架配置精确计算，并预留系统余量。

## Evidence

[质询]KV Cache 的具体数值（5.37 GB）依赖于模型的具体架构参数（如层数、头数、头维度），这些参数未在陈述中给出，属于经验事实且无法仅从第一性原理推导；此外，'Overhead ≈ 3 GB' 是一个高度依赖具体推理框架（如 vLLM, TGI, llama.cpp）和系统配置的估算值，缺乏通用标准，存在口径混淆风险。 | 来源 [1][2][3] 仅涵盖 AWQ/GPTQ 量化算法原理，未提供具体内存计算公式或 KV Cache 量化策略的直接数据支持；Weights 计算逻辑正确（27B * 0.5B = 13.5GB），但 KV Cache 和 Overhead 的具体数值缺乏来源直接支持，且 KV Cache 是否必须保持 BF16 取决于具体实现（部分框架支持 FP8/INT8 KV Cache），故降级为定性表述。

## Search Query

Qwen3-27B INT4 AWQ KV cache BF16 memory footprint 24GB GPU feasibility 32k context

## Retrieval Sources

- {'url': 'https://blog.csdn.net/bumblebee16/article/details/167129055&rut=2431b040d4392d18dffb7a8f17b86a9576e628b80a92c5fbdef8bf28da193f87', 'type': 'ddg', 'title': '【模型量化⑤】Weight-Only INT4：AWQ与GPTQ两大算法深度解析-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_37647148/article/details/161776271&rut=fe61a36c5f2f092fad5634128462803eb9671522aca5834aab3bda206586d57f', 'type': 'ddg', 'title': '量化压缩实战：Int8 / Int4 / Awq / Gptq 全面对比 - Csdn博客'}
- {'url': 'https://xiayihann.github.io/AIInfraGuide/guides/%E6%A8%A1%E5%9D%97%E5%9B%9B-%E6%8E%A8%E7%90%86%E4%BC%98%E5%8C%96/%E7%AC%AC4%E7%AB%A0-%E9%87%8F%E5%8C%96/43-weight-only-int4-gptq%E4%B8%8Eawq/&rut=60bd937f03afaabca61f71141ce38b43d4edeb0f627c0abd4a7f560dcf5e5143', 'type': 'ddg', 'title': '4.3 Weight-only INT4 量化：GPTQ 与 AWQ - AIInfraGuide'}
