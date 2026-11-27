# N84: 损失厌恶系数 λ 与锚定效应系数 k_anchor 在卖家定价决策中的交互项系数 γ，即总价格偏差 = k_anchor * Anchor + λ * (Ref

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N24

## Claim

损失厌恶系数 λ 与锚定效应系数 k_anchor 在卖家定价决策中的交互项系数 γ，即总价格偏差 = k_anchor * Anchor + λ * (Reference - Expected) + γ * (Anchor * Loss_Aversion)，需量化 γ 以解释为何两者叠加导致 15-25% 的高溢价。

## Corrected Claim

现有文献主要研究损失厌恶和锚定效应对零售商订货量的影响，尚未在卖家定价决策中量化交互项系数 γ 以解释 15-25% 的高溢价，该具体量化结论缺乏直接来源支持。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上分别处理了定义、机制与验证，正交性良好且无冗余。但完备性存在缺陷：父节点要求解释'15-25%高溢价'，而子节点3的验证显示在标准参数下溢价为30.4%，超出了观测区间，且仅建议'引入抑制项'或'下调参数'，未提供具体的修正模型或量化方法（如具体的议价能力系数公式或参数校准范围），导致未能完整闭环解释该特定溢价区间。）

## Search Query

interaction effect loss aversion anchoring pricing bias coefficient

## Retrieval Sources

- {'url': 'http://www.gyjsjj.com/CN/10.3969/j.issn.1004-910X.2019.05.001&rut=76e74fdc1197355bd2b3790100148a10a43dd905880e6f5e289c3863daefdc9d', 'type': 'ddg', 'title': '考虑损失厌恶和锚定效应的零售商订货研究 - gyjsjj.com'}
- {'url': 'https://wenku.docs.qq.com/detail?docId=V8XUuQYxFs&rut=11e0d73ba885339433e582d897608289dd782c774423bc5694c79ebceb0e2be5', 'type': 'ddg', 'title': '考虑损失厌恶和锚定效应的零售商订货研究'}
