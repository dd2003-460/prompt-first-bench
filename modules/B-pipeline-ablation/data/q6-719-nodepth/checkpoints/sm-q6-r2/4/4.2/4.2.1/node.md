# N104: IP 地理库静态映射的准确率 A_geo，定义为正确将用户 IP 映射到最近 POP 的比例，典型商业 IP 库（如 GeoIP2）准确率在 90-95% 之间

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

IP 地理库静态映射的准确率 A_geo，定义为正确将用户 IP 映射到最近 POP 的比例，典型商业 IP 库（如 GeoIP2）准确率在 90-95% 之间，错误映射会导致用户被调度到次优 POP，增加 RTT。

## Corrected Claim

典型商业 IP 库（如 GeoIP2）在国家级定位准确率可达 95-99%，但在城市级定位准确率通常在 50-80% 之间；若用于调度至最近 POP，实际准确率取决于 POP 的地理粒度及 IP 库的城市级精度，错误映射确实会导致用户被调度到次优 POP，增加 RTT。

## Evidence

[质询]数值量级与口径混淆：来源[3]明确指出城市级定位精度仅为50-80%，而90-95%通常对应国家级或较粗粒度的定位。将'映射到最近POP'（通常隐含城市或区域级精度）的准确率直接断言为90-95%，缺乏对具体地理粒度（如国家vs城市）的限定，且与来源中城市级精度的数据存在潜在冲突。 | 来源[3]提供城市级精度50-80%，国家级95-99%，未直接支持'最近POP映射'在90-95%这一具体区间，属于经验事实且缺乏直接来源支持，故降级。

## Search Query

GeoIP database accuracy rate CDN routing

## Retrieval Sources

- {'url': 'https://www.maxmind.com/en/geoip/ip-geolocation-accuracy&rut=485a8188dee650ae61b0a2f5d7215800cbd524c9058a369ab829e0fb420ca90f', 'type': 'ddg', 'title': 'Understanding IP geolocation accuracy | MaxMind'}
- {'url': 'https://www.researchgate.net/profile/Abdullah-Yasin-Nur/publication/372091523_Accuracy_and_Coverage_Analysis_of_IP_Geolocation_Databases/links/64a5677f95bbbe0c6e16a810/Accuracy-and-Coverage-Analysis-of-IP-Geolocation-Databases.pdf&rut=8a6a095c9c0d6bbfacd40e8998f9718062298d90528e673973c6660063ad6463', 'type': 'ddg', 'title': 'PDF Accuracy and Coverage Analysis of IP Geolocation Databases'}
- {'url': 'https://www.ipinfo.im/zh/topics/tutorials/ip-geolocation-accuracy-explained&rut=12915754b0566fd1927779cb49593a7a2676bf524a7ac4b90b347f5f24caf8bc', 'type': 'ddg', 'title': 'IP 地理位置定位到底有多准？深度解析 IP Geolocation 的原理、精度与局限 - ipinfo.im · IP 信息'}
