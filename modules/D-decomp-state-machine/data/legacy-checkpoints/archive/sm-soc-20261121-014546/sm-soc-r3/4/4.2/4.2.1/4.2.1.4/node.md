# N285: 算法权重因子 W_algo：反映平台推荐算法对特定商品的曝光放大或抑制系数，若高溢价商品被算法降权，W_algo < 1，具体数值需从平台A/B测试日志或流量分

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N85

## Claim

算法权重因子 W_algo：反映平台推荐算法对特定商品的曝光放大或抑制系数，若高溢价商品被算法降权，W_algo < 1，具体数值需从平台A/B测试日志或流量分配数据中提取，假设基准值为1.0。

## Corrected Claim

算法权重因子 W_algo 用于定性反映平台推荐算法对特定商品曝光的影响方向（放大或抑制），其具体数值及基准设定依赖于特定平台的内部数据与算法策略，无法通用化假设。

## Evidence

[质询]该陈述将 W_algo 定义为具体的数值因子并假设基准值为 1.0，这属于平台内部算法的具体实现细节或经验参数，无法从第一性原理或数学公理中严格推导得出，且不同平台、不同时期的算法逻辑差异巨大，'基准值 1.0' 缺乏普适性依据。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该参数属于平台特定经验数据，不适用第一性原理推导条款）

## Search Query

platform algorithm weighting factor for high price listings exposure bias
