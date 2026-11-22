# N293: GMV_0 的计算口径存在 trade-off：若包含未支付订单，GMV_0 虚高约 5-10%；若仅包含已支付且未退款订单，GMV_0 更稳健但计算延迟。前沿

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82, N83, N84

## Claim

GMV_0 的计算口径存在 trade-off：若包含未支付订单，GMV_0 虚高约 5-10%；若仅包含已支付且未退款订单，GMV_0 更稳健但计算延迟。前沿工作点2：GMV_0 = Σ(已支付且 T_refund_window 内未退款订单金额)，其中 T_refund_window 通常为 7 天。此口径下 GMV_0 比‘下单口径’低约 7.5% (假设退款率 7.5%)。

## Corrected Claim

GMV_0 的计算口径存在 trade-off：若包含未支付订单，GMV_0 虚高约 5-10%；若仅包含已支付且未退款订单，GMV_0 更稳健但计算延迟。前沿工作点2：GMV_0 = Σ(已支付且 T_refund_window 内未退款订单金额)，其中 T_refund_window 通常为 7 天。此口径下 GMV_0 比‘下单口径’低约 7.5% (假设退款率 7.5%)。

## Evidence

先验知识/题面给定，逻辑校验通过：GMV口径定义符合电商业务常识，7.5%的退款率假设与7.5%的GMV差异在数学上自洽（假设无其他损耗），且属于knowledge范畴，无需外部来源支持。

## Search Query

GMV definition paid vs ordered refund window impact on baseline value
