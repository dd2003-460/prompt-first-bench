# N530: 工作点1 (High-Concurrency) 单请求 P99 延迟 < 2s 的可行性瓶颈分析：在 131072 tokens 输入下，Prefill 阶段耗

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N187, N188, N189

## Claim

工作点1 (High-Concurrency) 单请求 P99 延迟 < 2s 的可行性瓶颈分析：在 131072 tokens 输入下，Prefill 阶段耗时 T_prefill = 131072 / (Throughput_per_GPU)，若 V100 TP=4 下 Prefill 吞吐为 8000 tok/s，则 T_prefill ≈ 16.4s，远超 2s 目标，故该工作点仅适用于短输入 (<1k tokens) 场景

## Corrected Claim

工作点1 (High-Concurrency) 单请求 P99 延迟 < 2s 的可行性瓶颈分析：在 131072 tokens 输入下，Prefill 阶段耗时 T_prefill = 131072 / (Throughput_per_GPU)，若 V100 TP=4 下 Prefill 吞吐为 8000 tok/s，则 T_prefill ≈ 16.4s，远超 2s 目标，故该工作点仅适用于短输入 (<1k tokens) 场景

## Evidence

先验知识/题面给定，逻辑校验通过：131072/8000=16.4s，远超2s，结论自洽

## Search Query

LLM prefill latency calculation long context V100 tensor parallelism
