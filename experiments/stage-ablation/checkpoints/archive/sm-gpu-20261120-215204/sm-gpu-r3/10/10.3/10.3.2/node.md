# N401: Apple M4 Ultra 运行 Qwen3-27B (W4 量化) 的实际 Tokens/s 下限为 5.4 (819 GB/s 带宽 * 0.4 保守效率

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N151

## Claim

Apple M4 Ultra 运行 Qwen3-27B (W4 量化) 的实际 Tokens/s 下限为 5.4 (819 GB/s 带宽 * 0.4 保守效率 / 13.5 GB 权重)，上限为 10.9 (819 GB/s * 0.8 乐观效率 / 13.5 GB 权重)，表明其每美元吞吐量在 0.00045-0.00091 区间，进一步确认其性能成本比劣于 NVIDIA 方案。

## Corrected Claim

Apple M4 Ultra 在假设 819 GB/s 带宽和 13.5 GB 模型权重的条件下，Qwen3-27B (W4) 的理论吞吐量区间约为 5.4-10.9 Tokens/s。其每美元吞吐量是否劣于 NVIDIA 方案取决于具体的 NVIDIA 硬件型号、价格及软件优化程度，不能仅凭此单一指标绝对判定。

## Evidence

[质询]该陈述包含具体的硬件规格（M4 Ultra 带宽 819 GB/s）、模型量化后大小（13.5 GB）以及价格/成本比数据，这些属于经验事实。虽然 source 标记为 knowledge，但参考来源显示“本轮检索无可用来源”，且 M4 Ultra 的具体带宽和 Qwen3-27B W4 的精确大小并非通用第一性原理可推导的数学/物理常数，而是依赖具体硬件发布数据和模型实现细节的经验参数。若这些具体数值（如 819 GB/s 或 13.5 GB）与最新公开数据存在偏差，则结论错误。此外，将“每美元吞吐量”直接等同于“性能成本比劣于 NVIDIA”忽略了 NVIDIA 方案的具体型号、价格及软件栈开销，属于过度简化的比较。 | 逻辑推导过程（带宽*效率/权重=Tokens/s）自洽，量级合理。但作为 knowledge 节点，虽无需外部来源支持即可判 verified 的前提是“无可信攻击点”。此处攻击点在于具体经验参数（带宽、模型大小、价格比）的准确性无法在缺乏来源的情况下完全确证，且成本比较缺乏具体 NVIDIA 对照基准，存在经验事实不确定性，故降级为 degraded 以保留定性结论但修正具体数值依赖。
