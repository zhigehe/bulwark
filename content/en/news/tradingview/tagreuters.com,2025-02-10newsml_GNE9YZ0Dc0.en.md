---
title: "Groundbreaking Formal Verification Further Enhances the Quality of CHERIoT-Ibex"
date: "2025-02-10 21:50:00"
summary: "Collaboration milestone addresses key pain points of typical design verification (DV) approaches, improving confidence while reducing cost, time, and resource spendCAMBRIDGE, United Kingdom, Feb. 10, 2025 (GLOBE NEWSWIRE) — lowRISC C.I.C., the open silicon ecosystem organisation, today announced the addition of formal verification to the toolbox of open source design..."
categories:
  - "Reuters"
lang:
  - "en"
translations:
  - "en"
tags:
  - "Reuters"
menu: ""
thumbnail: ""
lead: ""
comments: false
authorbox: false
pager: true
toc: false
mathjax: false
sidebar: "right"
widgets:
  - "search"
  - "recent"
  - "taglist"
---

Collaboration milestone addresses key pain points of typical design verification (DV) approaches, improving confidence while reducing cost, time, and resource spend

CAMBRIDGE, United Kingdom, Feb. 10, 2025 (GLOBE NEWSWIRE) — lowRISC C.I.C., the open silicon ecosystem organisation, today announced the addition of formal verification to the toolbox of open source design verification (DV) techniques used to ensure the commercial level quality of the Microsoft-created CHERIoT-Ibex core, the processor at the heart of the UKRI-funded Sonata™ platform.

