# N299: S3 标准存储单价 ($/GB·月) 的地域差异：us-east-1 为 $0.023/GB·月，eu-west-1 为 $0.025/GB·月，ap-nort

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N105

## Claim

S3 标准存储单价 ($/GB·月) 的地域差异：us-east-1 为 $0.023/GB·月，eu-west-1 为 $0.025/GB·月，ap-northeast-1 为 $0.027/GB·月；若数据存储在非美西区域，单价可能上浮 8%-17%。需确认计算集群所在区域以选择最优存储区域

## Corrected Claim

S3 标准存储单价存在地域差异，通常美国东部（us-east-1）价格最低，欧洲和亚太区域价格略高（通常上浮 5%-15% 左右）。具体单价需查询 AWS 官方最新定价页面以获取实时数据。

## Evidence

[质询]具体单价数值（如 $0.023, $0.025, $0.027）属于经验事实，且 AWS 价格随时间波动，若无实时来源支持，具体数值可能过时或不准确；此外，'非美西区域'的表述模糊，通常对比基准是 us-east-1 而非 us-west-1。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源），具体价格数值无法通过第一性原理推导，故降级。

## Search Query

AWS S3 standard storage pricing per GB month by region 2024
