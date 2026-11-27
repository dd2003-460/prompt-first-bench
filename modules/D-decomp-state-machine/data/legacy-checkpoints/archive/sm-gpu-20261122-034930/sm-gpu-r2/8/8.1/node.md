# N142: Apple M4 Max统一内存带宽为546 GB/s，在Qwen3-27B INT8推理中，理论最大吞吐量约为546/27 ≈ 20 tokens/s（Mem

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N42

## Claim

Apple M4 Max统一内存带宽为546 GB/s，在Qwen3-27B INT8推理中，理论最大吞吐量约为546/27 ≈ 20 tokens/s（Memory-bound假设），实际受限于CPU-GPU数据搬运和调度，实测通常在15-18 tokens/s [待核验]。

## Corrected Claim

Apple M4 Max统一内存带宽为546 GB/s，在Qwen3-27B INT8推理中，理论最大吞吐量约为546/27 ≈ 20 tokens/s（Memory-bound假设），实际受限于CPU-GPU数据搬运和调度，实测通常在15-18 tokens/s（待核验）。

## Evidence

[质询]M4 Max 的内存带宽为 546 GB/s 是经验事实，且 Qwen3-27B 的具体模型参数（如实际参数量、量化后大小）及实测吞吐量（15-18 tokens/s）属于特定硬件与模型组合下的经验数据，无法仅从第一性原理严格推导，且缺乏外部来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Apple M4 Max LLM inference tokens per second Qwen 27B benchmark
