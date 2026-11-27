# N225: 量化情境随机噪声 σ_context 的方差贡献：定义 σ_context 为情绪、时间紧迫等情境因素引起的噪声，假设其贡献总方差的 30%，即 Var(σ_c

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N84

## Claim

量化情境随机噪声 σ_context 的方差贡献：定义 σ_context 为情绪、时间紧迫等情境因素引起的噪声，假设其贡献总方差的 30%，即 Var(σ_context) = 0.3 * Var(σ_noise_total)，需通过情境实验或自然实验数据估计其具体数值。

## Corrected Claim

量化情境随机噪声 σ_context 的方差贡献：定义 σ_context 为情绪、时间紧迫等情境因素引起的噪声，其具体方差贡献比例（如假设的30%）需通过情境实验或自然实验数据估计，而非固定常数。

## Evidence

[质询]该陈述中的具体数值（30%）属于经验性假设，缺乏普遍适用的理论依据或标准数据支持，且参考来源未提供相关证据，存在将特定情境下的假设泛化为通用定义的风险。 | 逻辑上方差分解自洽，但参考来源[1]仅讨论量化噪声的功率计算原理，与情境噪声的具体方差贡献比例无关，属于经验事实且缺来源支持。

## Search Query

situational noise buyer behavior variance context effects

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1888571409996961345&rut=bf6bb7a9f727f7307ff775b1a08873fdf323de4184c9ed88c3b14f58494da6ac', 'type': 'ddg', 'title': '量化噪声（均匀量化）功率为什么用方差计算？ - 知乎'}
