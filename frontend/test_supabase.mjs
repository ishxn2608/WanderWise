import { createClient } from '@supabase/supabase-js'

const sb = createClient(
  'https://dykejuhawpmduhkhackd.supabase.co',
  'sb_publishable_ZJ6G7oMPXrzwBCN0Ub1iYQ_iskpH0fu'
)

// Test 1: check auth settings
const { data: settings, error: se } = await sb.auth.getSession()
console.log('Session check:', se ? 'ERROR: ' + se.message : 'OK (no active session)')

// Test 2: signup with a real-format email
const ts = Date.now()
const { data, error } = await sb.auth.signUp({
  email: `ishan.test${ts}@gmail.com`,
  password: 'WanderWise2024!'
})
if (error) {
  console.log('SIGNUP ERROR:', error.message, '| code:', error.code, '| status:', error.status)
} else {
  console.log('SIGNUP OK:', data.user?.email, '| confirmed:', data.user?.confirmed_at ?? 'needs email confirmation')
}
