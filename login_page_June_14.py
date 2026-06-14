# AUTHENTICATION SECTION START
# ════════════════════════════════════════════════════════════════════════════

USERS_FILE = "users.csv"


def load_users() -> pd.DataFrame:
    """Load users from CSV. Creates the file with headers if it doesn't exist."""
    if not os.path.exists(USERS_FILE):
        df = pd.DataFrame(columns=["username", "password"])
        df.to_csv(USERS_FILE, index=False)
        return df
    return pd.read_csv(USERS_FILE)


def save_user(username: str, password: str) -> None:
    """Append a new user row to users.csv."""
    df = load_users()
    new_row = pd.DataFrame([{"username": username, "password": password}])
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


def show_login_page() -> None:
    """Render the Login page."""
    st.markdown("""
    <div class="auth-container">
        <div class="auth-logo">🌊</div>
        <div class="auth-title">HydroSense</div>
        <div class="auth-subtitle">Sign in to continue</div>
    </div>
    """, unsafe_allow_html=True)

    _, center, _ = st.columns([1, 2, 1])
    with center:
        username = st.text_input("Username", key="login_username", placeholder="Enter your username")
        password = st.text_input("Password", key="login_password", placeholder="Enter your password", type="password")

        if st.button("🔑 Login", use_container_width=True, key="login_btn"):
            if not username.strip() or not password.strip():
                st.error("⚠️ Please fill in both username and password.")
            elif verify_credentials(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username.strip()
                st.rerun()
            else:
                st.error("❌ Invalid username or password. Please try again.")

        st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align:center;font-size:0.82rem;"
            "color:rgba(214,232,245,0.4);font-family:Space Grotesk,sans-serif;'>"
            "Don't have an account?</p>",
            unsafe_allow_html=True
        )

        if st.button("✨ Create Account", use_container_width=True, key="go_signup_btn"):
            st.session_state.auth_page = "signup"
            st.rerun()


def show_signup_page() -> None:
    """Render the Signup page."""
    st.markdown("""
    <div class="auth-container">
        <div class="auth-logo">🌊</div>
        <div class="auth-title">Create Account</div>
        <div class="auth-subtitle">Join HydroSense</div>
    </div>
    """, unsafe_allow_html=True)

    _, center, _ = st.columns([1, 2, 1])
    with center:
        new_username = st.text_input("Choose Username", key="signup_username", placeholder="Pick a unique username")
        new_password = st.text_input("Create Password", key="signup_password", placeholder="Create a strong password", type="password")
        confirm_password = st.text_input("Confirm Password", key="signup_confirm", placeholder="Re-enter your password", type="password")

        if st.button("🚀 Sign Up", use_container_width=True, key="signup_btn"):
            if not new_username.strip() or not new_password.strip() or not confirm_password.strip():
                st.error("⚠️ All fields are required.")
            elif len(new_username.strip()) < 3:
                st.error("⚠️ Username must be at least 3 characters long.")
            elif len(new_password.strip()) < 4:
                st.error("⚠️ Password must be at least 4 characters long.")
            elif new_password != confirm_password:
                st.error("❌ Passwords do not match. Please try again.")
            elif username_exists(new_username):
                st.error(f"❌ Username **{new_username}** is already taken. Please choose another.")
            else:
                save_user(new_username.strip(), new_password.strip())
                st.success(f"✅ Account created for **{new_username}**! You can now log in.")
                st.session_state.auth_page = "login"
                st.rerun()

        st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)

        st.markdown(
            "<p style='text-align:center;font-size:0.82rem;"
            "color:rgba(214,232,245,0.4);font-family:Space Grotesk,sans-serif;'>"
            "Already have an account?</p>",
            unsafe_allow_html=True
        )

        if st.button("← Back to Login", use_container_width=True, key="go_login_btn"):
            st.session_state.auth_page = "login"
            st.rerun()


def show_logout_button() -> None:
    """Render the logout button + welcome message inside the sidebar."""
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
        """, unsafe_allow_html=True)

        if st.button("🔓 Logout", use_container_width=True, key="logout_btn"):
            st.session_state.authenticated = False
            st.session_state.username = ""
            st.session_state.auth_page = "login"
            st.rerun()


# ── Auth Gate ────────────────────────────────────────────────────────────────
init_session_state()

if not st.session_state.authenticated:
    if st.session_state.auth_page == "signup":
        show_signup_page()
    else:
        show_login_page()
    st.stop()   # <-- halts execution; nothing below renders until user is logged in

# ── Logout button available in sidebar for authenticated users ───────────────
show_logout_button()

# ════════════════════════════════════════════════════════════════════════════
# AUTHENTICATION SECTION END
