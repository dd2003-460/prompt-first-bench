# N135: 突发冷请求比例 p_cold 的量化定义：p_cold = R_cold_instant / R_total，其中 R_cold_instant 为瞬时窗口内针

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70, N71, N72

## Claim

突发冷请求比例 p_cold 的量化定义：p_cold = R_cold_instant / R_total，其中 R_cold_instant 为瞬时窗口内针对缓存中未驻留对象的请求率，该参数需通过流量监控或模拟中的泊松过程参数确定，以驱动驱逐数量 k_evict 的计算

## Corrected Claim

突发冷请求比例 p_cold 的量化定义：p_cold = R_cold_instant / R_total，其中 R_cold_instant 为瞬时窗口内针对缓存中未驻留对象的请求率，该参数需通过流量监控或模拟中的泊松过程参数确定，以驱动驱逐数量 k_evict 的计算

## Evidence

先验知识/题面给定，逻辑校验通过
