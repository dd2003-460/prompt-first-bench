# N373: T_threshold 的确定方法：T_threshold = T_target + 100ms 是经验值，但更严谨地应基于 P99 延迟分布的尾部风险。若 T

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N126

## Claim

T_threshold 的确定方法：T_threshold = T_target + 100ms 是经验值，但更严谨地应基于 P99 延迟分布的尾部风险。若 T_target = 100ms，则 T_threshold = 200ms。需验证在该阈值下，用户留存率是否出现断崖式下跌（如从 95% 降至 80%）。可通过历史 A/B 测试数据或行业基准（如 Google 的 200ms 阈值）进行校准。

## Corrected Claim

T_threshold 的确定方法：T_threshold = T_target + 100ms 是经验值，更严谨地应基于 P99 延迟分布的尾部风险。若 T_target = 100ms，则 T_threshold = 200ms。需验证在该阈值下，用户留存率是否出现断崖式下跌。可通过历史 A/B 测试数据或行业基准进行校准。

## Evidence

[质询]来源完全无关（图像阈值化 vs 系统延迟阈值），且'Google 200ms 阈值'作为行业基准缺乏具体出处支持，属于经验性断言。 | 参考来源[1]讨论的是OpenCV图像阈值化，与系统延迟阈值无关，无可用外部证据；该陈述为经验事实，逻辑自洽但缺来源支持。

## Search Query

optimal latency threshold for user retention mobile app 200ms

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/425181293&rut=af07e346eb315ab6eb04c65a8c3e4cbd25a2a23a92eebacf6a020771119235cc', 'type': 'ddg', 'title': 'OpenCV实战 | 一文剖析图像阈值化方法——adaptiveThreshold、 threshold、THRESH_OTSU（含公式推导）'}
