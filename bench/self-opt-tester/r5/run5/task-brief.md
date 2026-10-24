# origin: ai — R5 run5 任务书（arena 通道，9 步链路复跑，防复读新题）
你执行 self-optimization bench 的 9 步标准链路（与 run2 同协议），本轮新指标题（防复读）：
新增过程指标 M8「首次通过率 first-pass rate」：定义=交付物中一次性通过验证（未经修改重跑）的验证点数/总验证点数，0-100 打分；给出你的 M8 评分与依据，并评估 M8 与 M3（断点通过率）是否共线、是否应并入权重（|r|>0.7 规则）。
9 步链路（每步挂 M7 不可伪造锚点：文件存在/git hash/命令退出码/会话 URL）：
1 拉 pfb 仓库 prompt-first-bench（main 或你的 arena 分支，先 fetch 再动作，ls-remote 记录 HEAD）
2 读 loop/prompt-first/ 六个阶段文件（01→04.5）+ sop/arena-loop-pipeline.md，统计规则负载字节数
3 目标分解：对「M8 是否应入 bench」做正交分解（≤10 行）
4 信息调研：≥2 独立来源交叉验证 first-pass/首次通过率在 agent eval 文献或开源 bench 中的既有定义（找不到→标 unverified+URL，禁虚构）
5 交叉核验：矛盾点记录在案
6 行动分解：M8 打分表（含与 M3 的相关判断）
7 执行+验证：把 M8 定义写入 bench/self-opt-tester/run5/m8-proposal.md，git commit+push 到你的 arena 分支（无 main push 权限则分支+记录，禁伪造）
8 终检：ls-remote 验证 push 落点
9 汇总：9 步锚点清单 + M1-M8 自评分（M1 token 效率/M2 任务书行数≤200/M3 断点/M4 交叉验证独立源/M5 迭代轮数/M6 降级诚实/M7 锚点率/M8 首次通过率）+ 每分一句话依据
产出：pfb 你的 arena 分支 m8-proposal.md + 回执全文（含锚点清单）。降级如实记录，禁虚构。
