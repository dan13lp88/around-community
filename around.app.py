import streamlit as st
from textwrap import dedent
from supabase import create_client

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
# -----------------------------
# SUPABASE CONNECTION
# -----------------------------

def init_supabase():
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"],
    )


if "supabase_client" not in st.session_state:
    st.session_state.supabase_client = init_supabase()

supabase = st.session_state.supabase_client
# Temporary Supabase connection test
try:
    community_test = (
        supabase.table("communities")
        .select("name, state")
        .eq("slug", "lyons-ks")
        .execute()
    )

    if community_test.data:
        st.caption(
            f"🟢 Supabase connected • "
            f"{community_test.data[0]['name']}, "
            f"{community_test.data[0]['state']}"
        )

except Exception as e:
    st.caption(f"🔴 Supabase connection failed: {e}")
# ---------------------------------------------------------
# AUTHENTICATION STATE
# ---------------------------------------------------------

if "user" not in st.session_state:
    st.session_state.user = None

if "show_login" not in st.session_state:
    st.session_state.show_login = False

if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

if "profile" not in st.session_state:
    st.session_state.profile = None
    # ---------------------------------------------------------
# LOAD SIGNED-IN USER PROFILE
# ---------------------------------------------------------

if st.session_state.user is not None:
    try:
        profile_response = (
            supabase.table("profiles")
            .select("*")
            .eq("id", st.session_state.user.id)
            .execute()
        )

        if profile_response.data:
            st.session_state.profile = profile_response.data[0]
        else:
            st.session_state.profile = None

    except Exception as e:
        st.session_state.profile = None
# ---------------------------------------------------------
# DEMO SERVICE DATA
# ---------------------------------------------------------

# For now, service listings are stored only in the current
# Streamlit session. Later, this will be replaced by Supabase.

if "services" not in st.session_state:
    st.session_state.services = [
        {
            "name": "Jake's Lawn Service",
            "category": "Lawn Care",
            "description": "Mowing, trimming, cleanup and small residential yards.",
            "location": "Lyons and surrounding area",
            "phone": "",
        },
        {
            "name": "Smith Plumbing",
            "category": "Plumbing",
            "description": "Residential plumbing repairs, fixture replacement and small installations.",
            "location": "Lyons, Kansas",
            "phone": "",
        },
        {
            "name": "Main Street Cleaning",
            "category": "Cleaning",
            "description": "Home and small office cleaning services.",
            "location": "Lyons, Kansas",
            "phone": "",
        },
        {
            "name": "Rice County Handyman",
            "category": "Handyman",
            "description": "Small home repairs, assembly, maintenance and general handyman work.",
            "location": "Lyons and surrounding area",
            "phone": "",
        },
    ]

