# ════════════════════════════════════════════════════════════════════
# REGISTRATION MODULE  (paste inside your app.py CSS block)
# ════════════════════════════════════════════════════════════════════

# ── STEP 1: Add this CSS inside your st.markdown("""<style>...") block ──

"""
/* ── AUTH SECTION CSS ── */
.auth-wrap {
    display: flex;
    min-height: 80vh;
    align-items: center;
    justify-content: center;
    padding: 2rem 0;
}
.auth-panel {
    width: 100%;
    max-width: 480px;
    background: rgba(4,10,18,0.85);
    border: 1px solid rgba(0,200,255,0.18);
    border-radius: 28px;
    padding: 3rem 2.8rem 2.5rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 0 80px rgba(0,100,200,0.15), inset 0 1px 0 rgba(255,255,255,0.06);
    animation: authSlideIn 0.5s cubic-bezier(0.16,1,0.3,1) both;
}
@keyframes authSlideIn {
    from { opacity: 0; transform: translateY(30px) scale(0.97); }
    to   { opacity: 1; transform: translateY(0) scale(1); }
}
.auth-panel::before {
    content: '';
    position: absolute;
    top: 0; left: 10%; right: 10%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #00C8FF, #0055CC, transparent);
    border-radius: 0 0 4px 4px;
}
.auth-panel::after {
    content: '';
    position: absolute;
    bottom: -80px; right: -80px;
    width: 200px; height: 200px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(0,200,255,0.06) 0%, transparent 70%);
    pointer-events: none;
}
.auth-brand {
    text-align: center;
    margin-bottom: 2.2rem;
}
.auth-brand-icon {
    width: 64px; height: 64px;
    background: linear-gradient(135deg, rgba(0,200,255,0.2), rgba(0,80,200,0.3));
    border: 1px solid rgba(0,200,255,0.3);
    border-radius: 20px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    margin-bottom: 1rem;
    box-shadow: 0 0 30px rgba(0,200,255,0.15);
}
.auth-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.9rem;
    font-weight: 700;
    background: linear-gradient(135deg, #FFFFFF 0%, #80E8FF 60%, #0066CC 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.3rem;
}
.auth-subtitle {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: rgba(214,232,245,0.3);
}
.auth-tabs {
    display: flex;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 4px;
    margin-bottom: 2rem;
}
.auth-tab {
    flex: 1;
    text-align: center;
    padding: 0.55rem;
    border-radius: 10px;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.82rem;
    font-weight: 600;
    cursor: pointer;
    letter-spacing: 0.04em;
    transition: all 0.2s;
}
.auth-tab.active {
    background: linear-gradient(135deg, rgba(0,200,255,0.2), rgba(0,80,200,0.25));
    color: #00C8FF;
    border: 1px solid rgba(0,200,255,0.25);
}
.auth-tab.inactive { color: rgba(214,232,245,0.35); }
.auth-field-group { margin-bottom: 1rem; }
.auth-field-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.8rem;
}
.pw-strength-bar {
    height: 3px;
    border-radius: 3px;
    margin-top: 6px;
    background: rgba(255,255,255,0.06);
    overflow: hidden;
}
.pw-strength-fill {
    height: 100%;
    border-radius: 3px;
    transition: width 0.4s ease, background 0.4s ease;
}
.auth-divider {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    margin: 1.2rem 0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    color: rgba(214,232,245,0.2);
    letter-spacing: 0.15em;
    text-transform: uppercase;
}
.auth-divider::before, .auth-divider::after {
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(255,255,255,0.06);
}
/* Style text inputs inside auth forms */
.stTextInput input {
    background: rgba(0,200,255,0.04) !important;
    border: 1px solid rgba(0,200,255,0.15) !important;
    border-radius: 12px !important;
    color: #D6E8F5 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 0.65rem 1rem !important;
}
.stTextInput input:focus {
    border-color: rgba(0,200,255,0.5) !important;
    box-shadow: 0 0 0 3px rgba(0,200,255,0.08) !important;
}
.stTextInput > label {
    color: rgba(214,232,245,0.55) !important;
    font-size: 0.82rem !important;
    font-family: 'Space Grotesk', sans-serif !important;
}

/* ── DASHBOARD CSS ── */
.dash-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1.4rem 2rem;
    background: rgba(0,200,255,0.03);
    border: 1px solid rgba(0,200,255,0.1);
    border-radius: 20px;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.dash-header::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
    background: linear-gradient(180deg, #00C8FF, #0055CC);
    border-radius: 3px 0 0 3px;
}
.dash-welcome-text {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.35rem;
    font-weight: 700;
    color: #D6E8F5;
}
.dash-welcome-text span { color: #00C8FF; }
.dash-welcome-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.14em;
    color: rgba(214,232,245,0.3);
    text-transform: uppercase;
    margin-top: 3px;
}
.dash-time-badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: #00C8FF;
    background: rgba(0,200,255,0.08);
    border: 1px solid rgba(0,200,255,0.2);
    border-radius: 10px;
    padding: 0.4rem 0.9rem;
    letter-spacing: 0.06em;
}
.dash-kpi-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin-bottom: 1.5rem;
}
.dash-kpi {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 18px;
    padding: 1.4rem 1.2rem;
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s, transform 0.2s;
}
.dash-kpi:hover { border-color: rgba(0,200,255,0.2); transform: translateY(-2px); }
.dash-kpi::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,200,255,0.3), transparent);
}
.dash-kpi-icon {
    font-size: 1.5rem;
    margin-bottom: 0.7rem;
    display: block;
}
.dash-kpi-val {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.6rem;
    font-weight: 700;
    background: linear-gradient(135deg, #80E8FF, #0099FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
}
.dash-kpi-lbl {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: rgba(214,232,245,0.3);
    margin-top: 4px;
}
.dash-kpi-trend {
    font-size: 0.7rem;
    margin-top: 0.5rem;
    font-family: 'Space Grotesk', sans-serif;
}
.dash-kpi-trend.up { color: #00DC82; }
.dash-kpi-trend.down { color: #FF6B6B; }
.dash-kpi-trend.neutral { color: rgba(214,232,245,0.4); }
.dash-section-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #00C8FF;
    margin-bottom: 0.8rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.dash-section-title::after {
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(0,200,255,0.15);
}
.res-status-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.8rem;
    margin-bottom: 1.5rem;
}
.res-status-card {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px;
    padding: 1.1rem 1rem;
    position: relative;
    overflow: hidden;
}
.res-status-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.88rem;
    font-weight: 600;
    color: #D6E8F5;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.res-status-pct {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: #00C8FF;
}
.res-bar-bg {
    background: rgba(255,255,255,0.06);
    border-radius: 6px;
    height: 6px;
    overflow: hidden;
    margin-bottom: 0.5rem;
}
.res-bar-fill {
    height: 100%;
    border-radius: 6px;
    background: linear-gradient(90deg, #0055CC, #00C8FF);
}
.res-cap-row {
    display: flex;
    justify-content: space-between;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    color: rgba(214,232,245,0.28);
}
.dash-activity-feed {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 18px;
    padding: 1.2rem;
    margin-bottom: 1.5rem;
}
.activity-item {
    display: flex;
    align-items: flex-start;
    gap: 0.8rem;
    padding: 0.65rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.04);
    font-size: 0.82rem;
}
.activity-item:last-child { border-bottom: none; }
.activity-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    margin-top: 6px;
    flex-shrink: 0;
}
.activity-text { color: rgba(214,232,245,0.6); line-height: 1.5; }
.activity-time {
    margin-left: auto;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    color: rgba(214,232,245,0.25);
    flex-shrink: 0;
}
.dash-cta {
    background: linear-gradient(135deg, rgba(0,200,255,0.08), rgba(0,80,200,0.12));
    border: 1px solid rgba(0,200,255,0.2);
    border-radius: 20px;
    padding: 1.8rem 2rem;
    text-align: center;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.dash-cta::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 120px; height: 120px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(0,200,255,0.08) 0%, transparent 70%);
}
.dash-cta-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #D6E8F5;
    margin-bottom: 0.4rem;
}
.dash-cta-sub {
    font-size: 0.8rem;
    color: rgba(214,232,245,0.4);
    margin-bottom: 1rem;
    font-family: 'Space Grotesk', sans-serif;
}
.dash-mini-chart {
    display: flex;
    align-items: flex-end;
    gap: 4px;
    height: 48px;
    margin-bottom: 0.5rem;
}
.dash-bar {
    flex: 1;
    border-radius: 4px 4px 0 0;
    background: linear-gradient(180deg, #00C8FF, #0055CC);
    opacity: 0.7;
    min-height: 4px;
    transition: opacity 0.2s;
}
.dash-bar:hover { opacity: 1; }
.dash-chart-labels {
    display: flex;
    justify-content: space-between;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.55rem;
    color: rgba(214,232,245,0.2);
    margin-top: 4px;
}
.dash-alert {
    border-radius: 12px;
    padding: 0.75rem 1rem;
    margin-bottom: 0.6rem;
    display: flex;
    align-items: center;
    gap: 0.7rem;
    font-size: 0.82rem;
    font-family: 'Space Grotesk', sans-serif;
}
.dash-alert.info {
    background: rgba(0,200,255,0.06);
    border: 1px solid rgba(0,200,255,0.18);
    color: rgba(214,232,245,0.7);
}
.dash-alert.warn {
    background: rgba(255,160,0,0.06);
    border: 1px solid rgba(255,160,0,0.2);
    color: rgba(255,180,80,0.85);
}
.dash-alert.ok {
    background: rgba(0,220,130,0.06);
    border: 1px solid rgba(0,220,130,0.2);
    color: rgba(0,220,130,0.85);
}
/* auth-container kept for back-compat */
.auth-container { max-width:480px; margin:2rem auto; }

</style>

<!-- Cursor -->
<div class="cursor-dot" id="cursorDot"></div>
<div class="cursor-ring" id="cursorRing"></div>
<script>
const dot = document.getElementById('cursorDot');
const ring = document.getElementById('cursorRing');
let mx=0, my=0, rx=0, ry=0;
document.addEventListener('mousemove', e => { mx=e.clientX; my=e.clientY; dot.style.left=mx+'px'; dot.style.top=my+'px'; });
function animate(){
    rx += (mx-rx)*0.12; ry += (my-ry)*0.12;
    ring.style.left=rx+'px'; ring.style.top=ry+'px';
    requestAnimationFrame(animate);
}
"""

