# Phase 6: Project Testing

## Backend Unit Tests

Run with: `pytest -v` from the `backend/` directory.

| Test | Description | Status |
|------|-------------|--------|
| `test_health` | GET /api/health returns 200 + healthy status | ✅ Pass |
| `test_root` | GET / returns 200 + status ok | ✅ Pass |
| `test_fallback_itinerary` | POST /api/itinerary returns 2-day fallback plan | ✅ Pass |
| `test_invalid_dates` | End date before start date returns 422 | ✅ Pass |
| `test_missing_destination` | Missing destination returns 422 | ✅ Pass |
| `test_single_day_trip` | Single day trip returns 1-day plan | ✅ Pass |

**Total: 6/6 passing**

## Frontend Build Test

```
vite v6.4.5 building for production...
✓ 1622 modules transformed.
dist/index.html        0.46 kB
dist/assets/*.css     12.05 kB
dist/assets/*.js     399.57 kB
✓ built in 13.82s
```

## Manual Testing Checklist

- [x] Generate itinerary in demo mode (no API key)
- [x] Generate itinerary with Groq AI key
- [x] Sign up with email/password
- [x] Sign in with email/password
- [x] Save trip to Supabase
- [x] Save trip to localStorage (guest)
- [x] View saved trips
- [x] Load saved trip into planner
- [x] Print / Save as PDF
- [x] Mobile responsive layout
- [x] API health shows "API connected"

## Performance

- AI itinerary generation: ~5–15 seconds (Groq)
- Demo fallback: < 100ms
- Frontend initial load: < 2s
- Vercel build time: ~15s
