# N148: Pareto(β=0.9)热度分布的截断上限 P_max 的确定依据：P_max 对应总请求量5000万次/天在有限对象数N=10万下的最大单对象请求频率，需通

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N49, N50, N51

## Claim

Pareto(β=0.9)热度分布的截断上限 P_max 的确定依据：P_max 对应总请求量5000万次/天在有限对象数N=10万下的最大单对象请求频率，需通过归一化约束 Sum(f_i)=1 反解 P_max 或设定最小频率截断 P_min

## Corrected Claim

Pareto(β=0.9)热度分布的截断上限 P_max 由分布参数和对象总数 N=10万 决定，对应排名最靠前的对象请求频率；总请求量 5000万次/天 用于确定分布的尺度参数（归一化），而非直接反解 P_max；P_min 通常作为长尾截断阈值独立设定。

## Evidence

[质询]该陈述将P_max的确定依据描述为“需通过归一化约束反解”或“设定最小频率截断”，这在方法论上存在混淆。在Pareto分布中，P_max通常由分布参数（如α）和对象总数N直接决定（即第1名对象的频率），而非通过“归一化约束反解”（归一化用于确定分布的尺度参数，而非截断上限本身）；且“设定最小频率截断P_min”是处理长尾噪声的手段，与确定最大频率P_max的逻辑方向相反，二者并非并列的“确定依据”。 | 经验事实/工程参数，逻辑自洽但缺来源支持；检索无可用来源，且陈述中关于P_max确定方法的描述存在方法论上的不严谨（混淆了归一化参数估计与截断上限定义），故降级。

## Search Query

Pareto distribution truncation boundary for finite population frequency normalization
