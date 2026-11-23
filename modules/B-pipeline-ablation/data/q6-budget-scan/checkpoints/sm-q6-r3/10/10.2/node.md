# N142: 单流传输时间 $T_{transfer} = s_{avg} / B_{link}$。当 $s_{avg}$ 从 1MB 增至 5MB，单流传输时间增加 5 倍

- **status**: pending
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

父节点级核验未通过：不完备, 有冗余（1. 冗余：子节点1和子节点2本质上是同一公式 $T_{transfer} = s_{avg} / B_{link}$ 在不同参数 $s_{avg}$ 下的两个实例，属于参数化重复，应合并。2. 矛盾/错误：子节点2中称“增加4倍”通常指变为原来的4倍（即差值为3倍），但父节点明确指出“增加5倍”（即变为5倍，差值为4倍），且计算结果 4096/819.2=5 倍，子节点2的表述与计算结果及父节点逻辑存在歧义或矛盾。3. 不完备：父节点强调需“综合评估”排队延迟 $L_{queue}$ 对P99的影响，但子节点3在计算占比时完全忽略了 $L_{queue}$，仅使用 $L_{edge}+L_{processing}$，导致无法验证父节点关于“排队延迟降低可能抵消传输时间增加”的论点。）
