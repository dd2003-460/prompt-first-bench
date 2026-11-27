# N244: 低资本支出/长折旧工作点（RTX 4090）：单卡 $1,600，折旧周期 5 年，年化成本 $320/年；虽然年化 CapEx 最低，但缺乏 ECC 和高带宽

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

低资本支出/长折旧工作点（RTX 4090）：单卡 $1,600，折旧周期 5 年，年化成本 $320/年；虽然年化 CapEx 最低，但缺乏 ECC 和高带宽，在 32K 上下文下 KV Cache 读取成为瓶颈，有效 TPS 约为 20-30 tokens/s；若用于高并发服务，需多卡扩展，导致总 CapEx 和电力成本非线性上升，适合单用户或低并发本地推理。

## Corrected Claim

低资本支出/长折旧工作点（RTX 4090）：单卡 $1,600，折旧周期 5 年，年化成本 $320/年；虽然年化 CapEx 最低，但缺乏 ECC 和高带宽，在 32K 上下文下 KV Cache 读取成为瓶颈，有效 TPS 约为 20-30 tokens/s；若用于高并发服务，需多卡扩展，导致总 CapEx 和电力成本非线性上升，适合单用户或低并发本地推理。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 单卡价格约 $1600，5年折旧年化 $320 计算正确；无 ECC 和显存带宽（~1TB/s）限制导致长上下文 KV Cache 瓶颈及低并发 TPS 符合硬件特性与推理原理。
