# N296: 佣金率 r 的阶梯比例模式（前沿工作点2）：r = 2% if GMV_item < 100元; r = 4% if 100 <= GMV_item < 100

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82, N83, N84

## Claim

佣金率 r 的阶梯比例模式（前沿工作点2）：r = 2% if GMV_item < 100元; r = 4% if 100 <= GMV_item < 1000元; r = 5% if GMV_item >= 1000元。Trade-off：激励高单价交易，但计算复杂，卖家需预估佣金。量化：相比固定 3%，阶梯模式下高单价卖家感知成本增加 67% (5/3-1)，低单价卖家感知成本降低 33% (2/3-1)。

## Corrected Claim

佣金率 r 的阶梯比例模式（前沿工作点2）：r = 2% if GMV_item < 100元; r = 4% if 100 <= GMV_item < 1000元; r = 5% if GMV_item >= 1000元。Trade-off：激励高单价交易，但计算复杂，卖家需预估佣金。量化：相比固定 3%，阶梯模式下高单价卖家感知成本增加 67% (5/3-1)，低单价卖家感知成本降低 33% (2/3-1)。

## Evidence

先验知识/题面给定，逻辑校验通过：阶梯佣金定义清晰，量化计算 (5/3-1≈67%, 2/3-1≈-33%) 数学正确，Trade-off 描述符合经济直觉。

## Search Query

tiered commission structure high value items seller incentive impact
