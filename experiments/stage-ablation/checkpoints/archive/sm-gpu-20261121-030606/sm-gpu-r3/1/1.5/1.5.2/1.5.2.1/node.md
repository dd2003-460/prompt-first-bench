# N213: H100 SXM 80GB在2025年的云租赁均价约为$2.90/hour（AWS/Azure/GCP加权平均），若按7x24小时运行，年租赁成本为$25,40

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N98

## Claim

H100 SXM 80GB在2025年的云租赁均价约为$2.90/hour（AWS/Azure/GCP加权平均），若按7x24小时运行，年租赁成本为$25,404，远高于自购折旧成本$11,667，但在短期（<1年）使用场景下租赁可能更具现金流优势。

## Corrected Claim

H100 SXM 80GB在2025年的云租赁均价约为$2.90/hour（具体数值需实时查询），若按7x24小时运行，年租赁成本约为$25,404，通常高于自购折旧成本，但在短期（<1年）使用场景下租赁可能更具现金流优势。

## Evidence

[质询]具体数值（$2.90/hour, $25,404, $11,667）属于经验事实，且参考来源仅提供了价格查询入口或摘要，未直接给出2025年的具体加权均价及自购折旧对比数据，无法从现有来源直接验证精确数值。 | 经验事实，逻辑自洽但缺来源支持。来源[1][2][3]主题相关（H100 SXM租赁价格），但摘要未包含具体2025年均价$2.90及折旧对比数据，无法直接证实具体数值，故降级。

## Search Query

H100 SXM cloud rental price per hour 2025 AWS Azure GCP

## Retrieval Sources

- {'url': 'https://fastgpu.co/gpus/h100-sxm&rut=b3abd8302992529c3b15664a779eaaf7a09988ac706e83cb08531c914f57993a', 'type': 'ddg', 'title': 'H100 SXM cloud pricing and rental cost per hour | FastGPU'}
- {'url': 'https://fastgpu.co/gpus/h100&rut=eb2659bb5602d5c438b7404686044d93d9193691e6272a44a8f0d1f74a57443d', 'type': 'ddg', 'title': 'H100 cloud pricing and rental cost per hour | FastGPU'}
- {'url': 'https://skycisa.com/gpus/h100-sxm&rut=587d081c3ac6a9ca92121e6d1f663fa3746b1ab5b5faf9dcf321a9db82feb51e', 'type': 'ddg', 'title': 'H100 SXM cloud pricing — rent H100 SXM per hour · SkyCISA'}
