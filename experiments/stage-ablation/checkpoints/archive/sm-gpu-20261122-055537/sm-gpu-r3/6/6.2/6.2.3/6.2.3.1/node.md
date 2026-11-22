# N315: 修正父节点中 P_draw_4090 的取值：基于 N96 的 550W (450W GPU + 100W System) 为更严谨的基准，修正 N64 中 6

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

修正父节点中 P_draw_4090 的取值：基于 N96 的 550W (450W GPU + 100W System) 为更严谨的基准，修正 N64 中 600-650W 的高估（N64 可能包含了高负载 CPU 或额外外设），确认 ΔP_draw 基准值为 428W (550W - 122W)。

## Corrected Claim

修正父节点中 P_draw_4090 的取值：基于 N96 的 550W (450W GPU + 100W System) 为更严谨的基准，修正 N64 中 600-650W 的高估（N64 可能包含了高负载 CPU 或额外外设），确认 ΔP_draw 基准值为 428W (550W - 122W)。

## Evidence

先验知识/题面给定，逻辑校验通过：550W - 122W = 428W 计算正确，且基于更严谨的基准修正高估值符合工程逻辑。
