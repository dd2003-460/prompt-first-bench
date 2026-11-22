# N148: 小对象（S < 100KB）对总字节命中率折损的贡献占比 ΔH_small/ΔH_total 的解析表达式：ΔH_small/ΔH_total = (P_inv

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

小对象（S < 100KB）对总字节命中率折损的贡献占比 ΔH_small/ΔH_total 的解析表达式：ΔH_small/ΔH_total = (P_invalidate_small * (S_small/S_total)) / Σ(P_invalidate_i * (S_i/S_total))，其中 P_invalidate_small < 1% 且 S_small/S_total < 10%，需验证分母中其他区间的贡献是否显著大于分子，以确认 '<5%' 的结论是否依赖于分母被大对象区间主导。

## Corrected Claim

小对象（S < 100KB）对总字节命中率折损的贡献占比 ΔH_small/ΔH_total 的解析表达式：ΔH_small/ΔH_total = (P_invalidate_small * (S_small/S_total)) / Σ(P_invalidate_i * (S_i/S_total))，其中 P_invalidate_small < 1% 且 S_small/S_total < 10%，需验证分母中其他区间的贡献是否显著大于分子，以确认 '<5%' 的结论是否依赖于分母被大对象区间主导。

## Evidence

先验知识/题面给定，逻辑校验通过
