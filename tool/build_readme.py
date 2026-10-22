# -*- coding: utf-8 -*-
"""Generate README.md (overview page) plus functional.md / parametric.md / context.md (full lists organized exactly like the survey's sections).

Usage (from the repository root):  python3 tools/build_readme.py
Inputs (same directory as this script): survey_spec.py (placement + tags + notes), cited_bib.json (parsed bibliography),
arxiv_matches.json / crossref_matches.json (looked-up identifiers), link_overrides.json (manual fixes),
code_links_verified.txt (key -> GitHub URL). Outputs are written to the repository root.
"""
import json, re, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import survey_spec as S

SCR = os.path.dirname(os.path.abspath(__file__))
bib = json.load(open(os.path.join(SCR, 'cited_bib.json'), encoding='utf-8'))
arx = json.load(open(os.path.join(SCR, 'arxiv_matches.json'), encoding='utf-8'))
code = {}
for line in open(os.path.join(SCR, 'code_links_verified.txt'), encoding='utf-8'):
    p = line.split()
    if len(p) == 2:
        code[p[0]] = p[1]
cr_path = os.path.join(SCR, 'crossref_matches.json')
crossref = json.load(open(cr_path, encoding='utf-8')) if os.path.exists(cr_path) else {}
overrides_path = os.path.join(SCR, 'link_overrides.json')
overrides = json.load(open(overrides_path, encoding='utf-8')) if os.path.exists(overrides_path) else {}

REPO = "https://github.com/smileto1/A-Survey-of-Representation-as-Compression"

# ----------------------------------------------------------------------------- text helpers
ACCENTS = {
    r"\'e": "é", r"\'a": "á", r"\'i": "í", r"\'o": "ó", r"\'u": "ú", r"\'c": "ć", r"\'n": "ń", r"\'y": "ý",
    r'\"u': "ü", r'\"o': "ö", r'\"a': "ä", r'\"e': "ë", r'\"i': "ï",
    r"\`e": "è", r"\`a": "à", r"\^e": "ê", r"\^o": "ô", r"\~n": "ñ", r"\~a": "ã", r"\~o": "õ",
    r"\c{c}": "ç", r"\v{c}": "č", r"\v{s}": "š", r"\v{z}": "ž", r"\.z": "ż", r"\l": "ł", r"\o": "ø", r"\ss": "ß",
    r"\textregistered": "®", r"\&": "&", r"\_": "_", r"\%": "%", r"\#": "#", r"\$": "$",
}

def detex(s):
    if not s:
        return ""
    s = s.replace("\\textsuperscript{2}", "²").replace("$^2$", "²")
    for k, v in ACCENTS.items():
        s = s.replace(k, v)
    s = re.sub(r"\\[a-zA-Z]+\s*", "", s)
    s = s.replace("{", "").replace("}", "")
    s = s.replace("---", "—").replace("--", "–")
    s = re.sub(r"\s+", " ", s).strip()
    return s

def authors(e, maxn=8):
    raw = detex(e.get("author", ""))
    parts = [a.strip() for a in raw.split(" and ") if a.strip()]
    names = []
    for a in parts:
        if a.lower() == "others":
            names.append("et al.")
            continue
        if "," in a:
            last, first = [x.strip() for x in a.split(",", 1)]
            names.append(f"{first} {last}".strip())
        else:
            names.append(a)
    if len(names) > maxn:
        names = names[:maxn] + ["et al."]
    return ", ".join(names)

