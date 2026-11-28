# N19: 数据流序列化协议：模块间通信采用JSON Lines格式，每条消息包含message_id（UUID）、timestamp（ISO 8601）、payload（

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

数据流序列化协议：模块间通信采用JSON Lines格式，每条消息包含message_id（UUID）、timestamp（ISO 8601）、payload（模块特定数据）与checksum（SHA-256前8字节），确保消息完整性与顺序性，单次序列化/反序列化开销≤1ms。

## Corrected Claim

数据流序列化协议：模块间通信采用JSON Lines格式，每条消息包含message_id（UUID）、timestamp（ISO 8601）、payload（模块特定数据）与checksum（SHA-256前8字节），确保消息完整性与顺序性，单次序列化/反序列化开销≤1ms。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

JSON Lines message serialization checksum integrity LLM agent data flow
