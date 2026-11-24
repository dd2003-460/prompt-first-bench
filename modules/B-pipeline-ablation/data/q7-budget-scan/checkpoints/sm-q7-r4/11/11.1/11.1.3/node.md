# N700: price_per_req = ¥0.01/万次 是阿里云 OSS 标准 GET 请求价格，但 S3 等竞品价格为 $0.0004/1000 requests 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N289

## Claim

price_per_req = ¥0.01/万次 是阿里云 OSS 标准 GET 请求价格，但 S3 等竞品价格为 $0.0004/1000 requests (约 ¥0.028/万次)，且 LIST 请求价格更高 (¥0.01/万次 vs S3 $0.005/1000)；若数据湖频繁执行 ListObjects 操作，LIST 请求成本可能超过 GET 请求，需单独建模 LIST 频率。

## Corrected Claim

阿里云OSS和AWS S3的GET与LIST请求均按次计费，且LIST请求单价通常显著高于GET请求。若数据湖频繁执行ListObjects操作，LIST请求成本可能超过GET请求，需根据实际云厂商最新价目表及用量阶梯单独建模LIST频率以评估总成本。

## Evidence

[质询]阿里云OSS标准存储GET请求单价并非固定的¥0.01/万次，而是随请求量阶梯定价（通常更低，如¥0.0001/次即¥1/万次起），且S3 LIST请求价格（$0.005/1000）远高于GET（$0.0004/1000），原陈述中关于OSS GET价格的数值量级可能存在严重偏差或混淆了不同计费档位/地域。 | 经验事实，逻辑自洽但缺来源支持；OSS和S3的具体API调用价格属于动态变化的商业参数，且OSS采用阶梯计价，固定值¥0.01/万次缺乏普遍适用性，需降级为定性描述。

## Search Query

S3 vs OSS list objects request pricing comparison data lake
