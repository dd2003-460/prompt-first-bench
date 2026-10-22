# 阶段 02：资料搜集与网页 AI 交叉询问

## 操作流程

1. 读取阶段 01 的空缺条件，只围绕这些空缺搜集资料。
2. 必须先运行 `ralph prompt-first web-llm . "围绕阶段 01 空缺条件的具体核验问题" --context "阶段 02；只要求可复核来源线索"`，把真实回执写入阶段工件；网页 LLM 只提供线索，不是事实来源。必须直接调用已安装的 `ralph` 可执行文件；不要使用 `npx`、`npm`、管道或 `head` 包装它。若命令以未授权/未配置状态快速失败，记录完整失败原因后继续公开网页资料搜集，不得等待或循环重试。
3. 为每个关键主张记录来源标题、URL、发布或更新时间、实际观察时间、具体观察和不确定性。
4. 关键主张至少寻找两个相互独立的来源。厂商规格、独立评测、实际价格或用户实测应明确区分。
5. 对价格、库存、版本、政策、软件支持等易变事实，优先使用最近 7 天内的资料；若没有足够新资料，明确标为未解决。
6. 对稳定事实可以使用较早的一手资料，但必须说明它为什么仍然适用。
7. 记录搜索失败、登录限制、网页 LLM 不可用和零结果；这些不是证据，不能伪装成来源。对同一主张的 WebSearch 若返回 0 结果或失败，最多更换一次关键词；仍失败就记录失败原因和未解决状态，停止重复搜索并写入阶段工件。
8. WebFetch 只对最多 4 个已知、具体 URL 各尝试一次；单个 URL 无结果、403、404 或明显长时间无响应时立即记录状态，不要重复抓取或等待。至少拿到一个可读的一手页面后就停止抓取并写阶段工件。
9. 不要在本阶段写最终推荐，只收集证据、暂定结论和仍未解决的空缺。

## 可用工具索引

### 网页搜索工具

| 工具 | 适用场景 | 调用方式 |
|------|----------|----------|
| `ralph prompt-first web-llm` | 快速核验事实、获取线索 | `ralph prompt-first web-llm . "问题" --context "阶段 02"` |
| `ego-browser` | 需要登录状态、反爬绕过、动态渲染页面 | `ego-browser nodejs <<'EOF' ... EOF` |
| 浏览器工具（Hermes） | 需要视觉验证、复杂交互 | `browser_navigate` + `browser_snapshot` |
| `curl`/`wget` | 直接获取 API 或静态页面 | 终端命令 |

### ego-browser Skill 索引

**何时使用 ego-browser：**
- 需要用户登录状态的网站（如 Amazon、京东）
- 有反爬机制的网站（需要 Cookie/Session 维持）
- 动态渲染的页面（SPA、React/Vue 应用）
- 需要视觉验证的场景（截图确认）

**基本用法：**
```bash
# 检查 ego-browser 是否可用
command -v ego-browser

# 基本搜索
ego-browser nodejs <<'EOF'
const task = await useOrCreateTaskSpace('search-task')
await openOrReuseTab('https://www.google.com/search?q=GPU+型号')
cliLog(await snapshotText())
EOF

# 完成 task space
ego-browser nodejs <<'EOF'
const task = await useOrCreateTaskSpace('search-task')
await completeTaskSpace(task.id, { keep: false })
EOF

# 视觉工作流（截图分析）
ego-browser nodejs <<'EOF'
const task = await useOrCreateTaskSpace('visual-task')
await openOrReuseTab('https://example.com')
const screenshot = await captureScreenshot()
// 使用 vision 工具分析截图
EOF
```

**关键注意事项：**
- `@N` refs 只在最近的 `snapshotText()` 调用中有效
- `js()` 返回的是评估结果，不是 JSON 字符串
- `cliLog()` 是 heredoc 中唯一的输出机制
- 每次 heredoc 执行后 Node.js 运行时退出，状态不保留
- 必须调用 `completeTaskSpace()` 关闭 task space

### 浏览器工具（Hermes 内置）

**何时使用 Hermes 浏览器工具：**
- 需要与网页交互（点击、填写表单）
- 需要 JavaScript 执行环境
- 需要控制台输出调试

**基本用法：**
```
browser_navigate("https://example.com")
browser_snapshot()  # 获取页面结构
browser_click("@ref_id")  # 点击元素
browser_type("@ref_id", "text")  # 输入文本
```

## Reviewer 质检标准

- 阶段 01 的关键空缺是否逐项有证据或明确保留为未解决；
- 关键主张是否有足够独立来源；
- 易变事实是否接近当前日期，实际观察时间是否明确；
- 是否把网页 LLM 线索误写成事实来源；
- 是否记录并处理来源矛盾；
- 是否仍存在会改变下一阶段方案的关键证据缺口。

只要关键主张缺少独立来源、关键时效信息过期或存在未解释矛盾，必须 revise，repair_stage 写 02。

## 操作示例

### 示例：GPU 调研 — 价格核验

**阶段 01 空缺：** "各候选 GPU 的当前市场价格"

**执行步骤：**
```
1. 运行 web-llm 获取线索：
   ralph prompt-first web-llm . "RTX 4090 当前价格？" --context "阶段 02"

2. 运行 ego-browser 获取实时价格：
   ego-browser nodejs <<'EOF'
   const task = await useOrCreateTaskSpace('gpu-price')
   await openOrReuseTab('https://www.amazon.com/s?k=RTX+4090')
   cliLog(await snapshotText())
   EOF

3. 运行浏览器工具获取备选来源：
   browser_navigate("https://www.newegg.com/p/pl?d=RTX+4090")
   browser_snapshot()

4. 记录结果：
   - 来源 1：Amazon，$1,599，2024-01-15
   - 来源 2：Newegg，$1,649，2024-01-15
   - 来源 3：web-llm 线索，约 $1,600（无具体 URL，标记为线索）

5. 交叉核验：
   - Amazon 和 Newegg 价格一致（差异 < 5%），可信
   - web-llm 线索与实测一致，可作为辅助证据
```

### 示例：GPU 调研 — 显存带宽核验

**阶段 01 空缺：** "各候选 GPU 的显存带宽具体数值"

**执行步骤：**
```
1. 运行 web-llm 获取线索：
   ralph prompt-first web-llm . "RTX 4090 显存带宽 Gbps？" --context "阶段 02"

2. 查找一手规格页面：
   browser_navigate("https://www.nvidia.com/en-us/geforce/graphics-cards/4090/")
   browser_snapshot()

3. 记录结果：
   - 来源 1：NVIDIA 官方规格，2112 GB/s，2022-10-20 发布
   - 来源 2：TechPowerUp 数据库，2112 GB/s，2024-01-10 更新

4. 交叉核验：
   - 官方规格和第三方数据库一致
   - 显存带宽是硬件规格，不会变化，早期数据仍然有效
```
