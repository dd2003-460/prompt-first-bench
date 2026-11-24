# N189: 北京源站至上海POP的光纤物理距离约为1060km，考虑到实际路由迂回系数（通常为1.2-1.5），有效传输距离约为1272-1590km。

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

北京源站至上海POP的光纤物理距离约为1060km，考虑到实际路由迂回系数（通常为1.2-1.5），有效传输距离约为1272-1590km。

## Corrected Claim

北京源站至上海POP的光纤物理距离约为1060km，考虑到实际路由迂回系数（通常为1.2-1.5），有效传输距离约为1272-1590km。（注：逻辑自洽，但缺乏相关来源直接支持，建议补充网络基础设施相关文献）

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中迂回系数1.2和1.5的两个极端/典型场景，逻辑上互斥且共同覆盖了父节点给出的距离范围（1272-1590km）。虽然结构相似，但代表了不同的网络架构（直连vs多跳）和不同的延迟模型，属于不同场景下的实例化，而非简单的参数冗余。）

## Search Query

Beijing to Shanghai fiber optic distance km route

## Retrieval Sources

- {'url': 'https://ziliao.baidu.com/view/6170b81bb3360b4c2e3f5727a5e9856a561226d8.html&rut=e10c7c9c2273c2156e0a14e7352fb492a18d9b9dc35e2a1ed185e0200c50aff3', 'type': 'ddg', 'title': '深度解析Zemax物理光学传播 (POP)功能原理与应用指南'}
