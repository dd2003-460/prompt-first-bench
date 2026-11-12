# Lead TODO (ralph stop-hook 读这个文件; "- [ ]" = 未完成, "- [x]" = 完成)

## 已完成
- [x] drb-2 (pid 4633) 跑完 → 验树: id 62/62 唯一 (修复生效), 孤儿 18 (未修, 已报 CC L7), degraded 53/62 全通道型, fanout cap 未生效 (max=4, 已报 CC L7)

## 当前队列
- [ ] gpu 题新题面 (无 3s/token, commit a64221c1) 重跑一轮 S5 — 启动前确认 LLM proxy (8787) 存活, 后台跑, 完成后验树+对比旧题面分数
- [ ] CC bus L6+L7 靶点提案收口 — 等 CC 回执 (数字溯源/场景假设/id 修复/孤儿结构/fanout cap 口径), 收到后逐项验收
- [ ] runs-s5-sm-gpu.json 的 21 个重复 id: 清理或废弃决策 (D26 验收用文本匹配, 不依赖 id)
