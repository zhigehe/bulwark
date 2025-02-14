---
title: "Fujitsu and Yokohama National University achieve world's first real-time prediction of tornadoes associated with typhoons using supercomputer Fugaku"
date: "2025-02-12 11:18:33"
summary: "Kawasaki and Yokohama, JAPAN, Feb 12, 2025 - (JCN Newswire) - Fujitsu Limited and Yokohama National University today announced the achievement of the world's first real-time prediction of multiple typhoon-associated tornadoes using advanced supercomputing technology, significantly improving disaster preparedness.The new technology utilizes optimized large-scale parallel processing coupled with the enhanced..."
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

Kawasaki and Yokohama, JAPAN, Feb 12, 2025 - (JCN Newswire) - Fujitsu Limited and Yokohama National University today announced the achievement of the world's first real-time prediction of multiple typhoon-associated tornadoes using advanced supercomputing technology, significantly improving disaster preparedness.

The new technology utilizes optimized large-scale parallel processing coupled with the enhanced Cloud Resolving Storm Simulator (CReSS), a weather simulator developed by Professor Kazuhisa Tsuboki on Fujitsu's Fugaku supercomputer. This allows for a single, high-resolution simulations encompassing both large-scale typhoons and smaller-scale tornadoes, resulting in accurate, real-time predictions.

Previously, during simulations of Typhoon No. 10's tornadoes, which hit Japan's Kyushu area in August 2024, it took more than 11 hours to predict whether or not tornadoes would occur, making the predictions not practicably applicable. This technology was able to drastically reduce prediction time to 80 minutes, allowing the two partners to predict the occurrence of a tornado four hours in advance. This prediction calculation used only 5% of Fugaku's computational resources, indicating the potential for even larger-scale and faster predictions in the future.

The two partners will release the enhanced CReSS to the research community within fiscal year 2024, significantly improving the prediction of severe weather events and enhancing disaster mitigation efforts.

Background

Approximately 20% of tornadoes in Japan occur alongside typhoons. In response to increasing tornado damage, Japan began issuing tornado warnings in 2008. However, compared to weather phenomena like precipitation, which can be predicted with high accuracy, tornadoes are difficult to predict due to their small scale and short duration. Tornado warnings currently have a validity period of about one hour, and there is a demand for longer warning periods.

Fujitsu and Yokohama National University initiated a joint research project in November 2022, aiming to address societal challenges related to increasingly severe typhoons exacerbated by global warming. This collaboration, conducted under the Fujitsu Small Research Lab's "Fujitsu - Yokohama National University Typhoon Science and Technology Research Center Collaborative Research Laboratory," focuses on understanding typhoon formation mechanisms and accelerating and improving the accuracy of typhoon prediction simulations.

Accomplishments of the joint research project

1. Applied technology

The CReSS weather simulator, based on a high-precision weather simulations spanning cloud scales (horizontal 50m-2,000m) to mesoscales (horizontal 2km-2,000km), accurately simulates the formation and development of supercell thunderstorms that generate tornadoes. However, CReSS's original design was not suitable for the large-scale parallel processing (thousands of nodes) required for typhoon-associated tornado prediction, resulting in excessively long parallel computation times and rendering it unsuitable for real-time prediction.

To address this, a lightweight version of CReSS was developed, significantly reducing computational demands while maintaining the necessary prediction accuracy. Furthermore, Fujitsu's large-scale parallel processing technology was employed, optimizing simulation processing mapping for Fugaku's server network structure and implementing overlapped execution of computation and file output. This significantly reduced simulation time on Fugaku, enabling substantially faster prediction results than previously possible.

2. Application results

Prediction experiments were conducted using CReSS on 8,192 nodes of Fugaku for Typhoon No. 10, which caused tornado damage in Kyushu, Japan, in August 2024. Utilizing 3D spatial data including temperature, pressure, humidity, wind direction, and speed, the simulation successfully reproduced multiple tornadoes that occurred along the eastern coast of Kyushu. Figure 1 shows the simulation results for the entire typhoon, while Figure 2 visualizes the wind and cloud movement in a 20km x 20km area on the eastern coast of Kyushu, clearly showing multiple tornado formations.

