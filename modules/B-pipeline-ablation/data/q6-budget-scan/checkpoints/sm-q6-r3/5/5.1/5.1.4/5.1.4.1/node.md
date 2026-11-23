# N265: 公有云 CDN 日志压缩率 $\gamma$ 对存储成本的影响：访问日志（Access Log）通常可通过 Gzip 压缩至原始大小的 10%-20%，即 $\

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

公有云 CDN 日志压缩率 $\gamma$ 对存储成本的影响：访问日志（Access Log）通常可通过 Gzip 压缩至原始大小的 10%-20%，即 $\gamma \approx 0.15$；实际存储容量 $V_{stored} = V_{raw} \times \gamma = 60 \text{ TB} \times 0.15 = 9 \text{ TB} = 9,216 \text{ GB}$，修正后月存储成本 $C_{store}^{comp} = 9,216 \times 0.12 \approx 1,106$ 元/月。

## Corrected Claim

公有云 CDN 日志压缩率 $\gamma$ 对存储成本的影响：访问日志（Access Log）通常可通过 Gzip 压缩至原始大小的 10%-20%，即 $\gamma \approx 0.15$；实际存储容量 $V_{stored} = V_{raw} \times \gamma = 60 \text{ TB} \times 0.15 = 9 \text{ TB} = 9,216 \text{ GB}$，修正后月存储成本 $C_{store}^{comp} = 9,216 \times 0.12 \approx 1,106$ 元/月。

## Evidence

先验知识/题面给定，逻辑校验通过：Gzip对文本日志压缩率10%-20%符合工程常识，数学计算60TB*0.15=9TB=9216GB及9216*0.12=1105.92≈1106元均准确无误。
