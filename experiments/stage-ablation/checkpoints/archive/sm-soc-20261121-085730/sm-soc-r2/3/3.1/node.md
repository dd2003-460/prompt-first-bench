# N14: 买家驱动假说：买家通过‘高挂价=高质量’启发式减少搜索成本，其效用函数U_buyer = v - P - c_search·(1 - s)，其中s为信号强度，s

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

买家驱动假说：买家通过‘高挂价=高质量’启发式减少搜索成本，其效用函数U_buyer = v - P - c_search·(1 - s)，其中s为信号强度，s高时c_search降低，导致买家愿意接受更高P。

## Corrected Claim

买家驱动假说：买家通过‘高挂价=高质量’启发式减少搜索成本，其效用函数U_buyer = v - P - c_search·(1 - s)，其中s为信号强度，s高时c_search降低，导致买家愿意接受更高P。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一函数（P_max与s的关系）在三个不同参数点（s=0.8, 0.5, 0.2）的取值，属于高度冗余的参数化分解，而非独立的逻辑分支或机制维度。此外，父节点定义中s高时c_search降低，但子节点1中P_max = v + 0.5*c_base 的推导逻辑存疑（通常效用最大化时 P_max = v - c_search，若c_search降低，P_max应更接近v或略低于v，除非定义中v是保留价格且信号直接增加感知价值v，但父节点公式未体现v随s变化，仅体现c_search变化，导致子节点1的溢价逻辑与父节点公式推导不一致，存在内在矛盾风险）。）
