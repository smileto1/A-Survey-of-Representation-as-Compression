# -*- coding: utf-8 -*-
"""Placement of every work cited in the survey manuscript, mirroring its section structure.

Each entry: (bibkey, [mechanism tags], "one-line note paraphrasing how the manuscript describes it")
Groups mirror the \\subsubsection / \\textbf paragraph headings of Sections 3 and 4.
Stage labels follow the manuscript's capacity / rate / rate-distortion grouping.
"""

CAP = "Capacity"
RATE = "Rate Optimization"
RD = "RD Optimization"
EXT = "Extension"
CTX = "Context"

# ---------------------------------------------------------------------------
# Section 3: Functional Representations
# ---------------------------------------------------------------------------
FUNCTIONAL = {
    "route": "Functional",
    "anchor": "functional-representations",
    "title": "Functional Representations (Sec. 3)",
    "intro": (
        "Functional methods fit a query-conditioned observation operator and reconstruct by evaluating, "
        "interpolating or integrating a function- or field-like state (weights, modulations, latents, grids, "
        "tensors, hash features). The fitted state need not be the whole compressed object: a payload may "
        "combine weights, latents, grids, codebooks, masks and side information; the survey reserves the term "
        "codec for methods that specify a decodable serialization, all decoder-required state and complete payload accounting."
    ),
    "modalities": [
        {
            "name": "2D Image",
            "anchor": "functional-2d-image",
            "intro": "Central difficulty: fitting edges and textures without unchecked growth of instance-specific state.",
            "groups": [
                (CAP, "Representation Capacity Improvement — Input mappings", [
                    ("rahaman2019spectral", ["Spectral Bias", "Theory"], "Standard coordinate MLPs preferentially learn low frequencies"),
                    ("tancik2020fourier", ["Input Mapping"], "Fourier features let the effective kernel represent high-frequency functions"),
                    ("yan2024stagewise", ["Input Mapping"], "Stagewise positional encoding adapts base frequencies using local fractal dimensions"),
                    ("chu2024cpe", ["Input Mapping", "Partitioning", "Quantization"], "Chebyshev approximation + adaptable partitioning + integrated quantization"),
                ]),
                (CAP, "Representation Capacity Improvement — Activations", [
                    ("sitzmann2020implicit", ["Activation"], "SIREN: sinusoidal activations fit fine spatial variation"),
                    ("saragadam2023wire", ["Activation"], "WIRE: localized Gabor-wavelet responses"),
                    ("liu2024finer", ["Activation"], "FINER: variable-periodic activations control represented frequencies"),
                ]),
                (CAP, "Representation Capacity Improvement — Architectures", [
                    ("yan2025inram", ["Architecture", "Spatial Recombination", "Channel Recalibration"], "INRAM: Spatial Recombination and Channel Recalibration model spatial / channel relations"),
                    ("cai2024conv", ["Architecture", "Convolution"], "Conv-INR injects locality into the decoder"),
                    ("pham2023autoencoding", ["Predicted Parameters"], "Cross-instance autoencoding amortizes INR generation through predicted parameters"),
                    ("gordon2024d", ["Hypernetwork"], "D'OH: decoder-only random hypernetwork optimized for one signal, no offline data"),
                    ("ladune2023cool", ["Latent Grid", "Lightweight Decoder"], "COOL-CHIC: instance state in multi-resolution latent grids decoded by lightweight networks"),
                    ("kim2024c3", ["Latent Grid", "Lightweight Decoder"], "C3: latent grids + lightweight synthesis; grid symbols and entropy model are explicit rate carriers"),
                ]),
                (RATE, "Rate Optimization", [
                    ("li2023hybrid", ["Pruning"], "Weight sparsification removes fitted-network connections"),
                    ("jayasundara2025sinr", ["Sparse Coding", "Dictionary"], "SINR: INR-weight vectors represented with sparse dictionary codes"),
                    ("han2025towards", ["Bit-plane"], "Bit-plane decomposition changes weight discretization"),
                    ("dupont2021coin", ["Quantization", "Quantized Network Weights"], "COIN: fitted 32-bit parameters mapped to 16-bit values; quantized weights are the payload"),
                    ("dupont2022coin", ["Quantization", "Entropy Coding", "Meta-Learning", "Modulations"], "COIN++: quantizes and entropy-codes instance modulations of a meta-learned base network"),
                    ("chu2024cpe", ["Quantization"], "CPE integrates nonlinear quantization with representation design"),
                    ("catania2026paaf", ["Quantization", "Entropy Coding"], "PaaF: codec-side adaptive quantization and entropy coding; rate follows the serialized configuration"),
                ]),
                (RD, "Rate–Distortion Optimization", [
                    ("lee2023entropy", ["Entropy Constraint", "Probability Model over Parameters"], "Weight-level entropy constraint approximates quantization and regularizes a probability model over parameters"),
                    ("ladune2023cool", ["Latent Grid", "Autoregressive Model", "Rate–Distortion Objective"], "Jointly fits quantized multi-resolution latents, lightweight synthesis parameters and autoregressive models"),
                    ("kim2024c3", ["Latent Grid", "Autoregressive Model", "Rate–Distortion Objective"], "Jointly fits quantized latents, synthesis parameters and autoregressive entropy models"),
                    ("benjak2026lance", ["Spatial Hyperprior", "Locally Varying Latent Statistics"], "LANCE: predicts locally varying latent statistics from a forward-signaled spatial hyperprior"),
                    ("zhang2025fitted", ["Lossless", "Per-image Latents", "Entropy Coding"], "FNLIC: fits per-image latents, AR model and decoder; entropy-codes fitted state and image with a pre-fitted prior"),
                ]),
                (RD, "Rate–Distortion Optimization — Other objectives remain distinct", [
                    ("wu2025lotterycodec", ["Mask Selection"], "LotteryCodec relaxes binary-mask selection; a differentiable entropy estimate becomes codec evidence only when the selected symbols and side information are serialized"),
                    ("he2023recombiner", ["Variational Bayesian"], "Recombiner uses variational Bayesian compression"),
                ]),
            ],
        },
        {
            "name": "Video",
            "anchor": "functional-video",
            "intro": "Video adds temporal redundancy and decoding-throughput constraints; reported rates may cover different combinations of weights, embeddings, motion features and auxiliary models.",
            "groups": [
                (None, "Cited in the subsection introduction", [
                    ("chen2021nerv", ["Frame Indices to Frames", "Compressed Model Parameters"], "NeRV maps frame indices to frames, with compressed model parameters as its main payload"),
                ]),
                (CAP, "Representation Capacity Improvement — Spatial decoding", [
                    ("chen2023hnerv", ["Hybrid Representation", "Pyramidal Decoder"], "HNeRV: hybrid representation with a pyramidal decoder"),
                    ("kwan2023hinerv", ["Hierarchical Encoding"], "HiNeRV allocates capacity hierarchically across spatial scales"),
                ]),
                (CAP, "Representation Capacity Improvement — Temporal dependence", [
                    ("zhao2023dnerv", ["Frame Difference"], "D-NeRV encodes frame differences"),
                    ("lee2023ffnerv", ["Optical Flow"], "FFNeRV aggregates optical-flow-guided information"),
                    ("zhang2024boosting", ["Decoded Context"], "Conditional decoder reuses decoded context"),
                    ("maiya2023nirvana", ["Autoregressive"], "NIRVANA: autoregressive design reusing decoded context"),
                ]),
                (RATE, "Rate Optimization — Pruning and subnetwork selection", [
                    ("chen2021nerv", ["Pruning", "Quantization", "Entropy Coding"], "Post-fitting global pruning, quantization and entropy coding"),
                    ("zhao2023dnerv", ["Pruning", "Quantization", "Entropy Coding"], "NeRV-family pipeline: global pruning, quantization, entropy coding"),
                    ("chen2023hnerv", ["Pruning", "Quantization", "Entropy Coding"], "NeRV-family pipeline: global pruning, quantization, entropy coding"),
                    ("kwan2023hinerv", ["Pruning", "Magnitudes Relative to Layer Size"], "Scores magnitudes relative to layer size to accommodate layer-dependent redundancy"),
                    ("LotteryTicke", ["Lottery Ticket", "Sparse Subnetwork"], "Lottery-ticket search for sparse subnetworks in neural video representations"),
                    ("guo2025metanerv", ["Meta-Learning", "Faster Adaptation"], "MetaNeRV learns an initialization for faster adaptation"),
                ]),
                (RATE, "Rate Optimization — Quantization", [
                    ("chen2021nerv", ["Scalar Quantization", "Post-training"], "Scalar quantization after fitting and pruning"),
                    ("chen2023hnerv", ["Scalar Quantization", "Post-training"], "Scalar quantization after fitting and pruning"),
                    ("lee2023ffnerv", ["Quantization-aware Training", "STE"], "Moves discretization into training through a straight-through estimator"),
                    ("kwan2023hinerv", ["Quantization-aware Training", "Noise-based Simulation"], "Noise-based quantization simulation during training"),
                    ("xu2024vq", ["Vector Quantization", "Codebook"], "VQ-NeRV discretizes shallow and inter-frame residual features with learned codebooks"),
                ]),
                (RD, "Rate–Distortion Optimization", [
                    ("leguay2024cool", ["Latent Grid", "Entropy Coding", "Rate–Distortion Objective"], "COOL-CHIC video optimizes and entropy-codes per-frame latents and lightweight decoder parameters"),
                    ("gomes2023video", ["Entropy Constraint", "Representation and Quantizer"], "Jointly optimizes representation and quantizer under an entropy constraint on model weights"),
                    ("kwan2024nvrc", ["Entropy-model Parameters", "Entropy Model", "Rate–Distortion Objective"], "NVRC jointly optimizes and hierarchically codes representation, quantizer and entropy-model parameters"),
                    ("kwan2026nvrcpp", ["High-resolution Grids", "Complexity Levels"], "NVRC++: multiple high-resolution grids and entropy model across four decoder-complexity levels"),
                ]),
                (EXT, "Other Specialized Extensions", [
                    ("guo2025metanerv", ["Faster Adaptation"], "Targets adaptation time"),
                    ("chen2024fast", ["Training or Inference Throughput"], "Fast neural video coding targets training / inference throughput"),
                    ("E-NeRV", ["Architectural Factorization"], "E-NeRV reduces complexity through architectural factorization"),
                    ("zhao2024pnerv", ["Progressive Features"], "PNeRV reduces complexity through progressive feature processing"),
                    ("gwilliam2025design", ["Controlled Study", "Encoding Speed"], "Controlled study of INR components and training budgets (encoding speed evidence)"),
                ]),
            ],
        },
        {
            "name": "3D Static Scene",
            "anchor": "functional-3d-static-scene",
            "intro": "Static neural scenes must preserve view-dependent appearance and geometry; hybrid NeRFs move signal from an MLP into grids, tensors or hash tables, so compression concerns the full scene state.",
            "groups": [
                (None, "Cited in the subsection introduction", [
                    ("mildenhall2021nerf", ["Radiance Field", "MLP"], "Neural radiance field; hybrid NeRFs move signal from the MLP into grids, tensors or hash tables"),
                    ("yu2021plenoxelsradiancefieldsneural", ["Radiance Field", "Grid"], "Hybrid radiance field cited for moving signal from an MLP into grids (title: radiance fields without neural networks)"),
                    ("mueller2022instant", ["Radiance Field", "Hash Table"], "Hybrid radiance field cited for moving signal from an MLP into hash tables"),
                    ("TensoRF", ["Radiance Field", "Tensor"], "Hybrid radiance field cited for moving signal from an MLP into tensors"),
                ]),
                (CAP, "Representation Capacity Improvement — Hybrid spatial structures", [
                    ("mueller2022instant", ["Hash Grid"], "Instant NGP stores multi-resolution hash features"),
                    ("TensoRF", ["Vector–Matrix Components"], "TensoRF factorizes radiance fields into vector–matrix components"),
                    ("SqueezeNeRF", ["Factorization", "Inference-cache Memory"], "SqueezeNeRF factorizes FastNeRF to reduce inference-cache memory"),
                ]),
                (CAP, "Representation Capacity Improvement — Sampling and geometry", [
                    ("AdaNeRF", ["Adaptive Sampling"], "Learns adaptive sampling and shading to reduce rendering samples (computation, not parameter compression)"),
                    ("Depth-supervised", ["Depth Supervision"], "Depth supervision stabilizes sparse-view fitting"),
                    ("MVSNeRF", ["Multiview Cost Volume"], "Multiview cost volumes stabilize sparse-view fitting"),
                    ("Neuralsparse", ["Sparse Geometry", "Skip Empty Space"], "Sparse geometry skips empty space"),
                    ("Plen-VDB", ["Occupancy Structure"], "Occupancy structure skips empty space"),
                ]),
                (RATE, "Rate Optimization — Structural reduction", [
                    ("TensoRF", ["Factorization"], "Factorizes dense grids"),
                    ("Plen-VDB", ["Pruning", "Occupancy"], "Exploits occupancy to prune explicit parameters"),
                    ("Shell-Guided", ["Pruning", "Surfaces"], "Shell-guided pruning of voxel radiance fields using surfaces"),
                ]),
                (RATE, "Rate Optimization — Symbol reduction", [
                    ("Real-Time", ["Vector Quantization", "Codebook"], "Neural codebook maps features to codebook indices"),
                    ("VQRF", ["Vector Quantization", "Codebook"], "Vector-quantized radiance fields map features to codebook indices"),
                    ("Quant-NeRF", ["Scalar Quantization"], "Scalar quantization of features"),
                    ("MaskedWavelet", ["Wavelet", "Sparsity-aware Coding"], "Sparsity-aware coding of masked wavelet coefficients"),
                ]),
                (RD, "Rate–Distortion Optimization", [
                    ("bird20213d", ["Entropy Penalty", "Reparameterized Weights"], "cNeRF: entropy penalty on reparameterized weights"),
                    ("CodecNeRF", ["Encoder–Decoder", "Fine-tuning"], "CodecNeRF: encoder–decoder–fine-tuning pipeline"),
                    ("li2024nerfcodec", ["Learned Scene Features", "Rate–Distortion Objective"], "NeRFCodec attaches rate to learned scene features"),
                    ("Content-Aware", ["Scene-adaptive Parameter Precision"], "Content-Aware Radiance Fields: scene-adaptive parameter precision"),
                    ("ECRF", ["Frequency Domain"], "ECRF: rate on frequency-domain transform coefficients"),
                ]),
            ],
        },
        {
            "name": "Dynamic 4D Scenes & Volumetric Video",
            "anchor": "functional-dynamic-4d-scenes--volumetric-video",
            "intro": "Dynamic radiance fields motivate shared, factorized or predicted features instead of an independent full scene per instant.",
            "groups": [
                (None, "Representation evolution", [
                    ("cao2023hexplane", ["Coordinate-pair Planes"], "HexPlane factorizes spatiotemporal fields over coordinate-pair planes"),
                    ("fridovich2023kplanes", ["Coordinate-pair Planes"], "K-Planes: explicit radiance fields in space, time and appearance via plane factorization"),
                    ("wu2024tetrirf", ["Temporal Tri-planes"], "TeTriRF uses temporal tri-planes"),
                    ("zheng2024jointrf", ["Residual and Coefficient Grids", "Compression Subnetwork"], "JointRF combines residual and coefficient grids with a compression subnetwork"),
                    ("attal2023hyperreel", ["Keyframes"], "HyperReel uses keyframes"),
                ]),
                (None, "Bitstream formation", [
                    ("wang2024videorf", ["Conventional Video Codecs", "Feature Streams"], "VideoRF serializes learned 2D feature streams for conventional video coding"),
                    ("wu2024tetrirf", ["Conventional Video Codecs"], "Codes temporal tri-plane features conventionally"),
                ]),
                (None, "Joint optimization and delivery", [
                    ("hu2025vrvvc", ["Variable Rate", "Entropy Model"], "VRVVC: variable-rate quantization with a compact entropy model"),
                    ("zheng2024jointrf", ["Joint Optimization"], "Jointly optimizes representation and compression subnetwork"),
                    ("zhang2025nerflow", ["Adaptive Streaming", "Bitrate Ladder"], "NeRFlow adapts streaming by viewpoint and bitrate ladder"),
                ]),
            ],
        },
        {
            "name": "3D Shapes / Volumetric",
            "anchor": "functional-3d-shapes--volumetric",
            "intro": "INRs map coordinates to occupancy, SDF, displacement, density or attributes; carriers may be global weights, local networks, embedded features or hybrids.",
            "groups": [
                (CAP, "Representation Capacity Improvement", [
                    ("rahaman2019spectral", ["Spectral Bias"], "Spectral bias can make standard MLPs oversmooth geometric detail"),
                    ("sitzmann2020implicit", ["Activation"], "Periodic activations better fit fine geometry and texture"),
                    ("kim2024neuralvdb", ["Sparse Hierarchy", "VDB"], "NeuralVDB couples sparse VDB hierarchies with networks encoding lower-level topology and values"),
                    ("do2023volumetric", ["Space-varying Convolution", "Point Cloud"], "Geometry-dependent space-varying convolution models point-cloud attributes"),
                ]),
                (RATE, "Rate Optimization", [
                    ("gu2023nervi", ["Quantization", "Weights"], "NeRVI quantizes and encodes weights after fitting rendered visualization images"),
                    ("pentapati2025mesh", ["Quantization", "Displacement Field"], "Quantizes a learned displacement field over a coarse mesh"),
                    ("jayasundara2025sinr", ["Sparse Coding", "Dictionary"], "High-dimensional sparse codes with a dictionary whose atoms need not be transmitted"),
                    ("bird20213d", ["Entropy Coding"], "Entropy coding shortens quantized symbols when paired with a probability model"),
                ]),
                (RD, "Rate–Distortion Optimization", [
                    ("isik2022lvac", ["Rate–Distortion Lagrangian", "Point Cloud Attributes"], "LVAC optimizes a rate–distortion Lagrangian"),
                    ("huang2025linr", ["Lossless", "Point Cloud Geometry"], "LINR-PCGC: lossless geometry coding"),
                    ("ren2024necgs", ["Quantization-aware Training", "Auto-decoder", "Entropy Coding"], "NeCGS combines a quantization-aware auto-decoder with entropy coding"),
                ]),
            ],
        },
        {
            "name": "Other Data Modalities",
            "anchor": "functional-other-data-modalities",
            "intro": "Medical and Earth-system data differ in dimensionality, spectrum, geometry and fidelity requirements; comparisons require domain baselines and aligned payload boundaries.",
            "groups": [
                (None, "Biomedical Volumetric Data", [
                    ("yang2023sci", ["Block Partitioning", "Spectrum-concentrated Blocks"], "SCI partitions HiP-CT volumes into spectrum-concentrated blocks"),
                    ("li2025compact", ["fMRI", "Reusable Activation"], "Compact fMRI modeling: intra-region correlation, reusable activation patterns, inter-region similarity"),
                    ("dai2025implicit", ["Microscopy", "Pixel-wise Decoding"], "INIF supports adaptive pixel-wise decoding of microscopy data up to 5D"),
                ]),
                (None, "Climate and Atmospheric Data", [
                    ("xu2024hiha", ["Harmonic Decomposition", "Temporal Residual"], "HiHa: complex-harmonic decomposition, sparse storage, multi-resolution INRs, temporal residual coding"),
                    ("mostajeran2025context", ["Context Conditioning", "Weight Quantization"], "CA-INR conditions on physical context such as topography"),
                ]),
                (None, "Emerging Storage Media", [
                    ("le2024implicit", ["Multiple Description", "DNA Storage"], "Implicit neural multiple description coding for robustness in DNA storage"),
                ]),
            ],
        },
    ],
}

