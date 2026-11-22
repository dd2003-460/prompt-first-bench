# N248: RTX 4090 在不同负载状态下的实际功耗分布：Idle 约 20-30W，Prefill (Compute-bound) 接近 TDP 450W，Decod

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

RTX 4090 在不同负载状态下的实际功耗分布：Idle 约 20-30W，Prefill (Compute-bound) 接近 TDP 450W，Decode (Memory-bound) 约 300-350W；5年总电力成本需基于加权平均功耗计算，而非固定 TDP

## Corrected Claim

RTX 4090 在不同负载状态下的实际功耗分布：Idle 约 20-30W，Prefill (Compute-bound) 接近 TDP 450W，Decode (Memory-bound) 约 300-350W；5年总电力成本需基于加权平均功耗计算，而非固定 TDP

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 TDP为450W，Idle功耗通常在20-30W区间，Decode阶段受限于显存带宽功耗低于Compute-bound的Prefill阶段，符合GPU功耗分布规律及加权平均成本计算逻辑。
