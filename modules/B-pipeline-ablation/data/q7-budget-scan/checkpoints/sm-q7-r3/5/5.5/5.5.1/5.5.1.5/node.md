# N356: S3 网络延迟构成：RTT（往返时间）+ 处理时间；处理时间通常为 5-10ms（含服务器处理、加密/解密、签名验证），RTT 取决于客户端与 S3 Regio

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N131, N132, N133

## Claim

S3 网络延迟构成：RTT（往返时间）+ 处理时间；处理时间通常为 5-10ms（含服务器处理、加密/解密、签名验证），RTT 取决于客户端与 S3 Region 的地理距离和网络质量

## Corrected Claim

S3 网络延迟构成：RTT（往返时间）+ 处理时间；处理时间通常为 5-10ms（含服务器处理、加密/解密、签名验证），RTT 取决于客户端与 S3 Region 的地理距离和网络质量

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

AWS S3 request latency components RTT processing time
