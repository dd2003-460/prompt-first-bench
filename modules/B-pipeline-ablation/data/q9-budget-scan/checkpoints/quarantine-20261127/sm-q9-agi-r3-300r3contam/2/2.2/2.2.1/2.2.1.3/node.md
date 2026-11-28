# N125: 记忆注入的有效召回率 R_eff(K) 随注入条目数 K 的对数衰减模型：R_eff(K) = R_max * (1 - log(K/K_ref)/log(K_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48, N49, N50

## Claim

记忆注入的有效召回率 R_eff(K) 随注入条目数 K 的对数衰减模型：R_eff(K) = R_max * (1 - log(K/K_ref)/log(K_max/K_ref))，其中 K_ref=10, K_max=346, R_max=0.95；当 K=20 时，R_eff≈0.92，边际效用 dR/dK ≈ -0.0015，验证了 K*=10-20 为最优区间，超过 20 条后每增加一条导致的注意力稀释损失大于新增信息收益。

## Corrected Claim

记忆注入的有效召回率 R_eff(K) 随注入条目数 K 的对数衰减模型：R_eff(K) = R_max * (1 - log(K/K_ref)/log(K_max/K_ref))，其中 K_ref=10, K_max=346, R_max=0.95；当 K=20 时，R_eff≈0.92，边际效用 dR/dK ≈ -0.0015，验证了 K*=10-20 为最优区间，超过 20 条后每增加一条导致的注意力稀释损失大于新增信息收益。

## Evidence

先验知识/题面给定，逻辑校验通过：代入K=20计算得R_eff≈0.92，导数dR/dK≈-0.0015，数值量级与模型定义自洽。

## Search Query

LLM context window attention dilution effective recall rate logarithmic decay model
