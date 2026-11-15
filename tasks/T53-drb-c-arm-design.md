# DRB C 臂：27b+arena 混合架构接口设计（2026-11-15）

> origin: ai（设计稿，待实施）
> 关联：T53-drb-three-arm.md、s5_state_machine.py

## 一句话

C 臂 = 27b 做拆解/推理/核验 + arena 做检索。核心改动：S5 管线的 search_node 函数从 web-llm 换成 arena API。

## 当前架构

```
S5 管线（27b）
├── decompose（拆解）
├── search_node（检索）→ web-llm（超时率高）
├── verify_node（核验）
└── rework（返工）
```

## 目标架构（C 臂）

```
S5 管线（27b）
├── decompose（拆解）
├── search_node（检索）→ arena API（真实检索）
├── verify_node（核验）
└── rework（返工）
```

## 接口设计

### 1. arena 检索端点

**问题**：arena 是否有独立的检索 API？

**现状**：arena agent mode 是"全流程"（拆解+搜集+推理+核验+报告），没有独立的检索端点。

**方案**：用 arena agent mode 做"只检索不推理"——给 arena 一个 query，要求它只返回检索结果（来源+摘要），不做推理/核验。

### 2. search_node 改造

```python
def search_node_arena(node: dict) -> tuple[list, str | None]:
    """arena 检索：27b 生成 query → arena 检索 → 返回来源列表。"""
    query = node["claim"]
    # 调用 arena API（待实现）
    # 返回: (sources, error)
    # sources: [{url, title, snippet}, ...]
    pass
```

### 3. 实现路径

1. **查 arena API**：确认 arena 是否有可编程的检索端点（REST API / CLI / 只有 web UI）
2. **如果没有**：用 ego-browser 驱动 arena web UI，做"只检索不推理"的 agent mode 调用
3. **改造 search_node**：加 `--search-backend=arena` 参数，切换检索后端
4. **跑 drb-16**：C 臂 vs B 臂（web-llm）对比

## 缺口

| 子项 | 缺什么 | 怎么补 |
|---|---|---|
| arena 检索端点 | 是否有独立 API | 查 arena 文档 / 问 arena 团队 |
| ego-browser 驱动 | arena web UI 的检索流程 | 写 ego-browser 脚本 |
| search_node 改造 | 接口设计 + 实现 | 改 s5_state_machine.py |
| 跑 drb-16 | C 臂 run | 等 M1/M2 跑完 + arena 会话空闲 |

## 预测

- C 臂严格 verified 率 > B 臂（arena 检索返回真实来源，logic-only 比例下降）
- C 臂总分 > B 臂（检索质量提升 → 核验质量提升）
- C 臂 vs A 臂不确定（27b 的思考层 vs arena 的思考层）

## 下一步

1. [待查] arena 检索端点
2. [待建] search_node → arena 接口
3. [待跑] C 臂 drb-16
4. [待跑] 三臂 judge + 对比表
