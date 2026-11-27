# N179: T_cold (冷启动窗口期) 的工程定义：T_cold 取决于系统预热策略，典型值为 1 小时 (0.0417 天) 或 1 分钟 (0.000694 天)，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

T_cold (冷启动窗口期) 的工程定义：T_cold 取决于系统预热策略，典型值为 1 小时 (0.0417 天) 或 1 分钟 (0.000694 天)，需根据 CDN 节点上线频率确定，若节点每日重启则 T_cold = 1 天

## Corrected Claim

T_cold (冷启动窗口期) 的工程定义：T_cold 取决于系统预热策略，典型值为 1 小时 (0.0417 天) 或 1 分钟 (0.000694 天)，需根据 CDN 节点上线频率确定，若节点每日重启则 T_cold = 1 天

## Evidence

先验知识/题面给定，逻辑校验通过：T_cold 作为工程参数确实取决于预热策略，数值量级（1小时/1分钟/1天）符合 CDN 节点重启与缓存预热的一般工程实践，无内部矛盾。
