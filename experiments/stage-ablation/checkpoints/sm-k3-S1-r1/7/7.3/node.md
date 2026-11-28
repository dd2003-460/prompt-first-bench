# N37: MTP×4 投机解码在 V100 架构上的接受率（Acceptance Rate）R 与加速比 Speedup S 的非线性关系：S = R / (1 - R)

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

MTP×4 投机解码在 V100 架构上的接受率（Acceptance Rate）R 与加速比 Speedup S 的非线性关系：S = R / (1 - R) * (T_draft/T_target)，由于 V100 缺乏 FP8/FP4 快速草稿模型支持，草稿阶段可能回退至 FP16，导致 T_draft 增加，需实测 R 值（通常 Qwen3 系列在科研文本上 R≈0.6-0.8），以确定实际吞吐增益是否足以补偿硬件劣势。

## Corrected Claim

MTP×4 投机解码在 V100 架构上的加速比 S 取决于接受率 R、草稿长度 K 以及草稿与目标模型的推理耗时比。由于 V100 缺乏 FP8/FP4 支持，草稿阶段回退至 FP16 会增加 T_draft，从而降低潜在加速比。加速比并非由 S = R / (1 - R) * (T_draft/T_target) 决定，而是受限于最大草稿长度和实际接受长度。需实测 R 值（Qwen3 系列在科研文本上 R≈0.6-0.8）以评估实际吞吐增益。

## Evidence

[质询]公式 S = R / (1 - R) * (T_draft/T_target) 存在严重的量纲和逻辑错误。在投机解码中，加速比通常定义为理想情况下的最大加速倍数（约等于 K+1，其中K为草稿长度）乘以接受率带来的有效收益，或者更准确地说是 Target 生成一个 token 的时间除以 Speculative 生成一个 token 的平均时间。给定的公式结构混乱：如果 R 是接受率，(1-R) 在分母意味着随着接受率提高，加速比趋向无穷大，这不符合物理直觉（加速比有上限，取决于草稿模型速度比和最大草稿长度）。此外，T_draft/T_target 通常远小于 1（因为草稿模型小且快），将其乘以一个随 R 增大而增大的项，无法正确反映“接受率高则加速比高”的基本规律，且未包含草稿长度 K 这一关键变量。正确的近似公式通常涉及 (1 - R^(K+1)) / ((1-R) * (T_draft + T_target)) 之类的结构，或者简化为基于期望接受长度的计算。该公式本身是错误的。 | 逻辑校验失败：提供的加速比公式 S = R / (1 - R) * (T_draft/T_target) 在数学和物理直觉上均不成立（量纲错误，未包含草稿长度 K，且极限行为异常）。虽然 V100 不支持 FP8 导致 T_draft 增加的定性描述是合理的，但核心定量关系错误。由于 source 为 search 且无可用来源，且存在硬逻辑错误（公式错误），根据规则应判 failed 或 degraded。鉴于公式错误是硬伤，但定性部分（V100 限制、需实测）尚可保留，故降级并修正。

## Search Query

Multi-Token Prediction speculative decoding acceptance rate V100 GPU vLLM Qwen3 speedup factor
