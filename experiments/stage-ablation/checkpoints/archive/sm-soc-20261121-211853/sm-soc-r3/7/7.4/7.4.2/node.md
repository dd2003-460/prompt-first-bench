# N158: 卖家历史评分 $SellerScore$ 应作为连续变量进入回归，并检查其与 $\eta$ 的交互项 $\beta_{score} \times D_{high

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

卖家历史评分 $SellerScore$ 应作为连续变量进入回归，并检查其与 $\eta$ 的交互项 $\beta_{score} \times D_{high}$；若交互项显著为正，说明高评分卖家的高溢价信号更有效，此时单独控制 $SellerScore$ 会掩盖信号机制的异质性，需分层报告 $\eta$。

## Corrected Claim

卖家历史评分 $SellerScore$ 应作为连续变量进入回归，并检查其与 $\eta$ 的交互项 $\beta_{score} \times D_{high}$；若交互项显著为正，说明高评分卖家的高溢价信号更有效，此时单独控制 $SellerScore$ 会掩盖信号机制的异质性，需分层报告 $\eta$。

## Evidence

先验知识/题面给定，逻辑校验通过：在计量经济学中，若交互项显著，说明主效应存在异质性，单独控制主变量确实会掩盖这种异质性，分层报告是标准且正确的处理方式。
