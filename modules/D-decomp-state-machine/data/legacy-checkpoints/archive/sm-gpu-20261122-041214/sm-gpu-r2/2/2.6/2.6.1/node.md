# N94: H100 相比 A100 在 LLM 解码 (batch=1) 场景下的吞吐量提升主要源于显存带宽提升 (HBM3 3.35TB/s vs HBM2e 2.0T

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

H100 相比 A100 在 LLM 解码 (batch=1) 场景下的吞吐量提升主要源于显存带宽提升 (HBM3 3.35TB/s vs HBM2e 2.0TB/s)，提升比例约为 1.67 倍 (3.35/2.0)，而非算力提升；在预填充 (Prefill) 高算力场景下提升可达 2-3 倍。

## Corrected Claim

H100 相比 A100 在 LLM 解码 (batch=1) 场景下的吞吐量提升主要源于显存带宽提升 (HBM3 3.35TB/s vs HBM2e 2.0TB/s)，提升比例约为 1.67 倍 (3.35/2.0)，而非算力提升；在预填充 (Prefill) 高算力场景下提升可达 2-3 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 (HBM3) 带宽约 3.35TB/s，A100 (HBM2e) 带宽约 2.0TB/s，比值 1.675 符合陈述；LLM 解码 (batch=1) 为内存带宽瓶颈，预填充为算力瓶颈，逻辑自洽。

## Search Query

H100 vs A100 memory bandwidth HBM3 HBM2e LLM decode throughput ratio