# ---------------------------------------------------------------------------
# Section 4: Parametric Primitive Representations
# ---------------------------------------------------------------------------
PRIMITIVE = {
    "route": "Primitive",
    "anchor": "parametric-primitive-representations",
    "title": "Parametric Primitive Representations (Sec. 4)",
    "intro": (
        "Primitive methods organize fitted state as a variable-size collection of spatially addressable local "
        "elements (e.g., Gaussians) and reconstruct by projection, aggregation, splatting or rasterization. "
        "Primitive count and memory are compaction proxies, estimated entropy is a rate surrogate, and only "
        "serialized bits including all side information define operational rate."
    ),
    "modalities": [
        {
            "name": "2D Image",
            "anchor": "primitive-2d-image",
            "intro": "Image compression allocates finite positions, shapes and appearance attributes and then forms a decodable payload.",
            "groups": [
                (None, "2D Image", [
                    ("zhang20242d", ["Vector Quantization", "Entropy Coding"], "Parameterizes 2D Gaussians with vector quantization and entropy coding"),
                    ("zhang2024gaussianimage", ["Quantization", "Residual VQ"], "GaussianImage quantizes position and covariance and applies residual VQ to color"),
                    ("zhang2025image", ["Error-guided Progressive Allocation", "Progressive"], "Image-GS: error-guided progressive allocation"),
                    ("gao20252d", ["Dictionary", "Entropy Coding"], "Maps attributes to pre-trained dictionaries and entropy-codes their indices"),
                    ("liang2025structure", ["Structure-guided Init", "Adaptive Bit Width"], "Structure-guided initialization with adaptive bit widths"),
                    ("CHEN2026110521", ["Quadtree", "Entropy-balanced Regions"], "Quadtree partition, Gaussians allocated to approximately entropy-balanced regions"),
                    ("pan2026sgi", ["Seed-based Structure", "Context Model", "Entropy Coding"], "SGI couples seed-based structure to context-guided entropy coding"),
                    ("li2026gaussianimagepp", ["Densification", "Quantization-aware Training"], "GaussianImage++: distortion-driven densification with attribute-separated quantization-aware training"),
                    ("zhu2025large", ["Level-of-Gaussian", "Large Image"], "LIG: Level-of-Gaussian fitting for large images"),
                    ("hu2025gaussiansr", ["Continuous Gaussian Fields", "Super-resolution"], "GaussianSR: continuous Gaussian fields for arbitrary-scale super-resolution"),
                ]),
            ],
        },
        {
            "name": "Video",
            "anchor": "primitive-video",
            "intro": "Video primitives introduce temporal state: geometry and appearance may be shared while changes are signaled over time.",
            "groups": [
                (None, "Video", [
                    ("bond2025gaussianvideo", ["Spatial and Temporal Features"], "GaussianVideo hierarchically refines spatial and temporal features"),
                    ("sun2024splatter", ["Canonical 3D Gaussian Proxies", "Motion"], "Splatter a Video: canonical 3D Gaussian proxies plus motion"),
                    ("smolak2024vegas", ["Folded Gaussians", "Frame-conditioned"], "VeGaS generates frame-conditioned 2D Gaussians through Folded-Gaussians"),
                    ("shah2026garv", ["Quantization", "Random Access", "Foveated"], "GaRV: quantized Gaussian video representation with random and foveated access"),
                    ("liu2025d2gv", ["Attribute Dimensionality", "Dimensionality Reduction"], "D2GV reduces attribute dimensionality with deformable 2D primitives (version-dependent descriptions)"),
                    ("wang2025gsvc", ["I-frame", "P-frame Splats", "Prediction", "Bitrate Control"], "GSVC codes the first frame as I-frame, predicts later P-frame splats, exposes bitrate control"),
                    ("gupta2025neural", ["Post-training Quant.", "Quantization-aware Training"], "ROI-NVC compares post-training and quantization-aware alternatives (rate–complexity choice)"),
                    ("teng2025gfix", ["Diffusion Enhancer", "LoRA", "Entropy Coding"], "GFix: single-step diffusion enhancer with modulated LoRA; entropy-codes the modulation parameters"),
                ]),
            ],
        },
        {
            "name": "3D Scenes",
            "anchor": "primitive-3d-scenes",
            "intro": "Static 3D payloads may include geometry, opacity, appearance and structure / context metadata; fitting and memory gains are kept distinct from coded-rate evidence.",
            "groups": [
                (CAP, "Representation Capacity Improvement — Initialization", [
                    ("kerbl20233d", ["Structure-from-Motion Point Cloud", "Rasterization", "Precursor"], "3DGS initializes Gaussian positions from the sparse SfM point cloud"),
                    ("niemeyer2025radsplat", ["Radiance Field-informed"], "RadSplat: radiance-field prior to initialize or supervise the fitted state"),
                    ("chen2024text", ["Diffusion-model Priors", "Text-to-3D"], "Diffusion-model prior / score distillation for text-to-3D"),
                    ("yi2024gaussiandreamer", ["Diffusion-model Priors", "Text-to-3D"], "Diffusion-model prior to initialize or supervise the fitted state"),
                    ("chung2024depth", ["Monocular Depth", "Sparse-view Settings"], "Monocular depth guides geometry in sparse-view settings"),
                    ("zhu2024fsgs", ["Monocular Depth", "Sparse-view Settings"], "FSGS: few-shot view synthesis with depth guidance"),
                    ("teotia2024gaussianheads", ["Object-specific Templates", "Avatar"], "GaussianHeads initializes primitives on a deformed facial template"),
                    ("zhao2024psavatar", ["Object-specific Templates", "Avatar"], "PSAvatar converts a FLAME mesh into a point-based morphable shape model"),
                ]),
                (CAP, "Representation Capacity Improvement — Constraints", [
                    ("liang2024gs", ["Normal Estimation", "Inverse Rendering"], "GS-IR: depth-derivation-based regularization for normal estimation"),
                    ("gao2024relightable", ["BRDF", "Inverse Rendering"], "Relightable 3D Gaussians augment the state with normals and BRDF parameters"),
                    ("chen2024text", ["Diffusion-model Priors", "Score Distillation"], "Diffusion-guided text-to-3D: priors including score-distillation guidance when dense multi-view observations are unavailable"),
                    ("yi2024gaussiandreamer", ["Diffusion-model Priors", "Score Distillation"], "Diffusion-guided text-to-3D: priors including score-distillation guidance when dense multi-view observations are unavailable"),
                ]),
                (CAP, "Representation Capacity Improvement — Optimization schedules", [
                    ("cheng2024gaussianpro", ["Progressive Propagation", "Densification"], "GaussianPro progressively propagates existing scene geometry to guide densification"),
                    ("zhang2024fregs", ["Coarse-to-fine Densification"], "FreGS: coarse-to-fine densification from low- to high-frequency components"),
                    ("liu2024citygaussian", ["Divide-and-conquer", "Level of Detail"], "CityGaussian: divide-and-conquer training with LoD for large scenes"),
                ]),
                (CAP, "Representation Capacity Improvement — Adaptive density control", [
                    ("kerbl20233d", ["Density Control"], "View-space positional gradients select primitives for cloning or splitting"),
                    ("fan2024lightgaussian", ["Pruning", "Significance Score", "Distillation"], "LightGaussian prunes using a global significance score with recovery / distillation"),
                    ("hamdi2024ges", ["Kernel Family"], "GES changes the kernel family and represents reported scenes with fewer particles"),
                    ("hu2024gauhuman", ["KL Divergence", "Merging"], "GauHuman: KL divergence guides split / clone and merges redundant Gaussians"),
                    ("zhang2024pixel", ["Pixel-aware Gradient"], "Pixel-GS introduces pixel-aware-gradient density control"),
                ]),
                (RATE, "Rate Optimization — Selecting primitives", [
                    ("navaneet2024compgs", ["Pruning"], "Opacity-, size- or resolution-aware rules remove low-contribution elements"),
                    ("papantonakis2024reducing", ["Pruning"], "Opacity-, size- or resolution-aware rules remove low-contribution elements"),
                    ("lee2024compact", ["Binary Mask", "Pruning"], "Compact3DGS uses a binary mask learned during fitting"),
                    ("ali2025elmgs", ["Pruning", "Quantization Step Sizes"], "ELMGS couples gradient- and opacity-aware pruning with compression; learns quantization step sizes"),
                    ("wang2024end", ["Dynamic Pruning", "Rate Term"], "RDO-Gaussian jointly optimizes dynamic pruning with a rate term"),
                    ("hanson2025pup", ["Sensitivity Score", "Fisher"], "PUP 3D-GS derives a sensitivity score from a Fisher approximation of the error Hessian"),
                ]),
                (RATE, "Rate Optimization — Discretizing their attributes", [
                    ("chen2024hac", ["Adaptive Scalar Quantization", "Hash-grid Assisted Context", "Entropy Coding"], "HAC: adaptive scalar quantization and learned probability model with entropy coding"),
                    ("fan2024lightgaussian", ["Vector Quantization", "Codebook"], "Clusters attributes using vector quantization / codebooks"),
                    ("niedermayr2024compressed", ["Vector Quantization", "DEFLATE"], "Compressed 3DGS: clusters attributes with vector quantization / codebooks and applies DEFLATE after quantization"),
                    ("wang2024end", ["Entropy-constrained Vector Quantization", "Entropy Coding"], "Entropy-constrained vector quantization with learned probability models"),
                    ("girish2024eagles", ["Quantized Latent Vectors", "Entropy Coding", "Pruning"], "EAGLES maps attributes to quantized latents, entropy-codes them, stores their decoder, prunes by influence"),
                    ("ma2026quantizationgs", ["Differentiable Low-bit Quantization", "Bit Packing", "zlib"], "QuantizationGS: differentiable low-bit quantization, bit packing and zlib"),
                ]),
                (RATE, "Rate Optimization — Predicting them from shared structure", [
                    ("lu2024scaffold", ["Anchor", "Prediction"], "Scaffold-GS: sparse anchor features predict nearby attributes"),
                    ("chen2024hac", ["Anchor", "Context Model"], "Anchor attributes predicted from hash-grid spatial context"),
                    ("chen2025hac++", ["Anchor", "Context Model"], "HAC++: towards 100× compression with anchor-based context"),
                    ("liu2024compgs", ["Anchor", "Prediction"], "CompGS: compressed Gaussian splatting with anchor-based prediction"),
                    ("wang2024contextgs", ["Anchor", "Anchor-level Context Model"], "ContextGS: anchor-level context model"),
                    ("hu2025excavating", ["Anchor", "Prediction"], "Anchor-based: sparse anchor features predict nearby attributes (title: sparse selection and structural optimization)"),
                    ("morgenstern2024compact", ["Feature Planes", "Self-organizing Gaussian Grids", "Conventional Video Codecs"], "Self-organizing Gaussian grids reorganize attributes into ordered planes that conventional video codecs can handle"),
                    ("lee2025compression", ["Feature Planes", "Conventional Video Codecs"], "Optimized feature planes handled by standard video codecs"),
                    ("zhan2025cat", ["Context-adaptive Triplane", "Channel Entropy Models", "Entropy Model"], "CAT-3DGS: context-adaptive spatial and channel entropy models"),
                    ("ren2024octree", ["Octree"], "Octrees provide spatial organization"),
                    ("xie2024mesongs", ["Octree"], "Octrees provide spatial organization (title: post-training compression via attribute transformation)"),
                    ("di2025gode", ["Level of Detail", "Progressive"], "GoDe arranges Gaussians into progressive Level-of-Detail layers"),
                    ("chen2025pcgs", ["Progressive", "Primitive Quantity and Attribute Quality"], "PCGS controls primitive quantity and attribute quality progressively"),
                    ("zoomers2025progs", ["Hierarchies"], "Cited with the hierarchy and progressive-LoD methods (title: progressive rendering of Gaussian splats)"),
                    ("chen2026fcgs", ["Feedforward Compression", "Inter- and Intra-Gaussian Context", "Multi-path Entropy Coding"], "FCGS models inter- and intra-Gaussian context with multi-path entropy coding"),
                    ("fu2026voxelgs", ["Quantized Scaffold", "Run-length Coding"], "Voxel-GS couples a quantized Scaffold-GS organization to run-length coding"),
                    ("sridhara2025region", ["Region-adaptive", "Hierarchical Encoding"], "Region-adaptive hierarchical encoding changes the partitioning of coded state"),
                ]),
                (RD, "Rate–Distortion Optimization", [
                    ("wang2024end", ["Rate–Distortion Objective", "Dynamic Pruning", "Entropy-constrained Vector Quantization"], "Dynamic pruning and entropy-constrained VQ in a differentiable D + λR objective"),
                    ("zhan2025cat", ["Rate–Distortion Objective", "Context Model"], "Anchor representation with context-adaptive entropy models under end-to-end RD objective"),
                    ("chen2025megs", ["Rendering-memory Problem", "Spherical Gaussians", "Pruning"], "MEGS²: primitive-number and SG-lobe pruning as a constrained rendering-memory problem (not coded bitrate)"),
                    ("shin2025leveraging", ["Restoration Prior", "Distortion Side"], "LIP-GS: learned image-restoration prior recovers quality degraded by Gaussian compression"),
                ]),
            ],
        },
        {
            "name": "Dynamic Scene",
            "anchor": "primitive-dynamic-scene",
            "intro": "Dynamic scenes add time-dependent geometry, appearance or motion; compression depends on which state is shared across time, which residual is transmitted and how both are reconstructed.",
            "groups": [
                (None, "Cited in the Fig. 7 caption", [
                    ("kerbl20233d", ["Reference Construction"], "Cited in the Fig. 7 caption among the representative methods and reference constructions for absolute, canonical + deformation, factorized and prediction-residual state organizations"),
                    ("wu20244d", ["Reference Construction"], "Cited in the Fig. 7 caption (see above)"),
                    ("yang2023real", ["Reference Construction"], "Cited in the Fig. 7 caption (see above)"),
                    ("lee2024fully", ["Reference Construction"], "Cited in the Fig. 7 caption (see above)"),
                    ("sun20243dgstream", ["Reference Construction"], "Cited in the Fig. 7 caption (see above)"),
                    ("girish2024queen", ["Reference Construction"], "Cited in the Fig. 7 caption (see above)"),
                    ("zhang2025d", ["Reference Construction"], "Cited in the Fig. 7 caption (see above)"),
                ]),
                (CAP, "Representation Capacity Improvement — Temporal parameterization", [
                    ("wu20244d", ["Canonical + Deformation", "HexPlane"], "Deformable 4D-GS: reuses a fitted reference set and predicts time-dependent changes"),
                    ("sun20243dgstream", ["Previous-frame Formulation", "Neural Transformation Cache"], "3DGStream transforms the preceding frame's Gaussians through a neural transformation cache and adds frame-specific primitives"),
                    ("huang2024sc", ["Sparse Control Points", "As-Rigid-As-Possible Loss"], "SC-GS: As-Rigid-As-Possible loss on sparse control points"),
                    ("wan2024superpoint", ["Superpoints", "Similar Motion Properties"], "Superpoint methods cluster Gaussians with similar motion"),
                    ("yang2023real", ["4D Primitives"], "Native 4DGS optimizes 4D primitives"),
                    ("lee2024fully", ["Samples and Interpolates", "Explicit"], "Ex4DGS samples and interpolates dynamic positions and rotations"),
                    ("oh2025hybrid", ["Mixed Allocation"], "Hybrid 3D–4DGS reserves 4D Gaussians for dynamic regions"),
                ]),
                (RATE, "Rate Optimization — Shrinking the temporal fitted state", [
                    ("gao2024hicom", ["Pruning", "Streaming"], "HiCoM removes low-opacity primitives while updating a stream"),
                    ("liu2025light4gs", ["Spatiotemporal Significance"], "Light4GS prunes deformable primitives using spatiotemporal significance"),
                    ("liu2024lgs", ["Contribution to Deformation", "Surgical Scene"], "LGS scores primitives by their contribution to deformation"),
                ]),
                (RATE, "Rate Optimization — Quantization", [
                    ("girish2024queen", ["Learned Latent Decoder", "Learned Gate", "Sparsification"], "QUEEN: learned latent decoder for attribute residuals and a learned gate to sparsify position residuals"),
                    ("chen20254dgs", ["Vector Quantization", "Codebook Context"], "4DGS-CC vector-quantizes canonical SH information and context-codes its codebook"),
                    ("hu20254dgc", ["Simulated Scalar Quantization", "Implicit Entropy Model"], "4DGC: differentiable simulated scalar quantization with an implicit entropy model"),
                    ("yin2026cagsstreaming", ["VQ-based Levels of Detail", "Tiled Gaussian Data"], "CAGS forms VQ-based LoDs and transmits tiled Gaussian data with a reference-image stream"),
                ]),
                (RATE, "Rate Optimization — Structural sharing", [
                    ("fu2025recon", ["Hierarchical Anchors", "Streaming"], "ReCon-GS: multi-level anchors for coarse-to-fine motion"),
                    ("huang2025adc", ["Hierarchical Anchors"], "ADC-GS: hierarchical anchors for coarse-to-fine motion"),
                    ("gao2024hicom", ["Coherent Motion"], "Hierarchically models coherent motion"),
                    ("chen2025motion", ["Motion-sensitive Keypoint Attributes", "Propagates Motion Locally"], "ComGS transmits sparse motion-sensitive keypoint attributes and propagates motion locally"),
                    ("tang2025compressing", ["Binary Transformation Cache"], "iFVC represents adjacent-frame changes through a binary transformation cache"),
                    ("yan2025instant", ["Anchor-driven Gaussian Motion Network", "Generalizable"], "Instant Gaussian Stream predicts inter-frame motion with an anchor-driven Gaussian motion network"),
                ]),
                (RATE, "Rate Optimization — Factorization", [
                    ("wu20244d", ["HexPlane"], "Factorizes spatiotemporal features with HexPlane"),
                    ("alruwayqi2025shade", ["Orthogonal Feature Planes", "Deformation Offset"], "SHaDe: orthogonal feature planes warped into canonical space through a deformation-offset field"),
                    ("wu2025swift4d", ["Static and Dynamic Primitives", "4D Hash"], "Swift4D separates static and dynamic primitives; compact multi-resolution 4D hash"),
                    ("zhong20254d", ["Background and Foreground", "Motion Grid"], "4D-MoDe: multi-resolution motion grid with a shared MLP"),
                    ("tang2025hgc", ["Layer-wise Compression", "SMPL-X", "Avatar"], "HGC-Avatar disentangles a structural layer from an SMPL-X motion layer; layer-wise compression"),
                    ("rai2026packuv", ["UV Atlas", "Conventional Video Codecs"], "PackUV organizes temporally coherent attributes as a progressive UV atlas for HEVC / FFV1"),
                    ("yin2025towards", ["Prior-guided", "Avatar"], "Prior-guided avatar compression exploits subject-specific structure"),
                ]),
                (RD, "Rate–Distortion Optimization — Explicit rate models", [
                    ("hu20254dgc", ["Motion Grids", "Sparsification", "Entropy Model", "Rate–Distortion Objective"], "4DGC jointly optimizes compact motion grids, sparse compensated Gaussians, simulated quantization and an implicit entropy model"),
                    ("zheng20254dgcpro", ["Layer-wise RD", "Attribute-specific Entropy"], "4DGCPro adds layer-wise RD supervision and attribute-specific entropy models"),
                    ("liu2025light4gs", ["Deep Context Model", "Pruning"], "Couples significance pruning to a deep context model"),
                    ("ho2026ted4dgs", ["Temporally Activated Deformation", "INR Hyperprior", "Channel-wise Autoregressive"], "TED-4DGS: temporally activated deformation, INR hyperprior, channel-wise autoregressive entropy models"),
                ]),
                (RD, "Rate–Distortion Optimization — Prediction-based systems", [
                    ("liu2025compgs++", ["Spatial and Temporal Neighbors", "Residual Coding"], "CompGS++ predicts primitives from spatial and temporal neighbors and codes residuals under a rate-constrained objective"),
                    ("chen20254dgs", ["Voxel Context", "Codebook Context", "Hyperprior"], "4DGS-CC codes 4D neural voxels and canonical 3DGS with spatiotemporal voxel context, codebook context and hyperpriors"),
                    ("zhang2025d", ["Group-of-Frames I–P Structure", "Motion Compensation", "Hyperprior"], "D-FCGS: Group-of-Frames I–P structure, control-point motion compensation, hyperprior + spatial–temporal priors"),
                ]),
            ],
        },
    ],
}

