import streamlit as st
from textwrap import dedent
import base64

# =========================================================
# AROUND
# Local community platform
# Powered by Milnova Software Solutions
# =========================================================


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="Around | Lyons, Kansas",
    page_icon="📍",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------
# CUSTOM STYLING
# ---------------------------------------------------------

st.markdown(
    dedent("""
        <style>

        :root {
            --around-bg: #F5F7FA;
            --around-surface: #FFFFFF;
            --around-text: #111827;
            --around-muted: #6B7280;
            --around-border: #E5E7EB;
            --around-primary: #2563EB;
            --around-hover: #F3F4F6;
        }

        /* =====================================================
           APP
           ===================================================== */

        .stApp {
            background: var(--around-bg);
            color: var(--around-text);
        }

        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 3rem;
            max-width: 1180px;
        }

        /* =====================================================
           GLOBAL TEXT
           ===================================================== */

        h1,
        h2,
        h3,
        h4,
        h5,
        h6,
        p,
        label {
            color: var(--around-text) !important;
        }

        [data-testid="stMarkdownContainer"] {
            color: var(--around-text);
        }

        /* =====================================================
           BRAND
           ===================================================== */

        .around-logo {
            font-size: 2.4rem;
            font-weight: 800;
            letter-spacing: -1.5px;
            margin-bottom: 0;
            color: var(--around-text);
        }

        .location-text {
            color: var(--around-muted);
            font-size: 0.95rem;
            margin-top: -5px;
        }

        /* =====================================================
           SIDEBAR
           ===================================================== */

        section[data-testid="stSidebar"] {
            background: var(--around-surface);
            border-right: 1px solid var(--around-border);
        }

        section[data-testid="stSidebar"] * {
            color: var(--around-text);
        }

        /* =====================================================
           WELCOME CARD
           ===================================================== */

        .welcome-card {
            background: var(--around-surface);
            border: 1px solid var(--around-border);
            border-radius: 18px;
            padding: 24px;
            margin-bottom: 20px;
        }

        .welcome-title {
            font-size: 1.65rem;
            font-weight: 750;
            color: var(--around-text);
            margin-bottom: 5px;
        }

        .welcome-subtitle {
            color: var(--around-muted);
            margin-bottom: 0;
            line-height: 1.5;
        }

        /* =====================================================
           CONTENT CARDS
           ===================================================== */

        .around-card {
            background: var(--around-surface);
            border: 1px solid var(--around-border);
            border-radius: 16px;
            padding: 20px;
            margin-bottom: 16px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        }

        .post-author {
            font-size: 1rem;
            font-weight: 700;
            color: var(--around-text);
        }

        .post-meta {
            color: var(--around-muted);
            font-size: 0.82rem;
            margin-top: 2px;
        }

        .post-text {
            color: var(--around-text);
            font-size: 1rem;
            line-height: 1.55;
            margin-top: 14px;
            margin-bottom: 12px;
        }

        .post-stats {
            color: var(--around-muted);
            font-size: 0.85rem;
            padding-top: 8px;
        }

        /* =====================================================
           CATEGORY PILLS
           ===================================================== */

        .pill {
            display: inline-block;
            padding: 5px 10px;
            border-radius: 999px;
            background: #EFF6FF;
            color: #1D4ED8;
            font-size: 0.75rem;
            font-weight: 700;
            margin-bottom: 10px;
        }

        /* =====================================================
           MARKETPLACE
           ===================================================== */

        .price {
            font-size: 1.35rem;
            font-weight: 800;
            color: var(--around-text);
            margin-top: 4px;
        }

        .item-title {
            font-size: 1.05rem;
            font-weight: 650;
            color: var(--around-text);
        }

        /* =====================================================
           INPUTS
           ===================================================== */

        [data-testid="stTextInput"] input {
            background: var(--around-surface);
            color: var(--around-text);
            border: 1px solid var(--around-border);
        }

        [data-testid="stTextInput"] input::placeholder {
            color: #9CA3AF;
        }

        /* =====================================================
           BUTTONS
           ===================================================== */

        .stButton > button {
            border-radius: 10px;
            font-weight: 600;
        }

        /* =====================================================
           FOOTER
           ===================================================== */

        .around-footer {
            text-align: center;
            color: #9CA3AF;
            font-size: 0.78rem;
            padding-top: 35px;
            padding-bottom: 15px;
        }

        /* =====================================================
           HIDE DEFAULT STREAMLIT ELEMENTS
           ===================================================== */

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        </style>
    """),
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------

def get_svg_base64(file_path):
    """Convert a local SVG file to base64 for reliable display."""
    with open(file_path, "rb") as svg_file:
        return base64.b64encode(svg_file.read()).decode()


def community_post(category, author, meta, text, reactions, comments):
    """Render a demo community post."""

    st.markdown(
        dedent(f"""
            <div class="around-card">
                <span class="pill">{category}</span>
                <div class="post-author">{author}</div>
                <div class="post-meta">{meta}</div>
                <div class="post-text">{text}</div>
                <div class="post-stats">
                    👍 {reactions} reactions &nbsp;&nbsp; 💬 {comments} comments
                </div>
            </div>
        """),
        unsafe_allow_html=True,
    )


def marketplace_card(title, price, meta):
    """Render a demo marketplace item."""

    st.markdown(
        dedent(f"""
            <div class="around-card">
                <div class="item-title">{title}</div>
                <div class="price">{price}</div>
                <div class="post-meta">{meta}</div>
            </div>
        """),
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown(
        dedent("""
            <div class="around-logo">around.</div>
            <div class="location-text">📍 Lyons, Kansas</div>
        """),
        unsafe_allow_html=True,
    )

    st.write("")

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "💬 Community",
            "🛍️ Marketplace",
            "🔨 Auctions",
            "🔧 Services",
            "🍔 Local Deals",
        ],
        label_visibility="collapsed",
    )

    st.divider()

    st.markdown("#### Your Around")

    if st.button(
        "➕ Create Post",
        use_container_width=True,
    ):
        st.toast("Posting will be available soon!")

    if st.button(
        "📦 Sell Something",
        use_container_width=True,
    ):
        st.toast("Marketplace listings are coming soon!")

    st.divider()

    st.markdown("**Not signed in**")

    st.caption(
        "Create a local account to post, sell, bid, and comment."
    )

    login_col, signup_col = st.columns(2)

    with login_col:
        if st.button(
            "Log in",
            use_container_width=True,
        ):
            st.toast("Login is coming next.")

    with signup_col:
        if st.button(
            "Sign up",
            use_container_width=True,
        ):
            st.toast("Account creation is coming next.")


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

