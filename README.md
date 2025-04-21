import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title='SND Claims YTD (2024-25)',
    page_icon='📊'
)

st.title(":rainbow[SND Claims YTD'2024-25']")
st.subheader(':red[You can find your WD_Claims below]', divider='rainbow')

# Load Excel data
file_path = 'SSC_and_Atta_Damage_Claims.xlsx'
data = pd.read_excel(file_path)

# Clean column names
data.columns = data.columns.str.strip()
data['WD Code'] = data['WD Code'].astype(str).str.strip()

# WD Code input
WD_Code = st.text_input("Please Enter Your WD Code")

if 'show_form' not in st.session_state:
    st.session_state['show_form'] = False

if WD_Code:
    WD_Code = WD_Code.strip()
    filtered_data = data[data['WD Code'] == WD_Code]

    if not filtered_data.empty:
        st.success("✅ Data Found Successfully")

        tab1, tab2, tab3 = st.tabs(["Received", "Not Received", "All"])

        with tab1:
            received_data = filtered_data[filtered_data['Status'].str.strip() == "Received"]
            if not received_data.empty:
                st.dataframe(received_data)
            else:
                st.warning("⚠️ No data found under 'Received'")

        with tab2:
            not_received_data = filtered_data[filtered_data['Status'].str.strip() == "Not Received"]
            if not not_received_data.empty:
                st.dataframe(not_received_data)

                # Button to show the form for data entry
                if st.button("Yes, I want to submit"):
                    st.session_state['show_form'] = True

                if st.session_state['show_form']:
                    updated_rows = []

                    st.markdown("---")
                    st.subheader("📝 Submit Details for Not Received Entries")

                    for idx, row in not_received_data.iterrows():
                        entry_no = row['Entry No'] if 'Entry No' in row else "N/A"
                        mt_value = row['MT'] if 'MT' in row else "N/A"
                        provision_amt = row.get('Provision Amount', 'Not Available')
                        if pd.isna(provision_amt):
                            provision_amt = "Not Available"

                        st.markdown(f"#### Entry No: `{entry_no}` | MT: `{mt_value}` | Provision Amount: `{provision_amt}`")

                        amount = st.number_input(
                            f"Enter Actual Claim Amount Received for Entry {entry_no}",
                            key=f"amount_{idx}",
                            step=1.0
                        )

                        uploaded_files = st.file_uploader(
                            f"Upload Files for Entry {entry_no} (JPG, PNG, PDF)",
                            type=["jpg", "png", "pdf"],
                            accept_multiple_files=True,
                            key=f"files_{idx}"
                        )

                        updated_rows.append({
                            "index": idx,
                            "amount": amount,
                            "files": uploaded_files
                        })

                    if st.button("Submit All Entries"):
                        desktop_path = Path.home() / "Desktop"
                        today_str = pd.Timestamp.today().strftime("%Y-%m-%d")
                        parent_folder = desktop_path / "SND_Claims_Uploads" / f"WD_{WD_Code}" / today_str
                        parent_folder.mkdir(parents=True, exist_ok=True)

                        for item in updated_rows:
                            idx = item['index']
                            amount = item['amount']
                            files = item['files']

                            data.loc[idx, "Actual WD Claims Amount Received"] = amount
                            data.loc[idx, "Status"] = "Received"

                            if "Remarks" in data.columns and data.loc[idx, "Remarks"] == "Pending":
                                data.loc[idx, "Remarks"] = "Done"

                            # Save files
                            if files:
                                for i, file in enumerate(files, start=1):
                                    file_ext = file.name.split('.')[-1]
                                    new_filename = f"{WD_Code}_Entry{idx+1}_{i}.{file_ext}"
                                    file_path = parent_folder / new_filename

                                    with open(file_path, "wb") as f:
                                        f.write(file.getbuffer())

                        # Save updated Excel
                        data.to_excel(file_path, index=False)
                        st.success("✅ All data saved to Excel successfully!")
                        st.dataframe(data[data['WD Code'] == WD_Code])

            else:
                st.warning("⚠️ No data found under 'Not Received'")

        with tab3:
            st.dataframe(filtered_data)

    else:
        st.warning("⚠️ No data found for this WD Code")
