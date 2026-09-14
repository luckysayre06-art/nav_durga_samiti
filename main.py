import streamlit as st
from pathlib import Path
import json
import uuid
import html


# ==================================================
# PAGE SETTINGS
# ==================================================

st.set_page_config(
    page_title="Nav Durga Utsav Samiti",
    page_icon="🪔",
    layout="wide"
)


# ==================================================
# FOLDERS
# ==================================================

BASE_DIR = Path(__file__).parent

ASSETS_DIR = BASE_DIR / "assets"
GALLERY_DIR = ASSETS_DIR / "gallery"
DATA_DIR = BASE_DIR / "data"

ASSETS_DIR.mkdir(exist_ok=True)
GALLERY_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)

CONTENT_FILE = DATA_DIR / "content.json"
AARTI_FILE = DATA_DIR / "aarti.json"


# ==================================================
# ADMIN PASSWORD
# ==================================================

ADMIN_PASSWORD = "HIMANSHU@786"


# ==================================================
# DEFAULT CONTENT
# ==================================================

DEFAULT_CONTENT = {
    "committee_name": "नव दुर्गा उत्सव समिति",
    "location": "New Salaiya",
    "tagline": "भक्ति, एकता और सेवा का उत्सव",
    "home_title": "जय माता दी 🙏",
    "home_text": "नव दुर्गा उत्सव समिति की आधिकारिक वेबसाइट पर आपका स्वागत है।",
    "about_title": "हमारे बारे में",
    "about_text": "नव दुर्गा उत्सव समिति New Salaiya की धार्मिक, सामाजिक और सांस्कृतिक समिति है।",
    "address": "New Salaiya, Sarni, Madhya Pradesh",
    "mobile": "यहाँ मोबाइल नंबर डालें",
    "email": "यहाँ ईमेल डालें",
    "footer_text": "श्रद्धा • सेवा • संस्कार"
}


DEFAULT_AARTIS = [
    {
        "id": "aarti_1",
        "title": "श्री दुर्गा आरती",
        "text": "यहाँ अपनी आरती का पूरा पाठ लिखें।"
    }
]


# ==================================================
# JSON FUNCTIONS
# ==================================================

def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_json(file_path, default_data):
    if not file_path.exists():
        save_json(file_path, default_data)
        return default_data

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(default_data, dict):
            if not isinstance(data, dict):
                data = {}

            for key, value in default_data.items():
                if key not in data:
                    data[key] = value

        if isinstance(default_data, list):
            if not isinstance(data, list):
                data = default_data

        save_json(file_path, data)
        return data

    except Exception:
        save_json(file_path, default_data)
        return default_data


content = load_json(CONTENT_FILE, DEFAULT_CONTENT)
aartis = load_json(AARTI_FILE, DEFAULT_AARTIS)


# ==================================================
# SESSION STATE
# ==================================================

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

if "gallery_version" not in st.session_state:
    st.session_state.gallery_version = 0


# ==================================================
# CSS DESIGN
# ==================================================

