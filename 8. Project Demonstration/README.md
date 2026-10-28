# Phase 8: Project Demonstration

## Live Demo

🌐 **App:** https://wanderwise-henna.vercel.app  
🔌 **API:** https://wanderwise-api.onrender.com/api/health  
📚 **API Docs:** https://wanderwise-api.onrender.com/docs

---

## Demo Script

### 1. Show the landing page
- Open https://wanderwise-henna.vercel.app
- Point out the "API connected" green dot (top right)
- Explain the hero section

### 2. Generate a demo itinerary
- Fill destination: `Ujjain, Madhya Pradesh`
- Dates: any 3-day range
- Budget: `10000 INR`
- Select interests: Culture, Spirituality, Food
- Click **Generate my itinerary**
- Show the day-by-day plan with cost estimates

### 3. Show AI mode
- Explain Groq API integration
- Show `generated_by: "ai"` vs `"fallback"` in the response

### 4. Show Supabase auth
- Click Sign in → Create account
- Generate an itinerary → Save trip
- Show "Trip saved to your Supabase account"

### 5. Show API documentation
- Open https://wanderwise-api.onrender.com/docs
- Demonstrate the interactive Swagger UI

---

## Key Features to Highlight

| Feature | Why it matters |
|---------|----------------|
| Demo mode | Works without any paid API key |
| Budget tracking | Shows remaining budget after activities |
| RLS security | Each user sees only their own trips |
| Responsive design | Works on mobile and desktop |
| Print to PDF | Offline access to your itinerary |

---

## Scalability & Future Plans

- Add Google Maps integration for route visualization
- Support more currencies and languages
- Add collaborative trip planning (multiple users)
- Add live hotel/flight price integration
- Mobile app (React Native) using the same backend API
