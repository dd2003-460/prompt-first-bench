# N278: 工作点B（性价比最优）：配置4名SRE（$N_{sre}=4$），采用2主2备轮班制，覆盖年假/病假，故障响应冗余度提升，年总人力成本 $C_{hr} = 4 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

工作点B（性价比最优）：配置4名SRE（$N_{sre}=4$），采用2主2备轮班制，覆盖年假/病假，故障响应冗余度提升，年总人力成本 $C_{hr} = 4 \times C_{sre}$，相比基线增加33%人力成本但消除单点故障导致的SLA违约风险（预计违约金 $F_{penalty} > C_{hr}^{diff}$）。

## Corrected Claim

工作点B（性价比最优）：配置4名SRE（$N_{sre}=4$），采用2主2备轮班制，覆盖年假/病假，故障响应冗余度提升，年总人力成本 $C_{hr} = 4 \times C_{sre}$，相比基线增加33%人力成本但消除单点故障导致的SLA违约风险（预计违约金 $F_{penalty} > C_{hr}^{diff}$）。

## Evidence

先验知识/题面给定，逻辑校验通过：4人相比3人基线增加33%成本符合数学逻辑，2主2备配置在SRE领域是消除单点故障的标准工程实践，且作为knowledge节点无需外部来源支持。