top_left, top_right = st.columns([4, 1])

with top_left:

    st.markdown(
        dedent("""
            <div class="around-logo">around.</div>
            <div class="location-text">Your community. All in one place.</div>
        """),
        unsafe_allow_html=True,
    )

with top_right:

    st.write("")

    if st.button(
        "🔔 Notifications",
        use_container_width=True,
    ):
        st.toast("No new notifications.")

st.write("")


# =========================================================
# HOME PAGE
# =========================================================

if page == "🏠 Home":

    st.markdown(
        dedent("""
            <div class="welcome-card">
                <div class="welcome-title">What's Around Lyons?</div>
                <div class="welcome-subtitle">
                    See what your neighbors are talking about,
                    what's for sale, local auctions, services,
                    and deals happening around town.
                </div>
            </div>
        """),
        unsafe_allow_html=True,
    )

    search = st.text_input(
        "Search Around",
        placeholder="Search posts, items, services, deals...",
        label_visibility="collapsed",
    )

    st.write("")

    # -----------------------------------------------------
    # QUICK ACCESS
    # -----------------------------------------------------

    quick1, quick2, quick3, quick4, quick5 = st.columns(5)

    with quick1:
        st.button(
            "💬 Community",
            use_container_width=True,
            key="home_community",
        )

    with quick2:
        st.button(
            "🛍️ Market",
            use_container_width=True,
            key="home_market",
        )

    with quick3:
        st.button(
            "🔨 Auctions",
            use_container_width=True,
            key="home_auctions",
        )

    with quick4:
        st.button(
            "🔧 Services",
            use_container_width=True,
            key="home_services",
        )

    with quick5:
        st.button(
            "🍔 Deals",
            use_container_width=True,
            key="home_deals",
        )

    st.write("")

    # -----------------------------------------------------
    # HOME CONTENT
    # -----------------------------------------------------

    feed, rail = st.columns(
        [2.15, 1],
        gap="large",
    )

    # -----------------------------------------------------
    # COMMUNITY FEED
    # -----------------------------------------------------

    with feed:

        st.subheader("Around today")

        community_post(
            category="COMMUNITY",
            author="👤 Sarah M.",
            meta="Lyons · 18 minutes ago",
            text=(
                "Does anyone know someone local who does small "
                "concrete jobs? Looking to get a section of "
                "sidewalk repaired."
            ),
            reactions=6,
            comments=4,
        )

        post1, post2 = st.columns(2)

        with post1:
            st.button(
                "♡ Like",
                key="like_1",
                use_container_width=True,
            )

        with post2:
            st.button(
                "💬 Comment",
                key="comment_1",
                use_container_width=True,
            )

        st.write("")

        community_post(
            category="ANNOUNCEMENT",
            author="📢 Lyons Community",
            meta="Lyons · 1 hour ago",
            text=(
                "Reminder: Community cleanup is this Saturday "
                "morning. Volunteers will meet downtown at "
                "8:00 AM."
            ),
            reactions=14,
            comments=3,
        )

        post3, post4 = st.columns(2)

        with post3:
            st.button(
                "♡ Like",
                key="like_2",
                use_container_width=True,
            )

        with post4:
            st.button(
                "💬 Comment",
                key="comment_2",
                use_container_width=True,
            )

        st.write("")

        community_post(
            category="LOCAL QUESTION",
            author="👤 Mike R.",
            meta="Lyons · 2 hours ago",
            text=(
                "Who around town sharpens mower blades? "
                "I'd rather take them somewhere local if possible."
            ),
            reactions=3,
            comments=8,
        )

    # -----------------------------------------------------
    # RIGHT RAIL
    # -----------------------------------------------------

    with rail:

        st.subheader("Marketplace")

        marketplace_card(
            title="Craftsman Push Mower",
            price="$125",
            meta="Listed today · Lyons",
        )

        st.button(
            "Browse Marketplace →",
            key="browse_market",
            use_container_width=True,
        )

        st.write("")

        st.subheader("Ending soon")

        st.markdown(
            dedent("""
                <div class="around-card">
                    <span class="pill">AUCTION</span>
                    <div class="item-title">Vintage Coca-Cola Cooler</div>
                    <div class="price">$86</div>
                    <div class="post-meta">Current bid · 7 bids</div>
                    <div class="post-text">
                        <strong>⏱ 2h 18m remaining</strong>
                    </div>
                </div>
            """),
            unsafe_allow_html=True,
        )

        st.button(
            "View Auction →",
            key="auction_home",
            use_container_width=True,
        )

        st.write("")

        st.subheader("Local deal")

        st.markdown(
            dedent("""
                <div class="around-card">
                    <span class="pill">TODAY</span>
                    <div class="item-title">🍔 Main Street Grill</div>
                    <div class="post-text">
                        Burger, fries & drink special — $9.99 today.
                    </div>
                </div>
            """),
            unsafe_allow_html=True,
        )

        st.button(
            "See Local Deals →",
            key="deals_home",
            use_container_width=True,
        )


