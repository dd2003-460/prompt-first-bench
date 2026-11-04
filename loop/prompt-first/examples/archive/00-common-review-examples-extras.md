# 00-common-review-examples 补充示例（R7 从 examples/00-common-review-examples.md 移出，一字未改）

> 原文件的 top-1 示例保留在 `examples/00-common-review-examples.md`。本文件是其后的全部小节。

---

## 环境自适应示例

```
✅ 正确做法：
[检测到输出被截断]
→ 降低输出长度，直接给出最简答案
→ 记录：当前模型输出被截断，已降低输出长度

❌ 错误做法：
→ 硬编码：设置 enable_thinking=false
→ 硬编码：设置 reasoning-budget=1000
```
