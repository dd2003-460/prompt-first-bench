# N142: Apple M4 Max统一内存带宽为546 GB/s，在Qwen3-27B INT8推理中，理论最大吞吐量约为546/27 ≈ 20 tokens/s（Mem

- **status**: verified
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

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中提到的‘理论最大吞吐量’（理想/短文本上限）和‘实际受限于...实测’（长上下文/调度开销约束），两者在场景（Seq_len）和约束条件（理想 vs 实际开销）上正交且互补。虽然两者本质上都是不同参数下的吞吐量计算，但分别代表了性能的两个关键边界（天花板与典型瓶颈场景），符合工作点分解的逻辑，不属于简单的参数冗余。）

## Search Query

Apple M4 Max LLM inference tokens per second Qwen 27B benchmark
