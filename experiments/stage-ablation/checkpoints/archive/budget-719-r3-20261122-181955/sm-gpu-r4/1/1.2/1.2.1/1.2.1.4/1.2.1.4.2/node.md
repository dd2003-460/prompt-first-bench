# N449: A100 80GB在32K上下文Decode阶段的实际有效带宽利用率修正：理论带宽2039 GB/s，实测LLM推理有效带宽通常为70-80%（因内存控制器效率

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N152

## Claim

A100 80GB在32K上下文Decode阶段的实际有效带宽利用率修正：理论带宽2039 GB/s，实测LLM推理有效带宽通常为70-80%（因内存控制器效率、缓存未命中等），修正后有效带宽 ≈ 1427-1631 GB/s。Decode理论吞吐量上限修正为 1631/(54+32.77) ≈ 18.8 tokens/s (上限) 至 1427/86.77 ≈ 16.4 tokens/s (下限)，而非基于理论带宽的23.5 tokens/s。

## Corrected Claim

A100 80GB在32K上下文Decode阶段的实际有效带宽利用率修正：理论带宽2039 GB/s，实测LLM推理有效带宽通常为70-80%（因内存控制器效率、缓存未命中等），修正后有效带宽 ≈ 1427-1631 GB/s。Decode理论吞吐量上限修正为 1631/(54+32.77) ≈ 18.8 tokens/s (上限) 至 1427/86.77 ≈ 16.4 tokens/s (下限)，而非基于理论带宽的23.5 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB HBM2e 理论带宽 2039 GB/s 符合规格；70-80% 有效带宽利用率符合 LLM 推理 Decode 阶段（Memory-bound）的工程经验；吞吐量计算 1631/86.77≈18.8 和 1427/86.77≈16.4 数学正确，且低于理论上限 23.5，逻辑自洽。

## Search Query

A100 effective memory bandwidth utilization LLM inference efficiency factor
