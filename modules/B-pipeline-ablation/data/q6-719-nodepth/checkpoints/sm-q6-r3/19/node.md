# N428: P99 延迟约束下的缓存预热时间 T_warmup 要求：为确保冷启动期间 P99 不超标，需在流量高峰前 24-48 小时完成热门对象预热。预热带宽需求 = 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

P99 延迟约束下的缓存预热时间 T_warmup 要求：为确保冷启动期间 P99 不超标，需在流量高峰前 24-48 小时完成热门对象预热。预热带宽需求 = (Hot_Object_Size × (1 - Hit_Rate_cold)) / T_warmup，若 Hot_Object_Size = 10TB, Hit_Rate_cold = 0, T_warmup = 24h，则需 416 Mbps 预热带宽，需预留独立预热通道或低优先级带宽。

## Corrected Claim

P99 延迟约束下的缓存预热时间 T_warmup 要求：为确保冷启动期间 P99 不超标，需在流量高峰前 24-48 小时完成热门对象预热。预热带宽需求 = (Hot_Object_Size × (1 - Hit_Rate_cold)) / T_warmup，若 Hot_Object_Size = 10TB, Hit_Rate_cold = 0, T_warmup = 24h，则需约 4.17 Gbps 预热带宽，需预留独立预热通道或低优先级带宽。

## Evidence

[质询]数值计算存在量级错误：10TB数据在24小时内传输所需的带宽约为4.17 Gbps，而非416 Mbps（相差10倍）；且参考来源讨论的是LLM推理服务的冷启动（毫秒/秒级），与TB级对象存储预热（小时级）场景不匹配。 | 逻辑校验发现带宽计算错误（10TB/24h ≈ 4.17 Gbps ≠ 416 Mbps），且来源[1]主题为vLLM推理延迟，与TB级缓存预热带宽需求无关，无法支持该具体数值结论。

## Retrieval Sources

- {'url': 'https://deepseek.csdn.net/6a16494a10ee7a33f275706f.html&rut=5c93c669e0c7bc36824e249d472de0f1a704dc0bebb580b52fba4a404e3a87d4', 'type': 'ddg', 'title': 'vLLM 部署 DeepSeek 时 P99 延迟突增：压测未覆盖的冷启动与预热策略'}
