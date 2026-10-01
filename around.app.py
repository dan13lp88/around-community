import streamlit as st
from datetime import datetime

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
    """
    <style>
        /* Main app */
        .stApp {
            background-color: #f6f7f9;
        }

        /* Reduce excessive Streamlit top spacing */
        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 3rem;
            max-width: 1180px;
        }

        /* Main brand */
        .around-logo {
            font-size: 2.4rem;
            font-weight: 800;
            letter-spacing: -1.5px;
            margin-bottom: 0;
            color: #171717;
        }

        .location-text {
            color: #6b7280;
            font-size: 0.95rem;
            margin-top: -5px;
        }

        /* Welcome card */
        .welcome-card {
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 18px;
            padding: 24px;
            margin-bottom: 20px;
        }

        .welcome-title {
            font-size: 1.65rem;
            font-weight: 750;
            color: #171717;
            margin-bottom: 5px;
        }

        .welcome-subtitle {
            color: #6b7280;
            margin-bottom: 0;
        }

        /* Cards */
        .around-card {
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
            padding: 20px;
            margin-bottom: 16px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.03);
        }

        .post-author {
            font-size: 1rem;
            font-weight: 700;
            color: #171717;
        }

        .post-meta {
            color: #8a8f98;
            font-size: 0.82rem;
        }

        .post-text {
            color: #262626;
            font-size: 1rem;
            line-height: 1.55;
            margin-top: 14px;
            margin-bottom: 12px;
        }

        .post-stats {
            color: #737780;
            font-size: 0.85rem;
            padding-top: 8px;
        }

        /* Category pill */
        .pill {
            display: inline-block;
            padding: 5px 10px;
            border-radius: 999px;
            background: #eef2f7;
            color: #4b5563;
            font-size: 0.75rem;
            font-weight: 600;
            margin-bottom: 10px;
        }

        /* Marketplace */
        .price {
            font-size: 1.35rem;
            font-weight: 800;
            color: #171717;
        }

        .item-title {
            font-size: 1.05rem;
            font-weight: 650;
            color: #252525;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #ffffff;
            border-right: 1px solid #e5e7eb;
        }

        /* Buttons */
        .stButton > button {
            border-radius: 10px;
            font-weight: 600;
        }

        /* Footer */
        .around-footer {
            text-align: center;
            color: #9ca3af;
            font-size: 0.78rem;
            padding-top: 35px;
            padding-bottom: 15px;
        }

        /* Hide Streamlit decoration */
        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <div class="around-logo">around.</div>
        <div class="location-text">📍 Lyons, Kansas</div>
        """,
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

    if st.button("➕ Create Post", use_container_width=True):
        st.toast("Posting will be available soon!")

    if st.button("📦 Sell Something", use_container_width=True):
        st.toast("Marketplace listings are coming soon!")

    st.divider()

    st.markdown("**Not signed in**")
    st.caption("Create a local account to post, sell, bid, and comment.")

    col1, col2 = st.columns(2)

    with col1:
        st.button("Log in", use_container_width=True)

    with col2:
        st.button("Sign up", use_container_width=True)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

top_left, top_right = st.columns([4, 1])

with top_left:
    st.markdown(
        """
        <div class="around-logo">around.</div>
        <div class="location-text">Your community. All in one place.</div>
        """,
        unsafe_allow_html=True,
    )

with top_right:
    st.write("")
    st.button("🔔  Notifications", use_container_width=True)

st.write("")

# ---------------------------------------------------------
# HOME
# ---------------------------------------------------------

