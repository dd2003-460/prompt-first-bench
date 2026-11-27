# N103: GPU TDP 修正值：RTX 4090 官方 TDP 450W，A100 80GB SXM4 官方 TDP 400W（非 N28 中误写的 300W），H10

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N28

## Claim

GPU TDP 修正值：RTX 4090 官方 TDP 450W，A100 80GB SXM4 官方 TDP 400W（非 N28 中误写的 300W），H100 SXM5 700W，L40S 350W，A6000 300W，Apple M3 Ultra 系统级功耗约 200-300W [修正自矛盾检测]

## Corrected Claim

GPU TDP 修正值：RTX 4090 官方 TDP 450W，A100 80GB SXM4 官方 TDP 400W，H100 SXM5 700W，L40S 350W，A6000 300W，Apple M3 Ultra 系统级功耗约 200-300W

## Evidence

[质询]参考来源仅提供了对比页面的标题和摘要，未包含具体的TDP数值文本，无法直接验证450W、400W等具体数值；且A100存在PCIe(300W)和SXM(400W)两种版本，若未明确区分易混淆，但陈述中已明确指定SXM4，逻辑上无矛盾，主要风险在于缺乏来源中的直接数值支持。 | 经验事实，逻辑自洽（数值符合已知硬件规格常识），但参考来源[2][3]仅涉及对比主题，未提供具体TDP数值支持，缺来源直接支持。

## Search Query

NVIDIA A100 80GB TDP watts RTX 4090 TDP H100 TDP L40S TDP

## Retrieval Sources

- {'url': 'https://duckduckgo.com/y.js?ad_domain=amazon.com&ad_provider=bingv7aa&ad_type=txad&click_metadata=MWqjfBb_L5nAMuewmJ%2DxuqVsv6uDWOflnHW4mGumdDvDtJRIkPaRV73pL4deoOwQSIeoy6sU89Of5zzO_gfV9gZ0ya0sFBLSUce5vcvWet10EUbpyJLU1fMfOq9qUkzc_yAhLcD_tZSPSwELdWvIMSZWvw9b6NU7g_zoaicSuQc.IxoSFJZcWtlXm89Sg8qIUA&rut=f7774b98106827296eff393801cf278c8a7a4559bfea56ac30e776d64ef1e415&u3=https%3A%2F%2Fwww.bing.com%2Faclick%3Fld%3De8O0xw4DcmDeRT6hETElORwjVUCUxUn2kgeRTfD9Q9ptgU%2Daa2HFaOV7i3AiHa0PxQg2AABD2FVZ5cxgLIkFC7%2DWHVyJD_TtWt5P_q6xoobA%2D1dyh8E1KUYZGinWbHI6ulRJBhE_gaibyOYIZtq3RoLmjSo3gAI8VuzTZSCxjFyYpPlIWSmVu07dsz9m4Iwq7Xri9B4kz7td7C0kb080sgyZTRqsg%26u%3DaHR0cHMlM2ElMmYlMmZ3d3cuYW1hem9uLmNvbSUyZnMlMmYlM2ZpZSUzZFVURjglMjZrZXl3b3JkcyUzZGdhbWluZyUyYm52aWRpYSUyYmdwdSUyNmluZGV4JTNkYXBzJTI2dGFnJTNkdHh0c3RkYmdkdC0yMCUyNnJlZiUzZHBkX3NsXzdyMXVjcGZtazlfYiUyNmFkZ3JwaWQlM2QxMjMwMzUzODI5NjY0NjYxJTI2aHZhZGlkJTNkNzY4OTcyODA1OTQ5ODglMjZodm5ldHclM2RzJTI2aHZxbXQlM2RiJTI2aHZibXQlM2RiYiUyNmh2ZGV2JTNkYyUyNmh2bG9jaW50JTNkJTI2aHZsb2NwaHklM2QxNDAxMjglMjZodnRhcmdpZCUzZGt3ZC03Njg5NzUyNzc0ODQ1MyUzYWxvYy05NiUyNmh5ZGFkY3IlM2QyNTU3NV8xMzU5MzQwNyUyNm1jaWQlM2QxYzA0NWUxZDFjNzkzOGRlYTdjZjIxZmI4YmU2N2RjYiUyNmxhbmd1YWdlJTNkZW5fVVMlMjZtc2Nsa2lkJTNkMzczNWFlODQ0NWMwMWI3NGFkZDBjNTg1YmRlODA5M2I%26rlid%3D3735ae8445c01b74add0c585bde8093b&vqd=4-213960633157786268329318653847627532106&iurl=%7B1%7DIG%3D01F956FA7D3A406A9625C4F131181F24%26CID%3D1DEDCA7447BE66693DD8D26C464C67FC%26ID%3DDevEx%2C5039.1&rut=6147abea88c7e70a68ce59943110c41157ac7fe70a68e4e6837581d88d464ac3', 'type': 'ddg', 'title': 'Shop gaming nvidia gpu - Amazon.com®'}
- {'url': 'https://computecomparison.com/compare-two-gpus/nvidia-a100-vs-nvidia-rtx-4090&rut=184a6101f352c05744304ef76c6f48e64d016bb3ec33f9815caef639db93eaca', 'type': 'ddg', 'title': 'NVIDIA A100 80GB vs NVIDIA RTX 4090 - Pricing, Specs, Strengths ...'}
- {'url': 'https://bizon-tech.com/gpu-benchmarks/NVIDIA-A100-80-GB-(PCIe)-vs-NVIDIA-RTX-4090/624vs637&rut=c6e08dfd7ab0cfbcf2346c3801483d9657994d56dfd9672cc6d3d270be949c7c', 'type': 'ddg', 'title': 'GPU Benchmarks NVIDIA A100 80 GB (PCIe) vs. NVIDIA RTX 4090'}
