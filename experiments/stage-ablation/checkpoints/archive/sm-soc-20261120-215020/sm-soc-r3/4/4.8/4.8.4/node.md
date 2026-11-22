# N73: 最小干预参数 $\lambda$ 与偏差区间 $\delta$ 的耦合关系：$\lambda_{min} = \frac{1}{\delta_{max}}$ 或

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N24

## Claim

最小干预参数 $\lambda$ 与偏差区间 $\delta$ 的耦合关系：$\lambda_{min} = \frac{1}{\delta_{max}}$ 或类似归一化公式，需验证当 $\delta_{max}$ 从 20% 降至 15% 时，$\lambda$ 从 0.5 增至 0.6 的逻辑是否成立（若 $\lambda=1/\delta$，则 $1/0.2=5$ vs $1/0.15=6.67$，与题面 0.5->0.6 不符，需澄清 $\lambda$ 的具体定义域和量纲）。

## Corrected Claim

最小干预参数 λ 与偏差区间 δ 的耦合关系需明确具体定义域和归一化系数；若采用简单倒数关系 λ=1/δ，则与题面数值不符，需进一步澄清模型设定。

## Evidence

[质询]陈述中提出的公式 λ_min = 1/δ_max 与题面数值（0.5->0.6）存在量级矛盾（5 vs 6.67），且参考来源完全无关，无法验证该耦合关系的具体定义域或归一化系数，属于缺乏来源支持的经验/模型参数假设。 | 参考来源[1]讨论孟德尔随机化，[2]讨论GNSS模糊度固定，均与最小干预参数λ及偏差区间δ的耦合关系无关，无可用外部证据；逻辑上陈述自身指出了公式与数值的矛盾并请求澄清，逻辑自洽但缺乏事实支撑。

## Search Query

platform algorithm penalty coefficient lambda price deviation normalization formula marketplace design

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/604939175&rut=ff900eb96b15b7cec2c4620819d2abd55219362e71b5fc5025a37128e324790b', 'type': 'ddg', 'title': 'R数据分析：孟德尔随机化中介的原理和实操二 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/618240953&rut=2f99d6c57635e33d8e31f795a72a6f2dc18afe00c4e784cf87ced6ea4ffec0f3', 'type': 'ddg', 'title': '【Gnss】Lambda 模糊度固定方法 - 知乎'}
