# N18: 工作点 2 (平衡性价比): INT4/FP8 精度。质量损失预估：INT4 AWQ/GPTQ 通常导致 1-3% 的 Perplexity 上升或 MMLU 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

工作点 2 (平衡性价比): INT4/FP8 精度。质量损失预估：INT4 AWQ/GPTQ 通常导致 1-3% 的 Perplexity 上升或 MMLU 下降 2-5 分 [待核验具体基准]。硬件要求：最少 25.5GB 显存。代表配置：1x RTX 4090 (24GB 需 offload 部分 KV 或启用 swap) 或 1x L4 (24GB) 或 1x A10 (24GB)。特点：显著降低显存需求和功耗，吞吐量提升 2-4x (相比 BF16)，质量损失在大多数通用任务中可接受。

## Corrected Claim

工作点 2 (平衡性价比): INT4/FP8 精度。质量损失预估：INT4 AWQ/GPTQ 通常导致轻微的 Perplexity 上升或 MMLU 下降（具体幅度视模型而定，常见范围约1-5%）。硬件要求：最少 25.5GB 显存。代表配置：1x RTX 4090 (24GB 需 offload 部分 KV 或启用 swap) 或 1x L4 (24GB) 或 1x A10 (24GB)。特点：显著降低显存需求和功耗，吞吐量相比 BF16 有显著提升（通常可达数倍），质量损失在大多数通用任务中可接受。

## Evidence

[质询]具体数值指标（Perplexity上升1-3%、MMLU下降2-5分、吞吐量提升2-4x）属于高度依赖模型规模、数据集及硬件环境的经验事实，参考来源仅提供了定性对比或不同模型（72B）的显存估算，未提供针对该特定工作点（隐含特定模型大小，如7B-13B级别，因25.5GB显存需求）的精确基准数据支持，存在以偏概全或数值量级偏差的风险。 | 来源[1][2][3]确认了INT4/FP8量化能显著降低显存并提升性能，但未提供具体的Perplexity/MMLU损失数值及2-4x吞吐倍数的直接证据；作为经验事实，缺乏直接来源支持，故降级。

## Search Query

Qwen3 27B INT4 quantization quality degradation benchmark perplexity MMLU drop

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_01050/article/details/151810257&rut=35adbf2145479fd83e44ed848f7c8bb1ddb6510f33c7e4e4e41938e7755a58b4', 'type': 'ddg', 'title': 'vLLM模型量化：INT4、INT8、FP8精度对比与实践指南-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_33402252/article/details/168045444&rut=21be0d7873f7198e8fe9f323d26e81549020ade36e3499346e048b74fd462c39', 'type': 'ddg', 'title': '大模型量化实战：从int4到fp8的精度与性能权衡 - Csdn博客'}
- {'url': 'https://guijiagi.com/posts/quantization-int4-int8-fp8/&rut=bc1733d9ca1aabb912bb3a0200b04514ecf5fd6816755bce123d5c57367ef9c8', 'type': 'ddg', 'title': '量化方案深度对比：Int4、Int8、Fp8的精度与速度权衡 | Ai 实战派 · 从技术到赚钱'}