# =========================================================
# COMMUNITY PAGE
# =========================================================

elif page == "💬 Community":

    st.title("Community")

    st.caption(
        "Talk about what's happening around town."
    )

    st.text_input(
        "Search community",
        placeholder="Search community posts...",
    )

    st.write("")

    if st.button(
        "➕ Create a Post",
        type="primary",
    ):
        st.toast(
            "Account-based posting will be available soon."
        )

    st.write("")

    community_post(
        category="COMMUNITY",
        author="👤 Sarah M.",
        meta="Lyons · 18 minutes ago",
        text=(
            "Does anyone know someone local who does small "
            "concrete jobs? Looking to get a section of "
            "sidewalk repaired."
        ),
        reactions=6,
        comments=4,
    )

    community_post(
        category="ANNOUNCEMENT",
        author="📢 Lyons Community",
        meta="Lyons · 1 hour ago",
        text=(
            "Reminder: Community cleanup is this Saturday "
            "morning. Volunteers will meet downtown at 8:00 AM."
        ),
        reactions=14,
        comments=3,
    )

    community_post(
        category="LOCAL QUESTION",
        author="👤 Mike R.",
        meta="Lyons · 2 hours ago",
        text=(
            "Who around town sharpens mower blades? "
            "I'd rather take them somewhere local if possible."
        ),
        reactions=3,
        comments=8,
    )


# =========================================================
# MARKETPLACE PAGE
# =========================================================

elif page == "🛍️ Marketplace":

    st.title("Marketplace")

    st.caption(
        "Buy and sell with people around you."
    )

    marketplace_search = st.text_input(
        "Search Marketplace",
        placeholder="What are you looking for?",
    )

    category = st.selectbox(
        "Category",
        [
            "All Categories",
            "Vehicles",
            "Home & Garden",
            "Electronics",
            "Tools",
            "Furniture",
            "Clothing",
            "Kids",
            "Free",
            "Other",
        ],
    )

    st.write("")

    top_market_left, top_market_right = st.columns(
        [4, 1]
    )

    with top_market_left:
        st.subheader("Items around you")

    with top_market_right:
        st.button(
            "➕ Sell",
            type="primary",
            use_container_width=True,
        )

    c1, c2, c3 = st.columns(3)

    with c1:

        marketplace_card(
            title="Craftsman Push Mower",
            price="$125",
            meta="Lyons · Listed today",
        )

    with c2:

        marketplace_card(
            title="Dining Table + 4 Chairs",
            price="$80",
            meta="Lyons · Listed yesterday",
        )

    with c3:

        marketplace_card(
            title="DeWalt Drill Set",
            price="$95",
            meta="Lyons · Listed today",
        )


