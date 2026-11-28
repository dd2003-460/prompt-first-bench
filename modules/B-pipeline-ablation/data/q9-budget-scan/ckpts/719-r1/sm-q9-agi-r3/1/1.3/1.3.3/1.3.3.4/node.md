# N141: 替代方案量化：在 V100 上使用 GPTQ/AWQ INT4 量化替代 NVFP4，INT4 在 CC 7.0 上有成熟的 Tensor Core 加速路径（

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

替代方案量化：在 V100 上使用 GPTQ/AWQ INT4 量化替代 NVFP4，INT4 在 CC 7.0 上有成熟的 Tensor Core 加速路径（通过 FP16 累加），其推理吞吐通常为 FP16 的 1.8-2.2 倍，且精度损失与 NVFP4 相当（Perplexity 增加 <0.1），是 V100 上的最优性价比量化格式

## Corrected Claim

在 V100 上使用 GPTQ/AWQ INT4 量化是常见的优化手段，相比 FP16 可显著降低显存占用并提升推理吞吐（具体倍数取决于实现和负载，通常有显著提升），且精度损失可控；由于 V100 不支持 NVFP4，该对比主要在于 INT4 相较于 FP16 的性价比优势。

## Evidence

[质询]V100 (CC 7.0) 不支持原生 INT4 Tensor Core 指令，所谓'成熟加速路径'通常指软件模拟或混合精度（如 FP16 存储+INT4 计算需特定库支持），且'1.8-2.2倍'及'Perplexity <0.1'为高度依赖模型规模、序列长度及具体实现（如 vLLM/TensorRT-LLM 版本）的经验数据，并非普适物理常数；此外，NVFP4 在 V100 上根本不可用（需 Hopper/Blackwell 架构），将其作为对比基准在 V100 语境下存在逻辑错位，虽可理解为'若能在 V100 上跑 NVFP4 则 INT4 更优'，但表述易引起歧义。 | 来源 [1][2][3] 均讨论 GPTQ/AWQ/INT4 量化技术及优势，但未提供 V100 上具体的 '1.8-2.2x' 吞吐倍数或 '<0.1' PPL 损失的直接实证数据，属于经验事实且缺乏特定硬件下的精确来源支持。

## Search Query

V100 INT4 quantization GPTQ AWQ inference throughput comparison FP16

## Retrieval Sources

- {'url': 'https://developer.aliyun.com/article/1769219&rut=6a27471f3313805ea10c1a64bf0ca00a4d73415edeb8d3acb2113decf139623d', 'type': 'ddg', 'title': '模型量化完全指南：Gguf、Gptq、Awq 怎么选-阿里云开发者社区'}
- {'url': 'https://guijiagi.com/posts/model-quantization-2026-int4-int8-awq-gptq-comparison/&rut=8d1299996b86f0c33fd94ee53cf69aabb600d1366483536f30ed6459050e71d6', 'type': 'ddg', 'title': '模型量化技术 2026：Int4/Int8/Awq/Gptq 实测对比'}
- {'url': 'https://blog.csdn.net/weixin_30952479/article/details/169421502&rut=d398e4512c76178958ff27a0673f78709c863bcb095ce529ae8684bc0af0447b', 'type': 'ddg', 'title': '大模型量化技术详解：Gptq与awq原理、实操与选型指南-csdn博客'}
