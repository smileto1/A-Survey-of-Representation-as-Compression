<div align=center>

# Instance-Fitted Representations for Data Compression: A Survey

### *Representation as Compression* — a curated list of instance-fitted (neural-overfitting / primitive-fitting) data compression methods

</div>

> **Instance-Fitted Representations for Data Compression: A Survey**  
> [Youneng Bao](https://github.com/baoyu2020)<sup>1</sup>, [Yulong Cheng](https://github.com/smileto1/)<sup>2</sup>, [Yiping Liu](https://nouise.github.io/DD-RUO/)<sup>2</sup>, [Jiacong Chen](https://github.com/ChenJiaCong-1005)<sup>1</sup>, Yongsheng Liang<sup>1</sup>  
>  
> <sup>1</sup>Shenzhen University (SZU), <sup>2</sup>Harbin Institute of Technology, Shenzhen (HITSZ)

---

> [!IMPORTANT]
> We welcome your help in improving the repository and paper. Please feel free to submit a [pull request](https://github.com/smileto1/A-Survey-of-Representation-as-Compression/pulls), open an [issue](https://github.com/smileto1/A-Survey-of-Representation-as-Compression/issues) or [contact us](#-contact) to:
>
> - Add a relevant paper not yet included.
> - Suggest a more suitable category or mechanism tag.
> - Update links, venues or code repositories.
> - Ask for clarification about any content.

---

## 📚 Contents

- [Scope and Taxonomy](#-scope-and-taxonomy)
- [Badge Legend](#-badge-legend)
- [Representative Milestones](#-representative-milestones)
- [Recent Papers (2026)](#-recent-papers-2026)
- [Source-Verified Empirical Anchors](#-source-verified-empirical-anchors-sec-5)
- **[Functional Representations ](functional.md)**
    - [2D Image](functional.md#functional-2d-image)
    - [Video](functional.md#functional-video)
    - [3D Static Scene](functional.md#functional-3d-static-scene)
    - [Dynamic 4D Scenes & Volumetric Video](functional.md#functional-dynamic-4d-scenes--volumetric-video)
    - [3D Shapes / Volumetric](functional.md#functional-3d-shapes--volumetric)
    - [Other Data Modalities](functional.md#functional-other-data-modalities)
- **[Parametric Primitive Representations ](parametric.md)**
    - [2D Image](parametric.md#primitive-2d-image)
    - [Video](parametric.md#primitive-video)
    - [3D Scenes](parametric.md#primitive-3d-scenes)
    - [Dynamic Scene](parametric.md#primitive-dynamic-scene)
- **[Background and Context ](context.md)**
    - [Traditional codecs (operational reference)](context.md#traditional-codecs-operational-reference)
    - [Amortized learned codecs and auxiliary refinement (context only)](context.md#amortized-learned-codecs-and-auxiliary-refinement-context-only)
    - [Theory](context.md#theory)
    - [Adjacent surveys](context.md#adjacent-surveys)
    - [Standardization](context.md#standardization)
    - [Hybrid carriers and hardware co-design ](context.md#hybrid-carriers-and-hardware-co-design-sec-6)
- [Bibliography](survey_refs.bib) · [Citation](#-citation) · [Contact](#-contact)

**Please check out all the papers by selecting the route or sub-area you are interested in. On this main page, only the representative milestones, the papers published in 2026 and the source-verified empirical anchors are shown.**

## 🧭 Scope and Taxonomy

**Instance-Fitted Representation Compression** represents an individual signal or scene by optimizing an instance-specific parametric state and storing or transmitting a coded form of that state. Fitting the target instance *constitutes* the encoding process, and reconstruction instantiates or evaluates the fitted state. Latent or coding-decision refinement inside an otherwise intact amortized or conventional codec is treated only as context. The reviewed literature covers 2D images, video, static and dynamic 3D scenes, and scientific or biomedical volumes; audio and text are outside the present scope.

The survey organizes the literature through a **two-route taxonomy** determined by the terminal reconstruction substrate and operator:

| Route | Fitted state | Terminal operator | Representative instances |
| --- | --- | --- | --- |
| **Functional Representations** ([list](functional.md)) | neural weights, modulations, latents, grids, tensors, hash features | query evaluation, interpolation, integration | SIREN, NeRF, COIN, NeRV, COOL-CHIC, NVRC |
| **Parametric Primitive Representations** ([list](parametric.md)) | a finite set of spatially addressable local elements (e.g. Gaussians) | projection, aggregation, splatting, rasterization | 3DGS, GaussianImage, HAC, 4D-GS, GSVC, 4DGC |

Hybrid designs stay inside the route of their terminal operator and only receive a secondary *Functional-hybrid* / *Primitive-hybrid* tag; *Cross-route hybrid* is reserved for systems with two genuine terminal operators. Within each modality bucket, methods are grouped by the survey's three analytical stages:

- **Capacity** — Representation Capacity Improvement: mechanisms that mainly shape distortion or computation (encodings, activations, hierarchies, initialization, density control).
- **Rate Optimization** — payload reduction: pruning, factorization, quantization, dictionaries / codebooks, structure or context modeling, bitstream formation.
- **RD Optimization** — Rate–Distortion Optimization: an explicit differentiable rate term during fitting (D + λ·R̂).

```
Instance-Fitted Representation Compression
├── Functional Representations (Sec. 3)            → functional.md
│   ├── 2D Image
│   ├── Video
│   ├── 3D Static Scene
│   ├── Dynamic 4D Scenes & Volumetric Video
│   ├── 3D Shapes / Volumetric
│   └── Other Data Modalities
├── Parametric Primitive Representations (Sec. 4)  → parametric.md
│   ├── 2D Image
│   ├── Video
│   ├── 3D Scenes
│   └── Dynamic Scene
└── Background & Context (Secs. 1, 2, 5, 6)        → context.md
    codecs · amortized learned codecs · theory · adjacent surveys · standards · hardware
```

> **Evidence boundary used throughout the survey.** Parameter count, primitive count, memory, checkpoint size, estimated entropy and serialized bits are *distinct* measures. A fitted representation becomes a coded payload only when its stored state and every decoder-required side information are specified and rate-accounted. Tags in this repository describe the *mechanism* each paper contributes as discussed in the survey; they do not rank methods.

Literature coverage was closed in **August 2026**. A paper appears under every heading in which the survey discusses it, so some works are listed more than once with different mechanism tags.

## 🏷️ Badge Legend

- ![arXiv](https://img.shields.io/badge/arXiv-2024.03-red) `red` — arXiv preprint (year.month of the arXiv version)
- ![Venue](https://img.shields.io/badge/CVPR-2024-blue) `blue` — conference / journal venue and year
- ![Route](https://img.shields.io/badge/Functional-2D_Image-purple) `purple` — taxonomy route and modality bucket (Functional / Primitive)
- ![Mechanism](https://img.shields.io/badge/Quantization-green) `green` — mechanism tags as discussed in the survey text
- ![Stage](https://img.shields.io/badge/Rate_Optimization-yellow) `yellow` — survey stage: Capacity / Rate Optimization / RD Optimization / Extension
- ![Context](https://img.shields.io/badge/Context-lightgrey) `grey` — background work cited for context (not a member of the two routes)

## ⭐ Representative Milestones

The milestones mapped on the survey's evolution figure (Fig. 2). Dashed entries in the figure denote representation precursors; the selection implies neither lineage nor ranking.

| **Title & Authors** | **Route · Modality** | **Mechanism · Stage** | **Links** |
| --- | :---: | --- | :---: |
| [![arXiv](https://img.shields.io/badge/arXiv-2021.03-red)]() <br>[COIN: Compression with implicit neural representations](https://arxiv.org/abs/2103.03123)<br>Emilien Dupont, Adam Goliński, Milad Alizadeh, Yee Whye Teh, Arnaud Doucet<br><sub>Weight-coded INR image codec: quantized network weights are the payload</sub> | [![Functional](https://img.shields.io/badge/Functional-2D_Image-purple)]() | [![Weight Payload](https://img.shields.io/badge/Weight_Payload-green)]() [![Quantization](https://img.shields.io/badge/Quantization-green)]() | [Paper](https://arxiv.org/abs/2103.03123)<br>[Code](https://github.com/EmilienDupont/coin) |
| [![NeurIPS](https://img.shields.io/badge/NeurIPS-2021-blue)]() <br>[NeRV: Neural representations for videos](https://arxiv.org/abs/2110.13903)<br>Hao Chen, Bo He, Hanyu Wang, Yixuan Ren, Ser Nam Lim, Abhinav Shrivastava<br><sub>Frame-index neural video representation; model parameters as payload</sub> | [![Functional](https://img.shields.io/badge/Functional-Video-purple)]() | [![Frame-index INR](https://img.shields.io/badge/Frame--index_INR-green)]() [![Pruning](https://img.shields.io/badge/Pruning-green)]() [![Quantization](https://img.shields.io/badge/Quantization-green)]() | [Paper](https://arxiv.org/abs/2110.13903)<br>[Code](https://github.com/haochen-rye/NeRV) |
| [![ICCV](https://img.shields.io/badge/ICCV-2023-blue)]() <br>[Cool-Chic: Coordinate-based low complexity hierarchical image codec](https://arxiv.org/abs/2212.05458)<br>Théo Ladune, Pierrick Philippe, Félix Henry, Gordon Clare, Thomas Leguay<br><sub>Instance state in multi-resolution latent grids with a lightweight decoder</sub> | [![Functional](https://img.shields.io/badge/Functional-2D_Image-purple)]() | [![Latent Grid](https://img.shields.io/badge/Latent_Grid-green)]() [![Autoregressive Model](https://img.shields.io/badge/Autoregressive_Model-green)]() | [Paper](https://arxiv.org/abs/2212.05458)<br>[Code](https://github.com/Orange-OpenSource/Cool-Chic) |
| [![NeurIPS](https://img.shields.io/badge/NeurIPS-2024-blue)]() <br>[NVRC: Neural video representation compression](https://arxiv.org/abs/2409.07414)<br>Ho Man Kwan, Ge Gao, Fan Zhang, Andrew Gower, David Bull<br><sub>Joint hierarchical coding of representation, quantizer and entropy-model parameters</sub> | [![Functional](https://img.shields.io/badge/Functional-Video-purple)]() | [![Hierarchical Coding](https://img.shields.io/badge/Hierarchical_Coding-green)]() [![Entropy Model](https://img.shields.io/badge/Entropy_Model-green)]() | [Paper](https://arxiv.org/abs/2409.07414)<br>[Code](https://github.com/hmkx/NVRC) |
| [![TOG](https://img.shields.io/badge/TOG-2023-blue)]() <br>[3D Gaussian splatting for real-time radiance field rendering](https://arxiv.org/abs/2308.04079)<br>Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis<br><sub>Point-based Gaussians with tile-based differentiable rasterization (representation precursor)</sub> | [![Primitive](https://img.shields.io/badge/Primitive-3D_Scenes-purple)]() | [![Rasterization](https://img.shields.io/badge/Rasterization-green)]() [![Density Control](https://img.shields.io/badge/Density_Control-green)]() | [Paper](https://arxiv.org/abs/2308.04079)<br>[Code](https://github.com/graphdeco-inria/gaussian-splatting) |
| [![ECCV](https://img.shields.io/badge/ECCV-2024-blue)]() <br>[GaussianImage: 1000 FPS image representation and compression by 2D Gaussian splatting](https://arxiv.org/abs/2403.08551)<br>Xinjie Zhang, Xingtong Ge, Tongda Xu, Dailan He, Yan Wang, Hongwei Qin, Guo Lu, Jing Geng, et al.<br><sub>2D Gaussian image representation with quantization and residual VQ</sub> | [![Primitive](https://img.shields.io/badge/Primitive-2D_Image-purple)]() | [![Quantization](https://img.shields.io/badge/Quantization-green)]() [![Residual VQ](https://img.shields.io/badge/Residual_VQ-green)]() | [Paper](https://arxiv.org/abs/2403.08551)<br>[Code](https://github.com/Xinjie-Q/GaussianImage) |
| [![ECCV](https://img.shields.io/badge/ECCV-2024-blue)]() <br>[HAC: Hash-grid assisted context for 3D Gaussian splatting compression](https://arxiv.org/abs/2403.14530)<br>Yihang Chen, Qianyi Wu, Weiyao Lin, Mehrtash Harandi, Jianfei Cai<br><sub>Hash-grid assisted context for anchor-based 3DGS compression</sub> | [![Primitive](https://img.shields.io/badge/Primitive-3D_Scenes-purple)]() | [![Anchor](https://img.shields.io/badge/Anchor-green)]() [![Context Model](https://img.shields.io/badge/Context_Model-green)]() [![Entropy Coding](https://img.shields.io/badge/Entropy_Coding-green)]() | [Paper](https://arxiv.org/abs/2403.14530)<br>[Code](https://github.com/YihangChen-ee/HAC) |
| [![CVPR](https://img.shields.io/badge/CVPR-2024-blue)]() <br>[4D Gaussian splatting for real-time dynamic scene rendering](https://arxiv.org/abs/2310.08528)<br>Guanjun Wu, Taoran Yi, Jiemin Fang, Lingxi Xie, Xiaopeng Zhang, Wei Wei, Wenyu Liu, Qi Tian, et al.<br><sub>Canonical Gaussians + HexPlane-factorized deformation (representation precursor)</sub> | [![Primitive](https://img.shields.io/badge/Primitive-Dynamic_Scene-purple)]() | [![Canonical + Deformation](https://img.shields.io/badge/Canonical_%2B_Deformation-green)]() [![HexPlane](https://img.shields.io/badge/HexPlane-green)]() | [Paper](https://arxiv.org/abs/2310.08528)<br>[Code](https://github.com/hustvl/4DGaussians) |
| [![NOSSDAV](https://img.shields.io/badge/NOSSDAV-2025-blue)]() <br>[GSVC: Efficient video representation and compression through 2D Gaussian splatting](https://arxiv.org/abs/2501.12060)<br>Longan Wang, Yuang Shi, Wei Tsang Ooi<br><sub>I-frame / P-frame 2D Gaussian video coding with bitrate control</sub> | [![Primitive](https://img.shields.io/badge/Primitive-Video-purple)]() | [![I/P Frames](https://img.shields.io/badge/I%2FP_Frames-green)]() [![Prediction](https://img.shields.io/badge/Prediction-green)]() | [Paper](https://arxiv.org/abs/2501.12060)<br>[Code](https://github.com/LonganWANG-cs/GSVC) |
| [![CVPR](https://img.shields.io/badge/CVPR-2025-blue)]() <br>[4DGC: Rate-aware 4D Gaussian compression for efficient streamable free-viewpoint video](https://arxiv.org/abs/2503.18421)<br>Qiang Hu, Zihan Zheng, Houqiang Zhong, Sihua Fu, Li Song, Xiaoyun Zhang, Guangtao Zhai, Yanfeng Wang<br><sub>Rate-aware 4D Gaussian compression with motion grids and entropy modeling</sub> | [![Primitive](https://img.shields.io/badge/Primitive-Dynamic_Scene-purple)]() | [![Motion Grids](https://img.shields.io/badge/Motion_Grids-green)]() [![Entropy Model](https://img.shields.io/badge/Entropy_Model-green)]() [![RD Objective](https://img.shields.io/badge/RD_Objective-green)]() | [Paper](https://arxiv.org/abs/2503.18421)<br>[Code](https://github.com/MediaX-SJTU/4DGC) |

## 🆕 Recent Papers (2026)

Papers from the two routes dated 2026 (by arXiv version or venue year). Each is listed with the first heading under which the survey discusses it; see the route pages for all placements.

| **Title & Authors** | **Route · Modality** | **Mechanism · Stage** | **Links** |
| --- | :---: | --- | :---: |
| [![arXiv](https://img.shields.io/badge/arXiv-2026.06-red)]() <br>[PaaF: Raising the perceived quality of INR-based image compression](https://arxiv.org/abs/2606.21655)<br>Lorenzo Catania, Dario Allegra<br><sub>PaaF: codec-side adaptive quantization and entropy coding; rate follows the serialized configuration</sub> | [![Functional](https://img.shields.io/badge/Functional-2D_Image-purple)]() | [![Quantization](https://img.shields.io/badge/Quantization-green)]() [![Entropy Coding](https://img.shields.io/badge/Entropy_Coding-green)]()<br>[![Rate Optimization](https://img.shields.io/badge/Rate_Optimization-yellow)]() | [Paper](https://arxiv.org/abs/2606.21655) |
| [![arXiv](https://img.shields.io/badge/arXiv-2026.05-red)]() <br>[LANCE: Locally adaptive neural context estimation for overfitted image compression](https://arxiv.org/abs/2605.20672)<br>Martin Benjak, Jörn Ostermann<br><sub>LANCE: predicts locally varying latent statistics from a forward-signaled spatial hyperprior</sub> | [![Functional](https://img.shields.io/badge/Functional-2D_Image-purple)]() | [![Context Model](https://img.shields.io/badge/Context_Model-green)]() [![Hyperprior](https://img.shields.io/badge/Hyperprior-green)]()<br>[![RD Optimization](https://img.shields.io/badge/RD_Optimization-yellow)]() | [Paper](https://arxiv.org/abs/2605.20672)<br>[Code](https://github.com/mbenjak/LANCE) |
| [![arXiv](https://img.shields.io/badge/arXiv-2026.06-red)]() <br>[Enhanced neural video representation compression across extreme complexity and quality scales](https://arxiv.org/abs/2606.28163)<br>Ho Man Kwan, Tianhao Peng, Fan Zhang, Mike Nilsson, Andrew Gower, David Bull<br><sub>NVRC++: multiple high-resolution grids and entropy model across four decoder-complexity levels</sub> | [![Functional](https://img.shields.io/badge/Functional-Video-purple)]() | [![High-res Grids](https://img.shields.io/badge/High--res_Grids-green)]() [![Complexity Levels](https://img.shields.io/badge/Complexity_Levels-green)]()<br>[![RD Optimization](https://img.shields.io/badge/RD_Optimization-yellow)]() | [Paper](https://arxiv.org/abs/2606.28163) |
| [![WACV](https://img.shields.io/badge/WACV-2026-blue)]() <br>[How to design and train your implicit neural representation for video compression](https://arxiv.org/abs/2506.24127)<br>Matthew Gwilliam, Roy Zhang, Namitha Padmanabhan, Hongyang Du, Abhinav Shrivastava<br><sub>Controlled study of INR components and training budgets (encoding speed evidence)</sub> | [![Functional](https://img.shields.io/badge/Functional-Video-purple)]() | [![Controlled Study](https://img.shields.io/badge/Controlled_Study-green)]() [![Encoding Speed](https://img.shields.io/badge/Encoding_Speed-green)]()<br>[![Extension](https://img.shields.io/badge/Extension-yellow)]() | [Paper](https://arxiv.org/abs/2506.24127) |
| [![Computers & Geosciences](https://img.shields.io/badge/Computers_%26_Geosciences-2026-blue)]() <br>[HiHa: Introducing hierarchical harmonic decomposition to implicit neural compression for atmospheric data](https://arxiv.org/abs/2411.06155)<br>Zhewen Xu, Baoxiang Pan, Xiaohui Wei, Hongliang Li, Dongyuan Tian, Zijian Li, Changzheng Liu<br><sub>HiHa: complex-harmonic decomposition, sparse storage, multi-resolution INRs, temporal residual coding</sub> | [![Functional](https://img.shields.io/badge/Functional-Other_Data_Modalities-purple)]() | [![Harmonic Decomposition](https://img.shields.io/badge/Harmonic_Decomposition-green)]() [![Temporal Residual](https://img.shields.io/badge/Temporal_Residual-green)]() | [Paper](https://arxiv.org/abs/2411.06155) |
| [![Signal Processing](https://img.shields.io/badge/Signal_Processing-2026-blue)]() <br>[Entropy-aware image representation via 2D Gaussian splatting](https://doi.org/10.1016/j.sigpro.2026.110521)<br>Jiacong Chen, Qingyu Mao, Shuai Liu, Chao Li, Jierun Lin, Xiandong Meng, Fanyang Meng, Yongsheng Liang<br><sub>Quadtree partition, Gaussians allocated to approximately entropy-balanced regions</sub> | [![Primitive](https://img.shields.io/badge/Primitive-2D_Image-purple)]() | [![Quadtree](https://img.shields.io/badge/Quadtree-green)]() [![Entropy-aware Allocation](https://img.shields.io/badge/Entropy--aware_Allocation-green)]()<br>[![Rate Optimization](https://img.shields.io/badge/Rate_Optimization-yellow)]() | [Paper](https://doi.org/10.1016/j.sigpro.2026.110521) |
| [![CVPR](https://img.shields.io/badge/CVPR-2026-blue)]() <br>[SGI: Structured 2D Gaussians for efficient and compact large image representation](https://arxiv.org/abs/2603.07789)<br>Zixuan Pan, Kaiyuan Tang, Jun Xia, Yifan Qin, Lin Gu, Chaoli Wang, Jianxu Chen, Yiyu Shi<br><sub>SGI couples seed-based structure to context-guided entropy coding</sub> | [![Primitive](https://img.shields.io/badge/Primitive-2D_Image-purple)]() | [![Seed Structure](https://img.shields.io/badge/Seed_Structure-green)]() [![Context Model](https://img.shields.io/badge/Context_Model-green)]() [![Entropy Coding](https://img.shields.io/badge/Entropy_Coding-green)]()<br>[![Rate Optimization](https://img.shields.io/badge/Rate_Optimization-yellow)]() | [Paper](https://arxiv.org/abs/2603.07789)<br>[Code](https://github.com/zx-pan/SGI) |
| [![AAAI](https://img.shields.io/badge/AAAI-2026-blue)]() <br>[GaussianImage++: Boosted image representation and compression with 2D Gaussian splatting](https://arxiv.org/abs/2512.19108)<br>Tiantian Li, Xinjie Zhang, Xingtong Ge, Tongda Xu, Dailan He, Jun Zhang, Yan Wang<br><sub>GaussianImage++: distortion-driven densification with attribute-separated quantization-aware training</sub> | [![Primitive](https://img.shields.io/badge/Primitive-2D_Image-purple)]() | [![Densification](https://img.shields.io/badge/Densification-green)]() [![QAT](https://img.shields.io/badge/QAT-green)]()<br>[![Rate Optimization](https://img.shields.io/badge/Rate_Optimization-yellow)]() | [Paper](https://arxiv.org/abs/2512.19108)<br>[Code](https://github.com/Sweethyh/GaussianImage_plus) |
| [![Inf. Sci.](https://img.shields.io/badge/Inf._Sci.-2026-blue)]() <br>[VeGaS: Video Gaussian splatting](https://arxiv.org/abs/2411.11024)<br>Weronika Smolak-Dyżewska, Dawid Malarz, Kornel Howil, Jan Kaczmarczyk, Marcin Mazur, Przemysław Spurek<br><sub>VeGaS generates frame-conditioned 2D Gaussians through Folded-Gaussians</sub> | [![Primitive](https://img.shields.io/badge/Primitive-Video-purple)]() | [![Folded Gaussians](https://img.shields.io/badge/Folded_Gaussians-green)]() [![Frame-conditioned](https://img.shields.io/badge/Frame--conditioned-green)]()<br>[![Capacity](https://img.shields.io/badge/Capacity-yellow)]() | [Paper](https://arxiv.org/abs/2411.11024)<br>[Code](https://github.com/gmum/VeGaS) |
| [![WACV](https://img.shields.io/badge/WACV-2026-blue)]() <br>[Gaussian representations for video](https://doi.org/10.1109/WACV61042.2026.00087)<br>Sachin Shah, Anustup Choudhury, Guan-Ming Su, Jaclyn Pytlarz, Christopher A. Metzler, Trisha Mittal<br><sub>GaRV: quantized Gaussian video representation with random and foveated access</sub> | [![Primitive](https://img.shields.io/badge/Primitive-Video-purple)]() | [![Quantization](https://img.shields.io/badge/Quantization-green)]() [![Random Access](https://img.shields.io/badge/Random_Access-green)]() [![Foveated](https://img.shields.io/badge/Foveated-green)]()<br>[![Capacity](https://img.shields.io/badge/Capacity-yellow)]() | [Paper](https://doi.org/10.1109/WACV61042.2026.00087) |
| [![ISCAS](https://img.shields.io/badge/ISCAS-2026-blue)]() <br>[GFix: Perceptually enhanced Gaussian splatting video compression](https://arxiv.org/abs/2511.06953)<br>Siyue Teng, Ge Gao, Duolikun Danier, Yuxuan Jiang, Fan Zhang, Nantheera Anantrasirichai, Thomas Davis, Zoe Liu, et al.<br><sub>GFix: single-step diffusion enhancer with modulated LoRA; entropy-codes the modulation parameters</sub> | [![Primitive](https://img.shields.io/badge/Primitive-Video-purple)]() | [![Diffusion Enhancer](https://img.shields.io/badge/Diffusion_Enhancer-green)]() [![LoRA](https://img.shields.io/badge/LoRA-green)]() [![Entropy Coding](https://img.shields.io/badge/Entropy_Coding-green)]()<br>[![RD Optimization](https://img.shields.io/badge/RD_Optimization-yellow)]() | [Paper](https://arxiv.org/abs/2511.06953) |
| [![TVCG](https://img.shields.io/badge/TVCG-2026-blue)]() <br>[PSAvatar: A point-based shape model for real-time head avatar animation with 3D Gaussian splatting](https://arxiv.org/abs/2401.12900)<br>Zhongyuan Zhao, Zhenyu Bao, Qing Li, Guoping Qiu, Kanglin Liu<br><sub>PSAvatar converts a FLAME mesh into a point-based morphable shape model</sub> | [![Primitive](https://img.shields.io/badge/Primitive-3D_Scenes-purple)]() | [![Template Prior](https://img.shields.io/badge/Template_Prior-green)]() [![Avatar](https://img.shields.io/badge/Avatar-green)]()<br>[![Capacity](https://img.shields.io/badge/Capacity-yellow)]() | [Paper](https://arxiv.org/abs/2401.12900) |
| [![C&G](https://img.shields.io/badge/C%26G-2026-blue)]() <br>[QuantizationGS: Differentiable quantization model for 3D Gaussian splatting compression](https://doi.org/10.1016/j.cag.2026.104596)<br>Yiming Ma, Hanlin Mou, Jing Tian, Tong Liu, Daobing Zhang<br><sub>QuantizationGS: differentiable low-bit quantization, bit packing and zlib</sub> | [![Primitive](https://img.shields.io/badge/Primitive-3D_Scenes-purple)]() | [![Differentiable Quantization](https://img.shields.io/badge/Differentiable_Quantization-green)]() [![Bit Packing](https://img.shields.io/badge/Bit_Packing-green)]() [![zlib](https://img.shields.io/badge/zlib-green)]()<br>[![Rate Optimization](https://img.shields.io/badge/Rate_Optimization-yellow)]() | [Paper](https://doi.org/10.1016/j.cag.2026.104596) |
| [![AAAI](https://img.shields.io/badge/AAAI-2026-blue)]() <br>[PCGS: Progressive compression of 3D Gaussian splatting](https://arxiv.org/abs/2503.08511)<br>Yihang Chen, Mengyao Li, Qianyi Wu, Weiyao Lin, Mehrtash Harandi, Jianfei Cai<br><sub>PCGS controls primitive quantity and attribute quality progressively</sub> | [![Primitive](https://img.shields.io/badge/Primitive-3D_Scenes-purple)]() | [![Progressive](https://img.shields.io/badge/Progressive-green)]() [![Quantity + Quality Control](https://img.shields.io/badge/Quantity_%2B_Quality_Control-green)]()<br>[![Rate Optimization](https://img.shields.io/badge/Rate_Optimization-yellow)]() | [Paper](https://arxiv.org/abs/2503.08511)<br>[Code](https://github.com/YihangChen-ee/PCGS) |
| [![TCSVT](https://img.shields.io/badge/TCSVT-2026-blue)]() <br>[Feedforward compression of static and streamable 3D Gaussian splatting](https://arxiv.org/abs/2410.08017)<br>Yihang Chen, Qianyi Wu, Mengyao Li, Weiyao Lin, Junhui Hou, Mehrtash Harandi, Jianfei Cai<br><sub>FCGS models inter- and intra-Gaussian context with multi-path entropy coding</sub> | [![Primitive](https://img.shields.io/badge/Primitive-3D_Scenes-purple)]() | [![Feedforward](https://img.shields.io/badge/Feedforward-green)]() [![Inter/Intra Context](https://img.shields.io/badge/Inter%2FIntra_Context-green)]() [![Multi-path Entropy Coding](https://img.shields.io/badge/Multi--path_Entropy_Coding-green)]()<br>[![Rate Optimization](https://img.shields.io/badge/Rate_Optimization-yellow)]() | [Paper](https://arxiv.org/abs/2410.08017)<br>[Code](https://github.com/YihangChen-ee/FCGS) |
| [![DCC](https://img.shields.io/badge/DCC-2026-blue)]() <br>[Voxel-GS: Quantized scaffold Gaussian splatting compression with run-length coding](https://arxiv.org/abs/2512.17528)<br>Chunyang Fu, Xiangrui Liu, Shiqi Wang, Zhu Li<br><sub>Voxel-GS couples a quantized Scaffold-GS organization to run-length coding</sub> | [![Primitive](https://img.shields.io/badge/Primitive-3D_Scenes-purple)]() | [![Quantized Scaffold](https://img.shields.io/badge/Quantized_Scaffold-green)]() [![Run-length Coding](https://img.shields.io/badge/Run--length_Coding-green)]()<br>[![Rate Optimization](https://img.shields.io/badge/Rate_Optimization-yellow)]() | [Paper](https://arxiv.org/abs/2512.17528) |
| [![DCC](https://img.shields.io/badge/DCC-2026-blue)]() <br>[Region-adaptive learned hierarchical encoding for 3D Gaussian splatting data](https://arxiv.org/abs/2510.22812)<br>Shashank N. Sridhara, Birendra Kathariya, Fangjun Pu, Peng Yin, Eduardo Pavez, Antonio Ortega<br><sub>Region-adaptive hierarchical encoding changes the partitioning of coded state</sub> | [![Primitive](https://img.shields.io/badge/Primitive-3D_Scenes-purple)]() | [![Region-adaptive](https://img.shields.io/badge/Region--adaptive-green)]() [![Hierarchical Encoding](https://img.shields.io/badge/Hierarchical_Encoding-green)]()<br>[![Rate Optimization](https://img.shields.io/badge/Rate_Optimization-yellow)]() | [Paper](https://arxiv.org/abs/2510.22812) |
| [![TCSVT](https://img.shields.io/badge/TCSVT-2026-blue)]() <br>[Light4GS: Lightweight compact 4D Gaussian splatting generation via context model](https://arxiv.org/abs/2503.13948)<br>Mufan Liu, Qi Yang, He Huang, Wenjie Huang, Zhenlong Yuan, Zhu Li, Yiling Xu, Yunfeng Guan<br><sub>Light4GS prunes deformable primitives using spatiotemporal significance</sub> | [![Primitive](https://img.shields.io/badge/Primitive-Dynamic_Scene-purple)]() | [![Spatiotemporal Significance Pruning](https://img.shields.io/badge/Spatiotemporal_Significance_Pruning-green)]()<br>[![Rate Optimization](https://img.shields.io/badge/Rate_Optimization-yellow)]() | [Paper](https://arxiv.org/abs/2503.13948)<br>[Code](https://github.com/Evan-sudo/Light4GS) |
| [![SIGGRAPH](https://img.shields.io/badge/SIGGRAPH-2026-blue)]() <br>[CAGS: Color-adaptive volumetric video streaming with dynamic 3D Gaussian splatting](https://arxiv.org/abs/2605.09279)<br>Daheng Yin, Yili Jin, Jianxin Shi, Isaac Ding, Miao Zhang, Fangxin Wang, Zhaowu Huang, Cong Zhang, et al.<br><sub>CAGS forms VQ-based LoDs and transmits tiled Gaussian data with a reference-image stream</sub> | [![Primitive](https://img.shields.io/badge/Primitive-Dynamic_Scene-purple)]() | [![VQ Levels of Detail](https://img.shields.io/badge/VQ_Levels_of_Detail-green)]() [![Tiled Streaming](https://img.shields.io/badge/Tiled_Streaming-green)]()<br>[![Rate Optimization](https://img.shields.io/badge/Rate_Optimization-yellow)]() | [Paper](https://arxiv.org/abs/2605.09279) |
| [![CVPR](https://img.shields.io/badge/CVPR-2026-blue)]() <br>[PackUV: Packed Gaussian UV maps for 4D volumetric video](https://arxiv.org/abs/2602.23040)<br>Aashish Rai, Angela Xing, Anushka Agarwal, Xiaoyan Cong, Zekun Li, Tao Lu, Aayush Prakash, Srinath Sridhar<br><sub>PackUV organizes temporally coherent attributes as a progressive UV atlas for HEVC / FFV1</sub> | [![Primitive](https://img.shields.io/badge/Primitive-Dynamic_Scene-purple)]() | [![UV Atlas](https://img.shields.io/badge/UV_Atlas-green)]() [![Video Codec Backend](https://img.shields.io/badge/Video_Codec_Backend-green)]()<br>[![Rate Optimization](https://img.shields.io/badge/Rate_Optimization-yellow)]() | [Paper](https://arxiv.org/abs/2602.23040)<br>[Code](https://github.com/aashishrai3799/packuv) |
| [![DCC](https://img.shields.io/badge/DCC-2026-blue)]() <br>[Towards efficient 3D Gaussian human avatar compression: A prior-guided framework](https://arxiv.org/abs/2510.10492)<br>Shanzhi Yin, Bolin Chen, Xinju Wu, Ru-Ling Liao, Jie Chen, Shiqi Wang, Yan Ye<br><sub>Prior-guided avatar compression exploits subject-specific structure</sub> | [![Primitive](https://img.shields.io/badge/Primitive-Dynamic_Scene-purple)]() | [![Prior-guided](https://img.shields.io/badge/Prior--guided-green)]() [![Avatar](https://img.shields.io/badge/Avatar-green)]()<br>[![Rate Optimization](https://img.shields.io/badge/Rate_Optimization-yellow)]() | [Paper](https://arxiv.org/abs/2510.10492) |
| [![WACV](https://img.shields.io/badge/WACV-2026-blue)]() <br>[TED-4DGS: Temporally activated and embedding-based deformation for 4DGS compression](https://arxiv.org/abs/2512.05446)<br>Cheng-Yuan Ho, He-Bi Yang, Jui-Chiu Chiang, Yu-Lun Liu, Wen-Hsiao Peng<br><sub>TED-4DGS: temporally activated deformation, INR hyperprior, channel-wise autoregressive entropy models</sub> | [![Primitive](https://img.shields.io/badge/Primitive-Dynamic_Scene-purple)]() | [![Temporally Activated Deformation](https://img.shields.io/badge/Temporally_Activated_Deformation-green)]() [![INR Hyperprior](https://img.shields.io/badge/INR_Hyperprior-green)]() [![Channel-wise AR](https://img.shields.io/badge/Channel--wise_AR-green)]()<br>[![RD Optimization](https://img.shields.io/badge/RD_Optimization-yellow)]() | [Paper](https://arxiv.org/abs/2512.05446)<br>[Code](https://github.com/NYCU-MAPL/TED-4DGS) |
| [![AAAI](https://img.shields.io/badge/AAAI-2026-blue)]() <br>[D-FCGS: Feedforward compression of dynamic Gaussian splatting for free-viewpoint videos](https://arxiv.org/abs/2507.05859)<br>Wenkang Zhang, Yan Zhao, Qiang Wang, Zhixin Xu, Li Song, Zhengxue Cheng<br><sub>D-FCGS: Group-of-Frames I–P structure, control-point motion compensation, hyperprior + spatial–temporal priors</sub> | [![Primitive](https://img.shields.io/badge/Primitive-Dynamic_Scene-purple)]() | [![GoF I–P Structure](https://img.shields.io/badge/GoF_I–P_Structure-green)]() [![Motion Compensation](https://img.shields.io/badge/Motion_Compensation-green)]() [![Hyperprior](https://img.shields.io/badge/Hyperprior-green)]()<br>[![RD Optimization](https://img.shields.io/badge/RD_Optimization-yellow)]() | [Paper](https://arxiv.org/abs/2507.05859)<br>[Code](https://github.com/Mr-Zwkid/D-FCGS) |

## 🔬 Source-Verified Empirical Anchors (Sec. 5)

The nine in-taxonomy anchors retained by the survey's targeted controlled audit (Table 3), with the primary reported mechanism tags used there. The survey treats their numbers as **source-local observations**: no cross-method panel passed the matched-protocol gate, so this table is not a leaderboard.

| Route | Taxonomy placement | Method | Primary mechanism | Links |
| --- | --- | --- | --- | :---: |
| Functional | 2D Image: End-to-End Optimization | [FNLIC](https://doi.org/10.1109/cvpr52734.2025.02165) | Latent fitting; entropy coding | [Paper](https://doi.org/10.1109/cvpr52734.2025.02165) · [Code](https://github.com/ZZ022/FNLIC) |
| Functional | Video: Rate Reduction | [HiNeRV](https://arxiv.org/abs/2306.09818) | Pruning; parameter quantization | [Paper](https://arxiv.org/abs/2306.09818) · [Code](https://github.com/hmkx/HiNeRV) |
| Functional | Dynamic 4D Scenes & Volumetric Video | [K-Planes](https://arxiv.org/abs/2301.10241) | Plane factorization | [Paper](https://arxiv.org/abs/2301.10241) · [Code](https://github.com/sarafridov/K-Planes) |
| Functional | Other Data Modalities: Climate and Atmospheric Data | [CA-INR](https://doi.org/10.1038/s41598-025-11092-w) | Context conditioning; weight quantization | [Paper](https://doi.org/10.1038/s41598-025-11092-w) |
| Functional | Other Data Modalities: Biomedical Volumetric Data | [SCI](https://arxiv.org/abs/2209.15180) | Block partitioning; weight serialization | [Paper](https://arxiv.org/abs/2209.15180) |
| Parametric Primitive | 2D Image | [GaussianImage](https://arxiv.org/abs/2403.08551) | Attribute quantization; residual VQ | [Paper](https://arxiv.org/abs/2403.08551) · [Code](https://github.com/Xinjie-Q/GaussianImage) |
| Parametric Primitive | 3D Scenes: Rate Optimization | [Compressed 3DGS](https://arxiv.org/abs/2401.02436) | Attribute quantization; DEFLATE | [Paper](https://arxiv.org/abs/2401.02436) · [Code](https://github.com/KeKsBoTer/c3dgs) |
| Parametric Primitive | 3D Scenes: Rate Optimization | [EAGLES](https://arxiv.org/abs/2312.04564) | Latent attributes; pruning; entropy coding | [Paper](https://arxiv.org/abs/2312.04564) · [Code](https://github.com/Sharath-girish/efficientgaussian) |
| Parametric Primitive | Dynamic Scene: Rate–Distortion Optimization | [4DGC](https://arxiv.org/abs/2503.18421) | Motion grids; sparsification; entropy modeling | [Paper](https://arxiv.org/abs/2503.18421) · [Code](https://github.com/MediaX-SJTU/4DGC) |

## 📝 Citation

If you find this survey or repository useful, please consider citing:

```bibtex
@article{bao2026instancefitted,
  title   = {Instance-Fitted Representations for Data Compression: A Survey},
  author  = {Bao, Youneng and Cheng, Yulong and Liu, Yiping and Chen, Jiacong and Liang, Yongsheng},
  year    = {2026},
  note    = {Manuscript. Repository: https://github.com/smileto1/A-Survey-of-Representation-as-Compression}
}
```

The BibTeX entries of all works listed here are collected in [`survey_refs.bib`](survey_refs.bib).

## ✉️ Contact

Questions, corrections and new entries are welcome through [GitHub issues](https://github.com/smileto1/A-Survey-of-Representation-as-Compression/issues) or pull requests. Maintainers: [Youneng Bao](https://github.com/baoyu2020), [Yulong Cheng](https://github.com/smileto1/), [Jiacong Chen](https://github.com/ChenJiaCong-1005).

## License

This repository is released under the [MIT License](LICENSE).
