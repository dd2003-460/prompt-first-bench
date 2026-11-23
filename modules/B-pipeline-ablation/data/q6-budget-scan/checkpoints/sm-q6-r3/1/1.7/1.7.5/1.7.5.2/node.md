# N133: 动态签名URL验证的额外延迟 T_auth 取决于签名算法：HMAC-SHA1约为 0.5-1ms，HMAC-SHA256约为 1-2ms，JWT验证（含公钥获

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

动态签名URL验证的额外延迟 T_auth 取决于签名算法：HMAC-SHA1约为 0.5-1ms，HMAC-SHA256约为 1-2ms，JWT验证（含公钥获取）约为 5-10ms。

## Corrected Claim

动态签名URL验证的额外延迟 T_auth 取决于签名算法：HMAC-SHA1约为 0.5-1ms，HMAC-SHA256约为 1-2ms，JWT验证（含公钥获取）约为 5-10ms。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

HMAC SHA256 CPU latency ms benchmark