\*

Figure 1: Simulation results of Typhoon No.10 in 2024, showing rainfall (left) and wind speed (right). The red circle on the right highlights an area of strong swirling winds.

\*

Figure 2: Reproduction of tornadoes associated with Typhoon No.10 in 2024 (20km x 20km): The red area represents strong swirling winds, likely a tornado, while the white area represents the swirling clouds above it.(This visualization was created by Yokohama National University using the VAPOR weather visualization tool.)

YouTube video:

Fujitsu and Yokohama National University achieve world's first real-time prediction of tornadoes associated with typhoons using supercomputer Fugaku (https://youtu.be/tY-R6Oj6G7A/)

Seishi Okamoto, EVP, Head of Fujitsu Research, Fujitsu Limited, comments:

"We're delighted to share the significant results from our collaborative research with Yokohama National University, a project spanning over two years. This success will further propel the integration of our expertise and technologies. By advancing research in typhoon development prediction and prediction simulation, we aim to help mitigate weather-related disasters and lessen their impact, contributing to solutions for global environment, one of Fujitsu's key materiality topics.

Professor Hironori Fudeyasu, Director, TRC, Institute of Multidisciplinary Sciences, Yokohama National University, comments:

Fujitsu - Yokohama National University Typhoon Science and Technology Research Center Collaborative Research Laboratory's research represents a major advancement in predicting typhoon-associated tornadoes, a previously challenging meteorological phenomenon. The supercomputer Fugaku and high-resolution modeling enabled high-precision simulations across scales, leading to real-time predictions crucial for improving early warning systems and mitigating the impact of these devastating events. This breakthrough is expected to significantly contribute to disaster risk reduction while minimizing environmental consequences.

Future Plans

To accelerate research on meteorological disasters, including typhoons, Fujitsu and Yokohama National University plan to publicly release the large-scale parallel version of CReSS within this fiscal year. Furthermore, based on these achievements, both organizations will work to further improve speed and prediction accuracy, leveraging AI technology. Through these efforts, we will contribute to solving global environmental issues, one of Fujitsu's key materiality topics.

Remarks:

This research was conducted with computing resources provided by the Fugaku supercomputer through the Fugaku Industrial Trial Project (Project Number: hp240255).

About Fujitsu

Fujitsu's purpose is to make the world more sustainable by building trust in society through innovation. As the digital transformation partner of choice for customers in over 100 countries, our 124,000 employees work to resolve some of the greatest challenges facing humanity. Our range of services and solutions draw on five key technologies: Computing, Networks, AI, Data & Security, and Converging Technologies, which we bring together to deliver sustainability transformation. Fujitsu Limited reported consolidated revenues of 3.7 trillion yen (US$26 billion) for the fiscal year ended March 31, 2024 and remains the top digital services company in Japan by market share. Find out more: www.fujitsu.com.

About Yokohama National University

YNU was established in 1949 as a national university by integrating 4 old-education-system schools and has 5 colleges and 6 graduate schools at its campus in Tokiwadai, Hodogaya-ku, Yokohama. YNU declares that it will make every effort to establish a strong footing in academic research and education by upholding 5 fundamental principles:'Be Active','Be Innovative','Be Open' ,'Be Global' and 'Be Diversity' cultivated as the spirit of YNU throughout its history. URL : https://www.ynu.ac.jp/english/special/message/.

Press Contacts

Fujitsu Limited

Public and Investor Relations Division

Inquiries

Yokohama National University

TRC, Institute of Multidisciplinary Sciences, Yokohama National University

trc-office@ynu.ac.jp

Source: Fujitsu Ltd

Copyright 2025 JCN Newswire . All rights reserved.

[Reuters](https://www.tradingview.com/news/reuters.com,2025-02-12:newsml_JCN95960a:0-fujitsu-and-yokohama-national-university-achieve-world-s-first-real-time-prediction-of-tornadoes-associated-with-typhoons-using-supercomputer-fugaku/)
