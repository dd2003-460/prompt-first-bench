# N83: 高挂价与短成交周期并存的统一解释模型：定义‘有效搜索成本降低率’$\eta_{eff}$ 为 $\eta_{eff} = 1 - \frac{C_{search

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

高挂价与短成交周期并存的统一解释模型：定义‘有效搜索成本降低率’$\eta_{eff}$ 为 $\eta_{eff} = 1 - \frac{C_{search, high}}{C_{search, base}}$。当平台算法将高挂价作为‘高质量/高价值’的正向信号（Signal Quality $q$）时，买家的搜索成本 $C_{search}$ 降低，导致 $\eta_{eff} > 0$。根据匹配理论，成交周期 $T$ 与搜索成本成正比，即 $T \propto C_{search}$。若 $\eta_{eff} = 0.2$（搜索成本降低20%），则成交周期 $T$ 缩短 20%，足以抵消因价格弹性 $\epsilon < 1$ 导致的成交量轻微下降，从而在宏观数据上呈现‘高价+短周期’的均衡态。

## Corrected Claim

在假设平台算法将高挂价视为高质量信号且该信号能显著降低买家搜索成本的理论模型下，若搜索成本降低率η_eff为20%，则成交周期理论上缩短20%，可能在宏观上抵消价格弹性带来的成交量下降，形成‘高价+短周期’的均衡态。

## Evidence

父节点级核验失败（LLM 错误）：Invalid \escape: line 7 column 101 (char 408)

## Retrieval Sources

- {'url': 'https://github.com/WVeLong/quant-reports/blob/main/pdf/02_%E9%AB%98%E9%A2%91%E9%87%8F%E4%BB%B7%E4%B8%8E%E7%9F%AD%E5%91%A8%E6%9C%9F%E5%9B%A0%E5%AD%90/20221225-%E5%BC%80%E6%BA%90%E8%AF%81%E5%88%B8-%E5%B8%82%E5%9C%BA%E5%BE%AE%E8%A7%82%E7%BB%93%E6%9E%84%E7%A0%94%E7%A9%B6%E7%B3%BB%E5%88%97(19)_%E6%97%A5%E5%86%85%E5%88%86%E9%92%9F%E6%94%B6%E7%9B%8A%E7%8E%87%E7%9A%84%E6%97%B6%E5%BA%8F%E7%89%B9%E5%BE%81%2C%E9%80%BB%E8%BE%91%E8%AE%A8%E8%AE%BA%E4%B8%8E%E5%9B%A0%E5%AD%90%E5%A2%9E%E5%BC%BA.pdf&rut=a527144c67b0bf5354c60198d984332209885b5703253eca6571a34b303216ba', 'type': 'ddg', 'title': 'PDF quant-reports/pdf/02_高频量价与短周期因子/20221225-开源证券-市场微观结构研究系列 (19)_日内分钟收益率的 ...'}
