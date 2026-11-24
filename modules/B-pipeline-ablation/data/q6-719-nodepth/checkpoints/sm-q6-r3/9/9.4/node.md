# N186: 无 BGP 接入时的跨网延迟惩罚 ΔT_cross (ms)：当用户运营商与 POP 接入运营商不一致时，P99 延迟增加 ΔT_cross ≈ 15-25ms

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

无 BGP 接入时的跨网延迟惩罚 ΔT_cross (ms)：当用户运营商与 POP 接入运营商不一致时，P99 延迟增加 ΔT_cross ≈ 15-25ms，需纳入 P99_self 的计算。

## Corrected Claim

无 BGP 接入时的跨网延迟惩罚 ΔT_cross (ms)：当用户运营商与 POP 接入运营商不一致时，P99 延迟增加 ΔT_cross ≈ 15-25ms，需纳入 P99_self 的计算。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点存在逻辑矛盾与冗余。子节点1计算基准值为14ms取整15ms，子节点3声称P99上限为30-40ms，这与父节点明确定义的15-25ms范围直接矛盾。此外，子节点1（基准）和子节点2（距离修正）本质上是同一个函数 ΔT_cross(d) 的不同分段或参数，属于冗余拆分。）

## Search Query

CDN POP cross-ISP latency penalty ms
