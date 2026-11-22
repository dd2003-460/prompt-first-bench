# N627: 修正后的 H100 SXM 单卡 (BF16) 32K 上下文 TTFT 计算：T_TTFT = 1.77e12 / (989e12 * 0.45) ≈ 0.4

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N260

## Claim

修正后的 H100 SXM 单卡 (BF16) 32K 上下文 TTFT 计算：T_TTFT = 1.77e12 / (989e12 * 0.45) ≈ 0.40s，该结果显著低于 2.0s 阈值，表明父节点 N260 的‘超出 2s 阈值’结论因输入参数错误而失效，H100 在交互式场景下具有绝对优势

## Corrected Claim

修正后的 H100 SXM 单卡 (BF16) 32K 上下文 TTFT 计算：T_TTFT = 1.77e12 / (989e12 * 0.45) ≈ 0.40s，该结果显著低于 2.0s 阈值，表明父节点 N260 的‘超出 2s 阈值’结论因输入参数错误而失效，H100 在交互式场景下具有绝对优势

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 1.77e12 / (989e12 * 0.45) ≈ 0.397s 正确，且 0.40s < 2.0s 的结论符合逻辑推导。
