# N611: 最小对象大小约束对监控费有效性的影响：S3 Intelligent-Tiering 对小于 128KB 的对象不收取监控费，但若温数据中平均对象大小为 128K

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N216

## Claim

最小对象大小约束对监控费有效性的影响：S3 Intelligent-Tiering 对小于 128KB 的对象不收取监控费，但若温数据中平均对象大小为 128KB（N31 假设），则所有对象均≥128KB，监控费全额生效；若存在大量小对象（如日志碎片 <128KB），实际计费数据量将低于逻辑数据量，需按对象大小分布加权计算有效计费 TB 数。

## Corrected Claim

最小对象大小约束对监控费有效性的影响：S3 Intelligent-Tiering 对小于 128KB 的对象不收取监控费，但若温数据中平均对象大小为 128KB（N31 假设），则所有对象均≥128KB，监控费全额生效；若存在大量小对象（如日志碎片 <128KB），实际计费数据量将低于逻辑数据量，需按对象大小分布加权计算有效计费 TB 数。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

S3 Intelligent-Tiering minimum object size 128KB monitoring fee exclusion