VENUE_MAP = [
    (r"Pattern Analysis and Machine Intelligence", "TPAMI"),
    (r"Circuits and Systems for Video Technology", "TCSVT"),
    (r"Transactions on Image Processing", "TIP"),
    (r"Transactions on Graphics", "TOG"),
    (r"Visualization and Computer Graphics", "TVCG"),
    (r"Computer Vision and Pattern Recognition Workshops", "CVPRW"),
    (r"Computer Vision and Pattern Recognition", "CVPR"),
    (r"International Conference on Computer Vision", "ICCV"),
    (r"European Conference on Computer Vision", "ECCV"),
    (r"Neural Information Processing Systems", "NeurIPS"),
    (r"International Conference on Learning Representations", "ICLR"),
    (r"International Conference on Machine Learning", "ICML"),
    (r"Transactions on Machine Learning Research", "TMLR"),
    (r"AAAI", "AAAI"),
    (r"Winter Conference on Applications of Computer Vision", "WACV"),
    (r"Asian Conference on Computer Vision", "ACCV"),
    (r"International Joint Conference on Artificial Intelligence", "IJCAI"),
    (r"ACM International Conference on Multimedia|ACM Multimedia", "ACM MM"),
    (r"SIGGRAPH", "SIGGRAPH"),
    (r"Data Compression Conference", "DCC"),
    (r"Picture Coding Symposium", "PCS"),
    (r"Acoustics, Speech", "ICASSP"),
    (r"International Conference on Image Processing", "ICIP"),
    (r"Visual Communications and Image Processing", "VCIP"),
    (r"Multimedia and Expo", "ICME"),
    (r"Multimedia Signal Processing", "MMSP"),
    (r"Circuits and Systems \(ISCAS\)|International Symposium on Circuits and Systems", "ISCAS"),
    (r"Signal Processing Letters", "SPL"),
    (r"Signal Processing Magazine", "SPM"),
    (r"Computer Graphics Forum", "CGF"),
    (r"Computers & Graphics|Computers \& Graphics", "C&G"),
    (r"Computers & Geosciences|Computers \& Geosciences", "Computers & Geosciences"),
    (r"Communications of the ACM", "CACM"),
    (r"Nature Computational Science", "Nat. Comput. Sci."),
    (r"Scientific Reports", "Sci. Rep."),
    (r"Information Sciences", "Inf. Sci."),
    (r"Signal Processing$", "Signal Processing"),
    (r"Displays", "Displays"),
    (r"Automatica", "Automatica"),
    (r"IEEE MultiMedia", "IEEE MultiMedia"),
    (r"Medical Image Computing", "MICCAI"),
    (r"3D Vision", "3DV"),
    (r"Network and Operating System Support", "NOSSDAV"),
    (r"Annual International Conference on Mobile Computing|MobiCom", "MobiCom"),
    (r"Architectural Support for Programming Languages|ASPLOS", "ASPLOS"),
    (r"International Symposium on Computer Architecture|ISCA", "ISCA"),
    (r"Frontiers in Signal Processing", "Front. Signal Process."),
    (r"Computational Visual Media", "CVM"),
    (r"Foundations and Trends", "FnT CGV"),
    (r"APSIPA", "APSIPA TSIP"),
    (r"Sensing and Imaging", "Sens. Imaging"),
    (r"Image and Graphics Technologies", "IGTA"),
    (r"Chinese Conference on Pattern Recognition", "PRCV"),
    (r"International Symposium on Machine Learning", "ISMLA"),
    (r"Proceedings of the ACM on Computer Graphics and Interactive Techniques", "PACMCGIT"),
    (r"TechRxiv", "TechRxiv"),
    (r"Mobile Systems", "MobiSys"),
    (r"^Version .*Google$", "Google"),
    (r"^ISO$", "ISO/IEC"),
    (r"^JPEG$", "JPEG"),
    (r"^MPEG", "MPEG"),
    (r"ICML 2023 Workshop", "ICML-W"),
    (r"IRE National Convention", "IRE Conv. Rec."),
    (r"MIT Press", "MIT Press"),
]

def venue_of(e):
    v = detex(e.get("journal") or e.get("booktitle") or e.get("publisher") or e.get("howpublished") or "")
    if re.match(r"arXiv", v, re.I):
        return ("arXiv", True)
    for pat, ab in VENUE_MAP:
        if re.search(pat, v, re.I):
            return (ab, False)
    if not v:
        return ("", False)
    return (v[:28], False)

