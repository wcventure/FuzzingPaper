# Recent Papers Related To Fuzzing

# All Papers (Classification according to Conference)

- S&P 2020
    - SAVIOR: Towards Bug-Driven Hybrid Testing

- S&P 2019
    - NEUZZ: Efficient Fuzzing with Neural Program Smoothing
    - Fuzzing File Systems via Two-Dimensional Input Space Exploration
    - ProFuzzer: On-the-fly Input Type Probing for Better Zero-day Vulnerability Discovery
    - Razzer: Finding Kernel Race Bugs through Fuzzing
    - Full-speed Fuzzing: Reducing Fuzzing Overhead through Coverage-guided Tracing 

- S&P 2018
    - T-Fuzz: fuzzing by program transformation
    - Angora: Efficient Fuzzing by Principled Search
    - CollAFL: Path Sensitive Fuzzing

- S&P 2017
    - NEZHA: Efficient Domain-Independent Differential Testing

- USENUX Security2019
    - MOPT: Optimize Mutation Scheduling for Fuzzers

- USENUX Security2018
    - MoonShine: Optimizing OS Fuzzer Seed Selection with Trace Distillation 
    - QSYM : A Practical Concolic Execution Engine Tailored for Hybrid Fuzzing 

- USENUX Security2017
    - kAFL: Hardware-Assisted Feedback Fuzzing for OS Kernels

- CCS 2018
    - Evaluating fuzz testing
    - Hawkeye Towards a Desired Directed Grey-box Fuzzer

- CCS 2017
    - Directed Greybox Fuzzing
    - Designing New Operating Primitives to Improve Fuzzing Performance
    - DIFUZE: Interface aware fuzzing for kernel drivers

- CCS 2016
    - Coverage-based Greybox Fuzzing as Markov Chain

- NDSS 2019
    - REDQUEEN: Fuzzing with Input-to-State Correspondence
    - PeriScope: An Effective Probing and Fuzzing Framework for the Hardware-OS Boundary 
    - Life after Speech Recognition: Fuzzing Semantic Misinterpretation for Voice Assistant Applications
    - Send Hardest Problems My Way: Probabilistic Path Prioritization for Hybrid Fuzzing
    - CodeAlchemist: Semantics-Aware Code Generation to Find Vulnerabilities in JavaScript Engines 

- NDSS 2018
    - IoTFuzzer: Discovering Memory Corruptions in IoT Through App-based Fuzzing 
    - What You Corrupt Is Not What You Crash: Challenges in Fuzzing Embedded Devices 
    - Enhancing Memory Error Detection for Large-Scale Applications and Fuzz Testing

- NDSS 2017
    - VUzzer: Application-aware Evolutionary Fuzzing
    - Driller: Argumenting Fuzzing Through Selective Symbolic Execution

- ICSE 2019
    - DifFuzz: Differential Fuzzing for Side-Channel Analysis
    - REST-ler: Stateful REST API Fuzzing
    - SLF: Fuzzing without Valid Seed Inputs
    - Superion: Grammar-Aware Greybox Fuzzing

- FSE 2018
    - Singularity: Pattern Fuzzing for Worst Case Complexity

- ASE 2018
    - ContractFuzzer: Fuzzing Smart Contracts for Vulnerability Detection
    - FairFuzz: A Targeted Mutation Strategy for Increasing Greybox Fuzz Testing Coverage

- PLDI 2019
    - Parser-Directed Fuzzing

- PLDI 2016
    - Coverage-Directed Differential Testing of JVM Implementations

- ACSAC 2018
    - TIFF: Using Input Type Inference To Improve Fuzzing


# All Papers (Classification according to Subject)

