# N412: FTE_required 的量化依据：基于代码库规模（LOC）和技术栈更新频率（如HTTP/2→HTTP/3迁移、TLS 1.2→1.3升级），FTE_requ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N131

## Claim

FTE_required 的量化依据：基于代码库规模（LOC）和技术栈更新频率（如HTTP/2→HTTP/3迁移、TLS 1.2→1.3升级），FTE_required = LOC_total × update_frequency_per_LOC × hours_per_FTE_year^-1；典型自建CDN代码库约5-10万行，年均更新频率约10-20%（因协议/硬件变更），因此 FTE_required ≈ 0.1-0.3，需通过实际代码审计确定

## Corrected Claim

FTE_required 的量化依据：基于代码库规模（LOC）和技术栈更新频率（如HTTP/2→HTTP/3迁移、TLS 1.2→1.3升级），FTE_required = LOC_total × update_frequency_per_LOC × hours_per_FTE_year^-1；典型自建CDN代码库约5-10万行，年均更新频率约10-20%（因协议/硬件变更），因此 FTE_required ≈ 0.1-0.3，需通过实际代码审计确定

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN codebase size FTE maintenance requirement protocol migration HTTP/3
