# ════════════════════════════════════════════════════════════════════
# DASHBOARD MODULE  (paste after show_logout_button() call)
# ════════════════════════════════════════════════════════════════════

if st.session_state.dashboard_page == "dashboard":
    now = datetime.now()
    hour = now.hour
    if hour < 12:   greeting = "Good Morning"
    elif hour < 17: greeting = "Good Afternoon"
    else:           greeting = "Good Evening"

    # ── Welcome Header ───────────────────────────────────────────────────
    st.markdown(f"""
    <div class="dash-header">
        <div>
            <div class="dash-welcome-text">{greeting}, <span>{st.session_state.username}</span> 👋</div>
            <div class="dash-welcome-sub">Chennai Reservoir Intelligence · Live Dashboard</div>
        </div>
        <div class="dash-time-badge">{now.strftime("%d %b %Y · %H:%M")}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── System Alerts ────────────────────────────────────────────────────
    st.markdown('<div class="dash-section-title">🔔 System Alerts</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="dash-alert ok">✅ &nbsp; All 4 reservoirs reporting normal. Last sync: today.</div>
    <div class="dash-alert info">ℹ️ &nbsp; Northeast Monsoon season active — elevated inflow expected through December.</div>
    <div class="dash-alert warn">⚠️ &nbsp; Chembarambakkam below 45% capacity — monitor intake levels.</div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

    # ── KPI Row ──────────────────────────────────────────────────────────
    st.markdown('<div class="dash-section-title">📊 Key Metrics</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="dash-kpi-grid">
        <div class="dash-kpi">
            <span class="dash-kpi-icon">🌊</span>
            <div class="dash-kpi-val">247.3</div>
            <div class="dash-kpi-lbl">Total Level (MCft)</div>
            <div class="dash-kpi-trend up">↑ 3.2% vs last week</div>
        </div>
        <div class="dash-kpi">
            <span class="dash-kpi-icon">💧</span>
            <div class="dash-kpi-val">77.2%</div>
            <div class="dash-kpi-lbl">Avg Capacity Fill</div>
            <div class="dash-kpi-trend up">↑ Healthy range</div>
        </div>
        <div class="dash-kpi">
            <span class="dash-kpi-icon">🌧️</span>
            <div class="dash-kpi-val">18.4 mm</div>
            <div class="dash-kpi-lbl">7-Day Rain Avg</div>
            <div class="dash-kpi-trend neutral">→ Moderate</div>
        </div>
        <div class="dash-kpi">
            <span class="dash-kpi-icon">📅</span>
            <div class="dash-kpi-val">Q4</div>
            <div class="dash-kpi-lbl">Current Season</div>
            <div class="dash-kpi-trend up">↑ NE Monsoon Active</div>
        </div>
        <div class="dash-kpi">
            <span class="dash-kpi-icon">🔮</span>
            <div class="dash-kpi-val">+7d</div>
            <div class="dash-kpi-lbl">Forecast Horizon</div>
            <div class="dash-kpi-trend neutral">→ ML Ensemble</div>
        </div>
        <div class="dash-kpi">
            <span class="dash-kpi-icon">📈</span>
            <div class="dash-kpi-val">16 yrs</div>
            <div class="dash-kpi-lbl">Training Data</div>
            <div class="dash-kpi-trend neutral">→ 2004–2020</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Reservoir Status + Mini Bar Chart ────────────────────────────────
    dash_left, dash_right = st.columns([3, 2], gap="large")

    with dash_left:
        st.markdown('<div class="dash-section-title">🏞️ Reservoir Status</div>', unsafe_allow_html=True)
        # (pct, current MCft, capacity MCft)
        reservoirs = [
            ("Poondi",         82, 76.7,  93.46),
            ("Cholavaram",     71, 22.0,  31.00),
            ("Red Hills",      90, 83.7,  93.00),
            ("Chembarambakkam",44, 45.4, 103.00),
        ]
        st.markdown('<div class="res-status-grid">', unsafe_allow_html=True)
        for name, pct, cur, cap in reservoirs:
            color = "#00DC82" if pct >= 75 else ("#FFB347" if pct >= 45 else "#FF6B6B")
            st.markdown(f"""
            <div class="res-status-card">
                <div class="res-status-name">
                    {name}
                    <span class="res-status-pct" style="color:{color};">{pct}%</span>
                </div>
                <div class="res-bar-bg">
                    <div class="res-bar-fill" style="width:{pct}%;
                        background:linear-gradient(90deg, {color}88, {color});"></div>
                </div>
                <div class="res-cap-row">
                    <span>{cur:.1f} MCft current</span>
                    <span>{cap:.0f} MCft max</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with dash_right:
        st.markdown('<div class="dash-section-title">📉 30-Day Trend</div>', unsafe_allow_html=True)
        import random
        random.seed(42)
        bar_heights = [55, 58, 60, 57, 62, 65, 63, 67, 70, 68,
                       72, 74, 71, 75, 78, 76, 80, 82, 79, 83,
                       85, 83, 80, 77, 81, 79, 82, 85, 84, 77]
        bars_html = "".join([
            f'<div class="dash-bar" style="height:{h}%;opacity:{0.5 + 0.5*(h/100)};"></div>'
            for h in bar_heights
        ])
        labels_html = "".join([
            f'<span>{d}</span>'
            for d in ["May 17", "May 24", "May 31", "Jun 7", "Jun 14"]
        ])
        st.markdown(f"""
        <div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);
            border-radius:18px;padding:1.4rem 1.2rem;">
            <div style="font-family:'JetBrains Mono',monospace;font-size:0.6rem;
                color:rgba(214,232,245,0.3);letter-spacing:0.12em;
                text-transform:uppercase;margin-bottom:0.8rem;">
                Total Fill Level % (30 days)
            </div>
            <div class="dash-mini-chart">{bars_html}</div>
            <div class="dash-chart-labels">{labels_html}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
        st.markdown('<div class="dash-section-title">📋 Recent Activity</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="dash-activity-feed">
            <div class="activity-item">
                <div class="activity-dot" style="background:#00DC82;"></div>
                <div class="activity-text">Poondi inflow rate increased by 12% overnight.</div>
                <div class="activity-time">2h ago</div>
            </div>
            <div class="activity-item">
                <div class="activity-dot" style="background:#00C8FF;"></div>
                <div class="activity-text">7-day forecast updated with latest rainfall data.</div>
                <div class="activity-time">5h ago</div>
            </div>
            <div class="activity-item">
                <div class="activity-dot" style="background:#FFB347;"></div>
                <div class="activity-text">Chembarambakkam level dipped below 45% threshold.</div>
                <div class="activity-time">1d ago</div>
            </div>
            <div class="activity-item">
                <div class="activity-dot" style="background:#00DC82;"></div>
                <div class="activity-text">Red Hills reached seasonal high of 90% capacity.</div>
                <div class="activity-time">2d ago</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── CTA to Predictor ─────────────────────────────────────────────────
    st.markdown("""
    <div class="dash-cta">
        <div class="dash-cta-title">🔮 Ready to run a 7-day forecast?</div>
        <div class="dash-cta-sub">
            Enter current rainfall & level data to get an ML-powered reservoir prediction.
        </div>
    </div>
    """, unsafe_allow_html=True)
    _, cta_btn, _ = st.columns([2, 2, 2])
    with cta_btn:
        if st.button("🌊  Open Water Level Predictor", use_container_width=True, key="dash_go_predictor"):
            st.session_state.dashboard_page = "predictor"
            st.rerun()

    st.stop()   # Don't render predictor while on dashboard