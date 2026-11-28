# N29: 成本-性能黑盒映射：建立电费与 Token 消耗的实时关联函数 $Cost(t) = P_{server}(t) \cdot E_{rate} + N_{tok

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

成本-性能黑盒映射：建立电费与 Token 消耗的实时关联函数 $Cost(t) = P_{server}(t) \cdot E_{rate} + N_{tokens}(t) \cdot C_{api}$。由于 V100 功耗 $P_{server}$ 随负载波动，需每 5 分钟采样一次功率。通过最小化 $Cost(t)$ 下的任务完成率 $S(t)$，找到最优的 '本地推理 vs 云端API' 切换阈值。预计当任务复杂度 $C_{task} > 5$ 步时，云端 API 的性价比更高。

## Corrected Claim

成本-性能黑盒映射：建立电费与 Token 消耗的实时关联函数 $Cost(t) = P_{server}(t) \cdot E_{rate} + N_{tokens}(t) \cdot C_{api}$。由于 V100 功耗 $P_{server}$ 随负载波动，需每 5 分钟采样一次功率。通过最小化 $Cost(t)$ 下的任务完成率 $S(t)$，找到最优的 '本地推理 vs 云端API' 切换阈值。预计当任务复杂度 $C_{task} > 5$ 步时，云端 API 的性价比更高。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

local GPU vs cloud API cost performance LLM complex tasks
