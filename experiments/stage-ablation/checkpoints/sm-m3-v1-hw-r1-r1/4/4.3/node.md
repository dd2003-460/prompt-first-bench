# N20: 量化 CoT-Critique 机制对推理链条稳定性的贡献：定义稳定性指标 $R_{stab} = 1 - \sigma_{output}$，其中 $\sigm

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

量化 CoT-Critique 机制对推理链条稳定性的贡献：定义稳定性指标 $R_{stab} = 1 - \sigma_{output}$，其中 $\sigma_{output}$ 为同一输入多次运行（n=10）输出结论的逻辑一致性方差；需对比开启 Critique 钩子前后 $R_{stab}$ 的变化量 $\Delta R_{stab}$，并测量由此带来的额外推理步数增加比例 $\Delta steps/steps_{base}$，以评估其对总耗时 $T_{total}$ 的影响。

## Corrected Claim

量化 CoT-Critique 机制对推理链条稳定性的贡献：定义稳定性指标 $R_{stab} = 1 - \sigma_{output}$，其中 $\sigma_{output}$ 为同一输入多次运行（n=10）输出结论的逻辑一致性方差；需对比开启 Critique 钩子前后 $R_{stab}$ 的变化量 $\Delta R_{stab}$，并测量由此带来的额外推理步数增加比例 $\Delta steps/steps_{base}$，以评估其对总耗时 $T_{total}$ 的影响。
