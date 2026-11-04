# ego-browser 用法（冻结自 02-information-research.md v1 · 按需读取）

> 阶段 02 的通道实现细节。**不是规则**，只在需要实际调用浏览器时读。
> R7 从 `02-information-research.md` 原样移出，一字未改。

---

## ego-browser 用法（单通道，驱动用户已登录的 ego-lite）

网页 LLM 交叉验证、登录态页面、动态渲染页面**一律走 ego-browser**，不用任何无头/非持久浏览器。全局规则与站点清单见 `AGENTS.md` §网页 LLM 交叉验证流程。

```bash
ego-browser nodejs <<'EOF'
const task = await taskSpace('my-task')        // 同名 space 可复用
const p1 = task.page('p1')
await p1.goto('https://example.com')
const s = await p1.snapshot()                  // 定位: @N ref / loc=css: / loc=role: / text= / xpath=
// await p1.fill('text=输入框', '内容')
// await p1.click('@3')
// await p1.waitForFunction(() => document.body.innerText.includes('完成'), { timeout: 60000 })
const reply = await p1.snapshot()
console.log(reply)
await task.finish({ keep: [] })                // 结束前必须 finish，否则留僵尸进程
EOF
```

**关键注意事项：**
- 选择器：快照 ref `@N`、`loc=css:`、`loc=role:`、`text=`、`xpath=`
- 等待：`waitForURL` / `waitForSelector` / `waitForFunction` / `waitForTimeout`
- 每次 heredoc 是独立 Node 运行时，跨次状态不保留；靠同名 `taskSpace` 复用浏览器会话
- 结束前必须 `task.finish({ keep: [] })`
- 不要用 Playwright 方法，不要另开浏览器实例
