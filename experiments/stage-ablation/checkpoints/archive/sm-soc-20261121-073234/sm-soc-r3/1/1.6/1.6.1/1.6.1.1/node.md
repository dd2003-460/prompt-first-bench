# N151: 二手市场信息透明度系数 ρ_info 的估算：ρ_info = 1 - (σ_price_uninformed / σ_price_total)，需验证 ρ_i

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N45

## Claim

二手市场信息透明度系数 ρ_info 的估算：ρ_info = 1 - (σ_price_uninformed / σ_price_total)，需验证 ρ_info < 0.5，即信息不对称导致的噪声占比超过 50%，基于平台公开描述完整度与成交价离散度计算。

## Corrected Claim

二手市场信息透明度系数 ρ_info 的估算需基于更严谨的计量模型（如使用描述完整度作为工具变量或构建代理指标），而非直接通过价格标准差的简单线性组合计算；当前公式缺乏理论依据和实证支持。

## Evidence

[质询]该公式 ρ_info = 1 - (σ_price_uninformed / σ_price_total) 在逻辑上存在严重缺陷：通常信息不对称（噪声）越大，价格离散度（σ_total）应越大，而非越小；且 σ_uninformed 是理论构造变量，无法直接从“平台公开描述完整度”和“成交价离散度”这两个可观测指标中直接计算得出，缺乏明确的实证映射关系。 | 参考来源[1]讨论的是上市公司KV指数（会计信息透明度），与二手市场价格离散度及该特定公式无关，无外部支持；且公式本身将信息不对称占比定义为噪声标准差与总标准差之差的补数，缺乏经济学直觉支撑（通常噪声占比高意味着总波动大，而非该公式暗示的关系），属于经验事实且逻辑存疑。

## Search Query

information transparency coefficient second hand market price dispersion

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/622092947&rut=7af665a42d649abc8b1cf4f06909131ca30405b9a011d2b41596d16222fa5340', 'type': 'ddg', 'title': 'Stata学习：如何构建企业信息透明度变量？ - 知乎'}
