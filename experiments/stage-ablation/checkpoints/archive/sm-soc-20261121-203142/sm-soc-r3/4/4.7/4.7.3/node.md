# N81: 收益项 B_intervention 的量化公式：B_intervention = ΔGMV * r + ΔU_buyer * WTP_buyer + ΔU_s

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

收益项 B_intervention 的量化公式：B_intervention = ΔGMV * r + ΔU_buyer * WTP_buyer + ΔU_seller * WTP_seller，其中 ΔGMV 为总成交额变化，WTP 为各方对效用提升的支付意愿；需分离短期流量红利与长期留存收益。

## Corrected Claim

收益项 B_intervention 的量化公式：B_intervention = ΔGMV * r + ΔU_buyer * WTP_buyer + ΔU_seller * WTP_seller，其中 ΔGMV 为总成交额变化，WTP 为各方对效用提升的支付意愿；需分离短期流量红利与长期留存收益。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的 ΔGMV、WTP_buyer、WTP_seller 以及 B_intervention 的短期/长期分解。各子节点定义清晰，无逻辑重叠或矛盾。虽然 B_short 和 B_long 都基于 ΔGMV 计算，但它们分别量化了父节点中‘短期流量红利’和‘长期留存收益’两个不同维度的贡献，属于必要的分解而非冗余。WTP_buyer 和 WTP_seller 虽然公式结构相似，但参数（η, R基准）和主体不同，不可合并。）

## Search Query

marketplace GMV impact of pricing algorithm optimization buyer seller welfare
