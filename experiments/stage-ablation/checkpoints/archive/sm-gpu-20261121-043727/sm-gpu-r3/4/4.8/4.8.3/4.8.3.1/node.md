# N226: ROCm 6.x 对 Qwen3-27B 的量化支持滞后量：以 vLLM/llama.cpp 官方 Release Notes 中 'Qwen3' 关键字出现时

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N85

## Claim

ROCm 6.x 对 Qwen3-27B 的量化支持滞后量：以 vLLM/llama.cpp 官方 Release Notes 中 'Qwen3' 关键字出现时间减去 CUDA 生态对应版本发布时间，计算时间差 ΔT_lag；若 ROCm 版本仅支持 BF16 而 CUDA 已支持 FP8，则 ΔT_lag 包含精度特性缺失惩罚，量化为性能损失系数 (1 - Throughput_ROCM_BF16 / Throughput_CUDA_FP8) [待核验]

## Corrected Claim

ROCm 6.x 已支持 Qwen3-27B 的 FP8 量化推理（基于 vLLM），但具体的量化支持滞后量 ΔT_lag 及性能损失系数需依据官方 Release Notes 时间戳及实测吞吐量数据另行计算，当前来源未提供具体数值。

## Evidence

[质询]该陈述定义了一个具体的量化指标（ΔT_lag 和性能损失系数），但参考来源仅提供了 ROCm 支持 FP8 的定性事实，未提供 vLLM/llama.cpp 官方 Release Notes 中 'Qwen3' 关键字出现的具体时间戳，也未提供 CUDA 生态对应版本的发布时间，更未提供具体的 Throughput 数值以计算该系数。因此，无法从现有来源验证该具体数值或时间差的存在。 | 来源 [1] 和 [3] 证实了 ROCm 环境下 vLLM 已支持 Qwen3 系列模型的 FP8 量化推理，这与陈述中隐含的'ROCm 支持 FP8'的前提一致，但缺乏计算 ΔT_lag 所需的具体时间数据和性能基准数据，属于经验事实且缺来源直接支持具体数值。

## Search Query

vLLM llama.cpp release notes Qwen3 AMD ROCm support date vs CUDA FP8

## Retrieval Sources

- {'url': 'https://www.modelscope.cn/posts/434795&rut=1742b29a5d337dbe7e5b1f8658219955848aa82c2b8888b5943d0aa99bdc5efc', 'type': 'ddg', 'title': '在AMD ROCm上部署Qwen3.6-27B-FP8：vLLM推理与服务实践'}
- {'url': 'https://www.modelscope.cn/posts/436771&rut=408cf4948af9227f9ba8eb10310e45199c31ff70a02b7a9158dcfbb9eda774f8', 'type': 'ddg', 'title': 'AMD ROCm 上部署 Qwen3.8-27B 多模态大模型：vLLM 推理优化实战'}
- {'url': 'https://developer.aliyun.com/article/1736725&rut=9c2bf7d4ac6ec10d9afd190dcacc723955c6df6bc66f72df0f26dbc2d3027e8b', 'type': 'ddg', 'title': '在 AMD ROCm DSW 上部署 Qwen3.6-27B-FP8：vLLM、MTP 解码加速与小并发压测'}
