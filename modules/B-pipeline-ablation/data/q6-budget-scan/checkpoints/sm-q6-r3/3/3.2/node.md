# N27: 缓存命中率模型：H_cache = 1 - (1 / (N_objects * α_zipf))，其中N_objects为可缓存对象总数，α_zipf为Zipf

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

缓存命中率模型：H_cache = 1 - (1 / (N_objects * α_zipf))，其中N_objects为可缓存对象总数，α_zipf为Zipf参数，典型值为80-95%（热点集中）/50-80%（长尾显著）

## Corrected Claim

缓存命中率通常随可缓存对象总数 N_objects 和 Zipf 参数 α_zipf 的增加而提高，典型范围约为 80-95%（热点集中）或 50-80%（长尾显著），具体数值需结合访问分布模型计算，而非简单套用 H = 1 - 1/(N*α) 公式。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点严重偏离父节点主题（混入了无关的人力/成本节点）；且存在逻辑矛盾（公式中的α_zipf与子节点中定义的Zipf指数α混淆）；部分子节点（如不同内容类型的α值）属于同一参数的具体实例，存在冗余。）
