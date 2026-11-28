# N72: 工作点B的边际收益/成本比最大化条件：当云端 API 处理的任务复杂度阈值 T_threshold 使得云端幻觉率 < 3% 且本地幻觉率 > 3% 时，切换至

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19, N20, N21

## Claim

工作点B的边际收益/成本比最大化条件：当云端 API 处理的任务复杂度阈值 T_threshold 使得云端幻觉率 < 3% 且本地幻觉率 > 3% 时，切换至云端，此时边际收益（幻觉率降低带来的研究结论可靠性提升）大于边际成本（API 费用增加），需通过 A/B 测试确定 T_threshold 的具体数值

## Corrected Claim

工作点B的边际收益/成本比最大化条件：当云端 API 处理的任务复杂度阈值 T_threshold 使得云端幻觉率显著低于本地幻觉率，且由此带来的研究结论可靠性提升（边际收益）大于 API 费用增加（边际成本）时，切换至云端；T_threshold 的具体数值需通过实验或数据分析确定。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 正交性违背：子节点1定义的T_threshold是基于线性回归的解析解，而子节点3定义的T_threshold是基于A/B测试曲线的交点（实证值），两者在方法论上存在冲突且未说明如何统一或验证一致性。2. 完备性缺失：父节点核心是“边际收益/成本比最大化”，但子节点2给出的MB公式中直接减去了总成本差，且未体现“最大化”过程（如求导或比较不同阈值的净收益），仅定义了单一阈值下的静态收益，忽略了动态优化逻辑。3. 冗余：子节点1和子节点3都旨在确定T_threshold的具体数值，属于同一目标的不同实现路径，应合并为“T_threshold的确定方法（理论推导+实证校准）”。）

## Search Query

hybrid local cloud LLM cost benefit analysis hallucination rate threshold
