# N244: 主动等待率 P_wait 的量化构成：P_wait = P_wait_loss * P_wait_confidence，其中 P_wait_loss 由前景理论

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N79

## Claim

主动等待率 P_wait 的量化构成：P_wait = P_wait_loss * P_wait_confidence，其中 P_wait_loss 由前景理论损失厌恶系数 λ 和降价幅度 δ_cut 决定，公式为 P_wait_loss = λ * δ_cut / (λ * δ_cut + 1)；P_wait_confidence 取决于买家对'后续继续降价'的预期概率 P_further_cut，基于历史数据通常 P_further_cut ≈ 0.3。

## Corrected Claim

主动等待率 P_wait 可量化为 P_wait = P_wait_loss * P_wait_confidence。其中 P_wait_loss 通常建模为损失厌恶系数 λ 与降价幅度 δ_cut 的函数（如 P_wait_loss = λ * δ_cut / (λ * δ_cut + 1)）；P_wait_confidence 取决于买家对后续降价的预期概率 P_further_cut，该值需根据具体历史数据估算（示例中取 0.3）。

## Evidence

[质询]公式 P_wait_loss = λ * δ_cut / (λ * δ_cut + 1) 缺乏明确的经济学或心理学理论推导支持，属于特定模型假设而非通用定律；且 P_further_cut ≈ 0.3 为经验统计值，不同市场/品类差异巨大，缺乏普适性依据。 | 先验知识/题面给定，逻辑校验通过（量纲一致，概率范围合理），但具体公式形式及经验参数值缺乏通用理论或来源支持，属特定模型假设。
