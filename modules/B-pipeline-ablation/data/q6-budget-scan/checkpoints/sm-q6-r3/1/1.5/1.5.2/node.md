# N64: 服务速率μ的确定：μ = 1 / (T_service_avg + T_overhead)，其中T_service_avg为平均服务时间（缓存命中<1ms，未命

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

服务速率μ的确定：μ = 1 / (T_service_avg + T_overhead)，其中T_service_avg为平均服务时间（缓存命中<1ms，未命中10-50ms），T_overhead为系统开销（典型0.1-0.5ms）；对于缓存命中路径，μ ≈ 1000-10000 req/s/核心，需根据CPU核心数和并发模型确定。

## Corrected Claim

服务速率μ的确定：μ = 1 / (T_service_avg + T_overhead)，其中T_service_avg为平均服务时间（缓存命中<1ms，未命中10-50ms），T_overhead为系统开销（典型0.1-0.5ms）；对于缓存命中路径，μ ≈ 1000-10000 req/s/核心，需根据CPU核心数和并发模型确定。

## Evidence

父节点级核验未通过：不完备（子节点分别详细分解了服务时间（缓存命中路径）和系统开销，两者正交且不冗余。但父节点明确提到了“未命中10-50ms”以及“需根据CPU核心数和并发模型确定”的服务速率μ，而子节点仅覆盖了“缓存命中”路径的服务时间，缺失了“未命中”路径的服务时间分解，且未涉及并发/核心数对μ的影响，导致完备性不足。）
