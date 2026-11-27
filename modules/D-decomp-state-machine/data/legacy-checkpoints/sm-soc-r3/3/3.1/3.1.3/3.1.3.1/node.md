# N184: 等待成本 C_wait 在‘降价触发观望’工作点下的量化：C_wait(t) = C_wait_base × (1 + η_drop × I_drop)，其中 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

等待成本 C_wait 在‘降价触发观望’工作点下的量化：C_wait(t) = C_wait_base × (1 + η_drop × I_drop)，其中 C_wait_base 为基准等待容忍时间（如 48h），η_drop ≈ 0.4（基于题面 60% 无咨询推断），I_drop=1 时 C_wait 增加 40%，意味着买家预期卖家会继续降价，从而将决策窗口从 48h 延长至 67.2h，导致即时咨询率下降至基线的 60%。

## Corrected Claim

等待成本 C_wait 在‘降价触发观望’工作点下的量化：C_wait(t) = C_wait_base × (1 + η_drop × I_drop)，其中 C_wait_base 为基准等待容忍时间（如 48h），η_drop ≈ 0.4（基于题面 60% 无咨询推断），I_drop=1 时 C_wait 增加 40%，意味着买家预期卖家会继续降价，从而将决策窗口从 48h 延长至 67.2h，导致即时咨询率下降至基线的 60%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导 48h * (1 + 0.4) = 67.2h 数学自洽，且与题面设定的 60% 基线及 40% 增量逻辑一致。

## Search Query

price drop signaling effect buyer wait time secondhand goods
