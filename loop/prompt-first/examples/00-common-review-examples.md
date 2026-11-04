# 00-common-review 操作示例

> origin: ai · 2026-10-27 从 00-common-review.md 外移

## 思考/输出循环检测示例

```
❌ 错误做法：
思考：我应该用工具A还是工具B？→ 工具A可能更好 → 但工具B也有优势 → 让我再想想...
（无限循环思考，没有结论）

✅ 正确做法：
思考：这是一个工具调用任务，直接执行即可。
[执行工具调用]
```

---

其余 1 个示例（负案例/边界案例）已移到 `examples/archive/00-common-review-examples-extras.md`，需要时再读。
