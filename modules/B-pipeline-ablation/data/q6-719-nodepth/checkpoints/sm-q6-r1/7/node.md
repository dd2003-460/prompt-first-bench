# N45: 日均请求总量 Q_day 的具体数值，基于假设平均对象大小 s=1MB 计算得出：Q_day = 2000GB / 1MB * 1024 ≈ 2,048,000

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

日均请求总量 Q_day 的具体数值，基于假设平均对象大小 s=1MB 计算得出：Q_day = 2000GB / 1MB * 1024 ≈ 2,048,000 requests/day (约 200万次/天)。

## Corrected Claim

日均请求总量 Q_day 的具体数值，基于假设平均对象大小 s=1MB 计算得出：Q_day = 2000GB / 1MB * 1024 ≈ 2,048,000 requests/day (约 200万次/天)。

## Evidence

逻辑推导成立，来源未直接覆盖（数学计算：2000 * 1024 = 2,048,000）

## Retrieval Sources

- {'url': 'https://blog.csdn.net/lang_niu/article/details/122378637&rut=1b947d64bbd6ce956791f5a470d436dcfa3f4372310fa6b9298b9e8910c09f8a', 'type': 'ddg', 'title': '关于请求量、请求资源、带宽三者之间测算-csdn博客'}
- {'url': 'https://www.infoq.cn/article/Nv49E30xoGam*5O6xHT5&rut=7fd1da5030017bb43c7a5d4e90f5c1acbca693bbde011b59e2971fd2013a761f', 'type': 'ddg', 'title': '日均千亿级别的数据请求量背后的秘密 - InfoQ'}
- {'url': 'https://itswuanran.github.io/posts/qps-caculate/&rut=87708026bec9ce38b6905897df6fb1db57c20bc704b33c1b2c075f7351ca65fd', 'type': 'ddg', 'title': '高并发下的QPS计算 - 安然写字的地方 - GitHub Pages'}
