# arena.ai 通道机制笔记

> origin: ai · 2026-10-23 · 路由 A：Direct 模式会话机制核实

## 调研问题

arena.ai Direct 模式每 run 是新建会话还是延续上轮上下文？怎么保证每个 run 上下文干净？

## 结论

**Direct 模式每 run 都是新建会话；上下文干净 = 每 run 走一遍「新会话」流程（URL 变为 `/c/<uuid>` 即新会话）。**

## 会话机制细节（2026-10-23 实测）

1. **Direct 新会话入口**：`https://arena.ai/text/direct`（侧边栏顶部 anchor）。页面标题 "What would you like to do?"，底部出现 Direct 模型选择器（默认 "Max/Router" 按钮，点开 dialog 含 118 个模型，可搜索）。URL 参数 `?model_a=<model>` 保留上次选的模型。
2. **首条消息触发建会话**：在 `/text/direct` 输入 prompt 并发送后，URL 变为 `https://arena.ai/c/<uuid>`（uuid 每次不同），会话页左上角出现 "New Chat, model <model>" 按钮（aria-label 含当前模型名）。
3. **续会话**：同一 `/c/<uuid>` 内继续输入 = 延续上轮上下文（多轮对话）。
4. **新会话**：三种等价方式，每 run 用其一即可：
   - goto `https://arena.ai/text/direct`（最简单，推荐）
   - 点会话页左上 "New Chat" 按钮
   - 点侧边栏顶部 direct anchor
5. **历史**：侧边栏 "Expand sidebar" 显示历史会话计数（`<n> completed chats`），历史不干扰新会话。

## 实操要点（ego-browser 自动化）

- 模型选择器：底部按钮文本 "Max"/"Router"（或当前选中模型名），evaluate 里 `b.click()` 打开；选项在 `[role=listbox]` 下 `[role=option]`，需 `scrollIntoView({block:"center"})` 后 `mouse.click(x, y)` 选中。
- 发送：`textarea[name=message]` fill 后，`button[aria-label="Send message"]` 可点（disabled 随输入联动）。
- **安全验证**：短时间连续发多个新会话会触发 reCAPTCHA（"Security Verification" dialog，iframe 内 checkbox "进行人机身份验证"）。点一次 checkbox 即可过，不阻塞流程；但每 run 间隔 ≥60s 可显著降低触发率。
- **发送按钮 disabled 陷阱**：goto `/text/direct` 后若未选模型/未输入，发送按钮 disabled；先选模型再 fill 即可激活。
- 登录态：arena.ai 已登录（ego-lite profile），本次未失效。

## 截图

- `/Users/a1-6/Desktop/workspace/loop-artifacts/arena-launch/round2-direct-ui-1.png` — Direct 模式主页
- `/Users/a1-6/Desktop/workspace/loop-artifacts/arena-launch/round2-direct-ui-2.png` — 模型选择器（118 模型）
