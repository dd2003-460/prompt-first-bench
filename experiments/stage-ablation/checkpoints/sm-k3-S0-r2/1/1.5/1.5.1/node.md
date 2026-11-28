# N43: Self-Consistency 采样次数 k 的最优值为 5；基于误差收敛曲线 E(k) = E_inf * exp(-λk)，当 k=5 时边际收益（每增加

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

Self-Consistency 采样次数 k 的最优值为 5；基于误差收敛曲线 E(k) = E_inf * exp(-λk)，当 k=5 时边际收益（每增加 1 次采样的准确率提升 <0.5%）低于推理延迟成本（增加 ~1.2s/token），故 k=5 为性价比拐点。

## Corrected Claim

Self-Consistency 采样次数 k 的选择需平衡准确率增益与推理成本；在典型大语言模型推理场景中，k=5 常被视为一个具有较高性价比的经验拐点，但具体最优值取决于模型能力、任务复杂度及延迟容忍度，并非固定不变的理论常数。

## Evidence

[质询]该陈述包含具体的经验参数（如'准确率提升<0.5%'、'延迟~1.2s/token'、'最优值k=5'），这些并非Self-Consistency算法的通用理论常数，而是高度依赖于具体模型规模、任务难度及硬件环境的经验观测值。将其表述为普适性的'最优值'和固定阈值缺乏普遍适用性，且不同研究（如原始论文或后续复现）中报告的边际收益拐点往往随上下文长度和模型大小波动，不存在统一的'k=5'黄金标准。 | source=knowledge，逻辑结构自洽（基于成本-收益权衡的决策逻辑），但具体数值（0.5%, 1.2s）属于特定场景下的经验数据，非第一性原理可推导的普适真理，且无外部来源验证其普适性，故降级为定性表述。

## Search Query

self-consistency sampling optimal k convergence curve LLM reasoning
