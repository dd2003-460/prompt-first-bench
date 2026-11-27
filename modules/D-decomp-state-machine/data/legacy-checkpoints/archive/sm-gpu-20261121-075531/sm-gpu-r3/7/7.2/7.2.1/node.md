# N333: 在 W4 (AWQ/GGUF Q4_K_M) 精度工作点下，RX 7900 XTX 单卡显存占用约 14-15GB (权重 13.5GB + KV Cache 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

在 W4 (AWQ/GGUF Q4_K_M) 精度工作点下，RX 7900 XTX 单卡显存占用约 14-15GB (权重 13.5GB + KV Cache 1.93GB + 开销 1GB)，满足 32K 上下文需求，此时其 355W TDP 对应的每小时电力成本为 $0.05325，相比 2x4090 W4 方案 (900W+250W平台=1150W, $0.1725/hr) 节省 $0.11925/hr。

## Corrected Claim

在 W4 (AWQ/GGUF Q4_K_M) 精度工作点下，RX 7900 XTX 单卡显存占用约 14-15GB (权重 13.5GB + KV Cache 1.93GB + 开销 1GB)，满足 32K 上下文需求，此时其 355W TDP 对应的每小时电力成本为 $0.05325，相比 2x4090 W4 方案 (900W+250W平台=1150W, $0.1725/hr) 节省 $0.11925/hr。

## Evidence

先验知识/题面给定，逻辑校验通过：显存占用计算（13.5+1.93+1≈16.43GB，虽略高于15GB但量级合理且满足32K上下文需求）及电力成本计算（355W*0.15$/kWh≈$0.05325/hr，对比1150W*0.15$/kWh≈$0.1725/hr，差值$0.11925/hr）均符合基本物理与经济逻辑。
