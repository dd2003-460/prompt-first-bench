# N94: 图片请求占比 P_img 与视频请求占比 P_vid 的分布比例，需根据平台业务日志确定；假设 P_img = 80%, P_vid = 20% 作为基准情景，

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N22

## Claim

图片请求占比 P_img 与视频请求占比 P_vid 的分布比例，需根据平台业务日志确定；假设 P_img = 80%, P_vid = 20% 作为基准情景，[待核验]。

## Corrected Claim

图片请求占比 P_img 与视频请求占比 P_vid 的分布比例需根据具体平台业务日志确定；在缺乏具体数据时，可假设 P_img = 80%, P_vid = 20% 作为示例情景，但需注明该假设的局限性。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点是同一参数（请求占比）的不同离散取值，属于冗余枚举而非正交维度；且父节点强调需根据日志确定分布，子节点仅给出假设情景，未涵盖‘实际日志验证’或‘分布不确定性’这一关键方面，导致不完备。）

## Search Query

social media platform image vs video traffic ratio statistics

## Retrieval Sources

- {'url': 'https://my.mail.ru/video/embed/9148137502752644046&rut=9ad7199ed6bc167e747803b42d85eb862cf8e506e8f529ac91f6f1bb28c1d203', 'type': 'ddg', 'title': 'nbar201010_480 :: video.mail.ru'}
- {'url': 'https://prmovie.com/&rut=df8d5b1aafd7f6e49942e05f967053997671f5f65c4efe365c287e94ccf2955f', 'type': 'ddg', 'title': 'prmovie.com'}
