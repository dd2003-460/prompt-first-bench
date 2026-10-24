# origin: ai — R5 run4 任务书（终态效度首测，n=1 仅定性）
任务：写 work/sum_col.py（仅 Python 标准库）。参数 `<csv路径> <列名>`；CSV 带表头，按列名定位，求该列数值之和，stdout 打印结果保留 2 位小数；列不存在 → stderr 报错且退出码非 0。
工作目录：/Users/a1-6/Desktop/workspace/projects/AI-计算科学/D1-efficiency-optimization/tasks/self-optimization-tester/loop-artifacts/stages/04.5/r5/run4/
步骤（3 断点，M3 锚点）：A 读本任务书并复述 4 条验收标准 → B 实现 sum_col.py → C 运行 `bash check-run4.sh`，4 用例全 PASS。
硬规则：① 禁改 check-run4.sh（sha256 已预登记，Lead 复验）② 禁外部网络 ③ 用例失败可改 sum_col.py 重跑，最多 3 次迭代；仍失败则如实记 loop-state，禁伪造通过。
产出：work/sum_col.py；loop-state.json（写本目录：每步命令+退出码+fs 证据、迭代次数、降级如实、check-run4.sh 最终退出码）。
验收（Lead 复验）：check-run4.sh 退出码 0；check-run4.sh sha256 未变；loop-state.json 存在且与实际退出码一致。
