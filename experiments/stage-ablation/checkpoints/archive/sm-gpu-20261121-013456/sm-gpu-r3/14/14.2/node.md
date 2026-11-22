# N301: RTX 3090 运行 Qwen3-27B INT4 量化模型时，理论最大吞吐量受限于显存带宽 936 GB/s，估算公式为 Throughput ≈ Band

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N125

## Claim

RTX 3090 运行 Qwen3-27B INT4 量化模型时，理论最大吞吐量受限于显存带宽 936 GB/s，估算公式为 Throughput ≈ Bandwidth / Model_Size_GB，即 936 / 13.5 ≈ 69.3 tokens/s（理论上限），实际因算子开销预计降至 40-50 tokens/s [待核验]。

## Corrected Claim

RTX 3090 运行 Qwen3-27B INT4 量化模型时，理论最大吞吐量受限于显存带宽 936 GB/s，估算公式为 Throughput ≈ Bandwidth / Model_Size_GB，即 936 / 13.5 ≈ 69.3 tokens/s（理论上限），实际因算子开销预计降至 40-50 tokens/s [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090显存带宽936GB/s为准确硬件参数，Qwen3-27B INT4量化后模型大小约13.5GB符合计算逻辑（27B*0.5bytes），吞吐量估算公式及数值推导正确。

## Search Query

RTX 3090 Qwen3-27B INT4 inference throughput tokens per second
