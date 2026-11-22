# N280: TCO 中时间成本修正公式：C_time_loss = (Throughput_NVLink - Throughput_PCIe) × Cost_per_tok

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N92

## Claim

TCO 中时间成本修正公式：C_time_loss = (Throughput_NVLink - Throughput_PCIe) × Cost_per_token × Total_tokens_generated；若 PCIe 方案吞吐下降 15%，则 3 年周期内多消耗的电力成本 ≈ 15% × C_power_base，需从 TCO 总额中扣除或视为隐性运维成本。

## Corrected Claim

TCO 中因吞吐下降导致的额外成本应包含计算资源占用时间延长带来的折旧/租赁成本及电力成本，而非仅简单等同于电力成本；若 PCIe 方案吞吐下降 15%，在固定负载下，完成相同任务所需时间增加约 17.6% (1/0.85 - 1)，由此产生的额外电力及计算资源成本需计入 TCO。

## Evidence

[质询]公式逻辑存在概念混淆：'时间成本'通常指因延迟导致的业务机会损失或人力等待成本，而非直接等同于'电力成本'。将吞吐差异直接乘以'单token成本'再关联到'电力成本'，忽略了计算成本（折旧/云租赁）通常占TCO大头的事实，且15%吞吐下降并不严格线性对应15%电力成本增加（存在固定开销和效率非线性）。 | 先验知识/题面给定，逻辑校验发现概念混淆：时间成本与电力成本非同一维度，且吞吐下降与电力成本增加非严格线性关系，无法从第一性原理严格推出该等式。
