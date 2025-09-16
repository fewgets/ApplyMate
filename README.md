# 🤖 ApplyMate — AI Job Application & Interview Assistant

> **ApplyMate** is an AI-powered personal job assistant that automates your entire application journey — from customizing resumes & cover letters to auto-applying for jobs and preparing you for interviews with interactive mock questions.

--- 

## 📌 Project Summary

ApplyMate streamlines the job hunting process by combining **NLP, OCR, and generative AI**.

* On **signup**, users provide personal details and upload their CV.
* When given a **job description** (text, file, or screenshot), ApplyMate parses the requirements and tailors a resume + cover letter.
* The system then **applies automatically** to the job portal on your behalf.
* Finally, ApplyMate supports you with **interview prep**, generating likely questions and simulating Q\&A sessions with interactive cards.

---

## ⚙️ Features

* 📝 **Smart Resume Customization** — Tailors CV for each job role
* 📄 **Cover Letter Generator** — Drafts professional letters aligned with JD
* 📤 **Auto Job Application** — Submits applications on your behalf
* 🖼 **Multi-Input JD Parsing** — Accepts JD as text, PDF, or image (OCR)
* 🎤 **Interactive Interview Prep** — Mock questions & practice cards
* 🧠 **AI-Powered** — Uses NLP & LLMs for semantic understanding
* 📊 **Application Tracking** — Keeps record of applied jobs
* 🌐 **Web App** — Accessible from browser, no installs needed
* ⚡ **Deployed on Vercel** for scalability and smooth user access

---

## 🧰 Tech Stack

| Component         | Tool / Service                  |
| ----------------- | ------------------------------- |
| Language          | Python 3.x / JavaScript         |
| Backend Framework | FastAPI / Flask / Node.js       |
| Frontend          | React / Next.js                 |
| Deployment        | Vercel (Web App Hosting)        |
| AI / NLP          | OpenAI API / HuggingFace        |
| OCR               | Tesseract / EasyOCR             |
| DB & Auth         | Supabase (PostgreSQL)           |
| File Storage      | Supabase Buckets / Google Drive |
| Styling / UI      | TailwindCSS / Shadcn UI         |
| State Mgmt        | Redux / Context API             |
| Notifications     | Email / Discord / WhatsApp API  |

---

## 🗂 Folder Structure

```bash
ApplyMate/
├── backend/                 # API logic (resume, JD parsing, auto apply)
│   ├── main.py              # FastAPI entry point
│   ├── resume_builder.py    # Resume customization logic
│   ├── cover_letter.py      # Cover letter generator
│   ├── jd_parser.py         # Job description parsing (OCR + NLP)
│   ├── auto_apply.py        # Job application automation
│   ├── interview_prep.py    # Mock interview module
│   ├── database.py          # Supabase/Postgres integration
│   └── requirements.txt     # Python dependencies
│
├── frontend/                # Next.js + React web app
│   ├── pages/               # Routes
│   ├── components/          # Reusable UI components
│   ├── styles/              # TailwindCSS + Shadcn UI styling
│   └── package.json         # Node dependencies
│
├── .env.example             # Environment variable template
├── README.md                # Documentation
└── vercel.json              # Vercel deployment config
```

---

## 📝 Setup Instructions

### 1) Clone the Repository

```bash
git clone https://github.com/your-username/ApplyMate.git
cd ApplyMate
```

### 2) Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

Configure `.env`:

```env
OPENAI_API_KEY=your_openai_key  
SUPABASE_URL=your_supabase_url  
SUPABASE_KEY=your_supabase_key  
GOOGLE_CREDENTIALS=path_to_google.json  
```

Run backend:

```bash
uvicorn main:app --reload
```

---

### 3) Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

### 4) Deploy on Vercel

1. Push repo to GitHub.
2. Go to [Vercel](https://vercel.com).
3. Import repo → Select `frontend` as root → Add env vars.
4. Deploy 🎉

---

## 🚀 How It Works

1. **Signup** → Provide details + upload CV
2. **Input JD** → Upload as text, file, or screenshot
3. **Customization** → AI rewrites CV & cover letter
4. **Auto-Apply** → Fills forms & submits application
5. **Interview Prep** → Interactive Q\&A session with mock questions

---

## 📩 Contact

👤 **Usama Shahid**

📧 [dev.usamashahid@gmail.com](mailto:dev.usamashahid@gmail.com)


🔗 [LinkedIn](https://linkedin.com/in/-usamashahid)

🐙 [GitHub](https://github.com/fewgets)

---

## 📜 License

This project is for **academic and career-assistance purposes**. Feel free to fork & improve, but credit is appreciated 🙏