st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(135deg, #fff8e8, #ffe4a8);
    }

    .top-header {
    background:
        linear-gradient(
            90deg,
            rgba(101, 0, 0, 0.70),
            rgba(168, 0, 0, 0.55),
            rgba(227, 109, 0, 0.45)
        ),
        url("./assets/mata_rani_header.PNG");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;

    padding: 45px 20px;
    border-radius: 0 0 35px 35px;
    text-align: center;
    box-shadow: 0 8px 25px #6b210044;
    margin-bottom: 25px;
}

    .top-header h1 {
        color: white !important;
        font-size: 42px;
        font-weight: 900;
        margin: 0;
        text-shadow: 2px 2px 5px #400000;
    }

    .top-header h2 {
        color: #fff4c2 !important;
        font-size: 24px;
        margin-top: 12px;
        font-weight: 700;
    }

    .top-header p {
        color: white !important;
        font-size: 19px;
        margin-top: 10px;
    }

    .hero-box {
        background: linear-gradient(120deg, #fff3ce, #ffd477);
        padding: 35px;
        border-radius: 28px;
        box-shadow: 0 8px 22px #6b300033;
        border-left: 8px solid #a80000;
    }

    .hero-box h1 {
        color: #850000 !important;
        font-size: 38px;
        font-weight: 900;
    }

    .hero-box p {
        color: #3e2114 !important;
        font-size: 18px;
        line-height: 1.8;
    }

    .section-heading {
        color: #850000 !important;
        font-size: 32px;
        font-weight: 900;
        border-bottom: 4px solid #e69a16;
        padding-bottom: 8px;
        margin-top: 20px;
        margin-bottom: 22px;
    }

    .custom-card {
        background: white;
        padding: 25px;
        border-radius: 22px;
        border: 1px solid #e4b45d;
        box-shadow: 0 5px 18px #6b300022;
        margin-bottom: 20px;
    }

    .custom-card h3 {
        color: #8b0000 !important;
    }

    .custom-card p {
        color: #352116 !important;
        font-size: 17px;
        line-height: 1.7;
    }

    .footer-box {
        background: linear-gradient(120deg, #650000, #a80000);
        padding: 28px;
        border-radius: 25px 25px 0 0;
        text-align: center;
        margin-top: 40px;
    }

    .footer-box h3,
    .footer-box p {
        color: white !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# HEADER
# ==================================================

st.markdown(
    f"""
    <div class="top-header">
        <h1>🪔 {html.escape(str(content.get("committee_name", DEFAULT_CONTENT["committee_name"])))}</h1>
        <h2>{html.escape(str(content.get("location", DEFAULT_CONTENT["location"])))}</h2>
        <p>🌺 {html.escape(str(content.get("tagline", DEFAULT_CONTENT["tagline"])))}</p>
    </div>
    """,
    unsafe_allow_html=True
)


# ==================================================
# MENU
# ==================================================

menu = st.radio(
    "मुख्य मेन्यू",
    [
        "🏠 Home",
        "📖 हमारे बारे में",
        "🎉 कार्यक्रम",
        "🖼️ Gallery",
        "📚 आरती बुक्स",
        "💰 हिसाब-किताब",
        "📞 संपर्क करें",
        "🔐 Admin Panel"
    ],
    horizontal=True,
    label_visibility="collapsed"
)

st.divider()


# ==================================================
# HOME
# ==================================================

if menu == "🏠 Home":

    st.markdown(
        '<div class="section-heading">🌺 स्वागत है</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns([1.15, 1], gap="large")

    with left:
        st.markdown(
            f"""
            <div class="hero-box">
                <h1>{html.escape(str(content.get("home_title", "जय माता दी 🙏")))}</h1>
                <p>{html.escape(str(content.get("home_text", "")))}</p>
                <p>{html.escape(str(content.get("about_text", "")))}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with right:
        home_image = ASSETS_DIR / "home_design.png"

       
    st.markdown(
        '<div class="section-heading">✨ हमारी विशेषताएँ</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class="custom-card">
                <h3>🙏 धार्मिक आयोजन</h3>
                <p>पूजा, आरती, नवरात्रि और धार्मिक कार्यक्रम।</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="custom-card">
                <h3>🤝 सामाजिक सेवा</h3>
                <p>समाज में सहयोग, एकता और सेवा की भावना।</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            """
            <div class="custom-card">
                <h3>🌸 सांस्कृतिक कार्यक्रम</h3>
                <p>भजन, कीर्तन और सांस्कृतिक कार्यक्रम।</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ==================================================
# ABOUT
# ==================================================

elif menu == "📖 हमारे बारे में":

    st.markdown(
        '<div class="section-heading">📖 हमारे बारे में</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="custom-card">
            <h3>{html.escape(str(content.get("committee_name", "")))}</h3>
            <p>{html.escape(str(content.get("about_text", "")))}</p>
            <p><b>स्थान:</b> {html.escape(str(content.get("location", "")))}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# PROGRAMS
# ==================================================

elif menu == "🎉 कार्यक्रम":

    st.markdown(
        '<div class="section-heading">🎉 हमारे कार्यक्रम</div>',
        unsafe_allow_html=True
    )

    programs = [
        ("🌸 कलश यात्रा", "सुबह 8:00 बजे", "समिति प्रांगण"),
        ("🙏 माता की आरती", "शाम 7:00 बजे", "दुर्गा पंडाल"),
        ("🍛 भंडारा", "दोपहर 12:00 बजे", "समिति प्रांगण"),
        ("🎶 सांस्कृतिक कार्यक्रम", "शाम 8:00 बजे", "मुख्य मंच")
    ]

    for title, time, place in programs:
        st.markdown(
            f"""
            <div class="custom-card">
                <h3>{title}</h3>
                <p><b>समय:</b> {time}</p>
                <p><b>स्थान:</b> {place}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ==================================================
# GALLERY
# ==================================================

elif menu == "🖼️ Gallery":

    st.markdown(
        '<div class="section-heading">🖼️ समिति Gallery</div>',
        unsafe_allow_html=True
    )

    uploaded_image = st.file_uploader(
        "📷 Gallery में image upload करें",
        type=["png", "jpg", "jpeg", "webp"],
        key=f"gallery_{st.session_state.gallery_version}"
    )

    if uploaded_image is not None:

        file_name = f"{uuid.uuid4().hex}_{uploaded_image.name}"
        save_path = GALLERY_DIR / file_name

        with open(save_path, "wb") as file:
            file.write(uploaded_image.getbuffer())

        st.success("Image Gallery में upload हो गई है।")
        st.session_state.gallery_version += 1
        st.rerun()

    gallery_images = [
        file for file in GALLERY_DIR.iterdir()
        if file.is_file()
        and file.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp"]
    ]

    if gallery_images:
        columns = st.columns(3)

        for index, image_path in enumerate(sorted(gallery_images)):
            with columns[index % 3]:
                st.image(
                    str(image_path),
                    caption=image_path.name,
                    use_container_width=True
                )
    else:
        st.info("अभी Gallery में कोई image नहीं है।")


# ==================================================
# AARTI BOOKS
# ==================================================

elif menu == "📚 आरती बुक्स":

    st.markdown(
        '<div class="section-heading">📚 आरती बुक्स</div>',
        unsafe_allow_html=True
    )

    st.write("यहाँ समिति की सभी आरतियाँ पढ़ सकते हैं।")

    if not aartis:
        st.info("अभी कोई आरती उपलब्ध नहीं है।")

    for index, aarti in enumerate(aartis, start=1):
        title = aarti.get("title", f"आरती {index}")
        text = aarti.get("text", "")

        with st.expander(f"🙏 {index}. {title}"):
            st.write(text)

# ==================================================
# ACCOUNT PAGE
# ==================================================

elif menu == "💰 हिसाब-किताब":

    st.markdown(
        '<div class="section-heading">💰 समिति का हिसाब-किताब</div>',
        unsafe_allow_html=True
    )

    donations = [
        {
            "नाम": "रमेश जी",
            "तारीख": "10-09-2026",
            "राशि": 5000,
            "माध्यम": "Cash"
        },
        {
            "नाम": "सुरेश जी",
            "तारीख": "11-09-2026",
            "राशि": 2500,
            "माध्यम": "UPI"
        }
    ]

    expenses = [
        {
            "खर्च": "सजावट",
            "तारीख": "11-09-2026",
            "राशि": 2500
        },
        {
            "खर्च": "पूजा सामग्री",
            "तारीख": "12-09-2026",
            "राशि": 1200
        }
    ]

    total_donation = sum(item["राशि"] for item in donations)
    total_expense = sum(item["राशि"] for item in expenses)
    balance = total_donation - total_expense

    a, b, c = st.columns(3)

    a.metric("कुल चंदा", f"₹{total_donation:,}")
    b.metric("कुल खर्च", f"₹{total_expense:,}")
    c.metric("बाकी राशि", f"₹{balance:,}")

    st.subheader("📥 चंदे का विवरण")
    st.dataframe(donations, use_container_width=True, hide_index=True)

    st.subheader("📤 खर्च का विवरण")
    st.dataframe(expenses, use_container_width=True, hide_index=True)


# ==================================================
# CONTACT PAGE
# ==================================================

elif menu == "📞 संपर्क करें":

    st.markdown(
        '<div class="section-heading">📞 संपर्क करें</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="custom-card">
            <h3>📍 पता</h3>
            <p>{html.escape(str(content.get("address", "")))}</p>

            <h3>📱 मोबाइल</h3>
            <p>{html.escape(str(content.get("mobile", "")))}</p>

            <h3>📧 ईमेल</h3>
            <p>{html.escape(str(content.get("email", "")))}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# ADMIN PANEL
# ==================================================

elif menu == "🔐 Admin Panel":

    st.markdown(
        '<div class="section-heading">🔐 Admin Panel</div>',
        unsafe_allow_html=True
    )

    if not st.session_state.admin_logged_in:

        password = st.text_input(
            "Admin password डालें",
            type="password"
        )

        if st.button("🔓 Login"):

            if password == ADMIN_PASSWORD:
                st.session_state.admin_logged_in = True
                st.success("Admin Login सफल हुआ।")
                st.rerun()
            else:
                st.error("गलत password है।")

    else:

        st.success("आप Admin Panel में लॉगिन हैं।")

        if st.button("🚪 Logout"):
            st.session_state.admin_logged_in = False
            st.rerun()

        st.divider()

        admin_tab1, admin_tab2, admin_tab3 = st.tabs(
            [
                "✏️ Website Edit",
                "📚 आरती Edit",
                "🖼️ Gallery Edit"
            ]
        )

        # ==================================================
        # WEBSITE EDIT
        # ==================================================

        with admin_tab1:

            st.subheader("✏️ Website की सभी जानकारी Edit करें")

            with st.form("complete_website_edit_form"):

                new_committee_name = st.text_input(
                    "समिति का नाम",
                    value=str(content.get("committee_name", ""))
                )

                new_location = st.text_input(
                    "स्थान",
                    value=str(content.get("location", ""))
                )

                new_tagline = st.text_input(
                    "Tagline",
                    value=str(content.get("tagline", ""))
                )

                new_home_title = st.text_input(
                    "Home Heading",
                    value=str(content.get("home_title", ""))
                )

                new_home_text = st.text_area(
                    "Home का मुख्य संदेश",
                    value=str(content.get("home_text", ""))
                )

                new_about_title = st.text_input(
                    "About Heading",
                    value=str(content.get("about_title", ""))
                )

                new_about_text = st.text_area(
                    "About की पूरी जानकारी",
                    value=str(content.get("about_text", ""))
                )

                new_address = st.text_input(
                    "पूरा पता",
                    value=str(content.get("address", ""))
                )

                new_mobile = st.text_input(
                    "मोबाइल नंबर",
                    value=str(content.get("mobile", ""))
                )

                new_email = st.text_input(
                    "ईमेल",
                    value=str(content.get("email", ""))
                )

                new_footer_text = st.text_input(
                    "Footer Text",
                    value=str(content.get("footer_text", ""))
                )

                save_website = st.form_submit_button(
                    "💾 सभी जानकारी Save करें"
                )

                if save_website:

                    content = {
                        "committee_name": new_committee_name,
                        "location": new_location,
                        "tagline": new_tagline,
                        "home_title": new_home_title,
                        "home_text": new_home_text,
                        "about_title": new_about_title,
                        "about_text": new_about_text,
                        "address": new_address,
                        "mobile": new_mobile,
                        "email": new_email,
                        "footer_text": new_footer_text
                    }

                    save_json(CONTENT_FILE, content)

                    st.success("Website की सभी जानकारी save हो गई।")
                    st.rerun()


        # ==================================================
        # AARTI EDIT
        # ==================================================

        with admin_tab2:

            st.subheader("📚 नई आरती जोड़ें")

            with st.form("new_aarti_form"):

                new_aarti_title = st.text_input(
                    "आरती का नाम"
                )

                new_aarti_text = st.text_area(
                    "आरती का पूरा पाठ",
                    height=250
                )

                add_aarti = st.form_submit_button(
                    "🙏 आरती Save करें"
                )

                if add_aarti:

                    if new_aarti_title.strip() and new_aarti_text.strip():

                        aartis.append(
                            {
                                "id": uuid.uuid4().hex,
                                "title": new_aarti_title,
                                "text": new_aarti_text
                            }
                        )

                        save_json(AARTI_FILE, aartis)

                        st.success("नई आरती save हो गई।")
                        st.rerun()

                    else:
                        st.warning("आरती का नाम और पूरा पाठ भरें।")

            st.divider()

            st.subheader("🗑️ आरती हटाएँ")

            if not aartis:
                st.info("हटाने के लिए कोई आरती नहीं है।")

            for index, aarti in enumerate(aartis):

                title = aarti.get("title", f"आरती {index + 1}")

                col1, col2 = st.columns([5, 1])

                with col1:
                    st.write(f"🙏 {title}")

                with col2:

                    if st.button(
                        "Delete",
                        key=f"delete_aarti_{index}"
                    ):

                        aartis.pop(index)
                        save_json(AARTI_FILE, aartis)
                        st.success("आरती हटा दी गई।")
                        st.rerun()


        # ==================================================
        # GALLERY EDIT
        # ==================================================

        with admin_tab3:

            st.subheader("🗑️ Gallery से फोटो हटाएँ")

            gallery_images = [
                file for file in GALLERY_DIR.iterdir()
                if file.is_file()
                and file.suffix.lower()
                in [".png", ".jpg", ".jpeg", ".webp"]
            ]

            if not gallery_images:
                st.info("Gallery में कोई फोटो नहीं है।")

            for index, image_path in enumerate(sorted(gallery_images)):

                col1, col2 = st.columns([3, 1])

                with col1:
                    st.image(str(image_path), width=180)

                with col2:

                    if st.button(
                        "❌ Delete",
                        key=f"delete_gallery_{index}"
                    ):

                        image_path.unlink()
                        st.success("फोटो हटा दी गई।")
                        st.rerun()


# ==================================================
# FOOTER
# ==================================================

st.markdown(
    f"""
    <div class="footer-box">
        <h3>🪔 {html.escape(str(content.get("committee_name", DEFAULT_CONTENT["committee_name"])))}</h3>
        <p>
            {html.escape(str(content.get("location", DEFAULT_CONTENT["location"])))}
            • {html.escape(str(content.get("footer_text", DEFAULT_CONTENT["footer_text"])))}
        </p>
        <p>© 2026 Nav Durga Utsav Samiti</p>
    </div>
    """,
    unsafe_allow_html=True
)           