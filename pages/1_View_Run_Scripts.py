import os
import streamlit as st
import io
import contextlib
import matplotlib.pyplot as plt
from datetime import datetime

SCRIPTS_FOLDER = "codes"

st.set_page_config(page_title="Saved Scripts", page_icon="📂")

st.title("📂 View & Run Saved Python Scripts")

# Ensure the folder exists
if not os.path.exists(SCRIPTS_FOLDER):
    os.makedirs(SCRIPTS_FOLDER)

# List all Python files in the directory
script_files = [f for f in os.listdir(SCRIPTS_FOLDER) if f.endswith('.py')]

if not script_files:
    st.info("No scripts found. Generate some code using the chatbot first.")
else:
    selected_script = st.selectbox("📜 Select a script to view/run:", script_files)

    script_path = os.path.join(SCRIPTS_FOLDER, selected_script)

    # Read and display script content
    with open(script_path, "r") as f:
        script_code = f.read()
    st.code(script_code, language='python')

    # Show last modified time
    last_modified = os.path.getmtime(script_path)
    st.caption(f"🕒 Last modified: {datetime.fromtimestamp(last_modified).strftime('%Y-%m-%d %H:%M:%S')}")

    # Run the script
    if st.button("▶️ Run Script"):
        output_buffer = io.StringIO()
        safe_globals = {"plt": plt, "__builtins__": __builtins__}
        safe_locals = {}

        try:
            with contextlib.redirect_stdout(output_buffer):
                exec(script_code, safe_globals, safe_locals)
            st.success("✅ Script ran successfully!")
        except Exception as e:
            st.error(f"❌ Error running script: {str(e)}")

        output = output_buffer.getvalue()
        if output:
            st.subheader("🖨️ Script Output:")
            st.text(output)

        # Show all matplotlib plots
        figures = [plt.figure(n) for n in plt.get_fignums()]
        if figures:
            st.subheader("📊 Visual Output (if any):")
            for fig in figures:
                st.pyplot(fig)
            plt.close('all')  # Clear all plots

    # Option to delete the script
    if st.button("🗑️ Delete Script"):
        os.remove(script_path)
        st.success(f"✅ Script '{selected_script}' deleted.")
        st.rerun()

    # Refresh script list
    if st.button("🔄 Refresh Script List"):
        st.rerun()