- [**Differential Fuzzing**](#differential-fuzzing)
  - [DifFuzz: Differential Fuzzing for Side-Channel Analysis (ICSE 2019)](#diffuzz-differential-fuzzing-for-side-channel-analysis-icse-2019)
  - [NEZHA: Efficient Domain-Independent Differential Testing (S&P 2017)](#nezha-efficient-domain-independent-differential-testing-sp-2017)
  - [Coverage-Directed Differential Testing of JVM Implementations (PLDI 2016)](#coverage-directed-differential-testing-of-jvm-implementations-pldi-2016)

- [**Evaluate Fuzzing**](#evaluate-fuzzing)
  - [Evaluating Fuzz Testing (CCS 2018)](#evaluating-fuzz-testing-ccs-2018)

- [**Kernel Fuzzing**](#kernel-fuzzing)
  - [PeriScope: An Effective Probing and Fuzzing Framework for the Hardware-OS Boundary (NDSS2019)](#periscope-an-effective-probing-and-fuzzing-framework-for-the-hardware-os-boundary-ndss2019)
  - [Fuzzing File Systems via Two-Dimensional Input Space Exploration (S&P 2019)](#fuzzing-file-systems-via-two-dimensional-input-space-exploration-sp-2019)
  - [Razzer: Finding Kernel Race Bugs through Fuzzing (S&P 2019)](#razzer-finding-kernel-race-bugs-through-fuzzing-sp-2019)
  - [kAFL: Hardware-Assisted Feedback Fuzzing for OS Kernels (Usenix Security2017)](#kafl-hardware-assisted-feedback-fuzzing-for-os-kernels-usenix-security2017)
  - [DIFUZE: Interface aware fuzzing for kernel drivers (CCS 2017)](#difuze-interface-aware-fuzzing-for-kernel-drivers-ccs-2017)

- [**Hybrid Fuzzing**](#hybrid-fuzzing)
  - [SAVIOR: Towards Bug-Driven Hybrid Testing (S&P 2020)](#savior-towards-bug-driven-hybrid-testing-sp-2020)
  - [Send Hardest Problems My Way: Probabilistic Path Prioritization for Hybrid Fuzzing (NDSS 2019)](#send-hardest-problems-my-way-probabilistic-path-prioritization-for-hybrid-fuzzing--ndss-2019)
  - [QSYM: A Practical Concolic Execution Engine Tailored for Hybrid Fuzzing (USENUX Security2018)](#qsym-a-practical-concolic-execution-engine-tailored-for-hybrid-fuzzing-usenux-security2018)
  - [Angora: Efficient Fuzzing by Principled Search (S&P 2018)](#angora-efficient-fuzzing-by-principled-search-sp-2018)
  - [Driller: Argumenting Fuzzing Through Selective Symbolic Execution (NDSS 2016)](#driller-argumenting-fuzzing-through-selective-symbolic-execution-ndss-2016)

- [**Addressing Magic bytes \ checksum**](#addressing-magic-bytes-\-checksum)
  - [REDQUEEN: Fuzzing with Input-to-State Correspondence  (NDSS2019)](#redqueen-fuzzing-with-input-to-state-correspondence-ndss2019)
  - [T-Fuzz: fuzzing by program transformation (S&P 2018)](#t-fuzz-fuzzing-by-program-transformation-sp-2018)
  - [FairFuzz: A Targeted Mutation Strategy for Increasing Greybox Fuzz Testing Coverage (ASE 2018)](#fairfuzz-a-targeted-mutation-strategy-for-increasing-greybox-fuzz-testing-coverage-ase-2018)
  - [VUzzer: Application-aware Evolutionary Fuzzing (NDSS 2017)](#vuzzer-application-aware-evolutionary-fuzzing-ndss-2017)
  
- [**Inputs-aware Fuzzing**](#inputs-aware-fuzzing)
  - [Parser-Directed Fuzzing (PLDI 2019)](#parser-directed-fuzzing-pldi-2019)
  - [SLF: Fuzzing without Valid Seed Inputs (ICSE 2019)](#slf-fuzzing-without-valid-seed-inputs-icse-2019)
  - [Superion: Grammar-Aware Greybox Fuzzing (ICSE 2019)](#superion-grammar-aware-greybox-fuzzing-icse-2019)
  - [ProFuzzer: On-the-fly Input Type Probing for Better Zero-day Vulnerability Discovery (S&P 2019)](#profuzzer-on-the-fly-input-type-probing-for-better-zero-day-vulnerability-discovery-sp-2019)
  - [CodeAlchemist: Semantics-Aware Code Generation to Find Vulnerabilities in JavaScript Engines (NDSS 2019)](#codealchemist-semantics-aware-code-generation-to-find-vulnerabilities-in-javascript-engines-ndss-2019)
  - [TIFF: Using Input Type Inference To Improve Fuzzing (ACSAC 2018)](#tiff-using-input-type-inference-to-improve-fuzzing-acsac-2018)

- [**Directed Fuzzing**](#directed-fuzzing)
  - [Directed Greybox Fuzzing (CCS 2017)](#directed-greybox-fuzzing-ccs-2017)
  - [Hawkeye: Towards a Desired Directed Grey-box Fuzzer (CCS 2018)](#hawkeye-towards-a-desired-directed-grey-box-fuzzer-ccs-2018)

- [**Addressing Collision**](#addressing-collision)
  - [CollAFL: Path Sensitive Fuzzing (S&P 2018)](#collafl-path-sensitive-fuzzing-sp-2018)

- [**Fuzzing Overhead & Performance**](#fuzzing-overhead--performance)
  - [Full-speed Fuzzing: Reducing Fuzzing Overhead through Coverage-guided Tracing (S&P 2019)](#full-speed-fuzzing-reducing-fuzzing-overhead-through-coverage-guided-tracing-sp-2019)
  - [Designing New Operating Primitives to Improve Fuzzing Performance (CCS 2017)](#designing-new-operating-primitives-to-improve-fuzzing-performance-ccs-2017)

- [**Enhancing Memory Error**](#enhancing-memory-error)
  - [Enhancing Memory Error Detection for Large-Scale Applications and Fuzz Testing (NDSS 2018)](#enhancing-memory-error-detection-for-large-scale-applications-and-fuzz-testing-ndss-2018)
  - [AddressSanitizer: A Fast Address Sanity Checker  (USENUX Security2012)](#addressSanitizer-a-fast-address-sanity-checker-usenux-security2012)

- [**Schedule (Power & Mutation)**](#schedule-power--mutation)
  - [MOPT: Optimize Mutation Scheduling for Fuzzers (USENUX Security2019)](#)
  - [Coverage-based Greybox Fuzzing as Markov Chain (CCS 2016)](#coverage-based-greybox-fuzzing-as-markov-chain-ccs-2016)

- [**Learning-based Fuzzing**](#learning-based-fuzzing)
  - [NEUZZ: Efficient Fuzzing with Neural Program Smoothing (S&P 2019)](#neuzz-efficient-fuzzing-with-neural-program-smoothing-sp-2019)

- [**Fuzzing Machine Learning Model**](#fuzzing-machine-learning-model)
  - [TensorFuzz: Debugging Neural Networks with Coverage-Guided Fuzzing (2018)](#tensorfuzz-debugging-neural-networks-with-coverage-guided-fuzzing-2018)
  - [Coverage-Guided Fuzzing for Deep Neural Networks (2018)](#coverage-guided-fuzzing-for-deep-neural-networks-2018)

- [**Interesting Fuzzing**](#interesting-fuzzing)
  - [REST-ler: Stateful REST API Fuzzing  (ICSE 2019)](#rest-ler-stateful-rest-api-fuzzing--icse-2019)
  - [Life after Speech Recognition: Fuzzing Semantic Misinterpretation for Voice Assistant Applications (NDSS 2019)](#life-after-speech-recognition-fuzzing-semantic-misinterpretation-for-voice-assistant-applications-ndss-2019)
  - [ContractFuzzer: Fuzzing Smart Contracts for Vulnerability Detection (ASE 2018)](#contractfuzzer-fuzzing-smart-contracts-for-vulnerability-detection-ase-2018)
  - [IoTFuzzer: Discovering Memory Corruptions in IoT Through App-based Fuzzing (NDSS 2018)](#iotfuzzer-discovering-memory-corruptions-in-iot-through-app-based-fuzzing-ndss-2018)
  - [What You Corrupt Is Not What You Crash: Challenges in Fuzzing Embedded Devices (NDSS 2018)](#what-you-corrupt-is-not-what-you-crash-challenges-in-fuzzing-embedded-devices-ndss-2018)
  - [MoonShine: Optimizing OS Fuzzer Seed Selection with Trace Distillation (USENUX Security2018)](#moonshine-optimizing-os-fuzzer-seed-selection-with-trace-distillation-usenux-security2018)
  - [Singularity: Pattern Fuzzing for Worst Case Complexity (FSE 2018)](#singularity-pattern-fuzzing-for-worst-case-complexity-fse-2018)
  

# Differential Fuzzing

### DifFuzz: Differential Fuzzing for Side-Channel Analysis (ICSE 2019)

* <img src="image/youdao_note_24px.png">[Reading Note](http://note.youdao.com/noteshare?id=8e905e9d299cae5ceb3bbeac0591cfab&sub=9FCAB3A8AD4C48689095307EDD1A940A)
* <img src="image/pdf_24px.png">[Paper](./Paper/ICSE19_DIFFUZZ.pdf)

**Abstract:** Side-channel attacks allow an adversary to uncover secret program data by observing the behavior of a program with respect to a resource, such as execution time, consumed memory or response size. Side-channel vulnerabilities are difficult to reason about as they involve analyzing the correlations between resource usage over multiple program paths. We present DifFuzz, a fuzzing-based approach for detecting side-channel vulnerabilities related to time and space. DifFuzz automatically detects these vulnerabilities by analyzing two versions of the program and using resource-guided heuristics to find inputs that maximize the difference in resource consumption between secret-dependent paths. The methodology of DifFuzz is general and can be applied to programs written in any language. For this paper, we present an implementation that targets analysis of Java programs, and uses and extends the Kelinci and AFL fuzzers. We evaluate DifFuzz on a large number of Java programs and demonstrate that it can reveal unknown side-channel vulnerabilities in popular applications. We also show that DifFuzz compares favorably against Blazer and Themis, two state-of-the-art analysis tools for finding side-channels in Java programs.


### NEZHA: Efficient Domain-Independent Differential Testing (S&P 2017)

* <img src="image/youdao_note_24px.png">[Reading Note](http://note.youdao.com/noteshare?id=7e602068c641217947c97b287291c9c7&sub=32BD04EB8C00424E87FA7B948D38EC96)

* <img src="image/pdf_24px.png">[Paper](./Paper/SP17_NEZHA.pdf)

* <img src="image/ppt_24px.png">[Slides](./Paper/SP17_NEZHA_Slides.pdf)

* <img src="image/github_24px.png">[Code](https://github.com/nezha-dt/nezha)

Differential testing uses similar programs as cross-referencing oracles to find semantic bugs that do not exhibit explicit erroneous behaviors like crashes or assertion failures. Unfortunately, existing differential testing tools are domain-specific and inefficient, requiring large numbers of test inputs to find a single bug. In this paper, we address these issues by designing and implementing NEZHA, an efficient input-format-agnostic differential testing framework. The key insight behind NEZHA's design is that current tools generate inputs by simply borrowing techniques designed for finding crash or memory corruption bugs in individual programs (e.g., maximizing code coverage). By contrast, NEZHA exploits the behavioral asymmetries between multiple test programs to focus on inputs that are more likely to trigger semantic bugs. We introduce the notion of δ-diversity, which summarizes the observed asymmetries between the behaviors of multiple test applications. Based on δ-diversity, we design two efficient domain-independent input generation mechanisms for differential testing, one gray-box and one black-box. We demonstrate that both of these input generation schemes are significantly more efficient than existing tools at finding semantic bugs in real-world, complex software.


### Coverage-Directed Differential Testing of JVM Implementations (PLDI 2016)

* <img src="image/pdf_24px.png">[Paper](./Paper/PLDI16_JVM.pdf)

* <img src="image/ppt_24px.png">[Slides](./Paper/PLDI16_JVM.pptx)
  
Java virtual machine (JVM) is a core technology, whose reliability is critical. Testing JVM implementations requires painstaking effort in designing test classfiles (*.class) along with their test oracles. An alternative is to employ binary fuzzing to differentially test JVMs by blindly mutating seeding classfiles and executing the resulting mutants on different JVMs for revealing inconsistent behaviors. However, this blind approach is not cost effective in practice because (1) most of the mutants are invalid and redundant, and (2) the discovered JVM discrepancies, if any, mostly only concern compatibility issues, rather than actual defects.
This paper tackles this challenge by introducing classfuzz, a coverage-directed fuzzing approach that focuses on representative classfiles for differential JVM testing. Our core insight is to (1) mutate seeding classfiles using a set of predefined mutation operators and employ Markov Chain Monte Carlo (MCMC) sampling to guide mutator selection, and (2) execute the mutants on a reference JVM implementation and use coverage uniqueness as a discipline for accepting representative ones. The accepted classfiles are used as inputs to differentially test JVMs and find defects.
We have implemented classfuzz and conducted an extensive evaluation of it against existing fuzz testing algorithms. Our evaluation results show that classfuzz can enhance the ratio of discrepancy-triggering classfiles from 1.7% to 11.9%. We have also reported 62 defect-indicative discrepancies, along with the test classfiles, to JVM developers. A number of our reported issues have already been confirmed as JVM defects, and some even match recent clarifications and changes to the JVM specification, Java SE 8 Edition.



# Evaluate Fuzzing

### Evaluating Fuzz Testing (CCS 2018)

* <img src="image/youdao_note_24px.png">[Reading Note](http://note.youdao.com/noteshare?id=dce0794335cedbca49b3de99b38952b5&sub=5E92CEBD198B436D9133230B459EB03D)

* <img src="image/pdf_24px.png">[Paper](./Paper/CCS18_Evaluating.pdf)
 
**Abstract:** Fuzz testing has enjoyed great success at discovering security critical bugs in real software. Recently, researchers have devoted significant effort to devising new fuzzing techniques, strategies, and algorithms. Such new ideas are primarily evaluated experimentally so an important question is: What experimental setup is needed to produce trustworthy results? We surveyed the recent research literature and assessed the experimental evaluations carried out by 32 fuzzing papers. We found problems in every evaluation we considered. We then performed our own extensive experimental evaluation using an existing fuzzer. Our results showed that the general problems we found in existing experimental evaluations can indeed translate to actual wrong or misleading assessments. We conclude with some guidelines that we hope will help improve experimental evaluations of fuzz testing algorithms, making reported results more robust.



# Kernel Fuzzing

### PeriScope: An Effective Probing and Fuzzing Framework for the Hardware-OS Boundary (NDSS2019)

* <img src="image/pdf_24px.png">[Paper](./Paper/NDSS19_PeriScope.pdf)

**Abstract:** The OS kernel is an attractive target for remote attackers. If compromised, the kernel gives adversaries full system access, including the ability to install rootkits, extract sensitive information, and perform other malicious actions, all while evading detection. Most of the kernel's attack surface is situated along the system call boundary. Ongoing kernel protection efforts have focused primarily on securing this boundary; several capable analysis and fuzzing frameworks have been developed for this purpose.
However, there are additional paths to kernel compromise that do not involve system calls, as demonstrated by several recent exploits. For example, by compromising the firmware of a peripheral device such as a Wi-Fi chipset and subsequently sending malicious inputs from the Wi-Fi chipset to the Wi-Fi driver, adversaries have been able to gain control over the kernel without invoking a single system call. Unfortunately, there are currently no practical probing and fuzzing frameworks that can help developers find and fix such vulnerabilities occurring along the hardware-OS boundary.
We present PeriScope, a Linux kernel based probing framework that enables fine-grained analysis of device-driver interactions. PeriScope hooks into the kernel's page fault handling mechanism to either passively monitor and log traffic between device drivers and their corresponding hardware, or mutate the data stream on-the-fly using a fuzzing component, PeriFuzz, thus mimicking an active adversarial attack. PeriFuzz accurately models the capabilities of an attacker on peripheral devices, to expose different classes of bugs including, but not limited to, memory corruption bugs and double-fetch bugs. To demonstrate the risk that peripheral devices pose, as well as the value of our framework, we have evaluated PeriFuzz on the Wi-Fi drivers of two popular chipset vendors, where we discovered 15 unique vulnerabilities, 9 of which were previously unknown.


### Fuzzing File Systems via Two-Dimensional Input Space Exploration (S&P 2019)

* <img src="image/wechat_24px.png">[Reading Note From BAIZE](https://mp.weixin.qq.com/s/d2VEQTLtHV5Z-li6M3KBFA)

* <img src="image/pdf_24px.png">[Paper](./Paper/SP19_Fuzzing_File.pdf)

**Abstract:** File systems, a basic building block of an OS, are too big and too complex to be bug free. Nevertheless, file systems rely on regular stress-testing tools and formal checkers to find bugs, which are limited due to the ever-increasing complexity of both file systems and OSes. Thus, fuzzing, proven to be an effective and a practical approach, becomes a preferable choice, as it does not need much knowledge about a target. However, three main challenges exist in fuzzing file systems: mutating a large image blob that degrades overall performance, generating image-dependent file operations, and reproducing found bugs, which is difficult for existing OS fuzzers. Hence, we present JANUS, the first feedback-driven fuzzer that explores the two-dimensional input space of a file system, i.e., mutating metadata on a large image, while emitting image-directed file operations. In addition, JANUS relies on a library OS rather than on traditional VMs for fuzzing, which enables JANUS to load a fresh copy of the OS, thereby leading to better reproducibility of bugs. We evaluate JANUS on eight file systems and found 90 bugs in the upstream Linux kernel, 62 of which have been acknowledged. Forty-three bugs have been fixed with 32 CVEs assigned. In addition, JANUS achieves higher code coverage on all the file systems after fuzzing 12 hours, when compared with the state-of-the-art fuzzer Syzkaller for fuzzing file systems. JANUS visits 4.19x and 2.01x more code paths in Btrfs and ext4, respectively. Moreover, JANUS is able to reproduce 88-100% of the crashes, while Syzkaller fails on all of them.


### Razzer: Finding Kernel Race Bugs through Fuzzing (S&P 2019)

* <img src="image/wechat_24px.png">[Reading Note From BAIZE](https://mp.weixin.qq.com/s/nq1A12Dra2vUiQWbtLXctg)

* <img src="image/pdf_24px.png">[Paper](./Paper/SP19_Razzer.pdf)

**Abstract:** A data race in a kernel is an important class of bugs, critically impacting the reliability and security of the associated system. As a result of a race, the kernel may become unresponsive. Even worse, an attacker may launch a privilege escalation attack to acquire root privileges. In this paper, we propose Razzer, a tool to find race bugs in kernels. The core of Razzer is in guiding fuzz testing towards potential data race spots in the kernel. Razzer employs two techniques to find races efficiently: a static analysis and a deterministic thread interleaving technique. Using a static analysis, Razzer identifies over-approximated potential data race spots, guiding the fuzzer to search for data races in the kernel more efficiently. Using the deterministic thread interleaving technique implemented at the hypervisor, Razzer tames the non-deterministic behavior of the kernel such that it can deterministically trigger a race. We implemented a prototype of Razzer and ran the latest Linux kernel (from v4.16-rc3 to v4.18-rc3) using Razzer. As a result, Razzer discovered 30 new races in the kernel, with 16 subsequently confirmed and accordingly patched by kernel developers after they were reported.


### kAFL: Hardware-Assisted Feedback Fuzzing for OS Kernels (Usenix Security2017)

* <img src="image/wechat_24px.png">[Reading Note From BAIZE](https://mp.weixin.qq.com/s/46J-kU37SerZd2H3L2GiTw)

* <img src="image/pdf_24px.png">[Paper](./Paper/USENUX18_Kafl.pdf)

* <img src="image/ppt_24px.png">[Slides](./Paper/USENUX18_Kafl_Slides.pdf)

* <img src="image/github_24px.png">[Code](https://github.com/RUB-SysSec/kAFL)

**Abstract:** Many kinds of memory safety vulnerabilities have been endangering software systems for decades. Amongst other approaches, fuzzing is a promising technique to unveil various software faults. Recently, feedback-guided fuzzing demonstrated its power, producing a steady stream of security-critical software bugs. Most fuzzing efforts—especially feedback fuzzing—are limited to user space components of an operating system (OS), although bugs in kernel components are more severe, because they allow an attacker to gain access to a system with full privileges. Unfortunately, kernel components are difficult to fuzz as feedback mechanisms (i.e., guided code coverage) cannot be easily applied. Additionally, non-determinism due to interrupts, kernel threads, statefulness, and similar mechanisms poses problems. Furthermore, if a process fuzzes its own kernel, a kernel crash highly impacts the performance of the fuzzer as the OS needs to reboot.

In this paper, we approach the problem of coverage-guided kernel fuzzing in an OS-independent and hardware-assisted way: We utilize a hypervisor and Intel’s Processor Trace (PT) technology. This allows us to remain independent of the target OS as we just require a small user space component that interacts with the targeted OS. As a result, our approach introduces almost no performance overhead, even in cases where the OS crashes, and performs up to 17,000 executions per second on an off-the-shelf laptop. We developed a framework called kernel-AFL (kAFL) to assess the security of Linux, macOS, and Windows kernel components. Among many crashes, we uncovered several flaws in the ext4 driver for Linux, the HFS and APFS file system of macOS, and the NTFS driver of Windows.


### DIFUZE: Interface aware fuzzing for kernel drivers (CCS 2017)

* <img src="image/wechat_24px.png">[Reading Note From BAIZE](https://mp.weixin.qq.com/s/5-2PDBlRSW_kTJb1SW1spQ)

* <img src="image/pdf_24px.png">[Paper](./Paper/CCS17_DIFUZE.pdf)

* <img src="image/github_24px.png">[Code](https://github.com/ucsb-seclab/difuze)

**Abstract:** Device drivers are an essential part in modern Unix-like systems to handle operations on physical devices, from hard disks and printers to digital cameras and Bluetooth speakers. The surge of new hardware, particularly on mobile devices, introduces an explosive growth of device drivers in system kernels. Many such drivers are provided by third-party developers, which are susceptible to security vulnerabilities and lack proper vetting. Unfortunately, the complex input data structures for device drivers render traditional analysis tools, such as fuzz testing, less effective, and so far, research on kernel driver security is comparatively sparse. In this paper, we present DIFUZE, an interface-aware fuzzing tool to automatically generate valid inputs and trigger the execution of the kernel drivers. We leverage static analysis to compose correctly-structured input in the userspace to explore kernel drivers. DIFUZE is fully automatic, ranging from identifying driver handlers, to mapping to device file names, to constructing complex argument instances. We evaluate our approach on seven modern Android smartphones. The results showthat DIFUZE can effectively identify kernel driver bugs, and reports 32 previously unknown vulnerabilities, including flaws that lead to arbitrary code execution.



# Hybrid Fuzzing:

### SAVIOR: Towards Bug-Driven Hybrid Testing (S&P 2020)

Hybrid testing combines fuzz testing and concolic execution. It leverages fuzz testing to test easy-to-reach code regions and uses concolic execution to explore code blocks guarded by complex branch conditions. As a result, hybrid testing is able to reach deeper into program state space than fuzz testing or concolic execution alone. Recently, hybrid testing has seen significant advancement. However, its code coveragecentric design is inefficient in vulnerability detection. First, it blindly selects seeds for concolic execution and aims to explore new code continuously. However, as statistics shows, a large portion of the explored code is often invulnerable. Therefore, giving equal attention to every part of the code during hybrid testing is a non-optimal strategy. It also slows down the detection of real vulnerabilities by over 43%. Second, classic hybrid testing quickly moves on after reaching a chunk of code, rather than examining the hidden defects inside. It may frequently miss subtle yet exploitable vulnerabilities despite that it has already explored the vulnerable code paths.

We propose SAVIOR, a new hybrid testing framework pioneering a bug-driven principle. Unlike the existing hybrid testing tools, SAVIOR prioritizes the concolic execution of the seeds that are likely to uncover more vulnerabilities. Moreover, SAVIOR verifies all vulnerable program locations along the executing program path. By modeling faulty situations using SMT constraints, SAVIOR reasons the feasibility of vulnerabilities and generates concrete test cases as proofs. Our evaluation shows that the bugdriven approach outperforms the mainstream automated testing techniques, including the state-of-the-art hybrid testing driven by code coverage. On average, SAVIOR detects vulnerabilities 43.4% faster than DRILLER and 44.3% faster than QSYM, leading to the discovery of 88 and 76 more security violations, respectively. According to the experimental result on 11 well-fuzzed benchmark programs, SAVIOR triggers 481 unique security violations within the first 24 hours.


### Send Hardest Problems My Way: Probabilistic Path Prioritization for Hybrid Fuzzing (NDSS 2019)

* <img src="image/pdf_24px.png">[Paper](./Paper/NDSS19_Probabilistic.pdf)

**Abstract:** Hybrid fuzzing which combines fuzzing and concolic execution has become an advanced technique for software vulnerability detection. Based on the observation that fuzzing and concolic execution are complementary in nature, the state-of-the-art hybrid fuzzing systems deploy "demand launch" and "optimal switch" strategies. Although these ideas sound intriguing, we point out several fundamental limitations in them, due to oversimplified assumptions. We then propose a novel "discriminative dispatch" strategy to better utilize the capability of concolic execution. We design a novel Monte Carlo based probabilistic path prioritization model to quantify each path's difficulty and prioritize them for concolic execution. This model treats fuzzing as a random sampling process. It calculates each path's probability based on the sampling information. Finally, our model prioritizes and assigns the most difficult paths to concolic execution. We implement a prototype system DigFuzz and evaluate our system with two representative datasets. Results show that the concolic execution in DigFuzz outperforms than that in a state-of-the-art hybrid fuzzing system Driller in every major aspect. In particular, the concolic execution in DigFuzz contributes to discovering more vulnerabilities (12 vs. 5) and producing more code coverage (18.9% vs. 3.8%) on the CQE dataset than the concolic execution in Driller.


### QSYM: A Practical Concolic Execution Engine Tailored for Hybrid Fuzzing (USENUX Security2018)

* <img src="image/youdao_note_24px.png">[Reading Note](http://note.youdao.com/noteshare?id=f086faa409a5c6dfabb382e6747381c5&sub=AD1D3F4E3EBC4DCD85694DCAC43EA32B)

* <img src="image/pdf_24px.png">[Paper](./Paper/USENUX18_QSYM.pdf)

* <img src="image/github_24px.png">[Code]([./Paper/USENUX18_QSYM.pdf](https://github.com/sslab-gatech/qsym))


**Abstract:** Recently, hybrid fuzzing has been proposed to address the limitations of fuzzing and concolic execution by combining both approaches. The hybrid approach has shown its effectiveness in various synthetic benchmarks such as DARPA Cyber Grand Challenge (CGC) binaries, but it still suffers from scaling to find bugs in complex, real-world software. We observed that the performance bottleneck of the existing concolic executor is the main limiting factor for its adoption beyond a small-scale study.
To overcome this problem, we design a fast concolic execution engine, called QSYM, to support hybrid fuzzing. The key idea is to tightly integrate the symbolic emulation with the native execution using dynamic binary translation, making it possible to implement more fine-grained, so faster, instruction-level symbolic emulation. Additionally, QSYM loosens the strict soundness requirements of conventional concolic executors for better performance, yet takes advantage of a faster fuzzer for validation, providing unprecedented opportunities for performance optimizations, e.g., optimistically solving constraints and pruning uninteresting basic blocks.
Our evaluation shows that QSYM does not just outperform state-of-the-art fuzzers (i.e., found 14× more bugs than VUzzer in the LAVA-M dataset, and outperformed Driller in 104 binaries out of 126), but also found 13 previously unknown security bugs in eight real-world programs like Dropbox Lepton, ffmpeg, and OpenJPEG, which have already been intensively tested by the state-of-the-art fuzzers, AFL and OSS-Fuzz.


### Angora: Efficient Fuzzing by Principled Search (S&P 2018)

* <img src="image/youdao_note_24px.png">[Reading Note](https://securitygossip.com/blog/2019/01/03/angora-efficient-fuzzing-by-principled-search/)

* <img src="image/pdf_24px.png">[Paper](./Paper/SP18_Angora.pdf)

* <img src="image/github_24px.png">[Code](https://github.com/AngoraFuzzer/Angora)

**Abstract:** Abstract-Fuzzing is a popular technique for finding software bugs. However, the performance of the state-of-the-art fuzzers leaves a lot to be desired. Fuzzers based on symbolic execution produce quality inputs but run slow, while fuzzers based on random mutation run fast but have difficulty producing quality inputs. We propose Angora, a new mutation-based fuzzer that outperforms the state-of-the-art fuzzers by a wide margin. The main goal of Angora is to increase branch coverage by solving path constraints without symbolic execution. To solve path constraints efficiently, we introduce several key techniques: scalable byte-level taint tracking, context-sensitive branch count, search based on gradient descent, and input length exploration. On the LAVA-M data set, Angora found almost all the injected bugs, found more bugs than any other fuzzer that we compared with, and found eight times as many bugs as the second-best fuzzer in the program who. Angora also found 103 bugs that the LAVA authors injected but could not trigger. We also tested Angora on eight popular, mature open source programs. Angora found 6, 52, 29, 40 and 48 new bugs in file, jhead, nm, objdump and size, respectively. We measured the coverage of Angora and evaluated how its key techniques contribute to its impressive performance.


### Driller: Argumenting Fuzzing Through Selective Symbolic Execution (NDSS 2016)

* <img src="image/pdf_24px.png">[Paper](./Paper/NDSS16_Driller.pdf)

**Abstract:** Memory corruption vulnerabilities are an everpresent risk in software, which attackers can exploit to obtain unauthorized access to confidential information. As products with access to sensitive data are becoming more prevalent, the number of potentially exploitable systems is also increasing, resulting in a greater need for automated software vetting tools. DARPA recently funded a competition, with millions of dollars in prize money, to further research focusing on automated vulnerability finding and patching, showing the importance of research in this area. Current techniques for finding potential bugs include static, dynamic, and concolic analysis systems, which each having their own advantages and disadvantages. A common limitation of systems designed to create inputs which trigger vulnerabilities is that they only find shallow bugs and struggle to exercise deeper paths in executables. We present Driller, a hybrid vulnerability excavation tool which leverages fuzzing and selective concolic execution in a complementary manner, to find deeper bugs. Inexpensive fuzzing is used to exercise compartments of an application, while concolic execution is used to generate inputs which satisfy the complex checks separating the compartments. By combining the strengths of the two techniques, we mitigate their weaknesses, avoiding the path explosion inherent in concolic analysis and the incompleteness of fuzzing. Driller uses selective concolic execution to explore only the paths deemed interesting by the fuzzer and to generate inputs for conditions that the fuzzer cannot satisfy. We evaluate Driller on 126 applications released in the qualifying event of the DARPA Cyber Grand Challenge and show its efficacy by identifying the same number of vulnerabilities, in the same time, as the top-scoring team of the qualifying event.

**Note:** 我们都知道，fuzzing对于一些比较宽松的限制(比如x>0)能够很容易的通过变异产生一些输入达到该条件；而symbolic execution非常擅长求解一下magic value(比如x == deadleaf)。这是一篇比较经典的将concolic execution和fuzzing结合在一起的文章，该文章的主要思想就是先用AFL等Fuzzer根据seed进行变异，来测试程序。当产生的输入一直走某些路径，并没有探测到新的路径时，此时就"stuck"了。这时，就是用concolic execution来产生输入，保证该输入能走到一些新的分支。从而利用concolic execution来辅助fuzz。



# Addressing Magic bytes \ checksum: 

### REDQUEEN: Fuzzing with Input-to-State Correspondence (NDSS2019)

* <img src="image/youdao_note_24px.png">[Reading Note](http://note.youdao.com/noteshare?id=6a4b00d912eab145d1c1f32f11bde3e0&sub=7DADC02169A14B33979BCCB2556E4526)

* <img src="image/pdf_24px.png">[Paper](./Paper/NDSS19_REDQUEEN.pdf)

**Abstract:** Automated software testing based on fuzzing has experienced a revival in recent years. Especially feedback-driven fuzzing has become well-known for its ability to efficiently perform randomized testing with limited input corpora. Despite a lot of progress, two common problems are magic numbers and (nested) checksums. Computationally expensive methods such as taint tracking and symbolic execution are typically used to overcome such roadblocks. Unfortunately, such methods often require access to source code, a rather precise description of the environment (e.g., behavior of library calls or the underlying OS), or the exact semantics of the platform's instruction set.
In this paper, we introduce a lightweight, yet very effective alternative to taint tracking and symbolic execution to facilitate and optimize state-of-the-art feedback fuzzing that easily scales to large binary applications and unknown environments. We observe that during the execution of a given program, parts of the input often end up directly (i.e., nearly unmodified) in the program state. This input-to-state correspondence can be exploited to create a robust method to
overcome common fuzzing roadblocks in a highly effective and efficient manner. Our prototype implementation, called REDQUEEN, is able to solve magic bytes and (nested) checksum tests automatically for a given binary executable. Additionally, we show that our techniques outperform various state-of-the-art tools on a wide variety of targets across different privilege levels (kernel-space and userland) with no platform-specific code. REDQUEEN is the first method to find more than 100% of the bugs planted in LAVA-M across all targets. Furthermore, we were able to discover 65 new bugs and obtained 16 CVEs in multiple programs and OS kernel drivers. Finally, our evaluation demonstrates that REDQUEEN is fast, widely applicable and outperforms concurrent approaches by up to three orders of magnitude.


### T-Fuzz: fuzzing by program transformation (S&P 2018)

* <img src="image/youdao_note_24px.png">[Reading Note](https://blog.csdn.net/Chen_zju/article/details/80934710)

* <img src="image/pdf_24px.png">[Paper](./Paper/SP18_T-Fuzz.pdf)

* <img src="image/github_24px.png">[Code]([https://github.com/Ljiee/fairfuzz](https://github.com/HexHive/T-Fuzz))

**Abstract:** Fuzzing is a simple yet effective approach to discover software bugs utilizing randomly generated inputs. However, it is limited by coverage and cannot find bugs hidden in deep execution paths of the program because the randomly generated inputs fail complex sanity checks, e.g., checks on magic values, checksums, or hashes. To improve coverage, existing approaches rely on imprecise heuristics or complex input mutation techniques (e.g., symbolic execution or taint analysis) to bypass sanity checks. Our novel method tackles coverage from a different angle: by removing sanity checks in the target program. T-Fuzz leverages a coverage-guided fuzzer to generate inputs. Whenever the fuzzer can no longer trigger new code paths, a light-weight, dynamic tracing based technique detects the input checks that the fuzzer-generated inputs fail. These checks are then removed from the target program. Fuzzing then continues on the transformed program, allowing the code protected by the removed checks to be triggered and potential bugs discovered. Fuzzing transformed programs to find bugs poses two challenges: (1) removal of checks leads to over-approximation and false positives, and (2) even for true bugs, the crashing input on the transformed program may not trigger the bug in the original program. As an auxiliary post-processing step, T-Fuzz leverages a symbolic execution-based approach to filter out false positives and reproduce true bugs in the original program. By transforming the program as well as mutating the input, T-Fuzz covers more code and finds more true bugs than any existing technique. We have evaluated T-Fuzz on the DARPA Cyber Grand Challenge dataset, LAVA-M dataset and 4 real-world programs (pngfix, tiffinfo, magick and pdftohtml). For the CGC dataset, T-Fuzz finds bugs in 166 binaries, Driller in 121, and AFL in 105. In addition, found 3 new bugs in previously-fuzzed programs and libraries.


### FairFuzz: A Targeted Mutation Strategy for Increasing Greybox Fuzz Testing Coverage (ASE 2018)

* <img src="image/youdao_note_24px.png">[Reading Note](http://note.youdao.com/noteshare?id=5525c7a18e8681302229e9466290aac2&sub=C4769EA799584C5D89994FE397F76981)

* <img src="image/pdf_24px.png">[Paper](./Paper/ASE18_Fairfuzz.pdf)

* <img src="image/github_24px.png">[Code](https://github.com/Ljiee/fairfuzz)

**Abstract:** In recent years, fuzz testing has proven itself to be one of the most effective techniques for finding correctness bugs and security vulnerabilities in practice. One particular fuzz testing tool, American Fuzzy Lop (AFL), has become popular thanks to its ease-of-use and bug-finding power. However, AFL remains limited in the bugs it can find since it simply does not cover large regions of code. If it does not cover parts of the code, it will not find bugs there. We propose a two-pronged approach to increase the coverage achieved by AFL. First, the approach automatically identifies branches exercised by few AFL-produced inputs (rare branches), which often guard code that is empirically hard to cover by naively mutating inputs. The second part of the approach is a novel mutation mask creation algorithm, which allows mutations to be biased towards producing inputs hitting a given rare branch. This mask is dynamically computed during fuzz testing and can be adapted to other testing targets. We implement this approach on top of AFL in a tool named FairFuzz. We conduct evaluation on real-world programs against state-of-the-art versions of AFL. We find that on these programs FairFuzz achieves high branch coverage at a faster rate that state-of-the-art versions of AFL. In addition, on programs with nested conditional structure, it achieves sustained increases in branch coverage after 24 hours (average 10.6% increase). In qualitative analysis, we find that FairFuzz has an increased capacity to automatically discover keywords.


### VUzzer: Application-aware Evolutionary Fuzzing (NDSS 2017)

* <img src="image/youdao_note_24px.png">[Reading Note](http://note.youdao.com/noteshare?id=b0505524143c5f9439c6a5d9dcff9b1d&sub=D8A73723348B4976BA191B235EB13307)

* <img src="image/pdf_24px.png">[Paper](./Paper/NDSS17_Vuzzer.pdf)

* <img src="image/github_24px.png">[Code](https://github.com/vusec/vuzzer)

**Abstract:** Fuzzing is an effective software testing technique to find bugs. Given the size and complexity of real-world applications, modern fuzzers tend to be either scalable, but not effective in exploring bugs that lie deeper in the execution, or capable of penetrating deeper in the application, but not scalable.
In this paper, we present an application-aware evolutionary fuzzing strategy that does not require any prior knowledge of the application or input format. In order to maximize coverage and explore deeper paths, we leverage control- and data-flow features based on static and dynamic analysis to infer fundamental properties of the application. This enables much faster generation of interesting inputs compared to an application-agnostic approach. We implement our fuzzing strategy in VUzzer and evaluate it on three different datasets: DARPA Grand Challenge binaries (CGC), a set of real-world applications (binary input parsers), and the recently released LAVA dataset. On all of these datasets, VUzzer yields significantly better results than state-of-the-art fuzzers, by quickly finding several existing and new bugs.



# Inputs-aware Fuzzing

### Parser-Directed Fuzzing (PLDI 2019)

* <img src="image/pdf_24px.png">[Paper](./Paper/PLDI19_Parser.pdf)

**Abstract:** To be effective, software test generation needs to well cover the space of possible inputs. Traditional fuzzing generates large numbers of random inputs, which however are unlikely to contain keywords and other specific inputs of non-trivial input languages. Constraint-based test generation solves conditions of paths leading to uncovered code, but fails on programs with complex input conditions because of path explosion.
In this paper, we present a test generation technique specifically directed at input parsers. We systematically produce inputs for the parser and track comparisons made; after every rejection, we satisfy the comparisons leading to rejection. This approach effectively covers the input space: Evaluated on five subjects, from CSV files to JavaScript, our pFuzzer prototype covers more tokens than both random-based and constraint-based approaches, while requiring no symbolic analysis and far fewer tests than random fuzzers.


### SLF: Fuzzing without Valid Seed Inputs (ICSE 2019)

* <img src="image/pdf_24px.png">[Paper](./Paper/ICSE19_SLF.pdf)

**Abstract:** Fuzzing is an important technique to detect software bugs and vulnerabilities. It works by mutating a small set of seed inputs to generate a large number of new inputs. Fuzzers’ performance often substantially degrades when valid seed inputs are not available. Although existing techniques such as symbolic execution can generate seed inputs from scratch, they have various limitations hindering their applications in real-world complex software without source code. In this paper, we propose a novel fuzzing technique that features the capability of generating valid seed inputs. It piggy-backs on AFL to identify input validity checks and the input fields that have impact on such checks. It further classifies these checks according to their relations to the input. Such classes include arithmetic relation, object offset, data structure length and so on. A multi-goal search algorithm is developed to apply class specific mutations in order to satisfy inter-dependent checks all together. We evaluate our technique on 20 popular benchmark programs collected from other fuzzing projects and the Google fuzzer test suite, and compare it with existing fuzzers AFL and AFLFast, symbolic execution engines KLEE and S2E, and a hybrid tool Driller that combines fuzzing with symbolic execution. The results show that our technique is highly effective and efficient, out-performing the other tools.


### Superion: Grammar-Aware Greybox Fuzzing (ICSE 2019)

* <img src="image/pdf_24px.png">[Paper](./Paper/ICSE19_Superion.pdf)

**Abstract:** In recent years, coverage-based greybox fuzzing has proven itself to be one of the most effective techniques for finding security bugs in practice. Particularly, American Fuzzy Lop (AFL for short) is deemed to be a great success in fuzzing relatively simple test inputs. Unfortunately, when it meets structured test inputs such as XML and JavaScript, those grammar-blind trimming and mutation strategies in AFL hinder the effectiveness and efficiency. To this end, we propose a grammar-aware coverage-based grey-box fuzzing approach to fuzz programs that process structured inputs. Given the grammar (which is often publicly available) of test inputs, we introduce a grammar-aware trimming strategy to trim test inputs at the tree level using the abstract syntax trees (ASTs) of parsed test inputs. Further, we introduce two grammar-aware mutation strategies (i.e., enhanced dictionary-based mutation and tree-based mutation). Specifically, tree-based mutation works via replacing subtrees using the ASTs of parsed test inputs. Equipped with grammar-awareness, our approach can carry the fuzzing exploration into width and depth. We implemented our approach as an extension to AFL, named Superion; and evaluated the effectiveness of Superion on real-life large-scale programs (a XML engine libplist and three JavaScript engines WebKit, Jerryscript and ChakraCore). Our results have demonstrated that Superion can improve the code coverage (i.e., 16.7% and 8.8% in line and function coverage) and bug-finding capability (i.e., 30 new bugs, among which we discovered 21 new vulnerabilities with 16 CVEs assigned and 3.2K USD bug bounty rewards received) over AFL and jsfunfuzz.


### ProFuzzer: On-the-fly Input Type Probing for Better Zero-day Vulnerability Discovery (S&P 2019)

* <img src="image/youdao_note_24px.png">[Reading Note](http://note.youdao.com/noteshare?id=8e905e9d299cae5ceb3bbeac0591cfab&sub=9FCAB3A8AD4C48689095307EDD1A940A)

* <img src="image/pdf_24px.png">[Paper](./Paper/SP19_Profuzz.pdf)

* <img src="image/github_24px.png">[Code](https://github.com/profuzzer)

**Abstract:** Existing mutation based fuzzers tend to randomly mutate the input of a program without understanding its underlying syntax and semantics. In this paper, we propose a novel on-the-fly probing technique (called ProFuzzer) that automatically recovers and understands input fields of critical importance to vulnerability discovery during a fuzzing process and intelligently adapts the mutation strategy to enhance the chance of hitting zero-day targets. Since such probing is transparently piggybacked to the regular fuzzing, no prior knowledge of the input specification is needed. During fuzzing, individual bytes are first mutated and their fuzzing results are automatically analyzed to link those related together and identify the type for the field connecting them; these bytes are further mutated together following type-specific strategies, which substantially prunes the search space. We define the probe types generally across all applications, thereby making our technique application agnostic. Our experiments on standard benchmarks and real-world applications show that ProFuzzer substantially outperforms AFL and its optimized version AFLFast, as well as other state-of-art fuzzers including VUzzer, Driller and QSYM. Within two months, it exposed 42 zero-days in 10 intensively tested programs, generating 30 CVEs.


### CodeAlchemist: Semantics-Aware Code Generation to Find Vulnerabilities in JavaScript Engines (NDSS 2019)

* <img src="image/pdf_24px.png">[Paper](./Paper/NDSS2019_CodeAlchemist.pdf)

* <img src="image/ppt_24px.png">[Slides](./Paper/NDSS2019_CodeAlchemist_slidesz.pdf)

**Abstract:** JavaScript engines are an attractive target for attackers due to their popularity and flexibility in building exploits. Current state-of-the-art fuzzers for finding JavaScript engine vulnerabilities focus mainly on generating syntactically correct test cases based on either a predefined context-free grammar or a trained probabilistic language model. Unfortunately, syntactically correct JavaScript sentences are often semantically invalid at runtime. Furthermore, statically analyzing the semantics of JavaScript code is challenging due to its dynamic nature: JavaScript code is generated at runtime, and JavaScript expressions are dynamically-typed. To address this challenge, we propose a novel test case generation algorithm that we call semantics-aware assembly, and implement it in a fuzz testing tool termed CodeAlchemist. Our tool can generate arbitrary JavaScript code snippets that are both semantically and syntactically correct, and it effectively yields test cases that can crash JavaScript engines. We found numerous vulnerabilities of the latest JavaScript engines with CodeAlchemist and reported them to the vendors.

### TIFF: Using Input Type Inference To Improve Fuzzing (ACSAC 2018)

* <img src="image/pdf_24px.png">[Paper](./Paper/ACSAC18_TIFF.pdf)

**Abstract:** Developers commonly use fuzzing techniques to hunt down all manner of memory corruption vulnerabilities during the testing phase. Irrespective of the fuzzer, input mutation plays a central role in providing adequate code coverage, as well as in triggering bugs. However, each class of memory corruption bugs requires a different trigger condition. While the goal of a fuzzer is to find bugs, most existing fuzzers merely approximate this goal by targeting their mutation strategies toward maximizing code coverage. 

In this work, we present a new mutation strategy that maximizes the likelihood of triggering memory-corruption bugs by generating fewer, but better inputs. In particular, our strategy achieves bug- directed mutation by inferring the type of the input bytes. To do so, it tags each offset of the input with a basic type (e.g., 32-bit integer, string, array etc.), while deriving mutation rules for specific classes of bugs, We infer types by means of in-memory data-structure identification and dynamic taint analysis, and implement our novel mutation strategy in a fully functional fuzzer which we call TIFF (Type Inference-based Fuzzing Framework). Our evaluation on real-world applications shows that type-based fuzzing triggers bugs much earlier than existing solutions, while maintaining high code coverage. For example, on several real-world applications and libraries (e.g., poppler, mpg123 etc.), we find real bugs (with known CVEs) in almost half of the time and upto an order of magnitude fewer inputs than state-of-the-art fuzzers.



# Directed Fuzzing

### Directed Greybox Fuzzing (CCS 2017)

* <img src="image/pdf_24px.png">[Paper](./Paper/CCS17_aflgo.pdf)
  
* <img src="image/github_24px.png">[Code](https://github.com/aflgo/aflgo)
  
**Abstract:** Existing Greybox Fuzzers (GF) cannot be effectively directed, for instance, towards problematic changes or patches, towards critical system calls or dangerous locations, or towards functions in the stack-trace of a reported vulnerability that we wish to reproduce. In this paper, we introduce Directed Greybox Fuzzing (DGF) which generates inputs with the objective of reaching a given set of target program locations efficiently. We develop and evaluate a simulated annealing-based power schedule that gradually assigns more energy to seeds that are closer to the target locations while reducing energy for seeds that are further away. Experiments with our implementation AFLGo demonstrate that DGF outperforms both directed symbolic-execution-based whitebox fuzzing and undirected greybox fuzzing. We show applications of DGF to patch testing and crash reproduction, and discuss the integration of AFLGo into Google's continuous fuzzing platform OSS-Fuzz. Due to its directedness, AFLGo could find 39 bugs in several well-fuzzed, security-critical projects like LibXML2. 17 CVEs were assigned.


### Hawkeye: Towards a Desired Directed Grey-box Fuzzer (CCS 2018)

* <img src="image/youdao_note_24px.png">[Reading Note](https://note.youdao.com/ynoteshare1/index.html?id=6e9c7bba068ab022571e660ddd49c8fc&type=note#/)

* <img src="image/pdf_24px.png">[Paper](./Paper/CCS18_hawkeye.pdf)

**Abstract:** Grey-box fuzzing is a practically effective approach to test real-world programs. However, most existing grey-box fuzzers lack directedness, i.e. the capability of executing towards user-specified target sites in the program. To emphasize existing challenges in directed fuzzing, we propose Hawkeye to feature four desired properties of directed grey-box fuzzers. Owing to a novel static analysis on the program under test and the target sites, Hawkeye precisely collects the information such as the call graph, function and basic block level distances to the targets. During fuzzing, Hawkeye evaluates exercised seeds based on both static information and the execution traces to generate the dynamic metrics, which are then used for seed prioritization, power scheduling and adaptive mutating. These strategies help Hawkeye to achieve better directedness and gravitate towards the target sites. We implemented Hawkeye as a fuzzing framework and evaluated it on various real-world programs under different scenarios. The experimental results showed that Hawkeye can reach the target sites and reproduce the crashes much faster than state-of-the-art grey-box fuzzers such as AFL and AFLGo. Specially, Hawkeye can reduce the time to exposure for certain vulnerabilities from about 3.5 hours to 0.5 hour. By now, Hawkeye has detected more than 41 previously unknown crashes in projects such as Oniguruma, MJS with the target sites provided by vulnerability prediction tools; all these crashes are confirmed and 15 of them have been assigned CVE IDs.



# Addressing Collision:

### CollAFL: Path Sensitive Fuzzing (S&P 2018)

* <img src="image/youdao_note_24px.png">[Reading Note](http://note.youdao.com/noteshare?id=35d81c8856c520a17e27c66efd32a303&sub=229B45E6622E4995A3D7C63E529AE023)

* <img src="image/pdf_24px.png">[Paper](./Paper/SP18_ColLAFL.pdf)

**Abstract:** Coverage-guided fuzzing is a widely used and ef- fective solution to find software vulnerabilities. Tracking code coverage and utilizing it to guide fuzzing are crucial to coverage- guided fuzzers. However, tracking full and accurate path coverage is infeasible in practice due to the high instrumentation overhead. Popular fuzzers (e.g., AFL) often use coarse coverage information, e.g., edge hit counts stored in a compact bitmap, to achieve highly efficient greybox testing. Such inaccuracy and incompleteness in coverage introduce serious limitations to fuzzers. First, it causes path collisions, which prevent fuzzers from discovering potential paths that lead to new crashes. More importantly, it prevents fuzzers from making wise decisions on fuzzing strategies. In this paper, we propose a coverage sensitive fuzzing solution CollAFL. It mitigates path collisions by providing more accurate coverage information, while still preserving low instrumentation overhead. It also utilizes the coverage information to apply three new fuzzing strategies, promoting the speed of discovering new paths and vulnerabilities. We implemented a prototype of CollAFL based on the popular fuzzer AFL and evaluated it on 24 popular applications. The results showed that path collisions are common, i.e., up to 75% of edges could collide with others in some applications, and CollAFL could reduce the edge collision ratio to nearly zero. Moreover, armed with the three fuzzing strategies, CollAFL outperforms AFL in terms of both code coverage and vulnerability discovery. On average, CollAFL covered 20% more program paths, found 320% more unique crashes and 260% more bugs than AFL in 200 hours. In total, CollAFL found 157 new security bugs with 95 new CVEs assigned.



# Fuzzing Overhead & Performance：

### Full-speed Fuzzing: Reducing Fuzzing Overhead through Coverage-guided Tracing (S&P 2019)

* <img src="image/pdf_24px.png">[Paper](./Paper/SP19_Full-speed.pdf)

**Abstract:** Coverage-guided fuzzing is one of the most successful approaches for discovering software bugs and security vulnerabilities. Of its three main components: (1) test case generation, (2) code coverage tracing, and (3) crash triage, code coverage tracing is a dominant source of overhead. Coverage-guided fuzzers trace every test case's code coverage through either static or dynamic binary instrumentation, or more recently, using hardware support. Unfortunately, tracing all test cases incurs significant performance penalties--even when the overwhelming majority of test cases and their coverage information are discarded because they do not increase code coverage. To eliminate needless tracing by coverage-guided fuzzers, we introduce the notion of coverage-guided tracing. Coverage-guided tracing leverages two observations: (1) only a fraction of generated test cases increase coverage, and thus require tracing; and (2) coverage-increasing test cases become less frequent over time. Coverage-guided tracing encodes the current frontier of coverage in the target binary so that it self-reports when a test case produces new coverage--without tracing. This acts as a filter for tracing; restricting the expense of tracing to only coverage-increasing test cases. Thus, coverage-guided tracing trades increased time handling coverage-increasing test cases for decreased time handling non-coverage-increasing test cases. To show the potential of coverage-guided tracing, we create an implementation based on the static binary instrumentor Dyninst called UnTracer. We evaluate UnTracer using eight real-world binaries commonly used by the fuzzing community. Experiments show that after only an hour of fuzzing, UnTracer's average overhead is below 1%, and after 24-hours of fuzzing, UnTracer approaches 0% overhead, while tracing every test case with popular white- and black-box-binary tracers AFL-Clang, AFL-QEMU, and AFL-Dyninst incurs overheads of 36%, 612%, and 518%, respectively. We further integrate UnTracer with the state-of-the-art hybrid fuzzer QSYM and show that in 24-hours of fuzzing, QSYM-UnTracer executes 79% and 616% more test cases than QSYM-Clang and QSYM-QEMU, respectively.


### Designing New Operating Primitives to Improve Fuzzing Performance (CCS 2017)

* <img src="image/pdf_24px.png">[Paper](./Paper/CCS17_Designing.pdf.pdf)

* <img src="image/github_24px.png">[Code](https://github.com/sslab-gatech/perf-fuzz)

**Abstract:** Fuzzing is a software testing technique that finds bugs by repeatedly injecting mutated inputs to a target program. Known to be a highly practical approach, fuzzing is gaining more popularity than ever before. Current research on fuzzing has focused on producing an input that is more likely to trigger a vulnerability.
In this paper, we tackle another way to improve the performance of fuzzing, which is to shorten the execution time of each iteration. We observe that AFL, a state-of-the-art fuzzer, slows down by 24x because of file system contention and the scalability of fork() system call when it runs on 120 cores in parallel. Other fuzzers are expected to suffer from the same scalability bottlenecks in that they follow a similar design pattern. To improve the fuzzing performance, we design and implement three new operating primitives specialized for fuzzing that solve these performance bottlenecks and achieve scalable performance on multi-core machines. Our experiment shows that the proposed primitives speed up AFL and LibFuzzer by 6.1 to 28.9x and 1.1 to 735.7x, respectively, on the overall number of executions per second when targeting Google's fuzzer test suite with 120 cores. In addition, the primitives improve AFL's throughput up to 7.7x with 30 cores, which is a more common setting in data centers. Our fuzzer-agnostic primitives can be easily applied to any fuzzer with fundamental performance improvement and directly benefit large-scale fuzzing and cloud-based fuzzing services.



# Enhancing Memory Error:

### Enhancing Memory Error Detection for Large-Scale Applications and Fuzz Testing (NDSS 2018)

* <img src="image/youdao_note_24px.png">[Reading Note](http://note.youdao.com/noteshare?id=6228fef31b29b4ffbbbe1c1d80ef3fa0&sub=CB0D15A0D6394FA188C06B2BCB6367A3)

* <img src="image/pdf_24px.png">[Paper](./Paper/NDSS18_Enhancing_Paper.pdf)

* <img src="image/ppt_24px.png">[Slides](./Paper/NDSS18_Enhancing_Slides.pdf)

**Abstract:** Memory errors are one of the most common vulnerabilities for the popularity of memory unsafe languages including C and C++. Once exploited, it can easily lead to system crash (i.e., denial-of-service attacks) or allow adversaries to fully compromise the victim system. This paper proposes MEDS, a practical memory error detector. MEDS significantly enhances its detection capability by approximating two ideal properties, called an infinite gap and an infinite heap. The approximated infinite gap of MEDS setups large inaccessible memory region between objects (i.e., 4 MB), and the approximated infinite heap allows MEDS to fully utilize virtual address space (i.e., 45-bits memory space). The key idea of MEDS in achieving these properties is a novel user-space memory allocation mechanism, MEDSALLOC. MEDSALLOC leverages a page aliasing mechanism, which allows MEDS to maximize the virtual memory space utilization but minimize the physical memory uses. To highlight the detection capability and practical impacts of MEDS, we evaluated and then compared to Google’s state-of-the-art detection tool, AddressSanitizer. MEDS showed three times better detection rates on four real-world vulnerabilities in Chrome and Firefox. More importantly, when used for a fuzz testing, MEDS was able to identify 68.3% more memory errors than AddressSanitizer for the same amount of a testing time, highlighting its practical aspects in the software testing area. In terms of performance overhead, MEDS slowed down 108% and 86% compared to native execution and AddressSanitizer, respectively, on real-world applications including Chrome, Firefox, Apache, Nginx, and OpenSSL.


### AddressSanitizer: A Fast Address Sanity Checker  (USENUX Security2012)

* <img src="image/pdf_24px.png">[Paper](https://www.usenix.org/system/files/conference/atc12/atc12-final39.pdf)

* <img src="image/ppt_24px.png">[Slides](https://www.usenix.org/sites/default/files/conference/protected-files/serebryany_atc12_slides.pdf)

Memory access bugs, including buffer overflows and uses of freed heap memory, remain a serious problem for programming languages like C and C++. Many memory error detectors exist, but most of them are either slow or detect a limited set of bugs, or both.
This paper presents AddressSanitizer, a new memory error detector. Our tool finds out-of-bounds accesses to heap, stack, and global objects, as well as use-after-free bugs. It employs a specialized memory allocator and code instrumentation that is simple enough to be implemented in any compiler, binary translation system, or even in hardware.
AddressSanitizer achieves efficiency without sacrificing comprehensiveness. Its average slowdown is just 73% yet it accurately detects bugs at the point of occurrence. It has found over 300 previously unknown bugs in the Chromium browser and many bugs in other software.



# Schedule (Power & Mutation)

### MOPT: Optimize Mutation Scheduling for Fuzzers (USENUX Security2019)

* <img src="image/pdf_24px.png">[Paper](./Paper/USENUX19_MOPT.pdf)

* <img src="image/github_24px.png">[Code](https://github.com/puppet-meteor/MOpt-AFL)

**Abstract:** MOpt is a novel mutation scheduling scheme, which enables mutation-based fuzzers to discover vulnerabilities more efficiently. MOPT utilizes a customized Particle Swarm Optimization (PSO) algorithm to find the optimal selection probability distribution of operators with respect to fuzzing effectiveness, and provides a pacemaker fuzzing mode to accelerate the convergence speed of PSO. MOPT provides a good rationality, compatibility and steadiness, while introducing negligible costs. We make MOpt-AFL (one of the applications of MOpt-based fuzzers), seed sets used in the evaluation, results and the technical report with more details publicly available to facilitate the research in this area, which is available at: https://github.com/puppet-meteor/MOpt-AFL .


### Coverage-based Greybox Fuzzing as Markov Chain (CCS 2016)

* <img src="image/pdf_24px.png">[Paper](./Paper/CCS16_Markov_Chain.pdf)

* <img src="image/github_24px.png">[Code](https://github.com/mboehme/aflfast)

**Abstract:** Coverage-based Greybox Fuzzing (CGF) is a random testing approach that requires no program analysis. A new test is generated by slightly mutating a seed input. If the test exercises a new and interesting path, it is added to the set of seeds; otherwise, it is discarded. We observe that most tests exercise the same few "high-frequency" paths and develop strategies to explore significantly more paths with the same number of tests by gravitating towards low-frequency paths. We explain the challenges and opportunities of CGF using a Markov chain model which specifies the probability that fuzzing the seed that exercises path i generates an input that exercises path j. Each state (i.e., seed) has an energy that specifies the number of inputs to be generated from that seed. We show that CGF is considerably more efficient if energy is inversely proportional to the density of the stationary distribution and increases monotonically every time that seed is chosen. Energy is controlled with a power schedule.
We implemented the exponential schedule by extending AFL. In 24 hours, AFLFAST exposes 3 previously unreported CVEs that are not exposed by AFL and exposes 6 previously unreported CVEs 7x faster than AFL. AFLFAST produces at least an order of magnitude more unique crashes than AFL.



# Learning-based Fuzzing:

### NEUZZ: Efficient Fuzzing with Neural Program Smoothing (S&P 2019)

* <img src="image/pdf_24px.png">[Paper](./Paper/SP19_NEUZZ.pdf)

**Abstract:** Fuzzing has become the de facto standard technique for finding software vulnerabilities. However, even state-of-the-art fuzzers are not very efficient at finding hard-to-trigger software bugs. Most popular fuzzers use evolutionary guidance to generate inputs that can trigger different bugs. Such evolutionary algorithms, while fast and simple to implement, often get stuck in fruitless sequences of random mutations. Gradient-guided optimization presents a promising alternative to evolutionary guidance. Gradient-guided techniques have been shown to significantly outperform evolutionary algorithms at solving high-dimensional structured optimization problems in domains like machine learning by efficiently utilizing gradients or higher-order derivatives of the underlying function. However, gradient-guided approaches are not directly applicable to fuzzing as real-world program behaviors contain many discontinuities, plateaus, and ridges where the gradient-based methods often get stuck. We observe that this problem can be addressed by creating a smooth surrogate function approximating the target program's discrete branching behavior. In this paper, we propose a novel program smoothing technique using surrogate neural network models that can incrementally learn smooth approximations of a complex, real-world program's branching behaviors. We further demonstrate that such neural network models can be used together with gradient-guided input generation schemes to significantly increase the efficiency of the fuzzing process. Our extensive evaluations demonstrate that NEUZZ significantly outperforms 10 state-of-the-art graybox fuzzers on 10 popular real-world programs both at finding new bugs and achieving higher edge coverage. NEUZZ found 31 previously unknown bugs (including two CVEs) that other fuzzers failed to find in 10 real-world programs and achieved 3X more edge coverage than all of the tested graybox fuzzers over 24 hour runs. Furthermore, NEUZZ also outperformed existing fuzzers on both LAVA-M and DARPA CGC bug datasets.



# Fuzzing Machine Learning Model

### TensorFuzz: Debugging Neural Networks with Coverage-Guided Fuzzing (2018)

* <img src="image/pdf_24px.png">[Paper](./Paper/18_Tensorfuzz.pdf)

* <img src="image/github_24px.png">[Code](https://github.com/brain-research/tensorfuzz)

**Abstract:** Machine learning models are notoriously difficult to interpret and debug. This is particularly true of neural networks. In this work, we introduce automated software testing techniques for neural networks that are well-suited to discovering errors which occur only for rare inputs. Specifically, we develop coverage-guided fuzzing (CGF) methods for neural networks. In CGF, random mutations of inputs to a neural network are guided by a coverage metric toward the goal of satisfying user-specified constraints. We describe how fast approximate nearest neighbor algorithms can provide this coverage metric. We then discuss the application of CGF to the following goals: finding numerical errors in trained neural networks, generating disagreements between neural networks and quantized versions of those networks, and surfacing undesirable behavior in character level language models. Finally, we release an open source library called TensorFuzz that implements the described techniques.


### Coverage-Guided Fuzzing for Deep Neural Networks (2018)

* <img src="image/pdf_24px.png">[Paper](./Paper/18_Deep-neural-networks.pdf)

**Abstract:** In company with the data explosion over the past decade, deep neural network (DNN) based software has experienced unprecedented leap and is becoming the key driving force of many novel industrial applications, including many safety-critical scenarios such as autonomous driving. Despite great success achieved in various human intelligence tasks, similar to traditional software, DNNs could also exhibit incorrect behaviors caused by hidden defects causing severe accidents and losses. In this paper, we propose DeepHunter, an automated fuzz testing framework for hunting potential defects of general-purpose DNNs. DeepHunter performs metamorphic mutation to generate new semantically preserved tests, and leverages multiple plugable coverage criteria as feedback to guide the test generation from different perspectives. To be scalable towards practical-sized DNNs, DeepHunter maintains multiple tests in a batch, and prioritizes the tests selection based on active feedback. The effectiveness of DeepHunter is extensively investigated on 3 popular datasets (MNIST, CIFAR-10, ImageNet) and 7 DNNs with diverse complexities, under large set of 6 coverage criteria as feedback. The large-scale experiments demonstrate that DeepHunter can (1) significantly boost the coverage with guidance; (2) generate useful tests to detect erroneous behaviors and facilitate the DNN model quality evaluation; (3) accurately capture potential defects during DNN quantization for platform migration.



# Interesting Fuzzing

### REST-ler: Stateful REST API Fuzzing  (ICSE 2019)

* <img src="image/pdf_24px.png">[Paper](./Paper/ICSE19_DIFFUZZ.pdf)

**Abstract:** This paper introduces REST-ler, the first stateful REST API fuzzer. REST-ler analyzes the API specification of a cloud service and generates sequences of requests that automatically test the service through its API. REST-ler generates test sequences by (1) inferring producer-consumer dependencies among request types declared in the specification (eg inferring that “a request B should be executed after request A” because B takes as an input a resource-id x produced by A) and by (2) analyzing dynamic feedback from responses observed during prior test executions in order to generate new tests (eg learning that “a request C after a request sequence A;B is refused by the service” and therefore avoiding this combination in the future).
We present experimental results showing that these two techniques are necessary to thoroughly exercise a service under test while pruning the large search space of possible request sequences. We used REST-ler to test GitLab, a large open-source self-hosted Git service, as well as several Microsoft Azure and Office365 cloud services. REST-ler found 28 bugs in Gitlab and several bugs in each of the Azure and Office365 cloud services tested so far. These bugs have been confirmed by the service owners, and are either in the process of being fixed or have already been fixed.


### Life after Speech Recognition: Fuzzing Semantic Misinterpretation for Voice Assistant Applications (NDSS 2019)

* <img src="image/pdf_24px.png">[Paper](./Paper/NDSS19_Life.pdf)

**Abstract:** Popular Voice Assistant (VA) services such as Amazon Alexa and Google Assistant are now rapidly appifying their platforms to allow more flexible and diverse voice-controlled service experience. However, the ubiquitous deployment of VA devices and the increasing number of third-party applications have raised security and privacy concerns. While previous works such as hidden voice attacks mostly examine the problems of VA services’ default Automatic Speech Recognition (ASR) component, our work analyzes and evaluates the security of the succeeding component after ASR, i.e., Natural Language Understanding (NLU), which performs semantic interpretation (i.e., text-to-intent) after ASR’s acoustic-to-text processing. In particular, we focus on NLU’s Intent Classifier which is used in customizing machine understanding for third-party VA Applications (or vApps). We find that the semantic inconsistency caused by the improper semantic interpretation of an Intent Classifier can create the opportunity of breaching the integrity of vApp processing when attackers delicately leverage some common spoken errors.
In this paper, we design the first linguistic-model-guided fuzzing tool, named LipFuzzer, to assess the security of Intent Classifier and systematically discover potential misinterpretation-prone spoken errors based on vApps’ voice command templates. To guide the fuzzing, we construct adversarial linguistic models with the help of Statistical Relational Learning (SRL) and emerging Natural Language Processing (NLP) techniques. In evaluation, we have successfully verified the effectiveness and accuracy of LipFuzzer. We also use LipFuzzer to evaluate both Amazon Alexa and Google Assistant vApp platforms. We have identified that a large portion of real-world vApps are vulnerable based on our fuzzing result.


### ContractFuzzer: Fuzzing Smart Contracts for Vulnerability Detection (ASE 2018)

* <img src="image/youdao_note_24px.png">[Reading Note](https://securitygossip.com/blog/2019/01/21/contractfuzzer-fuzzing-smart-contracts-for-vulnerability-detection/)

* <img src="image/pdf_24px.png">[Paper](./Paper/ASE18_ContractFuzzer.pdf)

**Abstract:** Decentralized cryptocurrencies feature the use of blockchain to transfer values among peers on networks without central agency. Smart contracts are programs running on top of the blockchain consensus protocol to enable people make agreements while minimizing trusts. Millions of smart contracts have been deployed in various decentralized applications. The security vulnerabilities within those smart contracts pose significant threats to their applications. Indeed, many critical security vulnerabilities within smart contracts on Ethereum platform have caused huge financial losses to their users. In this work, we present ContractFuzzer, a novel fuzzer to test Ethereum smart contracts for security vulnerabilities. ContractFuzzer generates fuzzing inputs based on the ABI specifications of smart contracts, defines test oracles to detect security vulnerabilities, instruments the EVM to log smart contracts runtime behaviors, and analyzes these logs to report security vulnerabilities. Our fuzzing of 6991 smart contracts has flagged more than 459 vulnerabilities with high precision. In particular, our fuzzing tool successfully detects the vulnerability of the DAO contract that leads to USD 60 million loss and the vulnerabilities of Parity Wallet that have led to the loss of USD 30 million and the freezing of USD 150 million worth of Ether.


### IoTFuzzer: Discovering Memory Corruptions in IoT Through App-based Fuzzing (NDSS 2018)

* <img src="image/youdao_note_24px.png">[Reading Note](https://securitygossip.com/blog/2018/06/15/iotfuzzer-discovering-memory-corruptions-in-iot-through-app-based-fuzzing/)

* <img src="image/pdf_24px.png">[Paper](./Paper/NDSS18_IoTfuzzer.pdf)

* <img src="image/ppt_24px.png">[Slides](./Paper/NDSS18_IoTFuzzer_Slides.pdf)

**Abstract:** With more IoT devices entering the consumer market, it becomes imperative to detect their security vulnerabilities before an attacker does. Existing binary analysis based approaches only work on firmware, which is less accessible except for those equipped with special tools for extracting the code from the device. To address this challenge in IoT security analysis, we present in this paper a novel automatic fuzzing framework, called IOTFUZZER, which aims at finding memory corruption vulnerabilities in IoT devices without access to their firmware images. The key idea is based upon the observation that most IoT devices are controlled through their official mobile apps, and such an app often contains rich information about the protocol it uses to communicate with its device. Therefore, by identifying and reusing program-specific logic (e.g., encryption) to mutate the test case (particularly message fields), we are able to effectively probe IoT targets without relying on any knowledge about its protocol specifications. In our research, we implemented IOTFUZZER and evaluated 17 real-world IoT devices running on different protocols, and our approach successfully identified 15 memory corruption vulnerabilities (including 8 previously unknown ones).


### What You Corrupt Is Not What You Crash: Challenges in Fuzzing Embedded Devices (NDSS 2018)

* <img src="image/pdf_24px.png">[Paper](./Paper/NDSS18_Muench_paper.pdf)

* <img src="image/ppt_24px.png">[Slides](./Paper/NDSS18_Muench_Slides.pdf)

**Abstract:** As networked embedded systems are becoming more ubiquitous, their security is becoming critical to our daily life. While manual or automated large scale analysis of those systems regularly uncover new vulnerabilities, the way those systems are analyzed follows often the same approaches used on desktop systems. More specifically, traditional testing approaches relies on observable crashes of a program, and binary instrumentation techniques are used to improve the detection of those faulty states. In this paper, we demonstrate that memory corruptions, a common class of security vulnerabilities, often result in different behavior on embedded devices than on desktop systems. In particular, on embedded devices, effects of memory corruption are often less visible. This reduces significantly the effectiveness of traditional dynamic testing techniques in general, and fuzzing in particular. Additionally, we analyze those differences in several categories of embedded devices and show the resulting impact on firmware analysis. We further describe and evaluate relatively simple heuristics which can be applied at run time (on an execution trace or in an emulator), during the analysis of an embedded device to detect previously undetected memory corruptions.


### MoonShine: Optimizing OS Fuzzer Seed Selection with Trace Distillation (USENUX Security2018)

* <img src="image/wechat_24px.png">[Reading Note](https://mp.weixin.qq.com/s/L2XgaQB7BZzcptvOrhMvXg)

* <img src="image/pdf_24px.png">[Paper](./Paper/USENUX18_MoonShine.pdf)

**Abstract:** OS fuzzers primarily test the system call interface between the OS kernel and user-level applications for security vulnerabilities. The effectiveness of evolutionary OS fuzzers depends heavily on the quality and diversity of their seed system call sequences. However, generating good seeds for OS fuzzing is a hard problem as the behavior of each system call depends heavily on the OS kernel state created by the previously executed system calls. Therefore, popular evolutionary OS fuzzers often rely on hand-coded rules for generating valid seed sequences of system calls that can bootstrap the fuzzing process. Unfortunately, this approach severely restricts the diversity of the seed system call sequences and therefore limits the effectiveness of the fuzzers.
In this paper, we develop MoonShine, a novel strategy for distilling seeds for OS fuzzers from system call traces of real-world programs while still maintaining the dependencies across the system calls. MoonShine leverages light-weight static analysis for efficiently detecting dependencies across different system calls.
We designed and implemented MoonShine as an extension to Syzkaller, a state-of-the-art evolutionary fuzzer for the Linux kernel. Starting from traces containing 2.8 million system calls gathered from 3,220 real-world programs, MoonShine distilled down to just over 14,000 calls while preserving 86% of the original code coverage. Using these distilled seed system call sequences, MoonShine was able to improve Syzkaller's achieved code coverage for the Linux kernel by 13% on average. MoonShine also found 14 new vulnerabilities in the Linux kernel that were not found by Syzkaller.


### Singularity: Pattern Fuzzing for Worst Case Complexity (FSE 2018)

* <img src="image/pdf_24px.png">[Paper](./Paper/FSE18_PatternFuzzing.pdf)

**Abstract:** We describe a new blackbox complexity testing technique for determining the worst-case asymptotic complexity of a given application. The key idea is to look for an input pattern —rather than a concrete input— that maximizes the asymptotic resource usage of the program. Because input patterns can be described concisely as programs in a restricted language, our method transforms the complexity testing problem to optimal program synthesis. In particular, we express these input patterns using a new model of computation called Recurrent Computation Graph (RCG) and solve the optimal synthesis problem by developing a genetic programming algorithm that operates on RCGs. We have implemented the proposed ideas in a tool called Singularity and evaluate it on a diverse set of benchmarks. Our evaluation shows that Singularity can effectively discover the worst-case complexity of various algorithms and that it is more scalable compared to existing state-of-the-art techniques. Furthermore, our experiments also corroborate that Singularity can discover previously unknown performance bugs and availability vulnerabilities in real-world applications such as Google Guava and JGraphT.



# Reading Notes

- [DifFuzz (Side-channal analysis)](http://note.youdao.com/noteshare?id=06c39d23c76be5d0e6441a01c9eaff93&sub=B72A70BDD1DC47B39E56866B3903401B)
- [ProFuzzer (Inference input structure)](http://note.youdao.com/noteshare?id=8e905e9d299cae5ceb3bbeac0591cfab&sub=9FCAB3A8AD4C48689095307EDD1A940A)
- [FairFuzz (Target rare branches)](http://note.youdao.com/noteshare?id=5525c7a18e8681302229e9466290aac2&sub=C4769EA799584C5D89994FE397F76981)
- [FairFuzz & ProFuzzer](http://note.youdao.com/noteshare?id=79c7f05ba2a64163e28a0267c7e1b181&sub=2E7496DA67634505B5F3A5F326CD6B27)
- [NEZHA (Differential testing)](http://note.youdao.com/noteshare?id=7e602068c641217947c97b287291c9c7&sub=32BD04EB8C00424E87FA7B948D38EC96)
- [REDQUEEN](http://note.youdao.com/noteshare?id=6a4b00d912eab145d1c1f32f11bde3e0&sub=7DADC02169A14B33979BCCB2556E4526)
- [AddressSanitizer: A Fast Address Sanity Checker](http://note.youdao.com/noteshare?id=aecd3639e21a682555fd6b002a176937&sub=AF24A1A1E1534A49B00F7E504A4B111C)
- [Enhancing Memory Error Detection](http://note.youdao.com/noteshare?id=6228fef31b29b4ffbbbe1c1d80ef3fa0&sub=CB0D15A0D6394FA188C06B2BCB6367A3)