# N15: 当边界条件从'恒定温差'转变为'恒定热源功率'时，系统达到新的稳态所需的时间常数（Thermal Time Constant）与热容及热阻乘积相关，即 τ = 

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

当边界条件从'恒定温差'转变为'恒定热源功率'时，系统达到新的稳态所需的时间常数（Thermal Time Constant）与热容及热阻乘积相关，即 τ = R_th * C_th，其中 R_th = d/(k*A)。

## Corrected Claim

当边界条件从'恒定温差'转变为'恒定热源功率'时，系统达到新的稳态所需的时间常数（Thermal Time Constant）与热容及热阻乘积相关，即 τ = R_th * C_th，其中 R_th = d/(k*A)。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应热容公式推导、具体物性代入、基于错误参数的计算、基于真实参数的计算及对比，逻辑层次清晰且互不重叠，完整覆盖了父节点中关于时间常数计算及其对参数敏感性的所有关键方面。）

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/710541148&rut=6fdf9df6b1163381253f8b87a04dc4716a36278c40392739ccd55b459ee319d7', 'type': 'ddg', 'title': '一篇文章带你看穿传热的底层秘密---热传导方程及其求解方法'}
- {'url': 'https://zhuanlan.zhihu.com/p/2092613441622120109&rut=509f1bbadfd939601309d8c63be02b76360f1f597b2e3e96148023217de404a5', 'type': 'ddg', 'title': 'Fluent稳态与瞬态的选择依据 - 知乎'}