# ── STEP 2: Paste this Python code after your CSS block ──

USERS_FILE = "users.csv"


def load_users() -> pd.DataFrame:
    """Load users from CSV. Creates the file with headers if it doesn't exist."""
    if not os.path.exists(USERS_FILE):
        df = pd.DataFrame(columns=["username", "password"])
        df.to_csv(USERS_FILE, index=False)
        return df
    return pd.read_csv(USERS_FILE)


def save_user(username: str, password: str, full_name: str = "", email: str = "") -> None:
    """Append a new user row to users.csv."""
    df = load_users()
    new_row = pd.DataFrame([{"username": username, "password": password,
                              "full_name": full_name, "email": email,
                              "joined": datetime.now().strftime("%Y-%m-%d")}])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(USERS_FILE, index=False)


def username_exists(username: str) -> bool:
    """Return True if the username is already registered."""
    df = load_users()
    return username.strip().lower() in df["username"].str.strip().str.lower().values


def verify_credentials(username: str, password: str) -> bool:
    """Return True if username + password pair is valid."""
    df = load_users()
    df["username"] = df["username"].str.strip().str.lower()
    df["password"] = df["password"].str.strip()
    match = df[(df["username"] == username.strip().lower()) &
               (df["password"] == password.strip())]
    return not match.empty


