# N259: 运营成本 C_ops 的每千次通知成本需区分短信、APP 推送和邮件三种渠道，具体公式为 C_ops = (n_sms * c_sms + n_push * c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N86

## Claim

运营成本 C_ops 的每千次通知成本需区分短信、APP 推送和邮件三种渠道，具体公式为 C_ops = (n_sms * c_sms + n_push * c_push + n_email * c_email) / 1000，其中 c_sms, c_push, c_email 为各渠道单位成本，需根据平台用户渠道偏好分布加权计算。

## Corrected Claim

运营成本 C_ops 的每千次通知成本需区分短信、APP 推送和邮件三种渠道，具体公式为 C_ops = (n_sms * c_sms + n_push * c_push + n_email * c_email) / 1000，其中 c_sms, c_push, c_email 为各渠道单位成本，需根据平台用户渠道偏好分布加权计算。

## Evidence

先验知识/题面给定，逻辑校验通过
