# N257: 加权系数 k 的临界值计算：当 k = k_crit 时，非补贴商品曝光占比下降 ΔE_share 恰好等于其成交周期延长导致的 GMV 损失补偿点，即 k_c

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N85

## Claim

加权系数 k 的临界值计算：当 k = k_crit 时，非补贴商品曝光占比下降 ΔE_share 恰好等于其成交周期延长导致的 GMV 损失补偿点，即 k_crit = 1 + (ΔGMV_loss_target / (N_subsidized * GMV_per_item))，用于确定平台干预的最小有效强度。

## Corrected Claim

加权系数 k 的临界值 k_crit 需通过平台具体业务模型（包含转化率、客单价等参数）求解，使得非补贴商品曝光占比下降带来的GMV损失等于预设补偿目标，具体公式依赖于业务假设，不能简单表示为 1 + (ΔGMV_loss_target / (N_subsidized * GMV_per_item))。

## Evidence

[质询]公式中的量纲和逻辑不自洽：左侧 k_crit 是无量纲系数，右侧 (ΔGMV_loss_target / (N_subsidized * GMV_per_item)) 中，分子是金额（GMV损失），分母是 数量*金额/件 = 金额，虽然量纲看似消去，但 '1 + 无量纲数' 作为临界系数缺乏明确的物理或经济推导基础，且 '曝光占比下降' 与 'GMV损失' 之间的线性补偿关系假设过于简化，未考虑转化率、客单价等中间变量，属于经验性拟合公式而非第一性原理推导。 | source=knowledge，但公式存在逻辑/量纲疑点（曝光占比与GMV损失的直接线性补偿缺乏严谨推导），且无外部来源支持该特定公式形式，故降级。
