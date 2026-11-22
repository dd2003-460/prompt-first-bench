# N200: 2x RTX 4090 (FP8) 在 Qwen3-27B 32K context 下的有效吞吐率 Throughput_eff 计算：假设单卡 FP8 峰值吞

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N76

## Claim

2x RTX 4090 (FP8) 在 Qwen3-27B 32K context 下的有效吞吐率 Throughput_eff 计算：假设单卡 FP8 峰值吞吐为 40 tokens/s，受 PCIe 4.0 x16 (64GB/s) 带宽限制及 AllReduce 通信开销（约 20-30% 时间损耗）影响，有效吞吐降至 28-32 tokens/s，需对比 MI300X 单卡 FP8 实测吞吐（约 50-60 tokens/s）以量化性能差距

## Corrected Claim

单张RTX 4090 (FP8) 在 Qwen3-27B 下的解码吞吐约为 130 tokens/s。使用 2x RTX 4090 通过 PCIe 互联进行张量并行时，受限于 PCIe 带宽和 AllReduce 通信开销，有效吞吐通常低于单卡性能，具体数值取决于上下文长度和实现优化，但绝非 28-32 tokens/s 这一低量级。

## Evidence

[质询]数值量级严重错误：参考来源[1]明确显示单张RTX 4090在Qwen3-27B FP8下的解码速度约为132 tok/s，而陈述中假设单卡峰值仅为40 tokens/s，低估了3倍以上；此外，2x 4090通过PCIe互联进行AllReduce通信在32K长上下文下会导致严重的通信瓶颈，实际有效吞吐通常远低于单卡水平，不可能达到28-32 tokens/s（甚至可能低于单卡），且MI300X单卡50-60 tokens/s的实测数据也远低于其实际性能（通常可达数百tok/s）。 | 来源[1]直接矛盾：单卡RTX 4090实测132 tok/s，远高于陈述中的40 tokens/s假设；且多卡PCIe互联在长上下文下通信开销极大，陈述中的有效吞吐估算违背基本硬件性能直觉。

## Search Query

RTX 4090 dual GPU LLM inference throughput penalty PCIe bottleneck FP8 Qwen 27B benchmark

## Retrieval Sources

- {'url': 'https://huggingface.co/Qwen/Qwen3.8-27B-FP8/discussions/19&rut=555a8a7851cece2de2aedb546abe818db12ae918866a9ae6b3a1a3cd33f1b628', 'type': 'ddg', 'title': 'Qwen/Qwen3.8-27B-FP8 · 132 tok/s on RTX 4090 [48 GB] - Hugging Face'}
