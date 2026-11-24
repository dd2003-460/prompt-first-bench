# N609: Intelligent-Tiering 监控费适用对象界定：监控费仅对开启 IT 的存储桶内的对象计费，若冷数据（400TB）使用 S3 Glacier Dee

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N216

## Claim

Intelligent-Tiering 监控费适用对象界定：监控费仅对开启 IT 的存储桶内的对象计费，若冷数据（400TB）使用 S3 Glacier Deep Archive（无 IT 功能），则监控费仅针对温数据 100TB；若冷数据也使用 IT（如 S3 Standard-IA 或 One Zone-IA），则监控费覆盖全量 500TB。

## Corrected Claim

Intelligent-Tiering 监控费适用对象界定：监控费仅对开启 IT 的存储桶内的对象计费，若冷数据（400TB）使用 S3 Glacier Deep Archive（无 IT 功能），则监控费仅针对温数据 100TB；若冷数据也使用 IT（如 S3 Standard-IA 或 One Zone-IA），则监控费覆盖全量 500TB。

## Evidence

先验知识/题面给定，逻辑校验通过：S3 Intelligent-Tiering 监控费确实仅对启用该功能的存储桶内对象收取，Glacier Deep Archive 不支持 IT 故不产生监控费，逻辑自洽且符合 AWS 计费规则。

## Search Query

AWS S3 Intelligent-Tiering monitoring fee applicable storage classes Glacier Deep Archive
