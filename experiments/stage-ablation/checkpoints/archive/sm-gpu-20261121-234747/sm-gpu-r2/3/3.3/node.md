# N15: 工作点2-中性价比最优：2×消费卡（如2×RTX 3090 24GB）vs 1×数据卡（如1×L40S 48GB）在BF16/FP8精度下的TCO对比，需标注多

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

工作点2-中性价比最优：2×消费卡（如2×RTX 3090 24GB）vs 1×数据卡（如1×L40S 48GB）在BF16/FP8精度下的TCO对比，需标注多卡PCIe通信开销对吞吐的影响（如2×3090相对单卡4090的吞吐比）

## Corrected Claim

工作点2-中性价比评估：2×消费卡（如2×RTX 3090 24GB）与1×数据卡（如1×L40S 48GB）在BF16/FP8精度下的TCO需结合具体业务负载计算；多卡PCIe通信开销通常会导致2×3090的聚合吞吐低于单卡高性能卡（如4090/L40S）的线性扩展预期，具体吞吐比需实测标注。

## Evidence

[质询]该陈述包含具体的硬件TCO对比结论及性能吞吐比数值，属于经验事实。虽然逻辑框架（多卡通信开销影响吞吐）合理，但缺乏具体数据支持，且不同场景下TCO和吞吐比差异巨大，无法仅凭逻辑推导得出唯一确定的‘最优’结论或具体数值。 | 经验事实，逻辑自洽但缺来源支持。多卡PCIe通信确实会引入开销，但具体TCO和吞吐比需实测数据，无法从第一性原理严格推出具体数值。

## Search Query

2x RTX 3090 vs L40S TCO comparison multi-GPU PCIe overhead inference
