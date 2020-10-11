# 混合模糊测试技术

作为模糊测试的一个分支，已经渐渐成熟，很多论文都在此方面做出了比较大的贡献。
1. 2007年，"[Hybrid concolic testing](../Paper/Thesis12_Hybrid.pdf)" 第一次将符号执行和自动化软件测试结合起来，此项研究成为后来众多混合模糊测试的概念原型。
2. 2012年，"[Hybrid Fuzz Testing - Discovering Software Bugs via Fuzzing and Symbolic Execution](../Paper/ICSE07_Hybrid.pdf)" 首次提出混合模糊测试（Hybrid Fuzzing）
3. 2016年, "[Driller: Argumenting Fuzzing Through Selective Symbolic Execution](../Paper/NDSS16_Driller.pdf)"，不同于2007年的混合测试，Driller利用fork-server思想结合了模糊测试技术afl和符号执行技术，并实现了对二进制文件的高效漏洞挖掘。Driller奠定了后来混合模糊测试技术的发展方向，模糊测试技术加符号执行技术。  
4. 2018年, "[QSYM: A Practical Concolic Execution Engine Tailored for Hybrid Fuzzing](../Paper/USENIX18_QSYM.pdf)"，对Driller进行了大幅度的改进。  
5. 2019年混合模糊测试技术出现爆发，国内外研究人员纷纷被吸引过来：  
"[SAVIOR: Towards Bug-Driven Hybrid Testing](../Paper/SP20_SAVIOR.pdf)" 中，可以看出百度团队也参与到模糊测试的队列中。  
"[Send Hardest Problems My Way: Probabilistic Path Prioritization for Hybrid Fuzzing](../Paper/NDSS19_Probabilistic.pdf)" 中武汉大提出一种叫做DigFuzz的原型系统。  
值得一提的是，此时一些中文论文也开始出现相关研究，比如谢肖飞的 "[基于符号执行与模糊测试的混合测试方法](http://www.jos.org.cn/html/2019/10/5789.htm)"结合了AFL和KLEE。  
6. 2020年，[PANGOLIN](../Paper/SP20_PANGOLIN.pdf)

-- Summarized by [WayneDevMaze](https://github.com/WayneDevMaze)

