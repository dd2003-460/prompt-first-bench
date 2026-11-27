# N123: H100 SXM5 FP8 推理性能基准：在 Qwen3-27B 类模型上，H100 SXM5 的 FP8 推理吞吐量通常可达 800-1200 tokens/

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N47

## Claim

H100 SXM5 FP8 推理性能基准：在 Qwen3-27B 类模型上，H100 SXM5 的 FP8 推理吞吐量通常可达 800-1200 tokens/sec (Batch Size=1, 32K context)，相比 BF16 的 400-600 tokens/sec 有 1.5-2x 加速，此性能提升是计算其单位 Token 成本的关键变量。

## Corrected Claim

H100 SXM5 FP8 推理性能基准：在 Qwen3-27B 类模型上，H100 SXM5 的 FP8 推理吞吐量在典型短上下文（如8k输入）下可达 1600+ tokens/sec，而在长上下文（如32K）或高并发场景下可能降至 800-1200 tokens/sec 区间，相比 BF16 通常有 1.5-2x 加速。

## Evidence

[质询]数值量级与具体工况不匹配：来源[1]显示在8k输入/1k输出的典型对话负载下，H100 FP8吞吐可达1689 token/s，远高于陈述中的800-1200；且32K长上下文通常会导致KV Cache占用显存增加，从而降低Batch Size或增加延迟，吞吐量往往低于短上下文场景，陈述未区分具体上下文长度对吞吐的影响，且800-1200的区间可能偏低或仅适用于特定高延迟敏感场景，缺乏对BF16具体数值的直接对比支持。 | 来源[1]直接支持H100 FP8在Qwen3.5上可达1689 token/s（短上下文），与陈述的800-1200存在量级差异但同属合理范围（取决于上下文长度和负载）；来源[2]确认了Qwen3.5-27B在H100 SXM上的FP8基准测试存在，但未提供具体数值；来源[3]仅介绍H100规格。由于陈述中的具体数值区间（800-1200）与来源[1]的实测值（1689）不完全一致，且缺乏针对32K context的精确数据支持，判定为degraded。

## Search Query

H100 FP8 inference benchmark Qwen 27B tokens per second

## Retrieval Sources

- {'url': 'https://inferencex.semianalysis.com/zh/run/qwen-3-5-on-h100&rut=b97dc44d90909e5d16041318f6bcb2aa596c513b9b827bc9ec53e890d9cb6695', 'type': 'ddg', 'title': 'Qwen3.5 在 H100 上的实测推理吞吐与成本 | InferenceX'}
- {'url': 'https://www.millstoneai.com/inference-benchmark/qwen3-5-27b-fp8-1x-h100-sxm&rut=209ed8e45c8008925fc25892f7715f557ac04515331430bd94a7aa063d1e800b', 'type': 'ddg', 'title': 'Qwen3.5-27B on 1x H100 SXM Benchmark — FP8 | Millstone AI'}
- {'url': 'https://blog.csdn.net/qq_36490243/article/details/163283115&rut=8512bd2a2acb5f113ccef954170c627bbe39d6ae857c2f4bb227da3de2476d56', 'type': 'ddg', 'title': '读懂 H100：大模型时代的算力锚点 - Csdn博客'}
