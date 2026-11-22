# N199: H100 80GB 在 LLM Decode 阶段的实际有效内存带宽利用率修正系数 (Efficiency_Factor) 的量化范围：H100 HBM3 带宽

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N58

## Claim

H100 80GB 在 LLM Decode 阶段的实际有效内存带宽利用率修正系数 (Efficiency_Factor) 的量化范围：H100 HBM3 带宽极高，但在 Batch=1 时受限于内存控制器延迟和访问局部性，实测有效带宽通常为理论峰值 (3350 GB/s) 的 80%-90%。取中值 85% 计算，有效带宽 = 2847.5 GB/s。

## Corrected Claim

H100 80GB 在 LLM Decode 阶段（Batch=1）的实际有效内存带宽利用率受限于内存控制器延迟和访问局部性，通常低于理论峰值 (3350 GB/s)。具体利用率取决于模型架构和实现优化，一般认为在较高水平（如80%-90%区间），但需具体实测数据确认。

## Evidence

[质询]该陈述包含具体的经验性数值（80%-90%利用率、85%中值），属于硬件性能实测数据，无法从第一性原理推导。在缺乏参考来源支持的情况下，无法验证该具体数值范围的准确性，且不同模型、序列长度及实现细节下，Batch=1时的有效带宽利用率波动较大，固定为80-90%可能过于绝对。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）。

## Search Query

H100 LLM decode memory bandwidth efficiency
