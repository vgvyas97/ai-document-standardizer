import streamlit as st
from openai import OpenAI

# 1. Setup the Web Page Title and Layout
st.set_page_config(page_title="AI Documentation Standardizer", page_icon="📝", layout="wide")
st.title("📝 AI Documentation Standardizer & Replicator")
st.write("Transform disorganized engineering notes into pristine, company-standard SOPs or Runbooks instantly.")

# 2. Sidebar for API Key and Template Presets
api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Formatting Tip")
st.sidebar.write("Paste your company's official markdown layout into the 'Target Template' box, and the AI will copy its exact headers and style.")

# 3. Create Two Columns side-by-side for Inputs
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 1. Paste Your Raw, Messy Notes")
    raw_notes = st.text_area(
        "Enter raw terminal logs, unformatted drafts, or scattered notes...",
        height=300,
        placeholder="e.g., reset user vpn: go to okta, click reset token, wait 5 mins, tell user to login again with new code."
    )

with col2:
    st.subheader("📐 2. Paste Target Document Template")
    
    # Pre-populate a standard corporate template so the user doesn't have to type one from scratch
    default_template = (
        "# [DOCUMENT TITLE]\n\n"
        "## 🛠️ Prerequisites & Requirements\n"
        "- List access privileges, software versions, or credentials needed.\n\n"
        "## 🔄 Step-by-Step Execution Procedure\n"
        "1. First step...\n"
        "2. Second step...\n\n"
        "## ⚠️ Expected Outcomes & Verification\n"
        "- Describe how to verify this step was successful.\n\n"
        "## 🚨 Common Troubleshooting Steps\n"
        "- If X fails, do Y."
    )
    
    target_template = st.text_area(
        "Define the mandatory structural layout (Markdown supported):",
        value=default_template,
        height=300
    )

# 4. Generate Button
if st.button("Standardize & Replicate Document"):
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar to proceed.")
    elif not raw_notes:
        st.warning("Please paste your raw content notes first.")
    else:
        with st.spinner("Analyzing structure and formatting documentation..."):
            try:
                # Setup Google Gemini API connection
                client = OpenAI(
                    api_key=api_key,
                    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
                )
                
                # Rigid instructions forcing the AI to strictly respect the user's layout
                system_instruction = (
                    "You are an expert IT Technical Writer and Systems Documentation Specialist. "
                    "Your core task is to take messy, raw engineering notes and reorganize them "
                    "so they perfectly map into the exact structural headers and formatting style of the provided Target Template. "
                    "Do not skip sections. If information for a section is missing from the raw notes, "
                    "use your domain knowledge to write a logical technical placeholder or instruction."
                )
                
                user_prompt = (
                    f"TARGET TEMPLATE SCHEMA:\n{target_template}\n\n"
                    f"RAW NOTES TO RESTRUCTURE:\n{raw_notes}"
                )
                
                # Send context to Gemini
                response = client.chat.completions.create(
                    model="gemini-3.5-flash",
                    messages=[
                        {"role": "system", "content": system_instruction},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.1
                )
                
                # Display output
                st.success("Standardized Document Compiled!")
                st.markdown("---")
                st.markdown(response.choices[0].message.content)
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
