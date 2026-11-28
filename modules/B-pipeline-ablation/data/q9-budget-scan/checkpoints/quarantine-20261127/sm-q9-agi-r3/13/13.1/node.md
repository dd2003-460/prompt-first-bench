# N301: 在 4x V100 (TP=4, NVFP4) 上，Qwen3.8-27B 处理固定结构 CoT 提示 (长度约 500-800 tokens) 时的实测吞吐量

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N108

## Claim

在 4x V100 (TP=4, NVFP4) 上，Qwen3.8-27B 处理固定结构 CoT 提示 (长度约 500-800 tokens) 时的实测吞吐量下降系数为 0.75-0.80 (即速度降至自由形式提示的 75%-80%)，主要归因于 Attention 模块对长 Prompt 的 O(N^2) 计算复杂度及 KV Cache 显存占用增加导致的 Batch Size 潜在缩减。

## Corrected Claim

在 4x V100 (TP=4) 上，Qwen3.8-27B 处理长 CoT 提示时，由于 Attention 计算复杂度增加及 KV Cache 显存压力，吞吐量预计会低于自由形式短提示，但具体下降系数需实测验证。

## Evidence

[质询]来源摘要仅提及 Q4/Q8 量化对比和卡数缩放，未包含 NVFP4 量化格式、CoT 提示与自由形式提示的吞吐量对比数据，也未提供具体的 0.75-0.80 下降系数，属于关键数据缺失。 | 逻辑上 Attention O(N^2) 复杂度和 KV Cache 显存占用导致 Batch Size 缩减从而降低吞吐量的解释符合大模型推理的基本原理，但参考来源 [1] 仅涉及 Q4/Q8 量化基准，未覆盖 NVFP4 及特定提示类型的性能对比，缺乏直接数据支持。

## Search Query

vLLM throughput degradation long prompt vs short prompt attention complexity KV cache memory impact

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2072074634476909289&rut=e14e1b01b639a378ae8d7ef986fe88097d0f64a2bbbf119b0cbfae0037f1bd29', 'type': 'ddg', 'title': 'Qwen3.8-27B 实测：V100 上的部署要点与 Q4/Q8 全量基准'}
