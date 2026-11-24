# N572: 0-RTT 机制存在重放攻击风险，因此服务器必须对 Early Data 进行幂等性处理或严格验证；若业务场景（如图片/短视频下载）为非幂等写操作，0-RTT 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N196

## Claim

0-RTT 机制存在重放攻击风险，因此服务器必须对 Early Data 进行幂等性处理或严格验证；若业务场景（如图片/短视频下载）为非幂等写操作，0-RTT 不适用，仅适用于幂等读请求，此时节省的 1 RTT 延迟约为 20-50ms（取决于 RTT）。

## Corrected Claim

0-RTT 机制存在重放攻击风险，因此服务器必须对 Early Data 进行幂等性处理或严格验证；若业务场景（如图片/短视频下载）为非幂等写操作，0-RTT 不适用，仅适用于幂等读请求，此时节省的 1 RTT 延迟约为 20-50ms（取决于 RTT）。

## Evidence

先验知识/题面给定，逻辑校验通过：0-RTT重放风险及幂等性要求符合TLS 1.3协议规范，20-50ms延迟节省符合常见网络RTT量级。

## Search Query

TLS 1.3 0-RTT replay attack idempotent requests image download
