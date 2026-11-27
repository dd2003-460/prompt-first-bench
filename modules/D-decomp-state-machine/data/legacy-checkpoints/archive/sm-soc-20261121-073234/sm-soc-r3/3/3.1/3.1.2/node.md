# N64: 价格合理性指标计算式：R_i = P_list_i / P_median_30d_i，其中 P_median_30d_i 为商品i所属类目过去30天成交中位数

- **status**: pending
- **level**: L3
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N18

## Claim

价格合理性指标计算式：R_i = P_list_i / P_median_30d_i，其中 P_median_30d_i 为商品i所属类目过去30天成交中位数

## Corrected Claim

价格合理性指标计算式：R_i = P_list_i / P_median_30d_i，其中 P_median_30d_i 为商品i所属类目过去30天成交中位数

## Evidence

父节点级核验未通过：不完备（子节点在正交性上表现良好，分别针对数据清洗（基准线质量）、粒度选择（类目定义）和时间窗口（季节性）三个不同维度进行分解，无重叠或矛盾。但在完备性上存在缺失：父节点定义了一个比率指标 R_i，除了分母 P_median 的构建外，分子 P_list_i（列表价/标价）的获取逻辑、有效性校验（如是否为空、是否为0、是否为促销价而非原价）也是计算该指标的关键环节，当前子节点未覆盖分子部分的定义与清洗规则。）
