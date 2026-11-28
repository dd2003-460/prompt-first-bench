# N44: 实验设计者Agent的触发条件量化定义：当假设生成器输出被验证者Agent初步通过且资源预估Cost_est < Budget_limit时启动；输入Schem

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10, N11, N12

## Claim

实验设计者Agent的触发条件量化定义：当假设生成器输出被验证者Agent初步通过且资源预估Cost_est < Budget_limit时启动；输入Schema为{approved_hypothesis, available_tools[], constraints[]}，输出为执行脚本或伪代码，终止条件为生成的代码通过静态语法检查(Syntax Check Pass)且无未知依赖(Undefined Dependency Count = 0)。

## Corrected Claim

实验设计者Agent的触发条件量化定义：当假设生成器输出被验证者Agent初步通过且资源预估Cost_est < Budget_limit时启动；输入Schema为{approved_hypothesis, available_tools[], constraints[]}，输出为执行脚本或伪代码，终止条件为生成的代码通过静态语法检查(Syntax Check Pass)且无未知依赖(Undefined Dependency Count = 0)。

## Evidence

父节点级核验未通过：不完备（子节点分别定义了触发阈值(Cost)、预算上限(Budget)和终止条件(Syntax)，三者维度不同，无重叠矛盾，故正交。但父节点明确包含“输入Schema”和“输出类型(脚本/伪代码)”的定义，而现有子节点仅覆盖了量化触发条件和部分终止细节，完全缺失了对输入数据结构及输出格式规范的分解，导致不完备。）

## Search Query

agent workflow experimental designer input output schema termination
