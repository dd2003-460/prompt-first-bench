
## r189 广播留痕 (2026-11-02)
微信推送失败：`retry-without-token: ret=-1 errcode=None errmsg=invalid request`（与 r187 同型，token 刷新链路问题）。消息已写入 /tmp/wx-msg.txt，内容见上。不重试（协议上限 1 次），继续干活。
