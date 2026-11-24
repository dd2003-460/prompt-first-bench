# N740: N254 激进工作点依赖公有云弹性扩容的冷启动延迟 T_cold_start 量化为 DNS 解析更新延迟 (30-60s) + 缓存预热时间 (Object_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N254

## Claim

N254 激进工作点依赖公有云弹性扩容的冷启动延迟 T_cold_start 量化为 DNS 解析更新延迟 (30-60s) + 缓存预热时间 (Object_Size / Warmup_Bandwidth)，若未预热，首请求延迟 = T_origin + T_transfer_from_origin

## Corrected Claim

N254 激进工作点依赖公有云弹性扩容的冷启动延迟 T_cold_start 量化为 DNS 解析更新延迟 (30-60s) + 缓存预热时间 (Object_Size / Warmup_Bandwidth)，若未预热，首请求延迟 = T_origin + T_transfer_from_origin

## Evidence

先验知识/题面给定，逻辑校验通过：冷启动延迟由DNS解析（秒级）和缓存预热（传输时间）组成符合网络与存储基本物理规律，未预热时回源延迟公式逻辑自洽。