# =========================================================
# AUCTIONS PAGE
# =========================================================

elif page == "🔨 Auctions":

    st.title("Auctions")

    st.caption(
        "Bid on items around you."
    )

    auction_left, auction_right = st.columns(
        [4, 1]
    )

    with auction_right:

        st.button(
            "➕ Create Auction",
            type="primary",
            use_container_width=True,
        )

    st.markdown(
        dedent("""
            <div class="around-card">
                <span class="pill">ENDING SOON</span>
                <div class="item-title">Vintage Coca-Cola Cooler</div>
                <div class="price">$86 current bid</div>
                <div class="post-meta">7 bids</div>
                <div class="post-text">
                    <strong>⏱ 2 hours 18 minutes remaining</strong>
                </div>
            </div>
        """),
        unsafe_allow_html=True,
    )

    bid = st.number_input(
        "Your bid",
        min_value=87.00,
        step=1.00,
    )

    if st.button(
        f"Place ${bid:.2f} bid",
        type="primary",
    ):
        st.warning(
            "You will need to sign in before placing a bid."
        )


# =========================================================
# SERVICES PAGE
# =========================================================

elif page == "🔧 Services":

    st.title("Services")

    st.caption(
        "Find someone around town who can help."
    )

    service_search = st.text_input(
        "What are you looking for?",
        placeholder=(
            "Handyman, mowing, plumbing, cleaning..."
        ),
    )

    category = st.selectbox(
        "Service category",
        [
            "All Services",
            "🔨 Handyman",
            "🌱 Lawn Care",
            "🚰 Plumbing",
            "⚡ Electrical",
            "❄️ HVAC",
            "🧹 Cleaning",
            "🌳 Tree Service",
            "🚗 Auto Repair",
            "🐕 Pet Services",
            "📸 Photography",
            "Other",
        ],
    )

    st.write("")

    services_header, service_action = st.columns(
        [4, 1]
    )

    with services_header:

        st.subheader(
            "Services around Lyons"
        )

    with service_action:

        st.button(
            "➕ List Service",
            type="primary",
            use_container_width=True,
        )

    st.markdown(
        dedent("""
            <div class="around-card">
                <span class="pill">LAWN CARE</span>
                <div class="post-author">🌱 Jake's Lawn Service</div>
                <div class="post-text">
                    Mowing, trimming, cleanup and small residential yards.
                </div>
                <div class="post-meta">
                    Serves Lyons and surrounding area
                </div>
            </div>
        """),
        unsafe_allow_html=True,
    )

    st.button(
        "View Contact Information",
        use_container_width=True,
    )


# =========================================================
# LOCAL DEALS PAGE
# =========================================================

elif page == "🍔 Local Deals":

    st.title("Local Deals")

    st.caption(
        "See what's good around town today."
    )

    deals_header, deals_action = st.columns(
        [4, 1]
    )

    with deals_header:

        st.subheader(
            "Today's deals"
        )

    with deals_action:

        st.button(
            "➕ Post Deal",
            type="primary",
            use_container_width=True,
        )

    st.markdown(
        dedent("""
            <div class="around-card">
                <span class="pill">TODAY'S DEAL</span>
                <div class="post-author">🍔 Main Street Grill</div>
                <div class="post-text">
                    <strong>Burger + fries + drink — $9.99</strong>
                    <br><br>
                    Available today from 11 AM – 8 PM.
                </div>
                <div class="post-meta">
                    Lyons, Kansas
                </div>
            </div>
        """),
        unsafe_allow_html=True,
    )

    st.markdown(
        dedent("""
            <div class="around-card">
                <span class="pill">SPECIAL</span>
                <div class="post-author">☕ Local Coffee Shop</div>
                <div class="post-text">
                    Buy any large drink and get a pastry for $1.
                </div>
                <div class="post-meta">
                    Today only
                </div>
            </div>
        """),
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

milnova_logo = get_svg_base64("MilnovaLogoUpdateLIGHTMODE.svg")

st.markdown(
    dedent(f"""
        <div class="around-footer">
            <strong>around.</strong>
            &nbsp;•&nbsp;
            Lyons, Kansas

            <br><br>

            Powered by Milnova Software Solutions

            <br>

            <img
                src="data:image/svg+xml;base64,{milnova_logo}"
                alt="Milnova Software Solutions"
                style="
                    width: 130px;
                    max-width: 40%;
                    margin-top: 10px;
                    height: auto;
                "
            >
        </div>
    """),
    unsafe_allow_html=True,
)
