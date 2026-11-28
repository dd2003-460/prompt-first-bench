# N604: Threshold_CAL阈值确定：基于历史数据，若设定Threshold_CAL=0.85，则Recall@Precision=0.9为0.88；若下调至0.

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N214, N215, N216

## Claim

Threshold_CAL阈值确定：基于历史数据，若设定Threshold_CAL=0.85，则Recall@Precision=0.9为0.88；若下调至0.80，Recall升至0.92但Precision降至0.85；需根据业务对假阳性（误杀正确结论）的容忍度选择阈值，通常科研场景优先保Recall，建议设为0.80。

## Corrected Claim

Threshold_CAL阈值的确定需基于历史数据权衡Recall与Precision。通常科研场景优先保Recall，倾向于设置较低阈值（如0.80左右），但具体最优阈值及对应的指标变化需根据实际业务数据的评估结果确定。

## Evidence

[质询]该陈述包含具体的经验性数值（如Threshold=0.85对应Recall=0.88等），这些数值高度依赖于特定的数据集分布和模型性能，无法从第一性原理或通用逻辑中推导得出，属于典型的经验事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体阈值与指标映射关系无法通过纯逻辑推导验证）

## Search Query

NLI entailment threshold precision recall tradeoff scientific claims verification
