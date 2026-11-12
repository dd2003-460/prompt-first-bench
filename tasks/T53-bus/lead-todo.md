# Lead TODO (ralph stop-hook 读这个文件; "- [ ]" = 未完成, "- [x]" = 完成)

## 已完成
- [x] drb-2 (pid 4633) 跑完 → 验树: id 62/62 唯一 (修复生效), 孤儿 18 (未修, 已报 CC L7), degraded 53/62 全通道型, fanout cap 未生效 (max=4, 已报 CC L7)

## 当前队列
- [x] gpu 题新题面重跑: 已启动 pid 11150 (proc_07adee4420ac), 无 resume 全新跑, log=drb-pilot/run-gpu-rerun-console.log, watch DONE/FATAL
- [ ] CC bus L6-L9 靶点提案收口 — 等 CC 回执 (数字溯源/场景假设/id 修复/孤儿结构口径), 收到后逐项验收 [fanout cap 已澄清非问题, 见 L9]
- [x] runs-s5-sm-gpu.json 废弃决策: 精确数据 12 dup ids (N19-N26 x5) 已报 CC L8, 文件整体废弃留作旧题面对照, D26 走文本匹配
- [x] gpu 新 run 题面确认: log 首行铁证用新题面("不设硬性延迟指标"); sm-gpu-r1/r2.json mtime=昨天21:56/22:08 是旧残留, pid 11150 还没写 ckpt(停在 r1 decompose); N1 claim 待 r1 ckpt 落盘后验
- [x] 修复后 hook 实证: 手动跑 N8 query "A.M. Best 保险前十" → 5 通道返回 5 源(含 ambest.com×2+sohu), 连通性本身没问题, all-5-failed 纯 regex 笔误
- [x] drb-2 51 节点自愈: reverify_drb2.py 全量后台跑 (pid 17041); smoke 1/3 healed(N8 verified), N9/N10 真缺数值源仍 degraded(非 bug); resume 确认救不回
- [ ] drb-2 reverify 全量收口: healed 比例 + still-degraded 原因分类
- [ ] gpu 新 run (pid 11150) 出树 → 验树 (id 唯一/孤儿/degraded 分布) + 与旧题面 run 分数对比 (口径差异标注)
