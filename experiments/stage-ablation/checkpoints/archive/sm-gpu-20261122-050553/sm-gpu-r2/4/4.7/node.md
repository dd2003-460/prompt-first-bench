# N26: 吞吐量指标 (Throughput) = Tokens_per_second_per_card × Number_of_cards；需测量 Qwen3-27B 

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N4, N5, N6

## Claim

吞吐量指标 (Throughput) = Tokens_per_second_per_card × Number_of_cards；需测量 Qwen3-27B 在 BF16/FP8/INT8 下各硬件的实测 tokens/s，作为延迟无关的性能基准。

## Corrected Claim

吞吐量指标 (Throughput) = Tokens_per_second_per_card × Number_of_cards；需测量 Qwen3-27B 在 BF16/FP8/INT8 下各硬件的实测 tokens/s，作为延迟无关的性能基准。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

Qwen3-27B inference throughput tokens per second BF16 FP8 INT8 benchmark
