# N43: ‘咨询’定义下的数据埋点字段映射：‘点击商品页’对应事件 ID 'product_view'，‘发送私信/留言’对应事件 ID 'message_sent'。需

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

‘咨询’定义下的数据埋点字段映射：‘点击商品页’对应事件 ID 'product_view'，‘发送私信/留言’对应事件 ID 'message_sent'。需从日志表中提取这两个字段的计数，计算转化率 Conv = Count(message_sent) / Count(product_view)。

## Corrected Claim

‘咨询’定义下的数据埋点字段映射：‘点击商品页’对应事件 ID 'product_view'，‘发送私信/留言’对应事件 ID 'message_sent'。需从日志表中提取这两个字段的计数，计算转化率 Conv = Count(message_sent) / Count(product_view)。

## Evidence

先验知识/题面给定，逻辑校验通过
