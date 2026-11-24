# N337: 公有云CDN冷启动延迟的量化分解：T_cold_start = T_connection_establishment + T_resource_scheduli

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N118

## Claim

公有云CDN冷启动延迟的量化分解：T_cold_start = T_connection_establishment + T_resource_scheduling + T_cache_warming，其中 T_connection_establishment（TCP/TLS握手）约为 100-300ms，T_resource_scheduling（实例启动）约为 3-10s，T_cache_warming（缓存预热）约为 5-15s，总延迟范围为 5-15s。

## Corrected Claim

公有云CDN冷启动延迟的量化分解：T_cold_start = T_connection_establishment + T_resource_scheduling + T_cache_warming，其中 T_connection_establishment（TCP/TLS握手）约为 100-300ms，T_resource_scheduling（实例启动）约为 3-10s，T_cache_warming（缓存预热）约为 5-15s，总延迟范围约为 8-25s（具体数值依架构和预热策略而异）。

## Evidence

[质询]数值量级与具体参数缺乏通用标准支持，不同云厂商、CDN架构（如边缘节点预热策略、连接复用机制）差异巨大，'100-300ms'握手和'3-10s'实例启动属于特定场景下的经验估计，而非普适物理或工程常数；此外，总延迟范围5-15s与分项之和（最小100ms+3s+5s≈8s，最大300ms+10s+15s≈25s）存在逻辑不一致，最小值计算错误（应为~8s而非5s）。 | 逻辑校验发现内部矛盾：分项最小值之和约为8s（0.1s+3s+5s），但陈述总延迟最小值为5s，存在明显算术错误；且作为knowledge节点，虽无需外部来源，但数值分解缺乏严谨推导，属于经验估计且存在计算瑕疵，故降级。
