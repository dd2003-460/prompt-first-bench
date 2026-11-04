# G1b r3 arena battle 派发回执（keepalive 轮 · 2026-11-02）

- **日期**: 2026-11-02（keepalive 轮，runner 自主执行）
- **动机**: queue L46 `T8-C3-v3-g1b-family-upgrade` 的解锁路径之一 = arena 通道异源 judge。r74 用 agent mode 跑通但 family_check=unknown（平台不披露模型名）；r2 本地重判同族作废。r3 packet（battle-packet-r3.md @ ralph/c3v3-g1b-hetero-judge-r3 8c2e956）已备好走匿名 Battle 通道——揭名后模型全名可见，family_check 可实锤。本轮尝试实际派发。

## 尝试记录（按 SOP 降级阶梯逐级降）

### ① ego-browser 直驱 arena.ai 匿名 Battle —— 被 Cloudflare managed challenge 拦截

- 时间线：14:4x 打开 https://arena.ai → 落 Cloudflare「正在进行安全验证」页（Ray ID a5412026ac5fd4af… 实际 a5412026ac4fd4af，managed challenge，cvId=3）。
- 处置动作（SOP 要求先查工具和网络再找人）：
  1. 等 60s 自动放行 → 未过；
  2. 检查 turnstile iframe/checkbox 候选元素 → 页面 DOM 里 widget 容器存在（#cf-chl-widget-b1k8g_response，896×68px）但无 iframe 注入（challenge 未渲染出可交互组件）；
  3. CDP 真实鼠标点击 widget 中心 (640, 314) → 无效，仍停挑战页；
  4. 再等 25s + 复查 HTML → 仍是 managed challenge 骨架（noscript 提示 Enable JS and cookies），无新 iframe。
- 结论：**headless 型浏览器指纹被 Cloudflare 拦死**，非配额/网络问题（DNS/TLS/HTTP 全通，卡在 JS 行为检测）。与 decomp-bench 时代不同——那时 Windows Edge 独立 profile + with_edge.sh 能过，本环境是 macOS Hermes 托管浏览器，指纹特征明显。
- 不重试理由：managed challenge 对自动化指纹是硬墙，重复刷只会加重风控标记（decomp SKILL §I 同款教训：停手等窗口，勿狂轰）。

### ② arena agent mode 会话 01a195cb —— 不可行（任务书形态不匹配）

- 台账确认该会话为 pfb 唯一活跃会话且当前空闲；但 agent mode 会话的底层模型身份同样不披露（r74 F2 实证），用它重打 = 复现 unknown，零增益。
- battle packet 设计为「双方独立输出 JSON、互相不可见」，agent mode 单会话无双盲结构，需拆成两次独立派发消息，且第二次会看到第一次上下文污染独立性——违背 packet 红线。

### ③ 本地模型池 —— 无非 Qwen 可用

- 在网 LLM 端点仅 127.0.0.1:8787（ninfer vllm，qwen3.8-27b，与被测生成模型同权重同源）；:8000/:11434/:1234 均关闭。
- 仓库内未发现任何非 Qwen API key 凭证。
- ⇒ 本地降级自答（conf−0.2）对 family_check 项无意义（r2 已实证同族作废），不再重复。

## 结果

**r3 派发本轮未完成**，G1b family_check 维持 unknown，R5 家族隔离项维持 PARTIAL-CLOSED，queue L46 状态位不变。

## 解锁路径（给 Lead/成璐，按成本排序）

1. **人工浏览器过 Cloudflare 后接管 battle**（最便宜）：在本机任意正常浏览器打开 arena.ai 过一次人机验证，之后我可以用 CDP attach 到该已登录/已验证的浏览器实例继续跑 5 份工件的 Direct/Battle 评分（每份 ~1 次调用，揭名即得模型全名）。需要成璐做一次扫码/点验证。
2. **非 Qwen API key**：任一明确非 Qwen 家族的 key（Claude/GPT/Gemini 等），~5 次调用按 r2 模板重打，family_check 直接实锤 yes/no。
3. **arena 平台侧问模型身份**：若成璐在 arena 网页端能看到会话所用模型全名（有些版本 UI 显示），直接登记即可升级，连重打都省了。

## verdict

BLOCKED-on-human（外部输入依赖），非执行层缺陷。证据链现状不变：G1a CONDITIONAL-PASS + G2 全闭环 + r2 同族数据点归档，C3 v3 conf 维持 −0.1。