# ---------------------------------------------------------------------------
# Context (Sections 1, 2, 5, 6): codecs, theory, surveys, standards, hardware
# ---------------------------------------------------------------------------
CONTEXT = {
    "anchor": "background-and-context",
    "title": "Context (Secs. 1, 2, 5, 6)",
    "intro": "Works the survey cites as operational references, theory, adjacent surveys, standardization and hardware context. They are not members of the two routes.",
    "groups": [
        ("Traditional codecs (operational reference)", [
            ("wallace1991jpeg", ["Block Transform"], "Baseline JPEG uses block transform coding"),
            ("skodras2001jpeg", ["Wavelet", "Resolution-scalable Access"], "JPEG2000: wavelet coding with resolution-scalable access"),
            ("wiegand2003overview", ["Established Codecs"], "H.264/AVC: prediction, transforms, quantization and entropy coding"),
            ("sullivan2012overview", ["Established Codecs"], "HEVC"),
            ("bross2021overview", ["Established Codecs"], "VVC"),
            ("galligan2018google", ["Mesh / Point Cloud"], "Draco codes mesh or point-cloud geometry and attributes"),
        ]),
        ("Amortized learned codecs; auxiliary refinement (context)", [
            ("balle2017end", ["Autoencoder", "Amortized"], "End-to-end optimized image compression"),
            ("balle2018variational", ["Hyperprior", "Amortized"], "Variational image compression with a scale hyperprior"),
            ("minnen2018joint", ["Autoregressive and Hierarchical Priors", "Amortized"], "Joint autoregressive and hierarchical priors"),
            ("he2022elic", ["Space-channel Contextual Adaptive Coding", "Amortized"], "ELIC; used as the amortized reference path in Table 2"),
            ("li2021deepcontextual", ["Comparator"], "DCVC; comparator in the Section 5 audit, outside the two routes"),
            ("campos2019content", ["Encoder-side Latent Optimization"], "Encoder-side latent optimization can improve per-image RD over a single amortized pass (auxiliary refinement)"),
            ("yang2020improving", ["Stochastic Annealing"], "Stochastic annealing can reduce discretization-related inference gaps in the tested variational setting (auxiliary refinement)"),
        ]),
        ("Theory", [
            ("rissanen1978modeling", ["MDL"], "Two-part Minimum Description Length"),
            ("grunwald2007minimum", ["MDL"], "The MDL principle"),
            ("shannon1959coding", ["Rate–Distortion Theory"], "Coding theorems with a fidelity criterion"),
            ("rahaman2019spectral", ["Spectral Bias"], "Spectral bias of neural networks"),
        ]),
        ("Adjacent surveys", [
            ("yang2023introduction", ["Neural Compression"], "Learned / neural compression survey"),
            ("mishra2022deep", ["Learned Image / Neural Compression"], "Deep architectures for image compression"),
            ("gao2022nerf", ["NeRF"], "NeRF review"),
            ("chen2024survey3dgs", ["3DGS"], "3DGS survey"),
            ("wu2024recent3dgs", ["3DGS"], "Recent advances in 3DGS"),
            ("keunen2025survey", ["INR Video Compression"], "Survey of INRs for video compression"),
            ("bagdasarian20253dgs", ["3DGS Compression"], "3DGS.zip: 3DGS compression survey"),
            ("ali2025compression", ["3DGS Compression"], "Compression in 3DGS: methods, trends, future directions"),
            ("wu2025survey", ["3DGS Compression", "Quality Assessment"], "Compression and quality assessment for 3DGS"),
        ]),
        ("Standardization", [
            ("ascenso2023jpeg", ["JPEG AI"], "Learning-based image coding standard"),
            ("jpeg2026workplan", ["JPEG AI"], "JPEG AI workplan and specifications"),
            ("iso2024nnc", ["Neural-network Parameters"], "ISO/IEC 15938-17:2024 compression of neural networks for multimedia content description"),
            ("mpeg2026gsc", ["Gaussian Splat Coding"], "MPEG exploration of Gaussian splat coding"),
        ]),
        ("Hybrid Representations and Algorithmic Synergy; Hardware Co-Design (Sec. 6)", [
            ("mueller2022instant", ["Multi-resolution Hash Grid"], "Multi-resolution hash grid with a compact MLP"),
            ("he2023shacira", ["Quantized Latent Weights", "Entropy Regularization"], "SHACIRA compresses learned feature grids through quantized latent weights and entropy regularization"),
            ("lee2024gscore", ["Architectural Support"], "GSCore: architectural support for 3DGS rendering"),
        ]),
    ],
}

