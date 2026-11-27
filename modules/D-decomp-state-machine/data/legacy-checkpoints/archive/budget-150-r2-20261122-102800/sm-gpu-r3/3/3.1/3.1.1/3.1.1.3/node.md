# N244: H100-80GB (SXM) 在 BF16 单卡推理（batch=1, seq=32K）下的实测有效带宽利用率约为 80-85%，得益于 HBM3 高带宽和优

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N88, N89, N90

## Claim

H100-80GB (SXM) 在 BF16 单卡推理（batch=1, seq=32K）下的实测有效带宽利用率约为 80-85%，得益于 HBM3 高带宽和优化的 Tensor Core 调度，对应实测吞吐为 45.6-48.8 tokens/s。

## Corrected Claim

H100-80GB (SXM) 在 BF16 单卡推理（batch=1, seq=32K）下，得益于 HBM3 高带宽和优化的 Tensor Core 调度，通常能实现较高的有效带宽利用率，具体吞吐率取决于模型规模，实测数据需参考特定基准测试。

## Evidence

[质询]数值量级与具体参数缺乏公开基准支持：H100 SXM 在 BF16 下理论峰值算力约为 989 TFLOPS，若带宽利用率高达 80-85%，意味着计算效率极高，但 batch=1, seq=32K 的长序列推理通常受限于内存带宽而非计算单元，且 45.6-48.8 tokens/s 的吞吐率对于 H100 而言偏低（通常 H100 在类似配置下可达 100+ tokens/s 或更高，取决于具体模型大小和实现），该具体数值组合（高带宽利用率 vs 中等吞吐）可能存在内部逻辑张力或特定未说明的模型约束。 | source=knowledge，逻辑上自洽（高带宽利用率与高吞吐正相关，但具体数值需结合模型参数量判断，此处假设模型较大导致吞吐受限），无外部来源支持，依据经验事实排除条款及 knowledge 节点规则，因缺乏直接来源支持且数值具体，降级为 degraded 以保留定性描述。

## Search Query

H100 SXM BF16 LLM inference throughput tokens/s measured
