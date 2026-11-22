# N118: 买家信任度下降系数 d=0.4 的统计显著性检验：通过逻辑回归模型 logit(P(no_inquiry)) = β0 + β1*price_drop + ε 

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

买家信任度下降系数 d=0.4 的统计显著性检验：通过逻辑回归模型 logit(P(no_inquiry)) = β0 + β1*price_drop + ε 计算，若 β1 的 p-value < 0.01，则 d 显著大于0；具体需计算 t = β1 / SE(β1)，若 β1=0.4, SE=0.1，则 t=4, p<0.001，[待核验]：需实际回归数据

## Corrected Claim

买家信任度下降系数 d=0.4 的统计显著性需通过逻辑回归模型检验。若回归结果显示 β1=0.4 且标准误 SE=0.1，则 t 统计量为 4，p 值小于 0.001，表明系数显著大于 0。具体数值需基于实际回归数据确定。

## Evidence

父节点级核验未通过：不完备（子节点分别计算了标准化系数和边际效应，两者在统计意义上是不同维度的指标，因此正交且不冗余。但是，父节点的核心目标是进行“统计显著性检验”（p-value, t-test），而子节点完全偏离了这一主题，转而计算效应量（Effect Size），导致未能覆盖父节点关于假设检验的关键方面，故不完备。）

## Search Query

logistic regression for price drop and inquiry rate in second-hand platforms lemon market effect

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1939013624329909636&rut=7a55550bc471703899bc6cacb6a30c061830fc54e052a1e8bbb142a0cf647425', 'type': 'ddg', 'title': '深度解析逻辑回归分析模型 | 附详细案例操作，模型步骤，数据检验等'}
