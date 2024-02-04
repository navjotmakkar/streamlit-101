import streamlit as st


#title
st.title("My App Title")

#header
st.header("Main header")

#subheader
st.subheader("Sub header")

#markdown
st.markdown("This is markdown **text** ")
st.markdown("# Head1")
st.markdown("## Head2")
st.markdown("### Head3")

#caption
st.caption("This is caption")

#code
st.code("""import pandas as pd
        pd.read_csv(pdffile)""")

#preformatted text
st.text("Some text")

#latex
st.latex("x = 2 * 2")

##divider
st.text("text1")
st.divider()
st.text("text2")

#write
st.write("st.write() Can be used to display lot of things")
