# N202: Self-Critique 轮数 K 的补偿阈值：当 α × β_cloud < 0.5 时，需增加 K 轮自我批判以弥补成功率缺口，K_min = ceil(

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N69

## Claim

Self-Critique 轮数 K 的补偿阈值：当 α × β_cloud < 0.5 时，需增加 K 轮自我批判以弥补成功率缺口，K_min = ceil((Target_Success_Prob - P_success_B) / ΔP_per_critique)，其中 ΔP_per_critique ≈ 5%（每轮批判平均提升的成功率），若 K_min > 3 则表明该任务类型不适合混合云方案，应直接全云或放弃。

## Corrected Claim

Self-Critique 轮数 K 的补偿策略：当 α × β_cloud < 0.5 时，需评估增加 K 轮自我批判以弥补成功率缺口。K 的最小值取决于每轮批判的实际提升幅度 ΔP_per_critique（该值随任务难度和模型能力动态变化，非固定 5%）。若所需 K 值过大（如超过 3 轮），通常表明该任务类型不适合混合云方案，应考虑全云部署或重新设计任务流程。

## Evidence

[质询]ΔP_per_critique ≈ 5% 是一个高度依赖具体任务类型、模型能力和提示词工程的经验参数，并非普适常数；将其作为固定值用于计算 K_min 缺乏理论依据，且不同场景下该值波动极大，可能导致阈值判断严重失真。 | source=knowledge，逻辑结构自洽（公式推导无误），但核心参数 ΔP_per_critique 为经验估计值，缺乏通用性支撑，故降级为定性建议。
