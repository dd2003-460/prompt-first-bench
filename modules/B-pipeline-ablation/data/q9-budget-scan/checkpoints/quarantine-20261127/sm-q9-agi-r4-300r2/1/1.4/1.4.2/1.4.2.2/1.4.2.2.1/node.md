# N265: 在 H_shift=0.5 nats 且 η=0.60 的工作点下，MTP×4 的接受率衰减曲线需满足 AcceptanceRate(step_k) > Thr

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N106

## Claim

在 H_shift=0.5 nats 且 η=0.60 的工作点下，MTP×4 的接受率衰减曲线需满足 AcceptanceRate(step_k) > Threshold_min (建议 0.85)，否则投机解码的有效加速比 S_eff 将低于 2.0；当前 vLLM 配置下，需监控第 4 步 MTP 的接受率，若连续 100 个请求平均接受率 < 0.80，则触发降级至 MTP×2。

## Corrected Claim

在 H_shift=0.5 nats 且 η=0.60 的工作点下，MTP×4 的接受率衰减需保持在较高水平（如建议阈值 0.85 以上）以维持有效加速比 S_eff ≥ 2.0；在特定 vLLM 配置中，若监控到第 4 步 MTP 的连续 100 个请求平均接受率低于 0.80，通常建议触发降级至 MTP×2 以平衡延迟与吞吐。

## Evidence

[质询]该陈述包含具体的工程阈值（H_shift=0.5 nats, η=0.60, Threshold_min=0.85, S_eff<2.0, 连续100请求<0.80触发降级），这些属于特定系统配置下的经验参数或启发式规则，并非从第一性原理或通用数学公理可直接推导出的必然真理。不同模型、硬件及负载条件下，最优阈值可能显著不同，缺乏普适性证明。 | source=knowledge，逻辑自洽（接受率下降导致加速比降低符合投机解码基本原理），但具体数值阈值属于经验事实，无外部来源支持且非第一性原理可严格推导，故降级。

## Search Query

vLLM multi-token prediction acceptance rate threshold degradation strategy
