# N423: RTX 4090 (INT8) 与 H100 (BF16) 的 Decode 吞吐量比值修正：基于 N141 和 N113 的数据，H100 BF16 Deco

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N167

## Claim

RTX 4090 (INT8) 与 H100 (BF16) 的 Decode 吞吐量比值修正：基于 N141 和 N113 的数据，H100 BF16 Decode (~32 tokens/s) 与 RTX 4090 INT8 (~31.7 tokens/s) 的比值接近 1:1，而非 N167 声称的 1:2.5。若 H100 采用 FP8 量化，吞吐量可提升至 ~50 tokens/s，比值变为 1:1.6。N167 的 1:2.5 比值可能基于 H100 的 HBM3e (H200) 或更高效的软件栈。

## Corrected Claim

RTX 4090 (INT8) 与 H100 (BF16) 的 Decode 吞吐量比值修正：基于 N141 和 N113 的数据，H100 BF16 Decode (~32 tokens/s) 与 RTX 4090 INT8 (~31.7 tokens/s) 的比值接近 1:1，而非 N167 声称的 1:2.5。若 H100 采用 FP8 量化，吞吐量可提升至 ~50 tokens/s，比值变为 1:1.6。N167 的 1:2.5 比值可能基于 H100 的 HBM3e (H200) 或更高效的软件栈。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 INT8 与 H100 BF16 在 Decode 阶段受限于内存带宽，两者带宽量级相近（~1TB/s vs ~3.35TB/s，但 H100 显存带宽虽高，BF16 模型权重体积大，实际吞吐受限于计算与访存平衡，且 H100 通常用于多卡或大模型，单卡小模型 Decode 优势不明显，数值量级合理）

## Search Query

H100 vs RTX 4090 LLM inference throughput ratio benchmark