def badge_txt(s):
    s = s.replace("-", "--").replace("_", "__").replace(" ", "_")
    s = s.replace("+", "%2B").replace("&", "%26").replace("#", "%23").replace("/", "%2F")
    return s

def badge(label, color, msg=None):
    if msg is None:
        return f"[![{label}](https://img.shields.io/badge/{badge_txt(label)}-{color})]()"
    return f"[![{label}](https://img.shields.io/badge/{badge_txt(label)}-{badge_txt(msg)}-{color})]()"

def arxiv_of(key, e):
    if key in overrides and "arxiv" in overrides[key]:
        return overrides[key]["arxiv"]
    v = detex(e.get("journal") or "")
    m = re.search(r"arXiv:\s*(\d{4}\.\d{4,5})", v)
    if m:
        return m.group(1)
    m = arx.get(key, {}).get("match")
    if m and m.get("score", 0) >= 0.9:
        return m["id"]
    return None

def arxiv_yymm(aid):
    m = re.match(r"(\d{2})(\d{2})\.", aid)
    return f"20{m.group(1)}.{m.group(2)}" if m else ""

def paper_link(key, e):
    if key in overrides and "paper" in overrides[key]:
        return overrides[key]["paper"]
    aid = arxiv_of(key, e)
    if aid:
        return f"https://arxiv.org/abs/{aid}"
    if e.get("doi"):
        return "https://doi.org/" + e["doi"].strip()
    cm = crossref.get(key, {}).get("match")
    if cm and cm.get("score", 0) >= 0.97 and cm.get("doi"):
        return "https://doi.org/" + cm["doi"]
    q = detex(e.get("title", ""))
    return "https://scholar.google.com/scholar?q=" + re.sub(r"\s+", "+", q)

STAGE_COLOR = {S.CAP: "yellow", S.RATE: "yellow", S.RD: "yellow", S.EXT: "yellow", S.CTX: "lightgrey"}
STAGE_LABEL = {S.CAP: "Representation Capacity Improvement", S.RATE: "Rate Optimization", S.RD: "Rate–Distortion Optimization", S.EXT: "Other Specialized Extensions"}

def row(key, tags, note, route=None, modality=None, stage=None):
    e = bib[key]
    title = detex(e.get("title", ""))
    year = e.get("year", "")
    ven, is_arxiv = venue_of(e)
    aid = arxiv_of(key, e)
    if is_arxiv or not ven:
        vb = badge("arXiv", "red", arxiv_yymm(aid) if aid else year)
    else:
        vb = badge(ven, "blue", year)
    link = paper_link(key, e)
    cell1 = f"{vb} <br>[{title}]({link})<br>{authors(e)}"
    if note:
        cell1 += f"<br><sub>{note}</sub>"
    if route and modality:
        area = badge(route, "purple", modality)
    elif route:
        area = badge(route, "purple")
    else:
        area = badge("Context", "lightgrey")
    tg = " ".join(badge(t, "green") for t in tags)
    if stage:
        tg += "<br>" + badge(STAGE_LABEL.get(stage, stage), STAGE_COLOR.get(stage, "yellow"))
    links = f"[Paper]({link})"
    cl = overrides.get(key, {}).get("code") or code.get(key)
    if cl:
        links += f"<br>[Code]({cl})"
    return f"| {cell1} | {area} | {tg} | {links} |"

HEADER = "| **Title & Authors** | **Route · Modality** | **Mechanism · Paper heading** | **Links** |\n| --- | :---: | --- | :---: |"