if page == "🏠 Home":

    st.markdown(
        """
        <div class="welcome-card">
            <div class="welcome-title">What's Around Lyons?</div>
            <div class="welcome-subtitle">
                See what your neighbors are talking about, what's for sale,
                local auctions, services, and deals happening around town.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    search = st.text_input(
        "Search Around",
        placeholder="Search posts, items, services, deals...",
        label_visibility="collapsed",
    )

    st.write("")

    # Quick access
    quick1, quick2, quick3, quick4, quick5 = st.columns(5)

    with quick1:
        st.button("💬\nCommunity", use_container_width=True)

    with quick2:
        st.button("🛍️\nMarket", use_container_width=True)

    with quick3:
        st.button("🔨\nAuctions", use_container_width=True)

    with quick4:
        st.button("🔧\nServices", use_container_width=True)

    with quick5:
        st.button("🍔\nDeals", use_container_width=True)

    st.write("")

    # Main content / right rail
    feed, rail = st.columns([2.15, 1], gap="large")

    # -----------------------------------------------------
    # COMMUNITY FEED
    # -----------------------------------------------------

    with feed:

        st.subheader("Around today")

        st.markdown(
            """
            <div class="around-card">
                <span class="pill">COMMUNITY</span>
                <div class="post-author">👤 Sarah M.</div>
                <div class="post-meta">Lyons · 18 minutes ago</div>

                <div class="post-text">
                    Does anyone know someone local who does small concrete jobs?
                    Looking to get a section of sidewalk repaired.
                </div>

                <div class="post-stats">
                    👍 6 reactions &nbsp;&nbsp; 💬 4 comments
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        post1, post2 = st.columns(2)

        with post1:
            st.button("♡ Like", key="like_1", use_container_width=True)

        with post2:
            st.button("💬 Comment", key="comment_1", use_container_width=True)

        st.markdown(
            """
            <div class="around-card">
                <span class="pill">ANNOUNCEMENT</span>
                <div class="post-author">📢 Lyons Community</div>
                <div class="post-meta">Lyons · 1 hour ago</div>

                <div class="post-text">
                    Reminder: Community cleanup is this Saturday morning.
                    Volunteers will meet downtown at 8:00 AM.
                </div>

                <div class="post-stats">
                    👍 14 reactions &nbsp;&nbsp; 💬 3 comments
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        post3, post4 = st.columns(2)

        with post3:
            st.button("♡ Like", key="like_2", use_container_width=True)

        with post4:
            st.button("💬 Comment", key="comment_2", use_container_width=True)

        st.markdown(
            """
            <div class="around-card">
                <span class="pill">LOCAL QUESTION</span>
                <div class="post-author">👤 Mike R.</div>
                <div class="post-meta">Lyons · 2 hours ago</div>

                <div class="post-text">
                    Who around town sharpens mower blades? I'd rather take
                    them somewhere local if possible.
                </div>

                <div class="post-stats">
                    👍 3 reactions &nbsp;&nbsp; 💬 8 comments
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # -----------------------------------------------------
    # RIGHT RAIL
    # -----------------------------------------------------

    with rail:

        st.subheader("Marketplace")

        st.markdown(
            """
            <div class="around-card">
                <div class="item-title">Craftsman Push Mower</div>
                <div class="price">$125</div>
                <div class="post-meta">Listed today · Lyons</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.button(
            "Browse Marketplace →",
            key="browse_market",
            use_container_width=True,
        )

        st.write("")

        st.subheader("Ending soon")

        st.markdown(
            """
            <div class="around-card">
                <span class="pill">AUCTION</span>
                <div class="item-title">Vintage Coca-Cola Cooler</div>
                <div class="price">$86</div>
                <div class="post-meta">
                    Current bid · 7 bids
                </div>
                <br>
                <strong>⏱ 2h 18m remaining</strong>
            </div>
            """,
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
            """
            <div class="around-card">
                <span class="pill">TODAY</span>
                <div class="item-title">🍔 Main Street Grill</div>
                <div class="post-text">
                    Burger, fries & drink special — $9.99 today.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.button(
            "See Local Deals →",
            key="deals_home",
            use_container_width=True,
        )

# ---------------------------------------------------------
# COMMUNITY PAGE
# ---------------------------------------------------------

elif page == "💬 Community":

    st.title("Community")
    st.caption("Talk about what's happening around town.")

    st.text_input(
        "Search community",
        placeholder="Search community posts...",
    )

    st.write("")

    st.info(
        "Community posting and comments will be connected to user accounts "
        "in an upcoming build."
    )

    st.markdown(
        """
        <div class="around-card">
            <div class="post-author">What's happening around Lyons?</div>
            <div class="post-text">
                Community posts, announcements, recommendations, questions,
                lost & found posts, and local conversations will appear here.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# MARKETPLACE PAGE
# ---------------------------------------------------------

elif page == "🛍️ Marketplace":

    st.title("Marketplace")
    st.caption("Buy and sell with people around you.")

    search = st.text_input(
        "Search Marketplace",
        placeholder="What are you looking for?",
    )

    categories = st.selectbox(
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
            "Other",
        ],
    )

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class="around-card">
                <div class="item-title">Craftsman Push Mower</div>
                <div class="price">$125</div>
                <div class="post-meta">Lyons · Listed today</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
            <div class="around-card">
                <div class="item-title">Dining Table + 4 Chairs</div>
                <div class="price">$80</div>
                <div class="post-meta">Lyons · Listed yesterday</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            """
            <div class="around-card">
                <div class="item-title">DeWalt Drill Set</div>
                <div class="price">$95</div>
                <div class="post-meta">Lyons · Listed today</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ---------------------------------------------------------
# AUCTIONS PAGE
# ---------------------------------------------------------

elif page == "🔨 Auctions":

    st.title("Auctions")
    st.caption("Bid local.")

    st.markdown(
        """
        <div class="around-card">
            <span class="pill">ENDING SOON</span>
            <div class="item-title">Vintage Coca-Cola Cooler</div>
            <div class="price">$86 current bid</div>
            <div class="post-text">
                7 bids
                <br><br>
                <strong>⏱ 2 hours 18 minutes remaining</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    bid = st.number_input(
        "Your bid",
        min_value=87.00,
        step=1.00,
    )

    st.button(
        f"Place ${bid:.2f} bid",
        type="primary",
    )

# ---------------------------------------------------------
# SERVICES PAGE
# ---------------------------------------------------------

elif page == "🔧 Services":

    st.title("Services")
    st.caption("Find someone around town who can help.")

    service_search = st.text_input(
        "What are you looking for?",
        placeholder="Handyman, mowing, plumbing, cleaning...",
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

    st.markdown(
        """
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
        """,
        unsafe_allow_html=True,
    )

    st.button(
        "View Contact Information",
        use_container_width=True,
    )

# ---------------------------------------------------------
# LOCAL DEALS PAGE
# ---------------------------------------------------------

elif page == "🍔 Local Deals":

    st.title("Local Deals")
    st.caption("See what's good around town today.")

    st.markdown(
        """
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
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
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
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="around-footer">
        around. &nbsp;•&nbsp; Lyons, Kansas
        <br>
        Powered by Milnova Software Solutions
    </div>
    """,
    unsafe_allow_html=True,
)
