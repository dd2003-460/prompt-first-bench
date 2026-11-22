# N31: 基准价 $P_{avg}$ 的计算窗口与偏差修正：若采用过去30天成交均价，需引入通胀/季节性修正因子 $\beta$，即 $P_{avg} = \frac{1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

基准价 $P_{avg}$ 的计算窗口与偏差修正：若采用过去30天成交均价，需引入通胀/季节性修正因子 $\beta$，即 $P_{avg} = \frac{1}{N}\sum P_{deal,i} \times \beta$；若 $\beta$ 偏差超过 5%，惩罚项将产生系统性误判，导致正常卖家被错误降权。

## Corrected Claim

基准价 $P_{avg}$ 的计算窗口与偏差修正：若采用过去30天成交均价，需引入通胀/季节性修正因子 $\beta$，即 $P_{avg} = \frac{1}{N}\sum P_{deal,i} \times \beta$；若 $\beta$ 偏差超过 5%，惩罚项将产生系统性误判，导致正常卖家被错误降权。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别处理了季节性修正、通胀修正、小样本统计偏差以及最终对惩罚项的影响量化，四个维度（时间周期性、宏观经济、统计显著性、结果影响）互不重叠且逻辑独立，共同构成了对父节点中'计算窗口与偏差修正'的完整覆盖。）

## Search Query

dynamic pricing baseline calculation window seasonality correction
