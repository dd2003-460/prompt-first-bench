# N378: Apple M2 Ultra 预填充阶段的实际 TTFT 修正系数 k_prefill_efficiency 通常为 0.6-0.8，主要受限于内存控制器延迟、

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N118

## Claim

Apple M2 Ultra 预填充阶段的实际 TTFT 修正系数 k_prefill_efficiency 通常为 0.6-0.8，主要受限于内存控制器延迟、指令调度开销及 Apple Silicon 编译器对大矩阵乘法的优化程度，实际 TTFT = Theoretical_TTFT / k_prefill_efficiency。

## Corrected Claim

Apple M2 Ultra 预填充阶段的实际 TTFT 通常高于理论值，受限于内存带宽、指令调度及编译器优化等因素，实际 TTFT 可表示为 Theoretical_TTFT / k_prefill_efficiency，其中 k_prefill_efficiency 为小于 1 的效率系数，具体数值需依据实际负载和硬件配置测定。

## Evidence

[质询]该陈述包含具体的经验参数（0.6-0.8）和特定的工程归因（内存控制器延迟、编译器优化程度），属于经验事实而非第一性原理可推导的数学或物理定律。在缺乏具体基准测试数据或官方技术白皮书支持的情况下，无法验证该特定系数范围的准确性及归因的排他性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该参数非第一性原理可推导）

## Search Query

Apple M2 Ultra LLM prefill latency efficiency benchmark
