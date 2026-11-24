# N237: 长尾区域月请求数 Tail_Monthly_Requests = DAU × Tail_User_Ratio × Avg_Requests_Per_User ×

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

长尾区域月请求数 Tail_Monthly_Requests = DAU × Tail_User_Ratio × Avg_Requests_Per_User × 30，其中 Tail_User_Ratio 为混合方案中长尾区域用户占比（通常 30%-50%），Avg_Requests_Per_User 为日均人均请求数（同 N145），需代入具体数值计算分母。

## Corrected Claim

长尾区域月请求数 Tail_Monthly_Requests = DAU × Tail_User_Ratio × Avg_Requests_Per_User × 30，其中 Tail_User_Ratio 为混合方案中长尾区域用户占比（通常 30%-50%），Avg_Requests_Per_User 为日均人均请求数（同 N145），需代入具体数值计算分母。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点存在严重的维度混淆和命名冲突：前三个子节点属于‘运维成本（Ops Cost）’维度，而第四个子节点属于‘流量负载（Traffic Volume）’维度，两者物理量纲不同，无法作为同一父节点下的并列子项。此外，前三个子节点实质上是同一‘运维配置参数’的三个不同工作点（取值），而非独立的正交概念。第四个子节点命名重复且仅覆盖了一个特定场景，未涵盖父节点公式中其他变量（如DAU变化）的影响。）

## Search Query

CDN tail traffic long tail users request distribution geographic distribution
