# N77: 算法屏蔽机制的量化假设：若平台算法对'降价后商品'施加曝光权重衰减因子 w_decay，则实际曝光量 E_exposure = E_base * w_decay

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

算法屏蔽机制的量化假设：若平台算法对'降价后商品'施加曝光权重衰减因子 w_decay，则实际曝光量 E_exposure = E_base * w_decay * (1 - t/T_decay)^δ。若 60% 无咨询是由曝光量降至基准的 15% 导致，则 w_decay ≈ 0.15 (假设咨询率与曝光量线性相关)，该参数可通过 A/B 测试中曝光日志与咨询率的回归系数估计。

## Corrected Claim

算法屏蔽机制的量化假设：若平台算法对'降价后商品'施加曝光权重衰减因子 w_decay，则实际曝光量 E_exposure = E_base * w_decay * (1 - t/T_decay)^δ。若 60% 无咨询是由曝光量降至基准的 15% 导致，则 w_decay ≈ 0.15 (假设咨询率与曝光量线性相关)，该参数可通过 A/B 测试中曝光日志与咨询率的回归系数估计。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

algorithm exposure decay factor price reduction marketplace A/B test
