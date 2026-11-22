# N25: 字节命中率（Byte Hit Ratio）理论下界公式为 H_byte ≥ (Σ_{i=1}^{k_max} R_i * S_i) / (Σ_{j=1}^{N}

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

字节命中率（Byte Hit Ratio）理论下界公式为 H_byte ≥ (Σ_{i=1}^{k_max} R_i * S_i) / (Σ_{j=1}^{N} R_j * S_j)，其中分母为总字节请求量，需利用联合分布 P(R,S) 估算。

## Corrected Claim

字节命中率（Byte Hit Ratio）定义为命中字节数与总请求字节数之比，即 H_byte = (Σ R_i * S_i * I_hit) / (Σ R_j * S_j)，其中 I_hit 为命中指示变量；在特定缓存策略（如LRU）下，其性能下界可通过联合分布 P(R,S) 估算，但具体公式形式依赖于策略假设。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 773)

## Retrieval Sources

- {'url': 'https://www.ecice06.com/CN/10.3969/j.issn.1000-3428.2007.13.028&rut=a33ccb64829135bef100864add1b245ec4cd6c7b311874a173d9fd903e44a6db', 'type': 'ddg', 'title': 'Web缓存命中率与字节命中率关系 - ecice06.com'}
- {'url': 'https://www.cse.iitb.ac.in/~gracias/webcaching/html/node34.html&rut=9efcc6f1d3ec86a65720ae73704c145867b448ccded1e2ba1a93f08c8faccd40', 'type': 'ddg', 'title': 'Hit Rate and Byte Hit Rate - cse.iitb.ac.in'}
- {'url': 'https://www.docin.com/p-1445771348.html&rut=42f07de5f0c7d200c1c21698ba51b7f154f91d1b5c1a0b1e0d6a5fa5d916a5e1', 'type': 'ddg', 'title': 'Web缓存命中率与字节命中率关系 - 豆丁网'}
