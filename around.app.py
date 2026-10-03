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
