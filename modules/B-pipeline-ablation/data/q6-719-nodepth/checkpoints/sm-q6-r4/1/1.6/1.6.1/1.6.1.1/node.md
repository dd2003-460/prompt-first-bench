# N194: TLS 1.3 标准握手（Full Handshake）确实只需 1 RTT 完成密钥交换和证书验证，因为 ClientHello 包含 key_share，S

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

TLS 1.3 标准握手（Full Handshake）确实只需 1 RTT 完成密钥交换和证书验证，因为 ClientHello 包含 key_share，ServerHello 包含 server key share 和证书，无需额外的 ChangeCipherSpec 往返。

## Corrected Claim

TLS 1.3 标准握手（Full Handshake）确实只需 1 RTT 完成密钥交换和证书验证，因为 ClientHello 包含 key_share，ServerHello 包含 server key share 和证书，无需额外的 ChangeCipherSpec 往返。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点之间存在逻辑重叠且存在事实性偏差。首先，子节点2声称Finished消息能在'同一RTT内完成'是错误的，TLS 1.3握手结束后，ClientFinished是在ServerHello发送后的下一个RTT（即1-RTT之后）发送的，而非与ServerHello在同一RTT内。其次，子节点1和子节点2都重复解释了'无需ChangeCipherSpec'和'密钥推导'这一核心机制，未体现正交性（一个应聚焦于协议结构/扩展字段，另一个应聚焦于消息流/时序）。最后，父节点未提及'证书验证'的具体细节（如链式验证或信任锚），子节点也未充分覆盖'证书验证'这一关键方面，仅笼统提及。）
