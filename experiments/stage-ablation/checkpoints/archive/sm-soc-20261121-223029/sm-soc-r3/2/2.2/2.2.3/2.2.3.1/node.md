# N174: 固定搜索成本 C_base = 5 min/次 的时间构成分解：C_base = T_input + T_scroll + T_read_desc，其中 T_i

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

固定搜索成本 C_base = 5 min/次 的时间构成分解：C_base = T_input + T_scroll + T_read_desc，其中 T_input 为关键词输入时间（约10s），T_scroll 为结果页浏览时间，T_read_desc 为商品详情阅读时间；需基于用户行为日志计算各分项的均值，验证5分钟是否为中位数而非平均值（因长尾用户会拉高均值）。

## Corrected Claim

固定搜索成本 C_base 的时间构成分解为 C_base = T_input + T_scroll + T_read_desc。具体数值（如5分钟或10秒）及统计指标（中位数或平均值）需基于实际用户行为日志数据计算验证，不能直接断定为固定值。

## Evidence

[质询]该陈述包含具体的经验性数值（C_base=5min, T_input=10s）及特定的统计分布假设（中位数vs平均值），属于经验事实而非第一性原理可推导内容，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

user search time breakdown e-commerce mobile app median vs mean session duration
