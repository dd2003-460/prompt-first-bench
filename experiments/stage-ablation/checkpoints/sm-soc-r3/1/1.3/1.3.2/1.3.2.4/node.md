# N135: 边界条件：噪声占比 σ_pref/μ 的阈值效应：当 σ_pref/μ > 0.35 时，分布尾部极端拉长，P99 可能出现 >50% 的异常溢价，此时‘高溢价

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N38

## Claim

边界条件：噪声占比 σ_pref/μ 的阈值效应：当 σ_pref/μ > 0.35 时，分布尾部极端拉长，P99 可能出现 >50% 的异常溢价，此时‘高溢价快速成交’现象消失，因为买家触发‘欺诈风险’启发式（N103），导致 T_close 急剧增加或无成交。

## Corrected Claim

边界条件：噪声占比 σ_pref/μ 存在阈值效应：当该比值超过一定阈值（如 0.35）时，分布尾部极端拉长，P99 可能出现显著异常溢价，此时‘高溢价快速成交’现象消失，因为买家触发‘欺诈风险’启发式（N103），导致 T_close 急剧增加或无成交。

## Evidence

[质询]该陈述包含具体的经验性阈值（0.35）和具体的统计后果（P99 > 50%），属于经验事实而非第一性原理可推导的数学或物理定律。在缺乏外部来源支持的情况下，无法验证该特定阈值和百分比的准确性，可能存在数值量级或具体参数设定的错误。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

threshold effect high price variance buyer fraud heuristic impact on time to sell
