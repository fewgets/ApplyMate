<!-- ApplyMate · README by Usama Shahid (fewgets) -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,55:0F3D3E,100:36FFC7&height=230&section=header&text=ApplyMate&fontSize=60&fontColor=FFFFFF&fontAlignY=36&desc=AI%20job%20application%20and%20interview%20assistant&descSize=17&descAlignY=58&animation=fadeIn" width="100%" alt="ApplyMate"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=700&color=36FFC7&center=true&vCenter=true&width=720&height=60&lines=Tailored+CVs+for+Every+Job;Cover+Letters+in+Seconds;Mock+Interviews+with+AI" alt="Typing SVG"/>

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js"/>
  <img src="https://img.shields.io/badge/Tesseract%20OCR-5A5A5A?style=for-the-badge&logo=google&logoColor=white" alt="Tesseract OCR"/>
  <img src="https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase"/>
  <img src="https://img.shields.io/badge/Status-F7B500?style=for-the-badge&logo=githubactions&logoColor=black" alt="Status"/>
</p>

</div>

---
> 🚧 **Status: in active development.** The first module (job-description OCR) is in this repo; the
> rest of the pipeline below is the planned design. Follow along or reach out if you'd like to collaborate.

## 📌 Overview

Applying for jobs is repetitive: rewrite the CV, write a new cover letter, fill the same forms,
then prepare for interviews from scratch. **ApplyMate** is an AI assistant that automates this
whole journey:

1. 📄 **Understand the job:** read a job description from text, a PDF or even a **screenshot** (OCR).
2. ✍️ **Tailor your documents:** rewrite your CV and generate a matching cover letter with an LLM.
3. 📤 **Apply:** fill in and submit the application for you.
4. 🎤 **Prepare:** generate likely interview questions and practise with interactive Q&A cards.

---

## 🗺️ Development Status

| Module | Description | Status |
|---|---|:-:|
| 🖼️ **JD Extractor** | OCR that reads job descriptions from images (OpenCV + Tesseract) | ✅ Done |
| 🧾 **JD Parser** | Extract skills, requirements and keywords with NLP | 🔄 In progress |
| 📝 **Resume Tailor** | LLM rewrites the CV to match the job | 📋 Planned |
| ✉️ **Cover Letter Generator** | Personalised letter for each role | 📋 Planned |
| 📤 **Auto-Apply** | Form filling and submission | 📋 Planned |
| 🎤 **Interview Coach** | Mock questions and practice cards | 📋 Planned |
| 🌐 **Web App** | Next.js frontend with Supabase auth, on Vercel | 📋 Planned |

---

## 🏗️ Planned Architecture

```mermaid
flowchart LR
    U[👤 User<br/>profile + CV] --> FE[🌐 Next.js app]
    JD[📄 Job description<br/>text · PDF · image] --> FE
    FE --> API[⚙️ FastAPI backend]
    API --> OCR[🖼️ OCR<br/>Tesseract]
    API --> LLM[🧠 LLM<br/>tailoring + Q&A]
    API --> DB[(☁️ Supabase<br/>users · applications)]
    LLM --> OUT[📄 CV · ✉️ Cover letter · 🎤 Interview prep]
```

---

## 🚀 Try the JD Extractor

```bash
git clone https://github.com/fewgets/ApplyMate.git
cd ApplyMate/backend

pip install opencv-python pytesseract
```

1. Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract). On Windows, set its path in `jdextract.py`.
2. Set `image_path` in `jdextract.py` to a screenshot of a job post.
3. Run:

```bash
python jdextract.py
```

The extracted job-description text is printed to the terminal.

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| OCR | OpenCV, Tesseract (`pytesseract`) |
| Backend *(planned)* | Python, FastAPI |
| AI *(planned)* | LLM APIs for rewriting, generation and Q&A |
| Frontend *(planned)* | Next.js, Tailwind CSS, shadcn/ui |
| Database *(planned)* | Supabase (PostgreSQL + Auth) |
| Hosting *(planned)* | Vercel |

---

## 🤝 Let's Work Together

<div align="center">

**Have an idea, a freelance project, or want to collaborate on something in AI?**
I'm always open to collaborations, freelance work and full-time opportunities.

<a href="mailto:shaikhusama541@gmail.com?subject=Collaboration%20-%20ApplyMate">
  <img src="https://img.shields.io/badge/Email-shaikhusama541%40gmail.com-36FFC7?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0D1117" alt="Email"/>
</a>
<a href="https://www.linkedin.com/in/-usamashahid/">
  <img src="https://img.shields.io/badge/LinkedIn-Usama%20Shahid-36FFC7?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0D1117" alt="LinkedIn"/>
</a>
<a href="https://github.com/fewgets">
  <img src="https://img.shields.io/badge/GitHub-fewgets-36FFC7?style=for-the-badge&logo=github&logoColor=white&labelColor=0D1117" alt="GitHub"/>
</a>

<br/><br/>

⭐ **If you like this project, please give it a star. It really helps!** ⭐

<br/>

<h3>"Spend your time preparing, not copy-pasting applications."</h3>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:36FFC7,55:0F3D3E,100:0D1117&height=150&section=footer&animation=twinkling" width="100%" alt="footer"/>

</div>
