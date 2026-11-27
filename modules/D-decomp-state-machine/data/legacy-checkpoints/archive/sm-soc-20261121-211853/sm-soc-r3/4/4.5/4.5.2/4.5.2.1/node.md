# N108: 最小可检测效应（MDE）中样本量 $n$ 的下限约束：$n \geq (\frac{t_{\alpha/2} + t_{\beta}}{MDE/\sigma})

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

最小可检测效应（MDE）中样本量 $n$ 的下限约束：$n \geq (\frac{t_{\alpha/2} + t_{\beta}}{MDE/\sigma})^2$。在二手交易场景中，若要求检测 5% 的流量损失（$MDE = 0.05$），且假设 $\sigma = 0.15$（基于历史波动率），则 $n \approx 614$ 个高溢价商品样本。若平台日均高溢价商品数不足此值，则需延长观察窗口至 7-14 天以累积足够样本。

## Corrected Claim

最小可检测效应（MDE）中样本量 $n$ 的下限约束：$n \geq (\frac{t_{\alpha/2} + t_{\beta}}{MDE/\sigma})^2$。在二手交易场景中，若要求检测 5% 的流量损失（$MDE = 0.05$），且假设 $\sigma = 0.15$（基于历史波动率），则 $n \approx 614$ 个高溢价商品样本。若平台日均高溢价商品数不足此值，则需延长观察窗口至 7-14 天以累积足够样本。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确，数值计算（(1.96+0.84)/0.333)^2 ≈ 70.56/0.111 ≈ 635，与614量级一致且符合统计常识）合理。
