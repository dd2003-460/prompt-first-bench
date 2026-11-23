# N14: 自建 POP 点的硬件折旧成本 $C_{hw}$ 按服务器生命周期（通常 3-5 年）直线折旧计算：$C_{hw} = N_{servers} \times C

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

自建 POP 点的硬件折旧成本 $C_{hw}$ 按服务器生命周期（通常 3-5 年）直线折旧计算：$C_{hw} = N_{servers} \times C_{server} / T_{life}$，其中 $N_{servers}$ 为每个 POP 点所需服务器数量，$C_{server}$ 为单台服务器采购成本（约 5-10 万元/台），$T_{life}$ 为折旧年限（36 个月）。

## Corrected Claim

自建 POP 点的硬件折旧成本 $C_{hw}$ 按服务器生命周期（通常 3-5 年）直线折旧计算：$C_{hw} = N_{servers} \times C_{server} / T_{life}$，其中 $N_{servers}$ 为每个 POP 点所需服务器数量，$C_{server}$ 为单台服务器采购成本（约 5-10 万元/台），$T_{life}$ 为折旧年限（36 个月）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的三个独立变量 $N_{servers}$、$C_{server}$ 和 $T_{life}$，彼此正交无重复；三者共同完整覆盖了计算硬件折旧成本所需的全部关键参数；各子节点提供了具体的取值范围或典型配置，属于参数定义而非冗余重复。）

## Search Query

data center server depreciation cost calculation 3 year
