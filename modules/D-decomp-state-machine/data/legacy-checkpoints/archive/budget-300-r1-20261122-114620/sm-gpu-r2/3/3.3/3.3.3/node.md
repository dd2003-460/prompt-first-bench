# N94: INT8 量化在 27B 规模模型上的质量损失边界条件：当模型参数规模 > 14B 且采用分组大小 (group_size) >= 128 的量化策略时，PPL

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

INT8 量化在 27B 规模模型上的质量损失边界条件：当模型参数规模 > 14B 且采用分组大小 (group_size) >= 128 的量化策略时，PPL 增加通常 < 3%；若 group_size < 64 或未校准 (calibration-free)，PPL 增加可能超过 5%，导致在 MMLU 数学子集上准确率下降 > 5%，此时不再满足 N22 定义的阈值。

## Corrected Claim

INT8 量化在 27B 规模模型上，采用较大分组大小 (group_size >= 128) 通常能保持较低的质量损失（PPL 增加较小）；而较小的 group_size (< 64) 或未校准策略往往导致更显著的性能下降，可能影响下游任务（如 MMLU）的准确率，具体损失幅度取决于量化算法与校准数据。

## Evidence

[质询]该陈述包含具体的经验性阈值（如 PPL 增加 < 3%、MMLU 准确率下降 > 5%），这些数值并非第一性原理可推导的数学或物理定律，而是依赖于具体模型架构、量化算法（如 GPTQ, AWQ, SmoothQuant）及校准数据集的经验统计结果。不同量化方法在相同 group_size 下的表现差异显著，直接断言统一的百分比边界缺乏普适性，且存在将特定实验结果泛化为通用规则的风险。 | source=knowledge，逻辑自洽（量化精度与 group_size 正相关符合直觉），但具体数值阈值属于经验事实，缺乏外部来源直接支持，且不同量化算法间存在差异，故降级为定性表述。
