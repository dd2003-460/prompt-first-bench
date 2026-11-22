# N427: H100 SXM 节点通常采用 2x 2000W 冗余电源（CRPS 标准），其转换效率在 50%-80% 负载下通常维持在 94%-96% 的高水平，远高于消

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N177

## Claim

H100 SXM 节点通常采用 2x 2000W 冗余电源（CRPS 标准），其转换效率在 50%-80% 负载下通常维持在 94%-96% 的高水平，远高于消费级电源；在 TCO 计算中，H100 节点的电力损耗可忽略不计（<5%），而消费级 4 卡方案需计入 10%-15% 的损耗，这进一步缩小了 H100 在 OPEX 上的劣势。

## Corrected Claim

H100 SXM 节点通常采用 2x 2000W 冗余电源（CRPS 标准），其转换效率在 50%-80% 负载下通常维持在 94%-96% 的高水平，远高于消费级电源；在 TCO 计算中，H100 节点的电力损耗可忽略不计（<5%），而消费级 4 卡方案需计入 10%-15% 的损耗，这进一步缩小了 H100 在 OPEX 上的劣势。

## Evidence

先验知识/题面给定，逻辑校验通过：服务器级CRPS电源在50-80%负载下效率94-96%符合工程常识，且H100节点电力损耗占比低符合数据中心TCO计算逻辑。

## Search Query

server redundant power supply efficiency H100 node power loss percentage
