# N141: 全模型通信占比计算：num_layers=64。总通信时间 ≈ 64 * (0.15 μs + 8 μs) ≈ 522 μs ≈ 0.52 ms。单 token

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

全模型通信占比计算：num_layers=64。总通信时间 ≈ 64 * (0.15 μs + 8 μs) ≈ 522 μs ≈ 0.52 ms。单 token 生成延迟 (Decode) 在 4xV100 TP=4 上约为 50-100ms (取决于 batch size 和 KV cache 长度)。通信占比 = 0.52ms / 50ms ≈ 1.04%，而非原 claim 的 <0.01%。这表明通信虽非绝对瓶颈，但已不可忽略，尤其在 batch size 较大时。

## Corrected Claim

全模型通信占比计算：num_layers=64。总通信时间 ≈ 64 * (0.15 μs + 8 μs) ≈ 522 μs ≈ 0.52 ms。单 token 生成延迟 (Decode) 在 4xV100 TP=4 上约为 50-100ms (取决于 batch size 和 KV cache 长度)。通信占比 = 0.52ms / 50ms ≈ 1.04%，而非原 claim 的 <0.01%。这表明通信虽非绝对瓶颈，但已不可忽略，尤其在 batch size 较大时。

## Evidence

先验知识/题面给定，逻辑校验通过：64层 * 8.15μs ≈ 521.6μs ≈ 0.52ms，计算无误；0.52ms / 50ms = 1.04%，量级与逻辑自洽。

## Search Query

vLLM decode latency 27B model V100 tensor parallelism communication overhead percentage
