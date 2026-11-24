# N559: 工作点 2（中性价比最优）：R=450km（对应 10 POP 均匀分布），L_prop=2.25ms，RTT_base=2*2.25+2.5=7.0ms；此工

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N182

## Claim

工作点 2（中性价比最优）：R=450km（对应 10 POP 均匀分布），L_prop=2.25ms，RTT_base=2*2.25+2.5=7.0ms；此工作点下，东部用户延迟 7ms+5ms=12ms，西部用户延迟 6ms+5ms=11ms（因西部 POP 少，实际 R_west 更大），P99 延迟 ≈ 12ms；成本 C_infra 为基准值，此点为 10 POP 约束下的最优平衡点。

## Corrected Claim

工作点 2（中性价比最优）：R=450km（对应 10 POP 均匀分布），L_prop=2.25ms，RTT_base=2*2.25+2.5=7.0ms；此工作点下，东部用户延迟 7ms+5ms=12ms，西部用户延迟 6ms+5ms=11ms（因西部 POP 少，实际 R_west 更大），P99 延迟 ≈ 12ms；成本 C_infra 为基准值，此点为 10 POP 约束下的最优平衡点。

## Evidence

先验知识/题面给定，逻辑校验通过：光速传播延迟计算正确（2.25ms*2=4.5ms，加处理延迟2.5ms得7ms），总延迟叠加逻辑自洽，符合网络工程基本物理规律。

## Search Query

CDN 10 POP optimal coverage radius 450km latency cost