def slug(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    return s




# ----------------------------------------------------------------------------- build
FILES = {"README.md": [], "functional.md": [], "parametric.md": [], "context.md": []}
def W(fname):
    return FILES[fname].append

def gh_slug(s):
    """GitHub heading anchor (emoji stripped, leading space kept as '-')."""
    s = s.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return s.rstrip().replace(" ", "-")

def group_parts(gname):
    """'Subsubsection — paragraph' -> (subsubsection, paragraph); otherwise (gname, None)."""
    if " — " in gname:
        a, b = gname.split(" — ", 1)
        return a, b
    return gname, None

BACK = "[← Back to main page](README.md)\n"
LEGEND = [
 "## 🏷️ Badge Legend\n",
 "- ![arXiv](https://img.shields.io/badge/arXiv-2024.03-red) `red` — arXiv preprint (year.month of the arXiv version)",
 "- ![Venue](https://img.shields.io/badge/CVPR-2024-blue) `blue` — conference / journal venue and year",
 "- ![Route](https://img.shields.io/badge/Functional-2D_Image-purple) `purple` — taxonomy route and modality bucket (Functional / Primitive)",
 "- ![Mechanism](https://img.shields.io/badge/Quantization-green) `green` — mechanism tags as discussed in the survey text",
 "- ![Heading](https://img.shields.io/badge/Rate_Optimization-yellow) `yellow` — the paper subsection heading under which the work is discussed: Representation Capacity Improvement / Rate Optimization / Rate–Distortion Optimization / Other Specialized Extensions",
 "- ![Context](https://img.shields.io/badge/Context-lightgrey) `grey` — background work cited for context (not a member of the two routes)\n",
 "Mechanism tags and one-line notes use the wording of the sentence in which the survey cites each work. Where the survey names a method without describing its mechanism, the tag is taken from the work's own title. Groups headed *Cited in …* collect works cited in a subsection introduction or a figure caption rather than under a mechanism heading; they carry no heading badge.\n",
]

# =============================================================== README.md
A = W("README.md")
A("<div align=center>\n")
A("# Instance-Fitted Representations for Data Compression: A Survey\n")
A("### *Representation as Compression* — a curated list of instance-fitted (neural-overfitting / primitive-fitting) data compression methods\n")
A("</div>\n")
A("> **Instance-Fitted Representations for Data Compression: A Survey**  ")
A("> [Youneng Bao](https://github.com/baoyu2020)<sup>1</sup>, [Yulong Cheng](https://github.com/smileto1/)<sup>2</sup>, [Yiping Liu](https://nouise.github.io/DD-RUO/)<sup>2</sup>, [Jiacong Chen](https://github.com/ChenJiaCong-1005)<sup>3</sup>, Yongsheng Liang<sup>3</sup>  ")
A(">  ")
A("> <sup>1</sup>City University of Hong Kong (CityUHK), <sup>2</sup>Harbin Institute of Technology, Shenzhen (HITSZ), <sup>3</sup>Shenzhen University (SZU)\n")
A("---\n")
A("> [!IMPORTANT]")
A("> We welcome your help in improving the repository and paper. Please feel free to submit a [pull request](" + REPO + "/pulls), open an [issue](" + REPO + "/issues) or [contact us](#-contact) to:")
A(">")
A("> - Add a relevant paper not yet included.")
A("> - Suggest a more suitable category or mechanism tag.")
A("> - Update links, venues or code repositories.")
A("> - Ask for clarification about any content.\n")
A("---\n")

A("## 📚 Contents\n")
A("- [Scope and Taxonomy](#-scope-and-taxonomy)")
A("- [Badge Legend](#-badge-legend)")
A("- [Representative Milestones (Fig. 2)](#-representative-milestones-fig-2)")
A("- [Recent Papers (2026)](#-recent-papers-2026)")
A("- **[Functional Representations (Sec. 3)](functional.md)**")
for m in S.FUNCTIONAL["modalities"]:
    A(f"    - [{m['name']}](functional.md#{gh_slug('Functional: ' + m['name'])})")
A("- **[Parametric Primitive Representations (Sec. 4)](parametric.md)**")
for m in S.PRIMITIVE["modalities"]:
    A(f"    - [{m['name']}](parametric.md#{gh_slug('Primitive: ' + m['name'])})")
A("- **[Context (Secs. 1, 2, 5, 6)](context.md)**")
for g, _ in S.CONTEXT["groups"]:
    A(f"    - [{g}](context.md#{gh_slug(g)})")
A("- [Bibliography](survey_refs.bib) · [Citation](#-citation) · [Contact](#-contact)\n")
A("**Every work cited in the survey is listed on the route pages above, organized exactly like the paper's sections. "
  "On this main page, only the representative milestones and the papers published in 2026 are shown.**\n")

A("## 🧭 Scope and Taxonomy\n")
A("**Instance-Fitted Representation Compression**: an encoding process belongs to this paradigm when fitting a representation state "
  "to the target instance *constitutes* the encoding process and reconstruction instantiates or evaluates that fitted state. "
  "A fitted state serves as a coded description only when its stored parameters and all decoder-required side information are specified "
  "and rate-accounted; representation precursors without a decodable payload remain in scope as substrates. Latent or coding-decision refinement inside an "
  "otherwise intact amortized or conventional codec is treated only as context. The reviewed literature covers 2D images, video, "
  "static and dynamic 3D scenes, and scientific or biomedical volumes; audio and text are outside the present scope.\n")
A("The survey organizes the literature through a **two-route taxonomy** determined by the terminal reconstruction substrate and operator:\n")
A("| Route | Fitted state | Terminal operator | Representative works |")
A("| --- | --- | --- | --- |")
A("| **Functional Representations** ([list](functional.md)) | neural weights, modulations, latents, grids, tensors, hash features | query evaluation, interpolation, integration | SIREN, NeRF, COIN, NeRV, COOL-CHIC, NVRC |")
A("| **Parametric Primitive Representations** ([list](parametric.md)) | a finite set of spatially addressable local elements (e.g. Gaussians) | projection, aggregation, splatting, rasterization | 3DGS, GaussianImage, HAC, 4D-GS, GSVC, 4DGC |\n")
A("Hybrid designs stay inside the route of their terminal operator and only receive a secondary *Functional-hybrid* / *Primitive-hybrid* tag; "
  "*Cross-route hybrid* is reserved for systems with two genuine terminal operators. Within each modality subsection the paper separates "
  "capacity allocation, payload reduction, and coded-rate optimization, and the route pages keep the paper's own headings:\n")
A("- **Representation Capacity Improvement** — inductive biases that primarily shape distortion and computation.")
A("- **Rate Optimization** — compaction that reshapes candidate carriers: pruning, factorization, quantization, dictionaries, structure or context modeling, bitstream formation.")
A("- **Rate–Distortion Optimization** — end-to-end methods that expose a differentiable rate term during fitting.\n")
A("```")
A("Instance-Fitted Representation Compression")
A("├── Functional Representations (Sec. 3)            → functional.md")
for i, m in enumerate(S.FUNCTIONAL["modalities"]):
    A(f"│   {'└──' if i == len(S.FUNCTIONAL['modalities'])-1 else '├──'} {m['name']}")
A("├── Parametric Primitive Representations (Sec. 4)  → parametric.md")
for i, m in enumerate(S.PRIMITIVE["modalities"]):
    A(f"│   {'└──' if i == len(S.PRIMITIVE['modalities'])-1 else '├──'} {m['name']}")
A("└── Context (Secs. 1, 2, 5, 6)                     → context.md")
A("    traditional codecs · amortized learned codecs · theory · adjacent surveys · standards · hardware")
A("```\n")
A("> **Evidence boundary used throughout the survey.** Parameter count, primitive count, memory, checkpoint size, estimated entropy and serialized bits are *distinct* measures. "
  "A fitted representation becomes a coded payload only when its stored state and every decoder-required side information are specified and rate-accounted. "
  "Tags in this repository describe the *mechanism* each paper contributes as discussed in the survey; they do not rank methods.\n")
A("Literature coverage was closed in **August 2026**. A paper appears under every heading in which the survey discusses it, so some works are listed more than once with different mechanism tags.\n")
for l in LEGEND: A(l)

# ---- milestones (Fig. 2)
A("## ⭐ Representative Milestones (Fig. 2)\n")
A("The milestones mapped on the survey's evolution figure. Dashed entries in the figure denote representation precursors; the selection implies neither lineage nor ranking.\n")
A(HEADER)
MS_NOTE = {
    "dupont2021coin": "Weight-coded INR image codec: quantized network weights are the payload",
    "chen2021nerv": "Frame-index neural video representation; model parameters as payload",
    "ladune2023cool": "Instance state in multi-resolution latent grids with a lightweight decoder",
    "kwan2024nvrc": "Joint hierarchical coding of representation, quantizer and entropy-model parameters",
    "kerbl20233d": "Point-based Gaussians with tile-based differentiable rasterization (representation precursor)",
    "zhang2024gaussianimage": "2D Gaussian image representation with quantization and residual VQ",
    "chen2024hac": "Hash-grid assisted context for anchor-based 3DGS compression",
    "wu20244d": "Canonical-deformation formulation; spatiotemporal features factorized with HexPlane (representation precursor)",
    "wang2025gsvc": "I-frame / P-frame 2D Gaussian video coding with bitrate control",
    "hu20254dgc": "Rate-aware 4D Gaussian compression with motion grids and entropy modeling",
}
MS_MOD = {
    "dupont2021coin": "2D Image", "chen2021nerv": "Video", "ladune2023cool": "2D Image", "kwan2024nvrc": "Video",
    "kerbl20233d": "3D Scenes", "zhang2024gaussianimage": "2D Image", "chen2024hac": "3D Scenes", "wu20244d": "Dynamic Scene",
    "wang2025gsvc": "Video", "hu20254dgc": "Dynamic Scene",
}
MS_TAGS = {
    "dupont2021coin": ["Weight Payload", "Quantization"], "chen2021nerv": ["Frame-index INR", "Pruning", "Quantization"],
    "ladune2023cool": ["Latent Grid", "Autoregressive Model"], "kwan2024nvrc": ["Hierarchical Coding", "Entropy Model"],
    "kerbl20233d": ["Rasterization", "Density Control"], "zhang2024gaussianimage": ["Quantization", "Residual VQ"],
    "chen2024hac": ["Anchor", "Context Model", "Entropy Coding"], "wu20244d": ["Canonical + Deformation", "HexPlane"],
    "wang2025gsvc": ["I/P Frames", "Prediction"], "hu20254dgc": ["Motion Grids", "Entropy Model", "RD Objective"],
}
for k, r in S.MILESTONES:
    A(row(k, MS_TAGS[k], MS_NOTE[k], route=r, modality=MS_MOD[k]))
A("")

# ---- recent papers (2026): first placement of each 2026 paper in the route pages
def is_recent(key):
    e = bib[key]
    aid = arxiv_of(key, e)
    if aid and aid[:2] == "26":
        return True
    return e.get("year", "") == "2026"

first_place = collections.OrderedDict()
for R in (S.FUNCTIONAL, S.PRIMITIVE):
    for m in R["modalities"]:
        for stage, gname, items in m["groups"]:
            for k, tags, note in items:
                if k not in first_place:
                    first_place[k] = (R["route"], m["name"], stage, tags, note)
recent = [k for k in first_place if is_recent(k)]
A("## 🆕 Recent Papers (2026)\n")
A("Papers from the two routes dated 2026 (by arXiv version or venue year). Each is listed with the first heading under which the survey discusses it; see the route pages for all placements.\n")
A(HEADER)
for k in recent:
    r, mod, st, tags, note = first_place[k]
    A(row(k, tags, note, route=r, modality=mod, stage=st))
A("")

A("## 📝 Citation\n")
A("If you find this survey or repository useful, please consider citing:\n")
A("```bibtex")
A("@article{bao2026instancefitted,")
A("  title   = {Instance-Fitted Representations for Data Compression: A Survey},")
A("  author  = {Bao, Youneng and Cheng, Yulong and Liu, Yiping and Chen, Jiacong and Liang, Yongsheng},")
A("  year    = {2026},")
A("  note    = {Manuscript. Repository: " + REPO + "}")
A("}")
A("```\n")
A("The BibTeX entries of all works listed here are collected in [`survey_refs.bib`](survey_refs.bib).\n")
A("## ✉️ Contact\n")
A("Questions, corrections and new entries are welcome through [GitHub issues](" + REPO + "/issues) or pull requests. "
  "Maintainers: [Youneng Bao](https://github.com/baoyu2020), [Yulong Cheng](https://github.com/smileto1/), [Jiacong Chen](https://github.com/ChenJiaCong-1005).\n")
A("## License\n")
A("This repository is released under the [MIT License](LICENSE).\n")

# =============================================================== route pages (heading tree = paper's section tree)
def emit_route(fname, R, emoji):
    A = W(fname)
    A(BACK)
    A(f"# {emoji} {R['title']}\n")
    A(R["intro"] + "\n")
    A("**Contents**\n")
    for m in R["modalities"]:
        A(f"- [{m['name']}](#{gh_slug(R['route'] + ': ' + m['name'])})")
        seen = []
        for st, g, items in m["groups"]:
            ss, para = group_parts(g)
            if ss not in seen and ss != m["name"]:
                seen.append(ss)
        if seen:
            A("    - " + " · ".join(seen))
    A("")
    for l in LEGEND: A(l)
    for m in R["modalities"]:
        A(f"## {R['route']}: {m['name']}\n")
        A(m["intro"] + "\n")
        current_ss = None
        for stage, gname, items in m["groups"]:
            ss, para = group_parts(gname)
            if ss != current_ss and ss != m["name"]:
                A(f"### {ss}\n")
            current_ss = ss
            if para:
                A("<details open>")
                A(f"<summary><strong>{para}</strong></summary>\n")
            A(HEADER)
            for k, tags, note in items:
                A(row(k, tags, note, route=R["route"], modality=m["name"], stage=stage))
            if para:
                A("</details>")
            A("")
    A(BACK)

emit_route("functional.md", S.FUNCTIONAL, "🔵")
emit_route("parametric.md", S.PRIMITIVE, "🟠")

# =============================================================== context page
A = W("context.md")
A(BACK)
A(f"# 📖 {S.CONTEXT['title']}\n")
A(S.CONTEXT["intro"] + "\n")
A("**Contents**\n")
for gname, items in S.CONTEXT["groups"]:
    A(f"- [{gname}](#{gh_slug(gname)})")
A("")
for gname, items in S.CONTEXT["groups"]:
    A(f"## {gname}\n")
    A(HEADER)
    for k, tags, note in items:
        A(row(k, tags, note, route=None, modality=None, stage=None))
    A("")
A(BACK)

OUT = os.path.dirname(SCR) if os.path.basename(SCR) == "tools" else os.path.join(SCR, "repo_out")
os.makedirs(OUT, exist_ok=True)
for fname, lines in FILES.items():
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write("\n".join(lines))

# ----------------------------------------------------------------------------- stats
alltext = "\n".join("\n".join(v) for v in FILES.values())
keys_in = set()
for R in (S.FUNCTIONAL, S.PRIMITIVE):
    for m in R["modalities"]:
        for st, g, items in m["groups"]:
            for k, t, n in items:
                keys_in.add(k)
for g, items in S.CONTEXT["groups"]:
    for k, t, n in items:
        keys_in.add(k)
print("files:", {f: f"{len(chr(10).join(v).encode())//1024} KB" for f, v in FILES.items()})
print("rows total:", alltext.count("\n| [!["), "; recent (2026):", len(recent), "; unique works:", len(keys_in | {k for k, _ in S.MILESTONES}), "/", len(bib))
nolink = [k for k in bib if paper_link(k, bib[k]).startswith("https://scholar")]
print("entries falling back to Scholar search:", len(nolink), nolink)
print("entries with code:", len([k for k in bib if (overrides.get(k, {}).get('code') or code.get(k))]))
