# N142: 单流传输时间 $T_{transfer} = s_{avg} / B_{link}$。当 $s_{avg}$ 从 1MB 增至 5MB，单流传输时间增加 5 倍

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

单流传输时间 $T_{transfer} = s_{avg} / B_{link}$。当 $s_{avg}$ 从 1MB 增至 5MB，单流传输时间增加 5 倍。虽然排队延迟降低，但传输时间增加可能抵消部分 P99 延迟的改善，需综合评估 $L_{p99} = L_{queue} + T_{transfer} + L_{processing}$。

## Corrected Claim

单流传输时间 $T_{transfer} = s_{avg} / B_{link}$。当 $s_{avg}$ 从 1MB 增至 5MB，单流传输时间增加 5 倍。虽然排队延迟降低，但传输时间增加可能抵消部分 P99 延迟的改善，需综合评估 $L_{p99} = L_{queue} + T_{transfer} + L_{processing}$。

## Evidence

先验知识/题面给定，逻辑校验通过：传输时间公式 T=s/B 成立，s 增加 5 倍则 T 增加 5 倍，逻辑自洽且量级合理。
