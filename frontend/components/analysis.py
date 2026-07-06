import streamlit as st
import pandas as pd
from services.api import analyze_report


def analysis_component():

    if "file_id" not in st.session_state:
        return

    st.header("🩺 Medical Analysis")

    if st.button("🩺 Analyze Medical Report"):

        with st.spinner("Analyzing report..."):

            response = analyze_report(
                st.session_state["file_id"]
            )

        if response.status_code == 200:

            data = response.json()
            analysis = data["analysis"]

            st.success("✅ Medical Analysis Completed")

            st.session_state["analysis_done"] = True

            # ==================================
            # Patient Information
            # ==================================

            patient = analysis.get("patient_information", {})

            st.subheader("👤 Patient Information")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Name",
                patient.get("name", "Not Available")
            )

            col2.metric(
                "Age",
                patient.get("age", "Not Available")
            )

            col3.metric(
                "Gender",
                patient.get("gender", "Not Available")
            )

            st.divider()

            # ==================================
            # Report Information
            # ==================================

            report = analysis.get("report_information", {})

            st.subheader("📋 Report Information")

            st.write(
                f"**Report Type:** {report.get('report_type', 'Not Available')}"
            )

            st.write(
                f"**Test Date:** {report.get('test_date', 'Not Available')}"
            )

            st.write(
                f"**Laboratory:** {report.get('laboratory', 'Not Available')}"
            )

            st.divider()

            # ==================================
            # Overall Health Risk
            # ==================================

            risk = analysis.get(
                "overall_health_risk",
                "Not Available"
            )

            st.subheader("🚨 Overall Health Risk")

            if risk.lower() == "low":
                st.success(f"🟢 {risk}")

            elif risk.lower() == "moderate":
                st.warning(f"🟡 {risk}")

            elif risk.lower() == "high":
                st.error(f"🔴 {risk}")

            else:
                st.info(risk)

            st.divider()

            # ==================================
            # Abnormal Parameters
            # ==================================

            st.subheader("⚠️ Abnormal Parameters")

            abnormal = analysis.get(
                "abnormal_parameters",
                []
            )

            if abnormal:

                rows = []

                for item in abnormal:

                    rows.append(
                        {
                            "Parameter": item.get(
                                "parameter",
                                "Not Available"
                            ),
                            "Value": item.get(
                                "value",
                                "Not Available"
                            ),
                            "Status": item.get(
                                "unit",
                                "Not Available"
                            ),
                        }
                    )

                df = pd.DataFrame(rows)

                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.success(
                    "No abnormal parameters detected."
                )

            st.divider()

            # ==================================
            # Possible Conditions
            # ==================================

            st.subheader("🩺 Possible Conditions")

            conditions = analysis.get(
                "possible_conditions",
                []
            )

            if conditions:

                for condition in conditions:

                    st.write(f"• {condition}")

            else:

                st.write("Not Available")

            st.divider()

            # ==================================
            # Medications
            # ==================================

            st.subheader("💊 Medications")

            medications = analysis.get(
                "medications",
                []
            )

            if medications:

                for medicine in medications:

                    if isinstance(medicine, dict):

                        st.write(
                            f"• {medicine.get('medication', 'Not Available')}"
                        )

                    else:

                        st.write(f"• {medicine}")

            else:

                st.write("Not Available")

            st.divider()

            # ==================================
            # Recommendations
            # ==================================

            st.subheader("✅ Recommendations")

            recommendations = analysis.get(
                "recommendations",
                []
            )

            if recommendations:

                for rec in recommendations:

                    if isinstance(rec, dict):

                        st.write(
                            f"• {rec.get('recommendation') or rec.get('description')}"
                        )

                    else:

                        st.write(f"• {rec}")

            else:

                st.write("Not Available")

        else:

            st.error(
                f"❌ Analysis Failed (Status Code: {response.status_code})"
            )

            st.write(response.text)