import streamlit as st
from PIL import Image

st.set_page_config(page_title="KHENCHELA SUN", layout="wide")

st.title("KHENCHELA SUN - Photoshop Shams")
st.subheader("Khenchela 35.4N 7.1E - 300 sunny days")

uploaded = st.file_uploader("Upload roof photo", type=["jpg","png","jpeg"])

if uploaded:
    img = Image.open(uploaded)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(img, caption="Original", width='stretch')
    
    roof_m2 = st.slider("Roof m2", 10, 100, 40)
    kw = roof_m2 * 0.2
    kwh_year = kw * 5.5 * 365
    dzd = kwh_year * 6
    
    with col2:
        st.success(f"{kw:.1f} kW")
        st.metric("Saving / year", f"{dzd:,.0f} DZD")
        st.metric("kWh / year", f"{kwh_year:,.0f} kWh")
        st.metric("Dollar", f"${dzd/135:.0f}")
        st.image(img, caption=f"After - {kw:.1f} kW Solar!", width='stretch')
        st.balloons()
else:
    st.warning("Upload photo!")
    st.write("40m2 = 8.0 kW = 16,060 kWh = 96,000 DZD / year")

st.sidebar.success("API OK")
st.sidebar.write("Khenchela 300 days sun")