if "show_service_form" not in st.session_state:
    st.session_state.show_service_form = False


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

        @media (max-width: 768px) {
            .st-key-footer_logo [data-testid="stHorizontalBlock"] {
                flex-wrap: nowrap !important;
            }

            .st-key-footer_logo [data-testid="stColumn"] {
                min-width: 0 !important;
            }
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
# SUPABASE CONNECTION STATUS
# ---------------------------------------------------------

try:
    community_test = (
        supabase.table("communities")
        .select("name, state, slug")
        .eq("slug", "lyons-ks")
        .execute()
    )

    if community_test.data:
        st.caption(
            f"🟢 Supabase connected • "
            f"{community_test.data[0]['name']}, "
            f"{community_test.data[0]['state']}"
        )
    else:
        st.warning("Supabase connected, but Lyons was not found.")

except Exception as e:
    st.error(f"Supabase connection failed: {e}")


# ---------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------

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


def service_card(service):
    """Render a service listing."""

    category_icons = {
        "Handyman": "🔨",
        "Lawn Care": "🌱",
        "Plumbing": "🚰",
        "Electrical": "⚡",
        "HVAC": "❄️",
        "Cleaning": "🧹",
        "Tree Service": "🌳",
        "Auto Repair": "🚗",
        "Pet Services": "🐕",
        "Photography": "📸",
        "Other": "🔧",
    }

    icon = category_icons.get(service["category"], "🔧")

    phone_html = ""

    if service.get("phone"):
        phone_html = (
            f'<div class="post-meta">📞 {service["phone"]}</div>'
        )

    st.markdown(
        dedent(f"""
            <div class="around-card">
                <span class="pill">{service["category"].upper()}</span>
                <div class="post-author">
                    {icon} {service["name"]}
                </div>
                <div class="post-text">
                    {service["description"]}
                </div>
                <div class="post-meta">
                    📍 Serves {service["location"]}
                </div>
                {phone_html}
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

    if st.session_state.user is None:

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
                st.session_state.show_login = True
                st.session_state.show_signup = False
                st.rerun()

        with signup_col:
            if st.button(
                "Sign up",
                use_container_width=True,
            ):
                st.session_state.show_signup = True
                st.session_state.show_login = False
                st.rerun()

        if st.session_state.show_login:

            st.markdown("##### Log in")

            login_email = st.text_input(
                "Email",
                key="login_email",
            )

            login_password = st.text_input(
                "Password",
                type="password",
                key="login_password",
            )

            if st.button(
                "Log in to Around",
                type="primary",
                use_container_width=True,
            ):
                try:
                    response = supabase.auth.sign_in_with_password(
                        {
                            "email": login_email,
                            "password": login_password,
                        }
                    )

                    st.session_state.user = response.user
                    st.session_state.show_login = False

                    st.rerun()

                except Exception as e:
                    st.error(f"Unable to log in: {e}")

        if st.session_state.show_signup:


            st.markdown("##### Create your Around account")

            signup_email = st.text_input(
                "Email",
                key="signup_email",
            )

            signup_password = st.text_input(
                "Password",
                type="password",
                key="signup_password",
            )

            if st.button(
                "Create Account",
                type="primary",
                use_container_width=True,
            ):
                try:
                    response = supabase.auth.sign_up(
                        {
                            "email": signup_email,
                            "password": signup_password,
                        }
                    )

                    if response.session:
                        st.session_state.user = response.user
                        st.session_state.show_signup = False
                        st.rerun()

                    else:
                        st.success(
                            "Account created! Check your email "
                            "to confirm your account."
                        )

                except Exception as e:
                    st.error(
                        f"Unable to create account: {e}"
                    )

            if st.button(
                "Resend confirmation email",
                use_container_width=True,
            ):
                try:
                    supabase.auth.resend(
                        {
                            "type": "signup",
                            "email": signup_email,
                            "options": {
                                "email_redirect_to": "https://around.streamlit.app",
                            },
                        }
                    )

                    st.success(
                        "Confirmation email sent! Check your inbox."
                    )

                except Exception as e:
                    st.error(
                        f"Unable to resend confirmation: {e}"
                    )

    else:

             if st.session_state.profile is not None:
            display_name = (
                st.session_state.profile.get("display_name")
                or st.session_state.profile["username"]
            )

            st.markdown(f"**{display_name}**")
            st.caption(
                f"@{st.session_state.profile['username']}  ·  📍 Lyons, Kansas"
            )

        else:
            st.markdown("**Signed in**")
            st.caption(st.session_state.user.email)

            st.markdown("##### Finish your Around profile")

            profile_username = st.text_input(
                "Username",
                placeholder="Example: danielp",
                key="profile_username",
            )

            profile_display_name = st.text_input(
                "Display name",
                placeholder="Example: Daniel P.",
                key="profile_display_name",
            )

            if st.button(
                "Create Profile",
                type="primary",
                use_container_width=True,
            ):
                if not profile_username.strip():
                    st.error("Please choose a username.")

                else:
                    try:
                        community_response = (
                            supabase.table("communities")
                            .select("id")
                            .eq("slug", "lyons-ks")
                            .single()
                            .execute()
                        )

                        community_id = community_response.data["id"]

                        profile_response = (
                            supabase.table("profiles")
                            .insert(
                                {
                                    "id": st.session_state.user.id,
                                    "community_id": community_id,
                                    "username": profile_username.strip(),
                                    "display_name": profile_display_name.strip()
                                    or None,
                                }
                            )
                            .execute()
                        )

                        st.session_state.profile = (
                            profile_response.data[0]
                        )

                        st.success("Your Around profile is ready!")
                        st.rerun()

                    except Exception as e:
                        st.error(
                            f"Unable to create profile: {e}"
                        )

        if st.button(
            "Log out",
            use_container_width=True,
        ):
            supabase.auth.sign_out()

            st.session_state.user = None
            st.session_state.show_login = False
            st.session_state.show_signup = False

            st.rerun()


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

    feed, rail = st.columns(
        [2.15, 1],
        gap="large",
    )

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

    # -----------------------------------------------------
    # SEARCH + FILTERS
    # -----------------------------------------------------

    service_search = st.text_input(
        "What are you looking for?",
        placeholder="Search services, businesses, or keywords...",
    )

    service_category = st.selectbox(
        "Service category",
        [
            "All Services",
            "Handyman",
            "Lawn Care",
            "Plumbing",
            "Electrical",
            "HVAC",
            "Cleaning",
            "Tree Service",
            "Auto Repair",
            "Pet Services",
            "Photography",
            "Other",
        ],
    )

    st.write("")

    # -----------------------------------------------------
    # SERVICES HEADER + LIST SERVICE BUTTON
    # -----------------------------------------------------

    services_header, service_action = st.columns(
        [4, 1]
    )

    with services_header:
        st.subheader("Services around Lyons")

    with service_action:
        if st.button(
            "➕ List Service",
            type="primary",
            use_container_width=True,
        ):
            st.session_state.show_service_form = (
                not st.session_state.show_service_form
            )

    # -----------------------------------------------------
    # LIST SERVICE FORM
    # -----------------------------------------------------

    if st.session_state.show_service_form:

        st.markdown("### List a Service")

        st.caption(
            "Add a service to Around. For this prototype, "
            "the listing will only remain during the current session."
        )

        with st.form("list_service_form"):

            service_name = st.text_input(
                "Business / Service Name",
                placeholder="Example: Jake's Lawn Service",
            )

            new_service_category = st.selectbox(
                "Category",
                [
                    "Handyman",
                    "Lawn Care",
                    "Plumbing",
                    "Electrical",
                    "HVAC",
                    "Cleaning",
                    "Tree Service",
                    "Auto Repair",
                    "Pet Services",
                    "Photography",
                    "Other",
                ],
                key="new_service_category",
            )

            service_description = st.text_area(
                "Description",
                placeholder=(
                    "Tell people what services you provide..."
                ),
            )

            service_location = st.text_input(
                "Service Area",
                value="Lyons, Kansas",
            )

            service_phone = st.text_input(
                "Phone (optional)",
                placeholder="Example: 620-555-1234",
            )

            form_left, form_right = st.columns(2)

            with form_left:
                submit_service = st.form_submit_button(
                    "List Service",
                    type="primary",
                    use_container_width=True,
                )

            with form_right:
                cancel_service = st.form_submit_button(
                    "Cancel",
                    use_container_width=True,
                )

            if submit_service:

                if not service_name.strip():
                    st.error(
                        "Please enter a business or service name."
                    )

                elif not service_description.strip():
                    st.error(
                        "Please enter a description."
                    )

                elif not service_location.strip():
                    st.error(
                        "Please enter a service area."
                    )

                else:

                    st.session_state.services.append(
                        {
                            "name": service_name.strip(),
                            "category": new_service_category,
                            "description": service_description.strip(),
                            "location": service_location.strip(),
                            "phone": service_phone.strip(),
                        }
                    )

                    st.session_state.show_service_form = False

                    st.success(
                        f"{service_name.strip()} was added to Around!"
                    )

                    st.rerun()

            if cancel_service:
                st.session_state.show_service_form = False
                st.rerun()

        st.divider()

    # -----------------------------------------------------
    # FILTER SERVICE LISTINGS
    # -----------------------------------------------------

    filtered_services = []

    for service in st.session_state.services:

        category_matches = (
            service_category == "All Services"
            or service["category"] == service_category
        )

        search_text = service_search.strip().lower()

        searchable_text = (
            f'{service["name"]} '
            f'{service["category"]} '
            f'{service["description"]} '
            f'{service["location"]}'
        ).lower()

        search_matches = (
            not search_text
            or search_text in searchable_text
        )

        if category_matches and search_matches:
            filtered_services.append(service)

    # -----------------------------------------------------
    # DISPLAY RESULTS
    # -----------------------------------------------------

    if filtered_services:

        st.caption(
            f"{len(filtered_services)} "
            f"{'service' if len(filtered_services) == 1 else 'services'} found"
        )

        for index, service in enumerate(filtered_services):

            service_card(service)

            if service.get("phone"):
                if st.button(
                    "View Contact Information",
                    key=f"service_contact_{index}_{service['name']}",
                    use_container_width=True,
                ):
                    st.info(
                        f"📞 {service['phone']}"
                    )

    else:

        st.info(
            "No services match your search or selected category."
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

st.markdown(
    '<div class="around-footer"><strong>around.</strong>&nbsp;•&nbsp;Lyons, Kansas<br><br>Powered by Milnova Software Solutions</div>',
    unsafe_allow_html=True,
)

with st.container(key="footer_logo"):
    logo_left, logo_center, logo_right = st.columns([4, 1, 4])

    with logo_center:
        st.image(
            "MilnovaLogoUpdateLIGHTMODE.svg",
            width=130,
        )
