# N92: 电力消耗中的'运行小时' (Annual_Hours) 需根据使用场景定义：本地工作站典型负载为 8-12 小时/天 (365-546 小时/年)，而数据中心推

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

电力消耗中的'运行小时' (Annual_Hours) 需根据使用场景定义：本地工作站典型负载为 8-12 小时/天 (365-546 小时/年)，而数据中心推理服务器为 24/7 运行 (8760 小时/年)；不同利用率场景下的年运行小时数直接决定电力成本占比。

## Corrected Claim

电力消耗中的'运行小时' (Annual_Hours) 需根据使用场景定义：本地工作站典型负载为 8-12 小时/天 (365-546 小时/年)，而数据中心推理服务器为 24/7 运行 (8760 小时/年)；不同利用率场景下的年运行小时数直接决定电力成本占比。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点仅覆盖了父节点中提及的'本地工作站'和'数据中心'两个极端场景，缺失了父节点明确提到的典型负载范围（8-12小时/天）的具体计算；同时，两个子节点本质上是同一计算公式在不同输入参数（运行小时数）下的实例化，属于参数化冗余而非结构性分解。）

## Search Query

typical annual operating hours local workstation vs data center inference server