# Figure 2 milestones (in the order the caption lists them)
MILESTONES = [
    ("dupont2021coin", "Functional"), ("chen2021nerv", "Functional"), ("ladune2023cool", "Functional"), ("kwan2024nvrc", "Functional"),
    ("kerbl20233d", "Primitive"), ("zhang2024gaussianimage", "Primitive"), ("chen2024hac", "Primitive"), ("wu20244d", "Primitive"),
    ("wang2025gsvc", "Primitive"), ("hu20254dgc", "Primitive"),
]

# Table 3 (Section 5): source-verified in-taxonomy empirical anchors
ANCHORS = [
    ("Functional", "2D Image: End-to-End Optimization", "zhang2025fitted", "FNLIC", "Latent fitting; entropy coding"),
    ("Functional", "Video: Rate Reduction", "kwan2023hinerv", "HiNeRV", "Pruning; parameter quantization"),
    ("Functional", "Dynamic 4D Scenes & Volumetric Video", "fridovich2023kplanes", "K-Planes", "Plane factorization"),
    ("Functional", "Other Data Modalities: Climate and Atmospheric Data", "mostajeran2025context", "CA-INR", "Context conditioning; weight quantization"),
    ("Functional", "Other Data Modalities: Biomedical Volumetric Data", "yang2023sci", "SCI", "Block partitioning; weight serialization"),
    ("Parametric Primitive", "2D Image", "zhang2024gaussianimage", "GaussianImage", "Attribute quantization; residual VQ"),
    ("Parametric Primitive", "3D Scenes: Rate Optimization", "niedermayr2024compressed", "Compressed 3DGS", "Attribute quantization; DEFLATE"),
    ("Parametric Primitive", "3D Scenes: Rate Optimization", "girish2024eagles", "EAGLES", "Latent attributes; pruning; entropy coding"),
    ("Parametric Primitive", "Dynamic Scene: Rate–Distortion Optimization", "hu20254dgc", "4DGC", "Motion grids; sparsification; entropy modeling"),
]
