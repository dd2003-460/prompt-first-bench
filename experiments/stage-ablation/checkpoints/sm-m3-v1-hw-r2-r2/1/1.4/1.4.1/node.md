# N42: V100 (SM70) 上 CUDA 7.0 架构缺乏原生 FP8 Tensor Core，vLLM 的 fp8 KV cache 配置实际触发 CPU off

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

V100 (SM70) 上 CUDA 7.0 架构缺乏原生 FP8 Tensor Core，vLLM 的 fp8 KV cache 配置实际触发 CPU offload 或 FP16 upcast 计算路径，导致每次 Attention 操作的访存带宽需求增加约 2-4 倍，直接削弱 MTP 验证阶段的批处理能力。

## Corrected Claim

V100 (SM70) 上 CUDA 7.0 架构缺乏原生 FP8 Tensor Core，vLLM 的 fp8 KV cache 配置需依赖 CPU offload 或 GPU 上的 FP16 upcast 路径，增加了数据搬运和转换开销，从而降低了 MTP 验证阶段的吞吐量。

## Evidence

[质询]将“缺乏原生FP8 Tensor Core”直接等同于“访存带宽需求增加2-4倍”存在逻辑跳跃。虽然V100确实不支持FP8硬件加速，但KV Cache的存储格式（FP8 vs FP16）主要影响的是显存占用和加载/存储时的数据量，而非计算本身的带宽需求。若仅指KV Cache的读写，带宽需求确实减半（FP8比FP16小一半，即FP16是FP8的2倍），但“2-4倍”的范围较宽且未明确区分是计算带宽还是I/O带宽，且“直接削弱MTP验证阶段”的因果链条过于简化，忽略了软件优化（如量化/反量化开销）可能带来的额外延迟，使得“2-4倍”这一具体数值缺乏严谨的推导基础。 | 先验知识/题面给定，逻辑校验通过。V100 (SM70) 确实不支持 FP8 Tensor Core，使用 FP8 KV Cache 必然涉及 CPU/GPU 间的转换或 upcast，导致额外的数据搬运和计算开销，定性描述正确，但具体倍数‘2-4倍’为经验估算，缺乏精确来源支持，故降级。
