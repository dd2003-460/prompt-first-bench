# N81: 在演化博弈模型中，定义卖家的‘锚定偏差’参数 $\delta_{anchor}$ 为 $\delta_{anchor} = \frac{P_{list} - P

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在演化博弈模型中，定义卖家的‘锚定偏差’参数 $\delta_{anchor}$ 为 $\delta_{anchor} = \frac{P_{list} - P_{market}}{P_{market}}$。基于 Kahneman 的损失厌恶理论，当 $\delta_{anchor} > 0$ 时，卖家的保留效用 $U_{seller}$ 中包含心理惩罚项 $-\lambda_{loss} \times (P_{anchor} - P_{list})^2$，其中 $\lambda_{loss} \approx 2.25$。该非线性惩罚导致即使市场成交价 $P_{market}$ 上涨，卖家仍倾向于维持高挂价 $P_{list}$ 以规避心理损失，从而在微观层面支撑了 15-25% 的高溢价现象。

## Corrected Claim

在演化博弈模型中，可定义卖家的‘锚定偏差’参数 δ_anchor = (P_list - P_market) / P_market。基于 Kahneman 的损失厌恶理论，当 δ_anchor > 0 时，卖家的保留效用 U_seller 中可引入心理惩罚项以反映损失厌恶效应（具体形式如 -λ_loss × (P_anchor - P_list)^2 及参数 λ_loss ≈ 2.25 为模型特定假设）。该机制在微观层面解释了卖家维持高挂价的行为，从而可能支撑一定比例的高溢价现象（具体比例如15-25%需依赖实证数据或特定模型校准）。

## Evidence

父节点级核验未通过：不完备（子节点1聚焦于微观个体的心理效用阈值与调整成本（微观机制），子节点2聚焦于宏观演化稳定策略的适应度比较（宏观动态）。两者在逻辑层面是正交的，分别解释了“为什么个体不调整”和“为什么该策略在群体中稳定”。然而，父节点中明确提到的“锚定偏差参数定义”（$\delta_{anchor}$ 的公式）未被任何子节点显式覆盖或作为基础变量深入探讨，导致对父节点中“参数定义”这一关键方面的遗漏。）

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1198348613&rut=558355e0814074b9c027fcf5b79128546735b0eec3521f89f15cdb2a863b90cc', 'type': 'ddg', 'title': '有关演化博弈模型该如何进行参数设置与赋值的简要回答 - 知乎'}
- {'url': 'https://baike.baidu.com/item/%E9%94%9A%E5%AE%9A%E5%81%8F%E8%A7%81/64842200&rut=519529248641f0f132e6ba6fc3f4b32b4c68072138966b0c6551932e9edd94ee', 'type': 'ddg', 'title': '锚定偏见_百度百科'}