![image1.png](https://s3.tradingview.com/news/image/tag:reuters.com,2025-02-10:newsml_GNE9YZ0Dc-ce9b65dbbbed42f9d21f1b8e24c1e052-resized.jpeg)

CHERIoT-Ibex pipeline with specification installed using a pipeline follower



Prof. Tom Melham and Louis-Emile Ploix of the University of Oxford, and Alasdair Armstrong of the University of Cambridge, have created an extensive formal verification framework to establish observational equivalence, using unbounded proofs, between the hardware and the RISC-V International Sail specification of instruction behaviour. This greatly strengthens confidence in the design’s conformance to the specification. The verification uses the Cadence Jasper™ tool, along with new Sail support to automatically build a SystemVerilog reference model from the specification. They describe their work in a pre-print paper published on arXiv, and have collaborated with Microsoft to upstream this into the open source CHERIoT-Ibex repository.

CHERIoT-Ibex is Microsoft’s open-source extension of lowRISC’s Ibex®, a 32-bit RISC-V processor. CHERIoT provides fine-grained memory protection for embedded systems, which deterministically mitigates over two thirds of memory vulnerabilities and enables efficient compartmentalization. Of course, it is critical that the hardware correctly *implements* the CHERIoT extension to ensure that the security guarantees it offers are valid. “Correct” implementation is defined in a standardised way for RISC-V using Sail. This is a domain-specific language which describes, in a formal but readable fashion, exactly what each processor instruction does.

This new formal verification framework and proof developed by the University of Oxford, the University of Cambridge, and lowRISC takes the formal specification for CHERIoT — written in Sail — and checks that for any stream of instructions the CHERIoT-Ibex implementation performs the same memory operations. This equivalence checking is decomposed into multiple steps to help the tool converge, by first proving simple properties, then using those to prove more and more complex ones. It is important to note that the proofs developed as part of this work are different from the more common *bounded* proofs, where only a limited amount of system evolution is explored for counter-examples. By contrast, unbounded proofs hold true for *all* possible executions. While no single verification technique should be relied on in isolation, a formal proof (in combination with a traditional functional verification flow) significantly increases confidence in the design.

Besides the work on CHERIoT-Ibex, lowRISC has also published an adaptation of this proof for *regular* Ibex (which of course also has extensive *conventional* DV), the main microprocessor core used in the OpenTitan® root of trust.

“We’re thrilled to see the achievement of this milestone, demonstrating that well managed open-source silicon designs can not just *match* the DV quality of commercial IP, in some cases they’re beginning to lead the field,” said Dr. Gavin Ferris, CEO of lowRISC. “The successful formal verification of CHERIoT-Ibex exemplifies our Silicon Commons approach, bringing the best of industry, academia and the open source community together through collaborative engineering — and moving the game forward for everyone. Now, not only can companies bring products to market cheaper and faster by leveraging open-source silicon designs, they can do so with the strongest possible assurance that specification fidelity has been maintained. We’re proud to have worked with Microsoft, the University of Oxford, University of Cambridge and Cadence to help make this fantastic result possible.”

“The CHERIoT-Ibex project has been an ideal challenge for our formal verification research at Oxford, which aims at both scientific innovation and strong real-world impact,” Professor Tom Melham and lead verification engineer Louis-Emile Ploix said. “We are delighted that our work has significantly helped to increase confidence in the commercial-grade quality of Microsoft’s CHERIoT-Ibex core, driven by the development of a new Sail to Verilog compiler by our colleagues at the University of Cambridge, and demonstrated new methodology for RISC-V formal verification. Our hope is that other RISC-V verification projects can substantially benefit from our experience, through our publications and open source formal verification code.”

“We are excited to see this formal verification milestone, building on the Sail formal specifications of RISC-V, CHERI RISC-V, and CHERIoT developed by multiple partners over recent years,” said Professor Peter Sewell at the University of Cambridge. “This links formal specifications of the instruction set, previously used for architecture design, hardware testing, software development, and formal reasoning about software, all the way down to the detailed hardware design. The work shows that full formal verification is viable for such designs with reasonable effort.”

“Finding and fixing bugs early in the design cycle is crucial to address the fast growing complexity of chip design. Formal verification is a key technology that allows teams to boost the functional verification productivity, reduce costs, improve quality, and ensure more reliable designs in less time,” Ziyad Hanna, Corporate Vice President of Cadence Design Systems, said. “We’re delighted that Cadence Jasper Formal Verification Platform has been instrumental in supporting this effort, contributing to the future of secure computing.”

lowRISC would like to thank all the supporters of the Sunburst project, with special thanks to Microsoft for contributing the core CHERI implementation within the CHERIoT-Ibex processor and making it open source. “Microsoft is thrilled to upstream an extensive formal verification framework and proof to the open-source CHERIoT-Ibex repository. The CHERIoT-Ibex core augments lowRISC's Ibex with the CHERIoT ISA extension,” said Tony Chen, Partner Security Architect at Microsoft. “The formal verification pioneered by Oxford University has instilled an unmatched level of confidence in the CHERIoT-Ibex core.”

CHERIoT-Ibex is the processor core of Sonata which puts CHERI technology into the hands of embedded-system engineers. Sonata is part of the Sunburst project, which is funded by DSbD and UKRI (Grant Number 107540). The early, foundational work at Oxford on the formal verification of CHERIoT-Ibex was funded by DSbD and UKRI as part of the SCorCH project (EPSRC Grant Number EP/V000225/1).

**About lowRISC®**

Founded in 2014 at the University of Cambridge Department of Computer Science and Technology, lowRISC is a not-for-profit company/CIC that provides a neutral home for collaborative engineering to develop and maintain commercial-quality open source silicon designs and tools for the long term. The lowRISC not-for-profit structure combined with full-stack engineering capabilities in-house enables the hosting and management of high-quality projects like OpenTitan and Sunburst via the Silicon Commons® approach.

**Media Contact**

lowRISC@w2comm.com

An infographic accompanying this announcement is available at https://www.globenewswire.com/NewsRoom/AttachmentNg/432a234b-dca0-44be-9118-91ca2b8996c4

[Reuters](https://www.tradingview.com/news/reuters.com,2025-02-10:newsml_GNE9YZ0Dc:0-groundbreaking-formal-verification-further-enhances-the-quality-of-cheriot-ibex/)
