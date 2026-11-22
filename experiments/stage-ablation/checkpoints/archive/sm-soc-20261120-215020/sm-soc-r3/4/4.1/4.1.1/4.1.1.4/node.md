# N147: 卖家退出临界点 $\delta_{exit}$ 为惩罚后预期收益低于保留效用 $U_{reserve}$ 的偏差阈值，即 $1 - \lambda \times

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

卖家退出临界点 $\delta_{exit}$ 为惩罚后预期收益低于保留效用 $U_{reserve}$ 的偏差阈值，即 $1 - \lambda \times \delta_{exit} < U_{reserve} / P_{max}$。若 $U_{reserve} = 0.1 P_{max}$，则线性模型下 $\delta_{exit} = (1 - 0.1) / \lambda = 0.9 / 0.5 = 180\%$，表明线性模型在 25% 偏差内不会导致退出。

## Corrected Claim

卖家退出临界点 $\delta_{exit}$ 为惩罚后预期收益低于保留效用 $U_{reserve}$ 的偏差阈值，即 $1 - \lambda \times \delta_{exit} < U_{reserve} / P_{max}$。若 $U_{reserve} = 0.1 P_{max}$，则线性模型下 $\delta_{exit} = (1 - 0.1) / \lambda = 0.9 / 0.5 = 180\%$，表明线性模型在 25% 偏差内不会导致退出。

## Evidence

先验知识/题面给定，逻辑校验通过：代数推导 $\delta_{exit} = (1 - U_{reserve}/P_{max}) / \lambda$ 正确，代入数值 $0.9/0.5=1.8$ (180%) 无误，且 180% > 25% 的结论符合逻辑。
