# N68: LRU 命中率积分表达式的分子项修正：由于 N26 指出 K_max > N，积分上限 ∫_0^{K_max} 应修正为 ∫_0^N（覆盖所有对象），分子变为总

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

LRU 命中率积分表达式的分子项修正：由于 N26 指出 K_max > N，积分上限 ∫_0^{K_max} 应修正为 ∫_0^N（覆盖所有对象），分子变为总请求字节数 ∑_{i=1}^N freq_i * size_i，因此 H_LRU_lb 在容量充足时趋近于 1，除非存在对象更新导致的失效（见子问 c）

## Corrected Claim

LRU 命中率积分表达式的分子项修正：由于 N26 指出 K_max > N，积分上限 ∫_0^{K_max} 应修正为 ∫_0^N（覆盖所有对象），分子变为总请求字节数 ∑_{i=1}^N freq_i * size_i，因此 H_LRU_lb 在容量充足时趋近于 1，除非存在对象更新导致的失效（见子问 c）

## Evidence

先验知识/题面给定，逻辑校验通过：LRU命中率定义为命中字节/总请求字节，当缓存容量N足以容纳所有对象（K_max > N且容量>=N）时，所有请求均命中，分子等于总请求字节，比值为1，逻辑自洽。
