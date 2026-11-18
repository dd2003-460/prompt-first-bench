# 动态可视化方案对比

## 1. LangSmith 付费模式

**免费额度**：
- Developer 计划：$0/月，5k base traces/月
- 超出后：$2.50/1k traces（14 天保留）或 $5.00/1k traces（400 天保留）

**付费内容**：
- 不是"额外功能付费"，是"用量付费"
- 免费额度内可以完整使用所有功能（tracing、evals、datasets、annotation queues、Prompt Hub、Playground）
- 超出后按 trace 数量计费

**结论**：对于 pfb 这种小规模实验（每天几十次 run），免费额度够用。

---

## 2. LangGraph Studio

**实现方式**：
- 本地开发服务器（`langgraph dev`）
- 需要 LangSmith API key（免费额度内可用）
- 可视化：节点 + 状态 + 执行轨迹

**功能**：
- 画布：节点 + 边（条件边用不同颜色/样式）
- 状态：每个节点的当前状态（pending/running/completed/failed）
- 大小比例：节点大小固定，不随状态变化
- 自动适应：有（pan/zoom）
- 缩放功能：有（滚轮缩放，拖动平移）

**限制**：
- 需要 Python >= 3.11
- 需要 Docker（桌面版）或本地服务器（web 版）
- 需要 LangSmith API key

---

## 3. 简单的稳定实现

**推荐方案**：JSON 映射到节点 + 日志记录

### 架构
```
状态机执行 → 日志文件（JSONL）→ 前端（React Flow）
```

### 日志格式
```json
{
  "timestamp": "2026-11-18T14:30:00Z",
  "node_id": "N1",
  "node_name": "decompose",
  "status": "running",
  "attempts": 1,
  "error": null,
  "duration_ms": 1234,
  "metadata": {...}
}
```

### 前端实现
- **React Flow**（开源，MIT 许可）
- 节点：从 JSON 日志解析
- 状态：颜色编码（pending=灰色，running=蓝色，completed=绿色，failed=红色）
- 大小比例：固定（不随状态变化）
- 自动适应：有（pan/zoom）
- 缩放功能：有（滚轮缩放，拖动平移）

### 优点
- 简单：日志文件 + 前端解析
- 稳定：不依赖外部服务
- 可扩展：支持多轮次步骤和状态变更

### 缺点
- 需要自己写前端
- 需要自己写日志格式

---

## 4. 现成工具对比

| 工具 | 许可 | 功能 | 限制 |
|------|------|------|------|
| LangSmith | 付费（免费额度 5k traces/月） | 节点 + 状态 + 执行轨迹 | 需要 API key |
| LangGraph Studio | 免费（需要 LangSmith API key） | 节点 + 状态 + 执行轨迹 | 需要 Python >= 3.11 + Docker |
| React Flow | MIT | 节点 + 边 + 自定义状态 | 需要自己写前端 |
| n8n | Sustainable Use License | 节点 + 状态 + 执行轨迹 | 不能商用 |
| Activepieces | MIT | 节点 + 状态 + 执行轨迹 | 集成目录较小 |
| Node-RED | Apache-2.0 | 节点 + 状态 + 执行轨迹 | 适合事件驱动，不适合状态机 |

---

## 5. 建议

**对于 pfb 状态机**：
1. **短期**：用 LangSmith 免费额度（5k traces/月够用）
2. **长期**：自己写 React Flow 前端（JSON 日志 + 前端解析）

**实现步骤**：
1. 状态机执行时写 JSONL 日志（每个节点的状态变更）
2. 前端用 React Flow 解析日志，渲染节点 + 边
3. 状态用颜色编码（pending/running/completed/failed）
4. 支持 pan/zoom（React Flow 内置）

**代码量**：
- 日志格式：~50 行
- 前端：~200 行（React Flow + 状态解析）