def init_session_state() -> None:
    """Initialise all session-state keys used by the auth system."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "auth_page" not in st.session_state:
        st.session_state.auth_page = "login"   # "login" | "signup"
    if "dashboard_page" not in st.session_state:
        st.session_state.dashboard_page = "dashboard"  # "dashboard" | "predictor"


def show_login_page() -> None:
    """Render the Login page — redesigned."""
    _, center, _ = st.columns([1, 2, 1])
    with center:
        st.markdown("""
        <div class="auth-panel">
            <div class="auth-brand">
                <div class="auth-brand-icon">🌊</div>
                <div class="auth-title">HydroSense</div>
                <div class="auth-subtitle">Chennai Reservoir Intelligence</div>
            </div>
            <div class="auth-tabs">
                <div class="auth-tab active">Sign In</div>
                <div class="auth-tab inactive" style="cursor:default;">Register</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        username = st.text_input("Username", key="login_username", placeholder="Enter your username")
        password = st.text_input("Password", key="login_password", placeholder="Enter your password", type="password")

        st.markdown("<div style='height:0.4rem'></div>", unsafe_allow_html=True)

        if st.button("🔑  Sign In", use_container_width=True, key="login_btn"):
            if not username.strip() or not password.strip():
                st.error("⚠️ Please fill in both fields.")
            elif verify_credentials(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username.strip()
                st.session_state.dashboard_page = "dashboard"
                st.rerun()
            else:
                st.error("❌ Invalid username or password.")

        st.markdown("""
        <div class="auth-divider">or</div>
        """, unsafe_allow_html=True)

        if st.button("✨  Create New Account", use_container_width=True, key="go_signup_btn"):
            st.session_state.auth_page = "signup"
            st.rerun()

        st.markdown("""
        <p style='text-align:center;font-size:0.7rem;color:rgba(214,232,245,0.2);
           font-family:JetBrains Mono,monospace;letter-spacing:0.1em;margin-top:1.5rem;'>
           SECURED · HYDROSENSE v2.0</p>
        """, unsafe_allow_html=True)


def show_signup_page() -> None:
    """Render the Signup page — unique animated registration module."""
    _, center, _ = st.columns([1, 2, 1])
    with center:
        st.markdown("""
        <div class="auth-panel">
            <div class="auth-brand">
                <div class="auth-brand-icon">🛰️</div>
                <div class="auth-title">Create Account</div>
                <div class="auth-subtitle">Join HydroSense Intelligence</div>
            </div>
            <div class="auth-tabs">
                <div class="auth-tab inactive" style="cursor:default;">Sign In</div>
                <div class="auth-tab active">Register</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Two-column name row
        c1, c2 = st.columns(2)
        with c1:
            full_name = st.text_input("Full Name", key="signup_fullname", placeholder="Your name")
        with c2:
            email = st.text_input("Email Address", key="signup_email", placeholder="you@example.com")

        new_username = st.text_input("Choose Username", key="signup_username", placeholder="min. 3 characters")

        new_password = st.text_input("Create Password", key="signup_password",
                                     placeholder="min. 4 characters", type="password")

        # Live password strength indicator
        pw = new_password or ""
        strength = 0
        if len(pw) >= 4:  strength += 1
        if len(pw) >= 8:  strength += 1
        if any(c.isdigit() for c in pw): strength += 1
        if any(not c.isalnum() for c in pw): strength += 1

        strength_colors = ["#FF3C3C", "#FF8C00", "#FFD700", "#00DC82"]
        strength_labels = ["Weak", "Fair", "Good", "Strong"]
        strength_widths = ["25%", "50%", "75%", "100%"]

        if pw:
            idx = max(0, strength - 1)
            st.markdown(f"""
            <div style="margin-top:-0.6rem;margin-bottom:0.8rem;">
                <div class="pw-strength-bar">
                    <div class="pw-strength-fill" style="width:{strength_widths[idx]};
                        background:{strength_colors[idx]};"></div>
                </div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:0.6rem;
                    color:{strength_colors[idx]};margin-top:4px;letter-spacing:0.1em;">
                    PASSWORD STRENGTH: {strength_labels[idx]}
                </div>
            </div>
            """, unsafe_allow_html=True)

        confirm_password = st.text_input("Confirm Password", key="signup_confirm",
                                          placeholder="Re-enter your password", type="password")

        # Password match hint
        if confirm_password and new_password:
            if new_password == confirm_password:
                st.markdown('<p style="font-size:0.72rem;color:#00DC82;font-family:JetBrains Mono,monospace;">✓ Passwords match</p>', unsafe_allow_html=True)
            else:
                st.markdown('<p style="font-size:0.72rem;color:#FF6B6B;font-family:JetBrains Mono,monospace;">✗ Passwords do not match</p>', unsafe_allow_html=True)

        st.markdown("<div style='height:0.3rem'></div>", unsafe_allow_html=True)

        if st.button("🚀  Create My Account", use_container_width=True, key="signup_btn"):
            if not new_username.strip() or not new_password.strip() or not confirm_password.strip():
                st.error("⚠️ Username and password fields are required.")
            elif len(new_username.strip()) < 3:
                st.error("⚠️ Username must be at least 3 characters.")
            elif len(new_password.strip()) < 4:
                st.error("⚠️ Password must be at least 4 characters.")
            elif new_password != confirm_password:
                st.error("❌ Passwords do not match.")
            elif email.strip() and "@" not in email:
                st.error("⚠️ Please enter a valid email address.")
            elif username_exists(new_username):
                st.error(f"❌ Username **{new_username}** is taken. Try another.")
            else:
                save_user(new_username.strip(), new_password.strip(),
                          full_name.strip(), email.strip())
                st.success(f"✅ Welcome aboard, **{new_username}**! Your account is ready.")
                st.session_state.auth_page = "login"
                st.rerun()

        st.markdown("""<div class="auth-divider">already registered</div>""", unsafe_allow_html=True)

        if st.button("← Back to Sign In", use_container_width=True, key="go_login_btn"):
            st.session_state.auth_page = "login"
            st.rerun()

        st.markdown("""
        <p style='text-align:center;font-size:0.65rem;color:rgba(214,232,245,0.15);
           font-family:JetBrains Mono,monospace;letter-spacing:0.1em;margin-top:1.2rem;'>
           YOUR DATA IS STORED LOCALLY · HYDROSENSE v2.0</p>
        """, unsafe_allow_html=True)


def show_logout_button() -> None:
    """Render the logout button + navigation inside the sidebar."""
    with st.sidebar:
        st.markdown(f"""
        <div style="padding:1rem 0 0.5rem;">
            <div style="font-family:'JetBrains Mono',monospace;font-size:0.6rem;
                letter-spacing:0.18em;text-transform:uppercase;
                color:rgba(214,232,245,0.35);margin-bottom:4px;">Signed in as</div>
            <div style="font-family:'Space Grotesk',sans-serif;font-size:1rem;
                font-weight:600;color:#00C8FF;">👤 {st.session_state.username}</div>
        </div>
        <hr style="border:none;border-top:1px solid rgba(0,200,255,0.12);margin:0.8rem 0;">
        <div style="font-family:'JetBrains Mono',monospace;font-size:0.6rem;
            letter-spacing:0.15em;text-transform:uppercase;
            color:rgba(214,232,245,0.25);margin-bottom:0.5rem;">Navigation</div>
        """, unsafe_allow_html=True)

        if st.button("🏠  Dashboard", use_container_width=True, key="nav_dashboard"):
            st.session_state.dashboard_page = "dashboard"
            st.rerun()
        if st.button("🌊  Water Predictor", use_container_width=True, key="nav_predictor"):
            st.session_state.dashboard_page = "predictor"
            st.rerun()

        st.markdown("<hr style='border:none;border-top:1px solid rgba(0,200,255,0.08);margin:0.8rem 0;'>", unsafe_allow_html=True)

        if st.button("🔓  Logout", use_container_width=True, key="logout_btn"):
            st.session_state.authenticated = False
            st.session_state.username = ""
            st.session_state.auth_page = "login"
            st.rerun()