# N64: 服务速率μ的确定：μ = 1 / (T_service_avg + T_overhead)，其中T_service_avg为平均服务时间（缓存命中<1ms，未命

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

服务速率μ的确定：μ = 1 / (T_service_avg + T_overhead)，其中T_service_avg为平均服务时间（缓存命中<1ms，未命中10-50ms），T_overhead为系统开销（典型0.1-0.5ms）；对于缓存命中路径，μ ≈ 1000-10000 req/s/核心，需根据CPU核心数和并发模型确定。

## Corrected Claim

服务速率μ的确定：μ = 1 / (T_service_avg + T_overhead)，其中T_service_avg为平均服务时间（缓存命中<1ms，未命中10-50ms），T_overhead为系统开销（典型0.1-0.5ms）；对于缓存命中路径，μ ≈ 1000-10000 req/s/核心，需根据CPU核心数和并发模型确定。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 μ=1/T 符合排队论基本定义；数值量级合理（1ms对应1000req/s，0.1ms对应10000req/s），符合典型系统性能常识。
